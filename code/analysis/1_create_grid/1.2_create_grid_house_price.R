############################################################

# This script takes in a set of lat-lons (representing the subgrid we sample)
# and the house price tiff generated from the rawdata file and create grid y data accordingly.

############################################################

# Packages
library(raster)
library(foreach)
library(doParallel)
library(reticulate)
library(data.table)
library(here)

rm(list=ls())

## Import config.R to set filepaths
mosaiks_code <- Sys.getenv("MOSAIKS_CODE")
if (mosaiks_code=="") {
  mosaiks_code = here("code")
}


for (city in c(#'Eldoret','Embu','Garissa','Kakamega','Kericho',
               #'Kisumu','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri',
               'Thika'
)) {
  source(file.path(mosaiks_code, "mosaiks", "config.R"))
  res_dir = file.path(res_dir, city)
  out_dir = file.path(out_dir, city)
  grid_dir = file.path(grid_dir, city)
  features_dir = file.path(features_dir, city)
  dir.create(out_dir, showWarnings=FALSE, recursive=TRUE)
  dir.create(grid_dir, showWarnings=FALSE, recursive=TRUE)
  dir.create(features_dir, showWarnings=FALSE, recursive=TRUE)
  
  ## Source the necessary helper files
  source(file.path(utils_dir, "R_utils.R"))
  ## Source city info
  source(file.path(mosaiks_code, "mosaiks", "city_info",paste0(city, ".r")))
  
  ########### INPUTS REQUIRED ############
  
  
  # Number of cores when parallelizing:
  args = commandArgs(trailingOnly=TRUE)
  if (length(args)==0) {
    no_cores = 4
  } else {
    no_cores = args[2]
  }
    
  
  
  # Filename/path for subgrid

  gridFile = file.path(data_dir,"int/grids",city, paste0("grid", "_",city, "_", as.character(zoom), "_", as.character(pixels), "_", 
                                                         sampling, "_",meters_per_grid,"_", format(S, scientific = FALSE),".npz"))
  
  ############## Pull in lat-lon samples 
  np <- import("numpy")
  npz1 <- np$load(gridFile)
  npz1$files
  sampLat = c(npz1$f[["lat"]])
  sampLon = c(npz1$f[["lon"]])
  zoom = npz1$f[["zoom"]]
  pixels = npz1$f[["pixels"]]
  ID = c(npz1$f[["ID"]])
  
  #Load Raster
  house = raster(file.path(data_dir,paste0("raw/applications/house_price/grid_",city,".tif")))
  crs = CRS(as.character("+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0"))
  
  house <- projectRaster(house, crs = crs)
  #Create 
  recs = centroidsToTiles(lat = sampLat, lon = sampLon, zoom = zoom, numPix = pixels)
  
  #crop the pop raster to the recs
  e = extent(recs)
  delta = .1
  e@xmin = e@xmin - delta
  e@xmax = e@xmax + delta
  e@ymin = e@ymin - delta
  e@ymax = e@ymax + delta
  house = crop(house, e)
  
  
  print('Extracting...')
  out = raster::extract(x = house, y = recs, fun = mean)
  
  df = cbind(ID, sampLon, sampLat, out)
  colnames(df) = c("ID","lon","lat","houseprice")
  dt = data.table(df)
  
  ### set the NA values to -999
  dt$houseprice[is.na(dt$houseprice)] = -999
  
  ### Save
  paste0("grid", "_",city, "_", as.character(zoom), "_", as.character(pixels), "_", 
         sampling, "_",meters_per_grid,"_", format(S, scientific = FALSE))
  label_dir = file.path(data_dir,"int/applications/housing", city)
  dir.create(label_dir, showWarnings=FALSE, recursive=TRUE)
  fn = file.path(label_dir, paste0("outcomes_sampled_houseprice_dense_",as.character(zoom), "_", as.character(pixels), "_", 
                                   sampling,"_",meters_per_grid,"_", S, ".csv"))
  
  write.csv(x = dt, file = fn)
  
  print("DONE DONE DONE")
  }
  

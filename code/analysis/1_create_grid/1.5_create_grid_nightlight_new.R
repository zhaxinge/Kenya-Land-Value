



############################################################

# This script takes in a set of lat-lons and the raw image data and crop the image accordingly

############################################################

# Packages
library(raster)
library(foreach)
library(doParallel)
library(reticulate)
library(data.table)
library(here)
library(jpeg)
library(raster)

rm(list=ls())

## Import config.R to set filepaths
mosaiks_code <- Sys.getenv("MOSAIKS_CODE")
if (mosaiks_code=="") {
  mosaiks_code = here("code")
}

for (city in c('Eldoret'
               #,'Embu','Garissa','Kakamega','Kisumu','Kericho',
               #'Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri',
               #'Thika'
)) {
  print(city)
  source(file.path(mosaiks_code, "mosaiks", "config.R"))
  ## Source the necessary helper files
  source(file.path(utils_dir, "R_utils.R"))
  res_dir = file.path(res_dir, city)
  out_dir = file.path(out_dir, city)
  grid_dir = file.path(grid_dir, city)
  features_dir = file.path(features_dir, city)
  dir.create(out_dir, showWarnings=FALSE, recursive=TRUE)
  dir.create(grid_dir, showWarnings=FALSE, recursive=TRUE)
  dir.create(features_dir, showWarnings=FALSE, recursive=TRUE)
  
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
  
  # Create an empty RasterBrick to store the images
  img_brick <- brick()
  
  # Loop through each year and load images
  for (i in 1:12) {
    # Load the TIFF image for the current city and year
    tiff_path <- file.path(data_dir, "raw/applications/lightnight_noreduce", paste0(i, ".tif"))
    img <- raster(tiff_path)
    
    # Add the image to the RasterBrick
    img_brick <- addLayer(img_brick, img)
  }
  
  # Calculate the mean value of the images
  img <- calc(img_brick, mean)
  # Set the extent of the image
  ext <- extent(lonmin, lonmax, latmin, latmax)
  extent(img) <- ext
  
  crs <- CRS(as.character("+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0"))
  crs(img)<- crs
  
  # Create tiles
  recs <- centroidsToTiles(lat = sampLat, lon = sampLon, zoom = zoom, numPix = pixels)
  
  output_dir <- file.path(data_dir, "raw/nightlight-2013",city)
  dir.create(output_dir, showWarnings=FALSE, recursive=TRUE)
  
  # Get the number of grid cells
  num_cells <- ncell(recs)
  
  # Loop through each grid cell
  for (i in 1:num_cells) { #TODO:num_cells
    # Extract the extent of the current grid cell
    tryCatch({
      cell_extent <- extent(recs[i])
      
      # Crop the image using the current grid cell extent
      cropped_image <- crop(img, cell_extent)
      image_dimensions <- dim(cropped_image)
      
      # Get the coordinates of the vertices of the grid cell
      vertices <- coordinates(cell_extent)

      # Calculate the centroid as the average of the vertices
      centroid <- apply(vertices, 2, mean)
      
      # Get the latitude and longitude of the centroid
      lat <- centroid[2]
      lon <- centroid[1]
      
      # Specify the output file path for the grid piece
      output_file <- file.path(output_dir, paste0(lat, "_", lon, "_", zoom, "_", image_dimensions[2], "_", image_dimensions[1], "_",ID[i], "_",".tif"))
      
      # Save the cropped image as a JPEG file
      writeRaster(cropped_image, filename = output_file,  format = "GTiff", options = "COMPRESS=LZW", overwrite = TRUE)
    }, 
    error = function(e) {
      errorMessage <- sprintf("Error in %s cell %d: %s",city, i, conditionMessage(e))
      print(errorMessage)
      # Handle the error condition as desired (e.g., log the error, continue processing, etc.)
    }
    )
  }
}


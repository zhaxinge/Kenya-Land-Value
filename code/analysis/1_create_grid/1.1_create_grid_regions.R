############################################################

# This script samples the grid for the set of zoomed
# dense sampling (every single grid) and then executes dense (but not fully dense) sampling
# for the remainder of each zoom region.

############################################################
rm(list = ls())

library(rgdal)
library(ggplot2)
library(sp)
library(raster)
library(maps)
library(mapdata)
library(maptools)
library(cowplot)
library(here)
library(dplyr)
library(rlang)

## Import config.R to set filepaths
mosaiks_code <- Sys.getenv("MOSAIKS_CODE")
if (mosaiks_code == "") {
  mosaiks_code <- here("code")
}

for (city in c(#'Eldoret','Embu','Garissa','Kakamega','Kericho',
               'Kisumu'
               #','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri',
               #'Thika'
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
  
  
 
  # initial number of samples to draw
  
  e <- extent(lonmin, lonmax, latmin, latmax)
  ext <- as.vector(e)
  
  
  
  gridvals <- makegrid(meters_per_grid, lonmin, lonmax, latmin, latmax)
  
  # Regularly sample throughout the rest of the zoom area
  latVals <- sort(gridvals[[2]])
  lonVals <- sort(gridvals[[1]])
  
  # store in samples df
  samples <- data.frame(lon = numeric(N * multiplier), lat = numeric(N * multiplier))
  
  # make the full grid, order by lat-lon, only take every Kth obs (K = total N in zoom / desired N in zoom)
  K <- round((length(latVals) * length(lonVals)) / (N * multiplier))
  counter <- 0
  for (ly in 1:length(latVals)) {
    for (lx in 1:length(lonVals)) {
      counter <- counter + 1 
      if (round(counter / K) == counter / K & counter / K <= N * multiplier) {
        samples$lat[counter / K] <- latVals[ly]
        samples$lon[counter / K] <- lonVals[lx]
      }
    }
  }
  
  # Remove incomplete cases
  samples <- samples[complete.cases(samples),]
  
  
  # Make polygons of all lat-lon grids in samples
  mysamples <- lapply(1:dim(samples)[1], function(i) {
    centroidsToTiles(samples$lat[i], samples$lon[i], zoom, pixels)
  })
  samprecs = list(mysamples, makeUniqueIDs = T) %>% 
    flatten() %>% 
    do.call(rbind, .)
  print(paste0("------ No. of images in rest of zoom: ", length(samprecs), " -----------"))
  
  
  
  
  ############################################################
  # Save .npz file for featurization
  ############################################################
  
  # Identify each obs as i,j using our full grid ID system
  latValsfull <- gridvals[[2]]
  lonValsfull <- gridvals[[1]]
  
  starttime <- Sys.time()
  allsamples <- samples  # Create allsamples data.frame
  S <- dim(allsamples)[1]
  allsamples$i <- integer(S)
  allsamples$j <- integer(S)
  
  for (n in 1:S) {
    lat_index <- which(latValsfull == allsamples$lat[n])
    lon_index <- which(lonValsfull == allsamples$lon[n])
    
    if (length(lat_index) == 0 || length(lon_index) == 0) {
      # Handle the case where lat or lon value is not found
      print("Lat or Lon value not found in latValsfull or lonValsfull")
      # Add appropriate error handling or continue to the next iteration
      next
    }
    
    allsamples$i[n] <- lat_index
    allsamples$j[n] <- lon_index
  }
  
  endtime <- Sys.time()
  print(endtime - starttime)
  
  allsamples$ID <- paste(allsamples$i, allsamples$j, sep = ",")
  
  # Export to npz
  filename <- paste0("grid", "_",city, "_", as.character(zoom), "_", as.character(pixels), "_", 
                     sampling, "_",meters_per_grid,"_", format(S, scientific = FALSE))
  np <- import("numpy")
  np$savez(file.path(grid_dir, paste0(filename, ".npz")), lon = allsamples$lon, lat = allsamples$lat, 
           ID = allsamples$ID, zoom = zoom, pixels = pixels)
  
  print("-------- Saved .npz! -----------")
}





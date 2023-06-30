from sentinelhub import SHConfig

config = SHConfig(
                instance_id='ac6e2286-5987-4181-9572-d8b53b409d4f',
                sh_client_id='da5becd0-6ef1-4c51-96ab-ed475544e32f',
                sh_client_secret='BcHDaWKKP2,;.]m4Yi<)(uF0]gJ)MoaVs7e&^)p]')

import geopandas as gpd
import os
import requests

import datetime
import os

import matplotlib.pyplot as plt
import numpy as np

from sentinelhub import (
    CRS,
    BBox,
    DataCollection,
    DownloadRequest,
    MimeType,
    MosaickingOrder,
    SentinelHubDownloadClient,
    SentinelHubRequest,
    bbox_to_dimensions,
)



def download_city_grid_imagery(shapefile_folder, output_folder, resolution):
    # Iterate over each shapefile in the folder
    for filename in os.listdir(shapefile_folder):
        if filename.endswith('.shp'):
            shapefile_path = os.path.join(shapefile_folder, filename)
            city_name = os.path.splitext(filename)[0][len('grid_'):]
            city_grids = gpd.read_file(shapefile_path)
            city_grids_4326 = city_grids.to_crs(4326)
            # Create a directory for the city if it doesn't exist
            city_folder = os.path.join(output_folder, city_name)
            os.makedirs(city_folder, exist_ok=True)
             # Extract the bounding box coordinates
            grid_bbox = city_grids_4326.geometry.bounds
            
            # Configure the Sentinel Hub credentials
            

            # Define the bounding box for your specific location
            min_longitude= min(grid_bbox.minx)
            min_latitude= min(grid_bbox.miny)
            max_longitude= max(grid_bbox.maxx)
            max_latitude= max(grid_bbox.maxy)

            bounding_box = BBox((min_longitude,min_latitude, max_longitude, max_latitude), CRS.WGS84)
            size = bbox_to_dimensions(bounding_box, resolution=resolution)
            if size[0] < 2500 and size[1] < 2500:
                width = size[0]
                height = size[1]
            elif size[0] > 2500:
                width = 2500
                height = size[1]
            else:
                width = size[0]
                height = 2500
           
            # Define the request parameters
            request = SentinelHubRequest(
                evalscript="""
                    //VERSION=3
                    function setup() {
                        return {
                            input: [{
                                bands: ["B02", "B03", "B04"], // Replace with desired RGB bands
                            }],
                            output: { bands: 3 }
                        };
                    }
                    function evaluatePixel(sample) {
                        return [sample.B04, sample.B03, sample.B02]; // Adjust bands accordingly
                    }
                """,
                input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L1C,
                    #time_interval=time_interval ,
                    mosaicking_order=MosaickingOrder.LEAST_CC,
                )
                ],
                bbox=bounding_box,
                size=(width,height),
                config=config,
                responses=[
                    SentinelHubRequest.output_response('default', MimeType.TIFF)
                ],
                data_folder= city_folder
            )
            print(size)
            # Execute the request and download the data
            data = request.get_data(save_data = True, raise_download_errors=True)[0]
            print(f"Image for {city_name} saved successfully.")


# usage
shapefile_folder = 'data/raw/grid'
output_folder = 'data/raw/images'
resolution = 10
#time_interval = ("2020-06-12", "2020-06-13")
download_city_grid_imagery(shapefile_folder, output_folder, resolution)

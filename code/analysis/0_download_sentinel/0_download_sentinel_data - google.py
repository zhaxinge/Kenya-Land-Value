import geopandas as gpd
import os
import requests
from PIL import Image

def download_city_grid_imagery(shapefile_folder, output_folder, resolution = 10):
    # Iterate over each shapefile in the folder
    for filename in os.listdir(shapefile_folder):
        if filename.endswith('.shp'):
            shapefile_path = os.path.join(shapefile_folder, filename)
            city_name = os.path.splitext(filename)[0][len('grid_'):]
            city_grids = gpd.read_file(shapefile_path)
            city_grids_4326 = city_grids.to_crs(4326)

             # Extract the bounding box coordinates
            grid_bbox = city_grids_4326.geometry.bounds
            grid_bbox_meters = city_grids.geometry.bounds
            height = (max(grid_bbox_meters.maxy) - min(grid_bbox_meters.miny))/resolution
            width = max(grid_bbox_meters.maxx) - min(grid_bbox_meters.minx)/resolution
            min_longitude= min(grid_bbox.minx)
            min_latitude= min(grid_bbox.miny)
            max_longitude= max(grid_bbox.maxx)
            max_latitude= max(grid_bbox.maxy)
            longitude_step = (max(grid_bbox.maxx) - min(grid_bbox.minx))/width
            latitude_step = (max(grid_bbox.maxy) - min(grid_bbox.miny))/height
            latitude = (min_latitude + max_latitude) / 2
            longitude = (min_longitude + max_longitude) / 2
            
            if width > 640 or height > 640:
                num_parts = 1
                if width > 640:
                    remaining_width = width - 640
                    num_parts += (remaining_width // 640)
                if height > 640:
                    remaining_height = height - 640
                    num_parts += (remaining_height // 640)

                # Create an empty composite image
                composite_image = Image.new('RGB', (int(width), int(height)))
                for part in range(int(num_parts)):
                    start_width = 640 * part
                    end_width = start_width + 640
                    part_width = int(min(end_width, width) - start_width)
                    min_longitude = min_longitude + (start_width* longitude_step)
                    max_longitude = min_longitude + (start_width* longitude_step) + (part_width * longitude_step)
                    
                    start_height = 640 * part
                    end_height = start_height + 640
                    part_height = int(min(end_height, height) - start_height)
                    min_latitude =  min_latitude + (start_height * latitude_step)
                    max_latitude = min_latitude + (start_height * latitude_step) + (part_height * latitude_step)

                    latitude = (min_latitude + max_latitude) / 2
                    longitude = (min_longitude + max_longitude) / 2

                    if part_width < 0 or part_height< 0:
                        pass 
                    else:
                        print((part_width, part_height))
            
                        # Parameters for the Google Static Maps API request
                        api_key = 'AIzaSyDjA3RaHC7xkwjNrmVo8ES7ksPF94kqEPw'  # Replace with your Google Static Maps API key
                        zoom = 14
                        image_size = f"{part_width}x{part_height}"
                        map_type = 'satellite'

                        # Construct the URL
                        url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={image_size}&maptype=satellite&key={api_key}"
                        # Send a GET request to fetch the image
                        response = requests.get(url)
                        # Create a directory for the city if it doesn't exist
                        city_folder = os.path.join(output_folder, city_name)
                        os.makedirs(city_folder, exist_ok=True)
                        # Save the image with city-specific filename
                        part_image_path = os.path.join(city_folder, f"{latitude}_{longitude}_{zoom}_{part_width}_{part_height}_{city_name}.jpg")
                        
                        with open(part_image_path, 'wb') as file:
                            file.write(response.content)
                        
                        # Open the part image
                        part_image = Image.open(part_image_path)

                        # Paste the part image into the composite image
                        composite_image.paste(part_image, (start_width, start_height))

                # Resize the composite image if necessary
                if composite_image.size[0] > 65500 or composite_image.size[1] > 65500:
                    composite_image = composite_image.resize((int(composite_image.size[0] / 16), int(composite_image.size[1] / 16)))

                # Save the composite image for the city
                #composite_image_path = os.path.join(output_folder, f"image_{city_name}.jpg")
                #composite_image.save(composite_image_path)

                print(f"Image for {city_name} saved successfully.")
            

# usage
shapefile_folder = 'data/raw/grid'
output_folder = 'data/raw/image'

download_city_grid_imagery(shapefile_folder, output_folder)

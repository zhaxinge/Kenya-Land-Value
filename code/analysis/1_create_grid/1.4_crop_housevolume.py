import geopandas as gpd
import rasterio
from rasterio.mask import mask
import os

# Read the shapefile
shapefile = gpd.read_file('Kenya-Land-Value/data/raw/volume/crop_grid.shp')
cities = ['Thika', 'Eldoret','Garissa', 'Kericho','Naivasha','Nairobi','Machakos','Nyeri','Kitui','Kisumu','Kakamega','Nakuru','Mombasa','Malindi', 'Embu']
# Output directory for cropped images
output_dir = 'Kenya-Land-Value\\data\\raw\\volume\\2010_NRES'

# Open the GeoTIFF image
with rasterio.open('Kenya-Land-Value/data/raw/volume/c2010_NRES_Clip.tif') as src:
    raster_crs = src.crs

    # Reproject the shapefile to match the CRS of the raster
    reprojected_shapefile = shapefile.to_crs(raster_crs)

    # Iterate over each polygon in the shapefile
    for index, row in reprojected_shapefile.iterrows():
        # Get the polygon geometry
        geometry = row.geometry
        city = cities[index]

        # Convert the polygon to the GeoJSON format
        json_geometry = [geometry.__geo_interface__]

        # Crop the image using the polygon geometry
        cropped_image, cropped_transform = mask(src, json_geometry, crop=True)

        # Create a new GeoTIFF file for the cropped image
        cropped_meta = src.meta.copy()
        cropped_meta.update({
            'driver': 'GTiff',
            'height': cropped_image.shape[1],
            'width': cropped_image.shape[2],
            'transform': cropped_transform
        })

        # Save the cropped image with a unique filename
        output_filename = f'cropped_NRES_{city}.tif'
        output_path = os.path.join(output_dir, output_filename)

        # Save the cropped image
        with rasterio.open(output_path, 'w', **cropped_meta) as dst:
            dst.write(cropped_image)


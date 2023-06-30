# coding: utf-8
import geopandas as gpd
# from rasterio.features import geometry_mask
import os
get_ipython().run_line_magic('pip', 'install geopandas')
get_ipython().run_line_magic('pip', 'install rasterio')
import geopandas as gpd
from rasterio.features import geometry_mask
import os
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    grid_mask_single = geometry_mask(grid_shapefile.geometry, out_shape=images.shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    if grid_mask is None:
        grid_mask = grid_mask_single
    else:
        grid_mask |= grid_mask_single
    print((grid_mask_single.shape))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    #grid_mask_single = geometry_mask(grid_shapefile.geometry, out_shape=images.shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(grid_shapefile)
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
def load_pickle_data(folder_path, city_name):
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pkl") and city_name in file_name:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "rb") as file:
                file_data = pickle.load(file)
                data.append(file_data)
    return data

# Define the path to the folder containing the city images
image_folder = c.sample_dir
def load_pickle_data(folder_path, city_name):
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pkl") and city_name in file_name:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "rb") as file:
                file_data = pickle.load(file)
                data.append(file_data)
    return data

# Define the path to the folder containing the city images
image_folder = 'data\\int\\img_matrices'
for city in c.cities:
    
    dataset = load_pickle_data(image_folder, city)   
    print(np.array(dataset))
cities =['Eldoret','Embu','Garissa','Kakamega','Kericho','Kisumu','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri','Thika']
for city in cities:
    
    dataset = load_pickle_data(image_folder, city)   
    dataset
import pickle
cities =['Eldoret','Embu','Garissa','Kakamega','Kericho','Kisumu','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri','Thika']
for city in cities:
    
    dataset = load_pickle_data(image_folder, city)   
    dataset
import pickle
import dill
get_ipython().run_line_magic('pip', 'install dill')
import pickle
import dill
def load_pickle_data(folder_path, city_name):
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pkl") and city_name in file_name:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "rb") as file:
                file_data = pickle.load(file)
                data.append(file_data)
    return data

# Define the path to the folder containing the city images
image_folder = 'data\\int\\img_matrices'
cities =['Eldoret','Embu','Garissa','Kakamega','Kericho','Kisumu','Kitui','Machakos','Malindi','Mombasa','Nairobi','Naivasha','Nakuru','Nyeri','Thika']
for city in cities:
    
    dataset = load_pickle_data(image_folder, city)   
    dataset
dataset
dataset[0].shape
dataset[0]
dataset[0].shape
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    grid_mask_single = geometry_mask(grid_shapefile.geometry, out_shape=(640,640), transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(grid_shapefile)
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
import geopandas as gpd
from rasterio.features import geometry_mask
import os
import rasterio
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    grid_mask_single = geometry_mask(grid_shapefile.geometry, out_shape=(640,640), transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(grid_shapefile)
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_mask_single 
grid_mask_single.shape
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    grid_mask_single = geometry_mask(grid_shapefile.geometry, out_shape=dataset[0].shape, transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(grid_shapefile)
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    grid_mask_single = geometry_mask(grid_shapefile.geometry, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(grid_shapefile)
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_mask_single.shape
grid_mask_single
dataset[:, :, 1] * grid_mask_single
dataset[0][:, :, 1] * grid_mask_single
avg(dataset[0][:, :, 1] * grid_mask_single)
mean(dataset[0][:, :, 1] * grid_mask_single)
np.mean(dataset[0][:, :, 1] * grid_mask_single)
import numpy as np
np.mean(dataset[0][:, :, 1] * grid_mask_single)
sum(dataset[0][:, :, 1] * grid_mask_single)
sum(grid_mask_single)
sum(sum(grid_mask_single))
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    for row in grid_shapefile:
        grid_mask_single = geometry_mask(row.geometry, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    for i in grid_shapefile.geometry:
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    for i in grid_shapefile.geometry:
        print(grid_shapefile.geometry)
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    print(grid_shapefile.bound)
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    print(grid_shapefile.geometry.bound)
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    print(grid_shapefile.geometry.bounds)
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    print(grid_shapefile.geometry.unary_union)
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
zoom_level = 14
distance_on_map = 100  # in meters
distance_on_earth = 9000  # in meters (1:9000 scale for zoom level 14)
tile_size = 256  # in pixels

pixels = (distance_on_map / distance_on_earth) * tile_size
pixels
640/pixels
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    print(grid_shapefile)
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
grid_folder_path = 'data/raw/grid' # Path to the folder containing grid files
# Get a list of grid files in the folder
grid_files = [file for file in os.listdir(grid_folder_path) if file.endswith('.shp')]

# Convert each grid file to a binary mask and combine them
grid_mask = None
for grid_file in grid_files:
    grid_shapefile = gpd.read_file(os.path.join(grid_folder_path, grid_file))
    print(grid_shapefile.dropna())
    for i in range(len(grid_shapefile.geometry)):
        print(grid_shapefile.geometry[i])
        grid_mask_single = geometry_mask(i, out_shape=dataset[0].shape[:2], transform=rasterio.Affine(1, 0, 0, 0, 1, 0), invert=True)
    #if grid_mask is None:
    #    grid_mask = grid_mask_single
    #else:
    #    grid_mask |= grid_mask_single
    print(sum(sum(grid_mask_single)))
# Apply the mask to crop the images
#cropped_images = []
#for channel in range(images.shape[2]):
#    cropped_image = images[:, :, channel] * grid_mask
#    print('cropped_image:',len(cropped_image))
#    cropped_images.append(cropped_image)
#    print('cropped_images:',len(cropped_images))

    #return np.stack(cropped_images, axis=2)
import fiona

# Open the shapefile
with fiona.open("grid.shp", "r") as grid_file:
    num_cells_x = len(set(feature["properties"]["x"] for feature in grid_file))
    num_cells_y = len(set(feature["properties"]["y"] for feature in grid_file))

print("Number of cells in x dimension:", num_cells_x)
print("Number of cells in y dimension:", num_cells_y)
import fiona

# Open the shapefile
with fiona.open("C:\Users\DELL\Documents\Github\kanyan\data\raw\grid\grid_Eldoret.shp", "r") as grid_file:
    num_cells_x = len(set(feature["properties"]["x"] for feature in grid_file))
    num_cells_y = len(set(feature["properties"]["y"] for feature in grid_file))

print("Number of cells in x dimension:", num_cells_x)
print("Number of cells in y dimension:", num_cells_y)
import fiona

# Open the shapefile
with fiona.open("C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp", "r") as grid_file:
    num_cells_x = len(set(feature["properties"]["x"] for feature in grid_file))
    num_cells_y = len(set(feature["properties"]["y"] for feature in grid_file))

print("Number of cells in x dimension:", num_cells_x)
print("Number of cells in y dimension:", num_cells_y)
import fiona

# Open the shapefile
with fiona.open("C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp", "r") as grid_file:
    schema = grid_file.schema
    attribute_names = [field[0] for field in schema["properties"].items()]
    num_cells_x = len(set(feature["properties"][attribute_names[0]] for feature in grid_file))
    num_cells_y = len(set(feature["properties"][attribute_names[1]] for feature in grid_file))

print("Number of cells in x dimension:", num_cells_x)
print("Number of cells in y dimension:", num_cells_y)
for filename in os.listdir(folder_path):
    if filename.endswith(".shp") and city_name in filename:
        shapefile_path = os.path.join(folder_path, filename)
        # Open the shapefile using geopandas
        gdf = gpd.read_file(shapefile_path)
        # Get the number of cells in x and y dimensions
        num_cells_x = len(set(gdf["x_attribute"]))
        num_cells_y = len(set(gdf["y_attribute"]))
        print("Shapefile:", filename)
        print("Number of cells in x dimension:", num_cells_x)
        print("Number of cells in y dimension:", num_cells_y)
        print()
folder_path = 'data/raw/grid'
for filename in os.listdir(folder_path):
    if filename.endswith(".shp"):
        shapefile_path = os.path.join(folder_path, filename)
        # Open the shapefile using geopandas
        gdf = gpd.read_file(shapefile_path)
        # Get the number of cells in x and y dimensions
        num_cells_x = len(set(gdf["x_attribute"]))
        num_cells_y = len(set(gdf["y_attribute"]))
        print("Shapefile:", filename)
        print("Number of cells in x dimension:", num_cells_x)
        print("Number of cells in y dimension:", num_cells_y)
        print()
folder_path = 'data/raw/grid'
for filename in os.listdir(folder_path):
    if filename.endswith(".shp"):
        shapefile_path = os.path.join(folder_path, filename)
        # Open the shapefile using geopandas
        gdf = gpd.read_file(shapefile_path)
        # Get the number of cells in x and y dimensions
        #num_cells_x = len(set(gdf["x_attribute"]))
        #num_cells_y = len(set(gdf["y_attribute"]))
        #print("Shapefile:", filename)
        #print("Number of cells in x dimension:", num_cells_x)
        #print("Number of cells in y dimension:", num_cells_y)
        #print()
gdf
fiona
import rasterio
for filename in os.listdir(folder_path):
    if filename.endswith(".shp"):
        shapefile_path = os.path.join(folder_path, filename)
        
        # Open the shapefile
        with rasterio.open(shapefile_path) as grid_file:
            num_cells_x = grid_file.width
            num_cells_y = grid_file.height
            #num_cells_x = len(set(feature["properties"][attribute_names[0]] for feature in grid_file))
            #num_cells_y = len(set(feature["properties"][attribute_names[1]] for feature in grid_file))

        print("Shapefile:", filename)
        print("Number of cells in x dimension:", num_cells_x)
        print("Number of cells in y dimension:", num_cells_y)
        print()
import rasterio
for filename in os.listdir(folder_path):
    if filename.endswith(".shp"):
        shapefile_path = os.path.join(folder_path, filename)
        
        # Open the shapefile
        with rasterio.open('data/raw/grid/grid_Eldoret.shp') as grid_file:
            num_cells_x = grid_file.width
            num_cells_y = grid_file.height
            #num_cells_x = len(set(feature["properties"][attribute_names[0]] for feature in grid_file))
            #num_cells_y = len(set(feature["properties"][attribute_names[1]] for feature in grid_file))

        print("Shapefile:", filename)
        print("Number of cells in x dimension:", num_cells_x)
        print("Number of cells in y dimension:", num_cells_y)
        print()
import fiona

# Open the shapefile
with fiona.open("C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp", "r") as grid_file:
    schema = grid_file.schema
    attribute_names = [field[0] for field in schema["properties"].items()]
    num_cells_x = len(set(feature["properties"][attribute_names[0]] for feature in grid_file))
    num_cells_y = len(set(feature["properties"][attribute_names[1]] for feature in grid_file))

print("Number of cells in x dimension:", num_cells_x)
print("Number of cells in y dimension:", num_cells_y)
attribute_names
schema
attribute_names[1]
for filename in os.listdir(shapefile_folder):
        if filename.endswith('.shp'):
            shapefile_path = os.path.join(shapefile_folder, filename)
            city_name = os.path.splitext(filename)[0][len('grid_'):]
            city_grids = gpd.read_file(shapefile_path)
            
             # Extract the bounding box coordinates
            grid_bbox = city_grids.geometry.bounds
for filename in os.listdir(folder_path):
        if filename.endswith('.shp'):
            shapefile_path = os.path.join(shapefile_folder, filename)
            city_name = os.path.splitext(filename)[0][len('grid_'):]
            city_grids = gpd.read_file(shapefile_path)
            
             # Extract the bounding box coordinates
            grid_bbox = city_grids.geometry.bounds
for filename in os.listdir(folder_path):
        if filename.endswith('.shp'):
            shapefile_path = os.path.join(folder_path, filename)
            city_name = os.path.splitext(filename)[0][len('grid_'):]
            city_grids = gpd.read_file(shapefile_path)
            
             # Extract the bounding box coordinates
            grid_bbox = city_grids.geometry.bounds
grid_bbox
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)
height
height/100
width/100
for filename in os.listdir(folder_path):
        if filename.endswith('.shp'):
            shapefile_path = os.path.join(folder_path, filename)
            city_name = os.path.splitext(filename)[0][len('grid_'):]
            city_grids = gpd.read_file(shapefile_path)
            
             # Extract the bounding box coordinates
            grid_bbox = city_grids.geometry.bounds
            height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
            width = max(grid_bbox.maxx) - min(grid_bbox.minx)
            print(height, width)
import rasterio
grid_folder_path = 'data/raw/grid'    
for filename in os.listdir(grid_folder_path):
    if filename.endswith(".shp")  and city_name in filename:
        shapefile_path = os.path.join(folder_path, filename)
        city_grids = gpd.read_file(shapefile_path)
        with rasterio.open(shapefile_path) as dataset:
            # Read the raster image as a numpy array
            image_array = dataset.read(1)

            # Reshape the image array to a 2D array
            reshaped_array = image_array.reshape(-1, 1)
            # Convert the reshaped array to a DataFrame
            df = pd.DataFrame(reshaped_array, columns=['Value'])
            out_file = (
                Path(c.sample_dir) 
                / f"label_{city}.pkl"
            )
            # Save the DataFrame as a CSV file
            df.to_csv(csv_path, index=False)
import geopandas as gpd
import rasterio
from rasterio.transform import from_origin

def shapefile_to_image(shapefile_path, image_path):
    # Read the shapefile using geopandas
    gdf = gpd.read_file(shapefile_path)
    
    # Create a new raster image using rasterio
    rows = cols = 1000  # Define the desired image dimensions
    transform = from_origin(gdf.bounds.minx, gdf.bounds.maxy, (gdf.bounds.maxx - gdf.bounds.minx) / cols, (gdf.bounds.maxy - gdf.bounds.miny) / rows)
    
    # Write the shapefile geometry to the raster image
    with rasterio.open(image_path, 'w', driver='GTiff', height=rows, width=cols, count=1, dtype='uint8', crs=gdf.crs, transform=transform) as dataset:
        for geometry in gdf.geometry:
            rasterize_value = 255  # Set the pixel value for the shape
            rasterio.features.geometry_mask([geometry], out_shape=(rows, cols), transform=transform, invert=True, default_value=rasterize_value, dtype='uint8', all_touched=True, nodata=0, filled=True, out=dataset.read(1))
import rasterio
grid_folder_path = 'data/raw/grid'    
for filename in os.listdir(grid_folder_path):
    if filename.endswith(".shp")  and city_name in filename:
        shapefile_path = os.path.join(folder_path, filename)
        city_grids = gpd.read_file(shapefile_path)
        with rasterio.open(shapefile_path) as dataset:
            # Read the raster image as a numpy array
            image_array = dataset.read(1)

            # Reshape the image array to a 2D array
            reshaped_array = image_array.reshape(-1, 1)
            # Convert the reshaped array to a DataFrame
            df = pd.DataFrame(reshaped_array, columns=['Value'])
            out_file = (
                Path(c.sample_dir) 
                / f"label_{city}.pkl"
            )
            # Save the DataFrame as a CSV file
            df.to_csv(csv_path, index=False)
import geopandas as gpd
import rasterio
from rasterio.transform import from_origin

def resize_images(im, folder_path, city_name):
    
    # Iterate over shapefiles in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".shp")  and city_name in filename:
            shapefile_path = os.path.join(folder_path, filename)

            city_grids = gpd.read_file(shapefile_path)
            
             # Extract the bounding box coordinates
            grid_bbox = city_grids.geometry.bounds
            num_cells_x =  int((max(grid_bbox.maxx) - min(grid_bbox.minx)) / 100)
            num_cells_y = int((max(grid_bbox.maxy) - min(grid_bbox.miny))/100)

            images_resized = skimage.transform.resize(np.array(im), (num_cells_x, num_cells_y), mode="constant", anti_aliasing=True)
            images = np.stack(images_resized, axis=0)
            return images
import geopandas as gpd
import rasterio
from rasterio.transform import from_origin

def shapefile_to_image(shapefile_path, image_path):
    # Read the shapefile using geopandas
    city_grids = gpd.read_file(shapefile_path)
            
     # Extract the bounding box coordinates
    grid_bbox = city_grids.geometry.bounds
    num_cells_x =  int((max(grid_bbox.maxx) - min(grid_bbox.minx)) / 100)
    num_cells_y = int((max(grid_bbox.maxy) - min(grid_bbox.miny))/100)

    
    # Create a new raster image using rasterio
    
    transform = from_origin(gdf.bounds.minx, gdf.bounds.maxy, (gdf.bounds.maxx - gdf.bounds.minx) / cols, (gdf.bounds.maxy - gdf.bounds.miny) / rows)
    
    # Write the shapefile geometry to the raster image
    with rasterio.open(image_path, 'w', driver='GTiff', height=num_cells_y, width=num_cells_x, count=1, dtype='uint8', crs=gdf.crs, transform=transform) as dataset:
        for i in range(len(gdf.geometry)):
            rasterize_value = gdf.val_persqm[i] 
            rasterio.features.geometry_mask([gdf.geometry[i]], out_shape=(num_cells_y, num_cells_x), transform=transform, invert=True, default_value=rasterize_value, dtype='uint8', all_touched=True, filled=True, out=dataset.read(1))
import geopandas as gpd
import rasterio
from rasterio.transform import from_origin

def shapefile_to_image(shapefile_path, image_path):
    # Read the shapefile using geopandas
    city_grids = gpd.read_file(shapefile_path)
            
     # Extract the bounding box coordinates
    grid_bbox = city_grids.geometry.bounds
    num_cells_x =  int((max(grid_bbox.maxx) - min(grid_bbox.minx)) / 100)
    num_cells_y = int((max(grid_bbox.maxy) - min(grid_bbox.miny))/100)

    
    # Create a new raster image using rasterio
    
    transform = from_origin(gdf.bounds.minx, gdf.bounds.maxy, (gdf.bounds.maxx - gdf.bounds.minx) / cols, (gdf.bounds.maxy - gdf.bounds.miny) / rows)
    
    # Write the shapefile geometry to the raster image
    with rasterio.open(image_path, 'w', driver='GTiff', height=num_cells_y, width=num_cells_x, count=1, dtype='uint8', crs=city_grids.crs) as dataset:
        for i in range(len(gdf.geometry)):
            rasterize_value = gdf.val_persqm[i] 
            rasterio.features.geometry_mask([gdf.geometry[i]], out_shape=(num_cells_y, num_cells_x), transform=transform, invert=True, default_value=rasterize_value, dtype='uint8', all_touched=True, filled=True, out=dataset.read(1))
import rasterio
grid_folder_path = 'data/raw/grid'    
for filename in os.listdir(grid_folder_path):
    if filename.endswith(".shp")  and city_name in filename:
        shapefile_path = os.path.join(folder_path, filename)
        city_grids = gpd.read_file(shapefile_path)
        
         # Extract the bounding box coordinates
        grid_bbox = city_grids.geometry.bounds
        num_cells_x =  int((max(grid_bbox.maxx) - min(grid_bbox.minx)) / 100)
        num_cells_y = int((max(grid_bbox.maxy) - min(grid_bbox.miny))/100)
        with rasterio.open(shapefile_path) as dataset:
            # Read the raster image as a numpy array
            image_array = dataset.read(1)

            # Reshape the image array to a 2D array
            reshaped_array = image_array.reshape(-1, 1)
            # Convert the reshaped array to a DataFrame
            df = pd.DataFrame(reshaped_array, columns=['Value'])
            out_file = (
                Path(c.sample_dir) 
                / f"label_{city}.pkl"
            )
            # Save the DataFrame as a CSV file
            df.to_csv(csv_path, index=False)
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)
gdf
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

import rasterio
from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    "path/to/output/raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

# Rasterize the shapefile geometry
shapes = (gdf.geometry, gdf.val_persqm)
rasterio.features.rasterize(shapes, out_shape=raster.shape, fill=0, out=raster.read(1))
raster.close()

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

import rasterio
from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    #"path/to/output/raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

# Rasterize the shapefile geometry
shapes = (gdf.geometry, gdf.val_persqm)
rasterio.features.rasterize(shapes, out_shape=raster.shape, fill=0, out=raster.read(1))
raster.close()

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    "C:\Users\DELL\Documents\Github\kanyan\data\int\img_matrices\raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

# Rasterize the shapefile geometry
shapes = (gdf.geometry, gdf.val_persqm)
rasterio.features.rasterize(shapes, out_shape=raster.shape, fill=0, out=raster.read(1))
raster.close()

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    "C:/Users/DELL/Documents/Github/kanyan/data/int/img_matrices/raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

# Rasterize the shapefile geometry
shapes = (gdf.geometry, gdf.val_persqm)
rasterio.features.rasterize(shapes, out_shape=raster.shape, fill=0, out=raster.read(1))
raster.close()

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    "C:/Users/DELL/Documents/Github/kanyan/data/int/img_matrices/raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

# Rasterize the shapefile geometry
shapes = [(gdf.geometry[i], gdf.val_persqm[i]) for i in 1:length(gdf.geometry)]
rasterio.features.rasterize(shapes, out_shape=raster.shape, fill=0, out=raster.read(1))
raster.close()

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    "C:/Users/DELL/Documents/Github/kanyan/data/int/img_matrices/raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

# Rasterize the shapefile geometry
shapes = [(gdf.geometry[i], gdf.val_persqm[i]) for i in range(len(gdf.geometry))]
rasterio.features.rasterize(shapes, out_shape=raster.shape, fill=0, out=raster.read(1))
raster.close()

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data
raster = rasterio.open(
    "C:/Users/DELL/Documents/Github/kanyan/data/int/img_matrices/raster.tif",
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=1,
    dtype=rasterio.uint8,
    crs=gdf.crs,
    transform=rasterio.Affine(1, 0, 0, 0, 1, 0)
)

with rasterio.open(raster_file) as src:
    # Read the raster data
    raster = src.read(1)
    # Get the shape of the raster
    out_shape = raster.shape

    # Create an empty numpy array with the same shape as the raster
    rasterized_array = np.zeros(out_shape, dtype=np.uint8)

    # Rasterize the shapefile geometry into the numpy array
    shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
    rasterized = rasterize(shapes, out_shape=out_shape, fill=0, default_value=255)
    np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = (max(grid_bbox.maxy) - min(grid_bbox.miny))
width = max(grid_bbox.maxx) - min(grid_bbox.minx)

from rasterio.features import geometry_mask


# Create a new raster to store the shapefile data

raster_file = "C:/Users/DELL/Documents/Github/kanyan/data/int/img_matrices/raster.tif",


with rasterio.open(raster_file) as src:
    # Read the raster data
    raster = src.read(1)
    # Get the shape of the raster
    out_shape = raster.shape

    # Create an empty numpy array with the same shape as the raster
    rasterized_array = np.zeros(out_shape, dtype=np.uint8)

    # Rasterize the shapefile geometry into the numpy array
    shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
    rasterized = rasterize(shapes, out_shape=out_shape, fill=0, default_value=255)
    np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = height(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

with rasterio.open(raster_file) as src:
    # Read the raster data
    raster = src.read(1)
    # Get the shape of the raster
    out_shape = raster.shape

    # Create an empty numpy array with the same shape as the raster
    rasterized_array = np.zeros(out_shape, dtype=np.uint8)

    # Rasterize the shapefile geometry into the numpy array
    shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
    rasterized = rasterize(shapes, out_shape=out_shape, fill=0, default_value=255)
    np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = height(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

# Rasterize the shapefile geometry into the numpy array
shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
rasterized = rasterize(shapes, out_shape=out_shape, fill=0, default_value=255)
np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = int(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

# Rasterize the shapefile geometry into the numpy array
shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
rasterized = rasterize(shapes, out_shape=out_shape, fill=0, default_value=255)
np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = int(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

# Rasterize the shapefile geometry into the numpy array
shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
rasterized = rasterize(shapes, out_shape=output_image,shape, fill=0, default_value=255)
np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = int(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

# Rasterize the shapefile geometry into the numpy array
shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
rasterized = rasterize(shapes, out_shape=output_image.shape, fill=0, default_value=255)
np.copyto(rasterized_array, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = int(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

# Rasterize the shapefile geometry into the numpy array
shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
rasterized = rasterize(shapes, out_shape=output_image.shape, fill=0, default_value=255)
np.copyto(output_image, rasterized)

print("Image saved successfully.")
import rasterio
import geopandas as gpd
from rasterio.features import rasterize

# Load the shapefile using geopandas
shapefile_path = 'C:/Users/DELL/Documents/Github/kanyan/data/raw/grid/grid_Eldoret.shp'
gdf = gpd.read_file(shapefile_path)

# Specify the output image size and resolution
grid_bbox = gdf.geometry.bounds
height = int(max(grid_bbox.maxy) - min(grid_bbox.miny))
width = int(max(grid_bbox.maxx) - min(grid_bbox.minx))

from rasterio.features import geometry_mask


# Create a new raster image with the desired size and resolution
output_image = np.zeros((height, width), dtype=np.uint8)

# Rasterize the shapefile geometry into the numpy array
shapes = [(geom, value) for geom, value in zip(gdf.geometry, gdf.val_persqm)]
rasterized = rasterize(shapes, out_shape=output_image.shape, fill=0, default_value=255)
np.copyto(output_image,rasterized.astype(np.uint8))

print("Image saved successfully.")
output_image

import os
import numpy as np
import pandas as pd

# Specify the folder containing the subfolders with .npz files
folder_path = "C:\\Users\\DELL\\Documents\\Github\\kanyan\\Kenya-Land-Value\\data\\int\\feature_matrix\\nightlight2013"

# Specify the path to the output concatenated .npz file
output_file = "C:\\Users\\DELL\\Documents\\Github\\kanyan\\Kenya-Land-Value\\data\\int\\applications\\lightnight\\concatenated_nightlight_2013_16.csv"

# Initialize an empty list to store the arrays
data = {
        "X": [],
        "latlon": [],
        "City": []
    }


for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    # Check if the item in the folder is a file with .npz extension
    if os.path.isfile(file_path) and file.endswith(".pkl"):
        # Extract the city name from the file name
        city_name = file.split("_")[0]
        # Load the array from the .npz file and append to the list
        loaded_data = np.load(file_path)
        data_array = loaded_data['X']  # Replace 'array_name' with the actual array name
        data['X'].append(data_array)
        data_latlon = loaded_data['latlon']
        data['latlon'].append(data_latlon)
        data['City'] = city_name



# Concatenate the arrays
concatenated_df = pd.DataFrame(data)
# Save the concatenated df to csv file
concatenated_df.to_csv(output_file, index=False)
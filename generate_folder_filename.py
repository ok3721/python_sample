import os
import pandas as pd
# Path of the directory
directory = "C:\\Users\\"

# Get all the files in the directory
files = os.listdir(directory)

# Create a list to store the full paths
file_paths = []

# Iterate over the list of files
for file in files:
    # Concatenate the file name and the directory path
    file_path = os.path.join(directory, file)
  
    file_paths.append(file_path)

print(file_paths)

df = pd.DataFrame(file_paths, columns=['name'])

df.to_excel("D:/test1.xlsx", index=False)

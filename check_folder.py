import os
import shutil

source_folder = 'C:\\path\\to\\source\\folder'
destination_folder = 'C:\\path\\to\\destination\\folder'

if os.listdir(source_folder):
    files = os.listdir(source_folder)
    for f in files:
        shutil.move(os.path.join(source_folder, f), os.path.join(destination_folder, f))
    print(f'Moved {len(files)} files from {source_folder} to {destination_folder}')
else:
    print(f'{source_folder} is empty')

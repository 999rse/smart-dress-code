import argparse
import os
import random
import shutil
import zipfile


parser = argparse.ArgumentParser(
    prog='Data aggregator',
    description='Aggregate datasets in zip extension from folder `raw` to `precessed` and split on train and valid parts'
)

parser.add_argument('-r', '--raw_folder', help='Path to folder with raw data (exmp. datasets.zip)')
parser.add_argument('-i', '--internal_folder', help='Path to folder where will be contains internal data')
parser.add_argument('-p', '--processed_folder', help='Path to folder where will be contain final data (splitted on train & valid parts)')
parser.add_argument('-t', '--trainp', type=float, default=0.8, help='Number from 0 to 1 represent the proportion of the dataset to include in the train split (default=0.8)')

args = parser.parse_args()

args.raw_folder = os.path.abspath(args.raw_folder)
args.internal_folder = os.path.abspath(args.internal_folder)
args.processed_folder = os.path.abspath(args.processed_folder)

# Create not existing folders
os.makedirs(args.internal_folder, exist_ok=True)
os.makedirs(args.processed_folder, exist_ok=True)


# Recursively unzip into `internal`` folder
for file_name in os.listdir(args.raw_folder):
    file_path = os.path.join(args.raw_folder, file_name)

    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(args.internal_folder)


# Get a list of all files inside the source folder and its subfolders
all_files = []
for foldername, subfolders, filenames in os.walk(args.internal_folder):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        all_files.append(file_path)

# Copy files from list to  destination folder
for file_path in all_files:
    shutil.copy(file_path, args.internal_folder)


# Remove not pairs file

# Get list of all files in folder
all_files = os.listdir(args.internal_folder)

# Create set for storage name of files and their extentions: .png/.jpg & .txt
png_jpg_files = set()
txt_files = set()

# Walk by all files and add their names (without ext.) in existing sets 
for file_name in all_files:
    name, extension = os.path.splitext(file_name)
    if extension in (".png", ".jpg"):
        png_jpg_files.add(name)
    elif extension == ".txt":
        txt_files.add(name)

# Define files that have a pair .png/.jpg, also .txt
files_with_pair = png_jpg_files.intersection(txt_files)

# Walk by all files and delete that doesn't have a pair 
for file_name in all_files:
    name, extension = os.path.splitext(file_name)
    if extension in (".png", ".jpg") and name not in files_with_pair:
        file_path = os.path.join(args.internal_folder, file_name)
        os.remove(file_path)


# Split to train and valid data

# Path to "train" folder
train_folder = os.path.join(args.processed_folder, 'train')
# Path to "valid" folder
valid_folder = os.path.join(args.processed_folder, 'valid')

# Create subfolders images' and 'labels' in 'train'
os.makedirs(os.path.join(train_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(train_folder, "labels"), exist_ok=True)

# Create subfolders 'images' and 'labels' in 'valid'
os.makedirs(os.path.join(valid_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(valid_folder, "labels"), exist_ok=True)

# Get list of files (images and txt files) in source folder
all_files_i = [f for f in os.listdir(args.internal_folder) if os.path.isfile(os.path.join(args.internal_folder, f))]

# Shuffle files
random.shuffle(all_files_i)

# Define which percentage of files will be in "train"
num_train_files = int(len(all_files_i) * args.trainp)

# Split on 'train' and 'test'
train_files = all_files_i[:num_train_files]
valid_files = all_files_i[num_train_files:]

# Copy files into relevant folders 
def copy_files(list_files, path2folder):
    for file_name in list_files:
        source_path = os.path.join(args.internal_folder, file_name)
        if file_name.endswith(".png") or file_name.endswith(".jpg", ):
            shutil.move(source_path, os.path.join(path2folder, "images"))
        elif file_name.endswith(".txt"):
            shutil.move(source_path, os.path.join(path2folder, "labels"))


copy_files(train_files, train_folder)
copy_files(valid_files, valid_folder)

print("Don't forget add data.yaml to datasets/processed that define type and number of classes in common dataset's")
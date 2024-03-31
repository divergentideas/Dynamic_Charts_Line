import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
import argparse

from matplotlib.image import imread
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.ticker as ticker

from skimage.transform import resize

# Add argument parsing
parser = argparse.ArgumentParser(description="Create a video from images.")
parser.add_argument("name", type=str, help="The name of the output file")
parser.add_argument("time", type=float, help="Time interval in seconds for each frame") # Changed type to float
args = parser.parse_args()

name = args.name
time = args.time

x = 1 / time * 60
fps = int(x * 34)
print("images were saved in images/export_all")
image = cv2.imread('images/export_all/0.png')
height, width, _ = image.shape

# Check if videos name does exist, then delete it before create new Videos
file_path='videos/'+name+'.mp4'
# if os.path.exists(file_path):
#     os.remove(file_path)

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(file_path, fourcc, fps, (width, height))

# Set the path to the images folder
path = 'Images/export_all'
# Loop through all the images in the folder
    # Loop through the images and write them to the video
x=(2060)
start=5
for i in range(start, start+x):
    year_check=str(i)
    image = cv2.imread(f'images/export_all/'+year_check+'.png')
    out.write(image)
    print(str(i))
print(file_path)
# Release the video writer
out.release()

import os
from PIL import Image, ImageFilter


# path

path_img_folder = "images/"
output_folder = "png image/"


# check is png image/exists if not created

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# loop in folder

for file_name in os.listdir(path_img_folder):
    img = Image.open(f"{path_img_folder}{file_name}")
    # adding filters
    filter_image = img.filter(ImageFilter.BLUR)
    name_without_extension = os.path.splitext(file_name)[0]
    filter_image.save(f"{output_folder}{name_without_extension}.png", "png")

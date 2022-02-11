"""
File: candy.py
Author: Jonathan Wright

Purpose: green screen.
"""

# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("img/beach.jpg")
image_object = Image.open("img/hiker.jpg")

w, h = image_original.size
pixels_original = image_original.load()
pixels_object = image_object.load()

image_new = Image.new("RGB", image_original.size)
pixels_new = image_new.load()

for j in range(w):
    for i in range(h):
        r,g,b = pixels_object[j,i]
        # print(r,g,b)
        if(r < 90 and g > 180 and b < 90):
            # print(pixels_object[j,i])
            pixels_new[j,i] = pixels_original[j,i]
        else:
            pixels_new[j,i] = pixels_object[j,i]

image_new.save("img/newimg.jpg")
image_new.show()

# print(pixels_object[0,0])

# This line attempts to open a new window to display the image.
# image_original.show()
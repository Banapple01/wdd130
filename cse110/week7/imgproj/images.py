"""
File: candy.py
Author: Jonathan Wright

Purpose: green screen.
"""

# This line imports or includes the library we will need
from PIL import Image

backgrounds = ["beach","desert","earth","field","forest","snowscape","sunset"]
replace = ["boat","cactus","cat_small","cat","harvester","hiker","penguin","spaceshuttle"]

input1 = ""
input2 = ""

while backgrounds.__contains__(input1) == False:
    for b in backgrounds:
        print(f'Opt: {b}')
    input1 = input("What background image would you like? ").lower()
    
while replace.__contains__(input2) == False:
    for r in replace:
        print(f'Opt: {r}')
    input2 = input("What replacement image would you like? ").lower()

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open(f"img/{input1}.jpg")
image_object = Image.open(f"img/{input2}.jpg")

w, h = image_original.size
pixels_original = image_original.load()
pixels_object = image_object.load()

image_new = Image.new("RGB", image_original.size)
pixels_new = image_new.load()

for j in range(w):
    for i in range(h):
        r,g,b = pixels_object[j,i]
        # print(r,g,b)
        if(r < 90 and g > 160 and b < 90):
            # print(pixels_object[j,i])
            pixels_new[j,i] = pixels_original[j,i]
        else:
            pixels_new[j,i] = pixels_object[j,i]

image_new.save("img/newimg.jpg")
image_new.show()

# print(pixels_object[0,0])

# This line attempts to open a new window to display the image.
# image_original.show()
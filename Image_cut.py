"""
Cut the Breast Cancer JPEG img into blocks
And then store the cuts
The blocks is used for training
"""

import numpy as np
from PIL import Image
dir_folder = r'C:\Users\nctu\Desktop\svs_scanner\cut_image'

# cut the svs image into blocks, each block has the block size block_size
def image_cut(img):
    filename = 0
    block_size = 200
    print (img.size)
    img_h = img.size[0]
    img_w = img.size[1]
    for r in range(0, img_w, block_size):
        for c in range(0, img_h, block_size):
          img = im.crop((c, r, c + block_size, r + block_size))
          img.save(str(dir_folder)+ '\\' + str(filename) + ".png")
          filename += 1

im = Image.open("myimg.png")
print (im.size)
image_cut(im)
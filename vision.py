# from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp

import numpy as np
import pathlib
from PIL import Image, ImageFilter
import glob
import os
from sys import argv


def items_display():
    # Open and display all the files in a directory
    files = pathlib.WindowsPath(r"")
    for path in files.iterdir():
        if path.is_file():
            with Image.open(path) as im:
                print((im.getdata()))
                print("OK:")
                im.show()


# The next part of the code will be able to test and classify image which will requers a few more modules
def classify_images():
    list_colours = []


"""Root mean square error (RMSE),
Peak signal-to-noise ratio (PSNR),
Structural Similarity Index (SSIM),
Feature-based similarity index (FSIM),
Information theoretic-based Statistic Similarity Measure (ISSM),
Signal to reconstruction error ratio (SRE),
Spectral angle mapper (SAM)
Universal image quality index (UIQ)
IMM"""


def messy():
    # To get familiar with the functions and aspects of an image

    with Image.open("") as im:
        print("get bands: ", im.getbands())
    with Image.open("") as im:
        print("get box: ", im.getbbox())
    with Image.open("") as im:
        print("get channel: ", np.array(im.getchannel(1))) # Get the value of the blue, red and green of each pixel
    with Image.open("") as im:
        print((im.getdata()))
    with Image.open("") as im:
        print((im.getcolors()))
    with Image.open("") as im:
        print((im.getdata()))
    with Image.open("") as im:
        print((im.getpixel((4, 5))))
    with Image.open("") as im:
        print(im.info)
        print(im.width * im.height) # Get the number of pixels


def check_rgb(image_path):
    with Image.open(image_path) as img:
        if img.getbands() == ('R', 'G', 'B'):
            print("Equals")
        else:
            print("Not equal")




messy()

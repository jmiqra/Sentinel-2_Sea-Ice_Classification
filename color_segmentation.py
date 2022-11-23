#!/usr/bin/python3

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_rgb_dist(img):

    # extract the red, green and blue pixels from the picture
    r, g, b = cv2.split(img)

    # Plot the range of the pixels
    # create a plot
    fig = plt.figure()
    fig.set_figheight(7) # 1.18in or 3cm
    fig.set_figwidth(12) # 2.75in or 7cm
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    # extract the total number of pixels
    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    plt.show()

def show_hsv_dist(img):
    # convert RGB to HSV
    hsv_nemo = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # extract the hue, saturation, and value
    h, s, v = cv2.split(hsv_nemo)

    fig = plt.figure()
    fig.set_figheight(7) # 1.18in or 3cm
    fig.set_figwidth(12) # 2.75in or 7cm
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    # extract the total number of pixels
    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")
    plt.show()

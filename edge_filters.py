import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("/Flower.jpg")
img = np.array(img,dtype=np.uint8)
def get_all_types_of_edges(img):
    laplace_kernel = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1],
    ])
    x_kernel = np.array([
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1],
    ])
    y_kernel = np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1],
    ])
    sharpen_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ])
    blur_kernel = (1/16) * np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
    ])

    # Laplace edges
    laplace_edges = cv2.filter2D(img, -1, laplace_kernel)
    x_edges = cv2.filter2D(img, -1, x_kernel)
    y_edges = cv2.filter2D(img, -1, y_kernel)
    sharp = cv2.filter2D(img, -1, sharpen_kernel)
    blur = cv2.filter2D(img, -1, blur_kernel)

    # Sobel edges
    sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
    sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    # Canny edges
    edges = cv2.Canny(image=img, threshold1=100, threshold2=200)

    laplace_edges_dict = {"Laplace": laplace_edges, "x_edges": x_edges, "y_edges": y_edges}
    sobel_edges_dict = {"Sobelx": sobelx, "Sobely": sobely, "Sobelxy": sobelxy}
    canny_edges_dict = {"Canny": edges}
    extra_filters_dict = {"Sharpen": sharp, "Blur": blur}

    return {"Laplace_edges": laplace_edges_dict, "Sobel_edges": sobel_edges_dict, "Canny_Edges": canny_edges_dict, "Extra_filters": extra_filters_dict}
def display_all(img):
  for k1 in img.keys():
    plt.figure()
    for k2 in img[k1].keys():
      print(k2)
      plt.imshow(img[k1][k2])
      plt.title(k1+"_"+k2)
      plt.show()
RGB_filter_outs = get_all_types_of_edges(img)
display_all(RGB_filter_outs)
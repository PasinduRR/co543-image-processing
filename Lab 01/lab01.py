import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('image.jpg')
print(img.shape)
plt.imshow(img)
plt.show() 

def imcomplement(img):
    return 1 - img

img2 = imcomplement(img)
plt.imshow(img2)
plt.show()
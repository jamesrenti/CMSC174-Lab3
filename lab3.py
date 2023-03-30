import cv2
import numpy as np
# import matplotlib as plt
import glob


path_count100 = glob.glob("C:/Users/Client/Desktop/lab03/IMAGES/100/*.jpg")
# path_count200 = glob.glob("C:/Users/Client/Desktop/lab03/IMAGES/200/*.jpg")
# path_count300 = glob.glob("C:/Users/Client/Desktop/lab03/IMAGES/300/*.jpg")
# path_count400 = glob.glob("C:/Users/Client/Desktop/lab03/IMAGES/400/*.jpg")

for file in path_count100:
    img = cv2.imread(file)
    cv2.imshow(img)
    cv2.waitKey()
    cv2.destroyAllWindows()
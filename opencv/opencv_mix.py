from django.conf import settings
import numpy as np
import cv2

# # def showImage():
# #     imgfile = '/Users/Public/python/testimage/1.jpg'
# #     img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

# #     cv2.imshow('model', img)
# #     cv2.waitKey(0)
# #     cv2.destroyAIIWindows()

# # showImage()

def opencv_mix(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    add_img1 = img1 + img2
    add_img2 = cv2.add(img1, img2)

    cv2.imwrite(imgfile1, add_img1)
    cv2.imwrite(imgfile2, add_img2)

        

import pickle as pl
import cv2
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import numpy as np

#img=mpimg.imread('D:\\000ASU\\Research\\line_detect\\dp\\full_CNN_labels.p')
#fr = open('C:\\Users\\LiQi\\Desktop\\20181016_deepLearn\\full_CNN_train.p','rb')
fr = open('DeepLearn-Lane-line-detection/full_CNN_labels.p','rb')
#fr = open('D:\\000ASU\\Research\\line_detect\\dp\\coeffs_train.p','rb')
#fr = open('D:\\000ASU\\Research\\line_detect\\dp\\coeffs_labels.p','rb')  
images = pl.load(fr)
fr.close()
img1 = images[50]

cv2.namedWindow('Image')
cv2.imshow('Image', img1)

cv2.imwrite("new_img_1.jpg", img1)

cv2.waitKey(0)

cv2.destroyAllWindows()
#print(data1)  
#data2 = pl.load(fr)  
#print(data2)  
#fr.close()  


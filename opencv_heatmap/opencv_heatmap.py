import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt#绘图库
img=cv.imread('1.png')#读文件

#img2=cv.imread('self.png')#读文件
#dst=cv.addweighted(img1,0.7,img2,0.3,0)#图像融合
#cv.imshow('dst',dst)#显示图像

#px=img[100,100]#获取这个像素的BGR的值
#print(px)
#blue=img[100,100,0]
#print(blue)#改变图像像素值1#img[50,200]=[255,255,255]#修改该点像素
#print(img[100,100])#cv.imshow('img',img)
#改变图像像素值2
#print(img.item(100,100,0))#0, 1, 2分别代表通道数，0代表Blue， 1代表Green， 2代表Red。
#print(img.item(100,100,1))
#print(img.item(100,100,2))
#img.itemset((10,10,0),0)#将(10,10)这点的蓝色通道值设为0
#print(img.item(10,10,0))#打印这点蓝色通道的值#img[:,:,0]=0#将整张图的蓝色通道值都设为0#cv.imshow('img',img)

#图像信息
#print(img.shape)#行，列，通道数，如果为灰度图像，则只有前两项
#print(img.size)#像素数目
#print(img.dtype)#数据类型

#图像ROI
#doa=img[300:350,200:250]
#img[400:450,300:350]=doa
#cv.imshow('img',img)

cv.waitKey(0)
cv.destroyAllWindows()
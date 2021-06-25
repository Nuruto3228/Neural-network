import numpy as np
import cv2
import network
im = cv2.imread("pic.img")
print(type(im))
a=[]
b=[]
for i in range(0,28):
	for j in range(0,28):
		if(im[i,j,1]==255):
			a.append(0)
			b.append(1)
		else:
			a.append(' ')
			b.append(0)
	print(' '.join(map(str, a)))
	a=[]

nw=
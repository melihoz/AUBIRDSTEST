import cv2
import numpy as np
import json
import re
import pandas as pd
import sys
import glob
import os
path2 = os.getcwd()
#Image locations here
json_fns = glob.glob("E:\\Melihoz\\yendata1\\yendata1\\**\\*.jpg",recursive=True)
numfiles=len(json_fns)
nf=0
#print(json_fns)
while (nf>=0 and nf<numfiles):
 z=json_fns[nf]
 image_name= os.path.basename(json_fns[nf])
 lent=len(image_name)
 print(z)
 image = cv2.imdecode(np.fromfile(json_fns[nf], dtype=np.uint8),
                   cv2.IMREAD_UNCHANGED)
# image=cv2.imread(json_fns[nf])


#Save location here
 path2="E:\\cropped\\"+z[3:-lent]
 if os.path.exists(path2)is False:
      os.makedirs(path2)
      #os.rename(path,path2)

 
 h,w,r =image.shape
#Change the split ratios for desired dimensions
 splitwidth=1024
 splitheight=600
 w1=int((w/splitwidth)+1)*splitwidth
 
 h1=int((h/splitheight)+1)*splitheight
 new_im = cv2.copyMakeBorder(image, 0, h1-h, 0, w1-w, cv2.BORDER_CONSTANT,
    value=0)
 i=0
 v=int(h1/splitheight)
 t=int(w1/splitwidth)

 while (i>=0 and i<v):
  
  
   y=0
   while (y>=0 and y<t):
    crop_img = new_im[i*splitheight:(i+1)*splitheight, y*splitwidth:(y+1)*splitwidth]
    filename=str(image_name[:-4])+str(i)+str(y)+".jpg"
    #cv2.imshow("asdsdasda",crop_img)
    #print(path+'\\'+filename,crop_img)
    is_success,im_buf_arr = cv2.imencode(".jpg", crop_img)
    im_buf_arr.tofile(path2+'\\'+filename)

 nf=nf+1
import cv2
import numpy as np
import json
import re
import pandas as pd
import sys
import glob
import os

import cv2
import numpy as np
import json
import re
import pandas as pd
import sys
import glob
import os
import csv

#THIS CODE ONLY WORKS FOR IMAGES SPLITTED WITH spliter.py in this folder.
json_fns = sorted(glob.glob("E:\\yendata\\yendata\\**\\*detected.jpg" ,recursive=True ))
#print(json_fns[0]+json_fns[1])
numfiles=len(json_fns)

nf=0
image=cv2.imread(json_fns[nf])
#getting stitch dimensions
hei,wei,r =image.shape
while (nf>=0 and nf<numfiles):
 nff=0
 z=json_fns[nf]
 image_name= os.path.basename(json_fns[nf])
 lent=len(image_name)
 base=z[:-lent]
 pathcsv=json_fns[nf][:-14]+"total.csv"
 with open(pathcsv,'r') as input_file:
    input=csv.reader(input_file,delimiter='\n')
    for line in input:
     birdcount=line[0]
 #print(nf)
 pathy="E:\\lastresults\\"+base[19:]+image_name[:-14]+"_"+str(birdcount)+".jpg"
 pathyy="E:\\lastresults\\"+base[19:]
# print(base[19:])
 if os.path.exists(pathyy)is False:
      os.makedirs(pathyy)
      #os.rename(path,path2)
 else:
  nf=nf+1
  continue
 json_fnsbase=sorted(glob.glob(base+"*detected.jpg",recursive=True))
 numfiless=len(json_fnsbase)
# print(json_fnsbase)
 
 while(nff>=0 and nff<numfiless):
 
  max=int(json_fnsbase[numfiless-1][-14:-12])
  
  He=int((max/10)+1)*hei
  We=((max%10)+1)*wei
  myimage = np.zeros((He,We,3),np.uint8)

  

 # img=cv2.imread(json_fnsbase[nff])
  img = cv2.imdecode(np.fromfile(json_fnsbase[nff], dtype=np.uint8),
                   cv2.IMREAD_UNCHANGED)
 # print(os.path.basename(json_fnsbase[nff]))
  for i in range(0,He,hei):
 
   for j in range (0,We,wei):
  
    for k in range (0,hei):
  
     for z in range (0,wei):   
      myimage[i+k][j+z]=img[k][z]
    
      if k==599 and z==1023:
       nff=nff+1
       if nff==numfiless:
        
        break
       img = cv2.imdecode(np.fromfile(json_fnsbase[nff], dtype=np.uint8),
                   cv2.IMREAD_UNCHANGED)
     # img=cv2.imread(json_fnsbase[nff])
       #print(nff)
       
 #print(nf)   
 nf=nf+1    #img=cv2.imread(json_fns[nf])  
 is_success,im_buf_arr = cv2.imencode(".jpg", myimage)
 im_buf_arr.tofile(pathy) 


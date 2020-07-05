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


#IMAGE AND CSV FILE LOCATIONS THIS CODE ASSUMES THEY ARE IN THE SAME FOLDER
json_fns = glob.glob("E:\\lastresults\**\\*.jpg", recursive=True)

 
 
 
print(json_fns)
numfiles=len(json_fns)

nf=0
while (nf>=0 and nf<numfiles):
 nff=0
 z=json_fns[nf]
 image_name= os.path.basename(json_fns[nf])
 lent=len(image_name)
 base=z[:-lent]
 linecounter=0
 print(json_fns[nf])
 pathcsv=json_fns[nf][:-4]+".csv"
 if os.path.exists(pathcsv)is False:
      nf=nf+1
      continue
      # #os.rename(path,path2)
 else:
     x=0
  
 img = cv2.imdecode(np.fromfile(json_fns[nf], dtype=np.uint8),
                   cv2.IMREAD_UNCHANGED)
  
 with open(pathcsv,'r') as input_file:
    input=csv.reader(input_file,delimiter=' ')
    totalbird=len((list(input)))-1
    totalbird=str(int(totalbird/4))
    input_file.close()
    
 with open(pathcsv,'r') as input_file:
    input=csv.reader(input_file,delimiter=' ')
    for line in input:
   
     
     if linecounter==0:
      linecounter+=1
    
      
      continue #ignoring first line for getting cordinates
    
     else:
      if linecounter%4==1:
       cordinates=line[0].split(",")
       #print(cordinates)
       xmin=int(cordinates[1])
       ymin=int(cordinates[2])
       #print("i was here"+str(xmin,ymin))
       linecounter+=1
      elif linecounter%4==2:
       linecounter+=1
      elif linecounter%4==3:
       linecounter+=1
      elif linecounter%4==0:
       cordinates=line[0].split(",")
       xmax=int(cordinates[1])
       ymax=int(cordinates[2])
       img = cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),3)
        #min cordinates, max cordinates, color, thickness
       linecounter+=1
 #print(nf)

 pathy=json_fns[nf][:-4]+"_"+totalbird+".jpg"#save path
 nf=nf+1    #img=cv2.imread(json_fns[nf])  
 is_success,im_buf_arr = cv2.imencode(".jpg", img)
 im_buf_arr.tofile(pathy)
 input_file.close()


import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import json
import glob 
sys.path.append("..")

import csv
from utils import label_map_util
from utils import visualization_utils as vis_util
CWD_PATH = os.getcwd()

MODEL_NAME = 'inference_graph'
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH,'inference_graph','labelmap.pbtxt')
#test location default is test folder in the project
json_fns = glob.glob(CWD_PATH+"\\test\\*.jpg",recursive=True)
print(json_fns)



numfiles=len(json_fns)
nf=0
totalbirds=0
while (nf>=0 and nf<numfiles):
 
 if nf>0: 
  basename2 = os.path.basename(json_fns[nf-1])
 lent=len(basename)
 PATH_TO_IMAGE = json_fns[nf]
 #results save location default is results folder in the project
 PATH_TO_SAVE_FOLDER=CWD_PATH+"\\results\\"
 PATH_TO_IMAGE_Detected = PATH_TO_SAVE_FOLDER+ basename[:-4]+"detected.jpg"
 PATH_TO_CSV = PATH_TO_SAVE_FOLDER+ basename[:-4]
 if nf>0:
  PATH_TO_TOTAL_CSV=PATH_TO_SAVE_FOLDER+basename2[:-6]  
 
 #If you want to use multi sub folder test set you can uncomment code below will save results to test image folder
 # PATH_TO_SAVE_FOLDER = json_fns[nf][:-lent]
 # PATH_TO_SAVE_FOLDER2 = json_fns[nf-1][:-lent]
 # PATH_TO_IMAGE_Detected = json_fns[nf][:-lent]+ basename[:-4]+"detected.jpg"
 # PATH_TO_CSV = PATH_TO_SAVE_FOLDER+ basename[:-4]
 # if nf>0:
  # PATH_TO_TOTAL_CSV=PATH_TO_SAVE_FOLDER2+basename2[:-6] 
      os.makedirs(PATH_TO_SAVE_FOLDER)
#if testing is aborted start from where you left
 if os.path.exists(PATH_TO_IMAGE_Detected)is True:
      nf=nf+1
      continue
      
                   cv2.IMREAD_UNCHANGED)
 h,w,r =image.shape
     h,
     w,
     PATH_TO_CSV,
 is_success,im_buf_arr = cv2.imencode(".jpg", image)
 im_buf_arr.tofile(PATH_TO_IMAGE_Detected)
 #cv2.imwrite(PATH_TO_IMAGE_Detected, image)
 if nf>0:
  if json_fns[nf][:-6]==json_fns[nf-1][:-6]:
   totalbirds=totalbirds+i
  else:
   with open(PATH_TO_TOTAL_CSV+"total.csv",'w') as output_file:
    datatot=[]
    datatot.append(totalbirds)
    out=csv.writer(output_file,lineterminator='\n')
    out.writerow(datatot)
    output_file.close()
    totalbirds=i
    
   
  

 nf=nf+1
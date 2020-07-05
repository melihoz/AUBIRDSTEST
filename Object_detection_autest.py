
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
  basename = os.path.basename(json_fns[nf])
 if nf>0: 
  basename2 = os.path.basename(json_fns[nf-1])
 lent=len(basename) #print(json_fns[nf])          
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
  # PATH_TO_TOTAL_CSV=PATH_TO_SAVE_FOLDER2+basename2[:-6]  if os.path.exists(PATH_TO_SAVE_FOLDER)is False:
      os.makedirs(PATH_TO_SAVE_FOLDER)
#if testing is aborted start from where you left
 if os.path.exists(PATH_TO_IMAGE_Detected)is True:
      nf=nf+1
      continue
         NUM_CLASSES = 1   label_map = label_map_util.load_labelmap(PATH_TO_LABELS) categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True) category_index = label_map_util.create_category_index(categories)   detection_graph = tf.Graph() with detection_graph.as_default():     od_graph_def = tf.GraphDef()     with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:         serialized_graph = fid.read()         od_graph_def.ParseFromString(serialized_graph)         tf.import_graph_def(od_graph_def, name='')      sess = tf.Session(graph=detection_graph)   image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')   detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')     detection_scores = detection_graph.get_tensor_by_name('detection_scores:0') detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')   num_detections = detection_graph.get_tensor_by_name('num_detections:0') image = cv2.imdecode(np.fromfile(PATH_TO_IMAGE, dtype=np.uint8),
                   cv2.IMREAD_UNCHANGED)
 h,w,r =image.shape #image = cv2.imread(PATH_TO_IMAGE)  image_expanded = np.expand_dims(image, axis=0)   (boxes, scores, classes, num) = sess.run(     [detection_boxes, detection_scores, detection_classes, num_detections],     feed_dict={image_tensor: image_expanded})    image,i=vis_util.visualize_boxes_and_labels_on_image_array(
     h,
     w,
     PATH_TO_CSV,     basename,     image,     np.squeeze(boxes),          np.squeeze(classes).astype(np.int32),     np.squeeze(scores),     category_index,     use_normalized_coordinates=True,     line_thickness=1,     min_score_thresh=0.8,     skip_labels=True,     skip_scores=True,     max_boxes_to_draw=800) # mydata_file = open("%s.json"%IMAGE_NAME[:-4],'w') # mydata_file.write(json.dumps(np.squeeze(scores).tolist())) # mydata_file.close()  #cv2.imshow('Object detector', image)
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
    
   
  
    #cv2.destroyAllWindows()
 nf=nf+1

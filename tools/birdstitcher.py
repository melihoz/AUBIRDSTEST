import os
import cv2
import numpy as np
import sys
import json
import glob 
import csv


json_fns = glob.glob("E:\\yendata\\yendata\\\**\\*[0-9][0-9].csv",recursive=True)
print(json_fns)
#print(json_fns)

#json_fns = glob.glob("E:\\dataset\\Melihoz\\kuslar\\atik\\sonbahar2013\\**\\*.jpg",recursive=True)
#print(json_fns)

numfiles=len(json_fns)
nf=0
totalbirds=0
databird=[]
totalbirdindexer=0

while (nf>=0 and nf<numfiles):
 csvname= os.path.basename(json_fns[nf])
 z=json_fns[nf]
 
 lent=len(csvname)
 lent2=lent-5
 base=z[:-lent]
 pathy="E:\\lastresults\\"+base[19:-(lent2)]+csvname[:-6]+".csv"
 x=0
 pathyy="E:\\lastresults\\"+base[19:]
 print(pathy)
 # if os.path.exists(pathy)is False:
      # #os.makedirs(pathyy)
      # #os.rename(path,path2)
      # x=x+1
 # else:
  # nf=nf+1
  # continue
 #IMAGE_NAME = os.path.basename(json_fns[nf]) 
 #lent=len(IMAGE_NAME)
 
#First csv file to load since there is no way to compare if image is changed base case written
 if nf==0:
  print(json_fns[nf])
  xm=int(json_fns[nf][-6:-4])%10
  #print(xm)
  ym=int(int(json_fns[nf][-6:-4])/10)
  #print(ym)
  with open(pathy,'w') as output_file:
    out=csv.writer(output_file,lineterminator='\n')
    data=[]
    data.append("id")
    data.append("x")
    data.append("y")
    out.writerow(data)
  with open(json_fns[nf],'r') as input_file:
    input=csv.reader(input_file,delimiter='\n')
    inputline=0
    for line in input:
     inputline+=1
     #print(line)
     if inputline==1:
      continue
     else:
      line=line[0].split(",")
      if totalbirdindexer%4==0:
       totalbirds+=1
       totalbirdindexer=0
      newline=[]
      newline.append("bird"+str(totalbirds))
      newline.append(int(line[1])+xm*1024) #normalizing cordinates here using the index of the image
      newline.append(int(line[2])+ym*600)
      totalbirdindexer+=1
      with open(pathy,'a') as output_file:
       out=csv.writer(output_file,lineterminator='\n') 
       out.writerow(newline)
  output_file.close()
  input_file.close()
  nf+=1
  continue
 else:
  if json_fns[nf][:-6]==json_fns[nf-1][:-6]:
   
   totalbirds=totalbirds
  else:
   
   totalbirds=0
   with open(pathy,'w') as output_file:
    out=csv.writer(output_file,lineterminator='\n')
    data=[]
    data.append("id")
    data.append("x")
    data.append("y")
    out.writerow(data)
   
  xm=int(json_fns[nf][-6:-4])%10
  ym=int(int(json_fns[nf][-6:-4])/10)
   
  with open(json_fns[nf],'r') as input_file:
    input=csv.reader(input_file,delimiter=' ')
    inputline=0
    for line in input:
     line=line[0].split(",")
     print(line)
     inputline+=1
     if inputline==1:
      continue
     else:
      if totalbirdindexer%4==0:
       totalbirds+=1
       totalbirdindexer=0
      newline=[]
      newline.append("bird"+str(totalbirds))
      newline.append(int(line[1])+xm*1024) #normalizing cordinates here using the index of the image
      newline.append(int(line[2])+ym*600)

      totalbirdindexer+=1
      with open(pathy,'a') as output_file:
       out=csv.writer(output_file,lineterminator='\n')
      
       out.writerow(newline)
  output_file.close()
  input_file.close()
  nf+=1
  continue
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:02:22 2018

@author: lilei0129
""" 

import cv2
import os  
  
def change_name(path1,path2, change):  #传入存储的list
	for file in os.listdir(path1):
            name =  os.path.join( file) 
            file_name = list(name)
            name_index = file_name.index('.')
            file_name = file_name[:name_index]
            file_name = ''.join(file_name)
            seg_name = file_name+'.png'
            file_name = file_name+'.jpg'
            file_name = os.path.join( change,file_name)
            seg_name = os.path.join( path2,seg_name)
            print file_name
            file_path = os.path.join( path1,file)  
            im = cv2.imread(file_path)
            cv2.imwrite(file_name,im)





def change_size(path1,path2, list_name):
	for file in os.listdir(path1):
            name =  os.path.join( file) 
            name = list(name)
            name_index = name.index('.')
            name = name[:name_index]
            name = ''.join(name)
            seg_name = name+'.png'
            seg_name =  os.path.join( path2,seg_name)  
            file_name = name+'.jpg'
            file_name =  os.path.join( path1,file_name) 
            seg_im = cv2.imread(seg_name)
            file_im = cv2.imread(file_name)

            sp1 = seg_im.shape
            sp2 = file_im.shape
            if sp1 != sp2:    
                sp = [name,sp1,sp2]
                sp_change =  sp2[::-1]
                res=cv2.resize(seg_im,sp_change,0)
                cv2.imwrite(seg_name,res)
                print sp
            
#            if os.path.isdir(file_name):
#                  os.listdir(file_name, list_name) 
#            else:
#                  list_name.append(file_name)


                		
path1 = "/opt/data1/lilei/Supervisely/people_segment/Images/train/"
path2 = "/opt/data1/lilei/Supervisely/people_segment/Segments/train/"
path3 = "/opt/data1/lilei/Supervisely/people_segment/Image_change/train/"
data1 = []
data2 = []


if __name__ == '__main__':
  change_name(path1,path2,path3)
  change_size(path3,path2,data1)
#  listdir(path2,data2)
  print data1

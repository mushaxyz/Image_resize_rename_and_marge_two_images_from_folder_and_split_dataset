# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 03:23:00 2022

@author: Ahmmad Musha
"""



################## Resize images form folder ##################

# from PIL import Image
# import os 
# # from datetime import datetime

# for image_file_name in os.listdir('WCEBleedGen_split82_seed42/train/Annotations'):
    
#     if image_file_name.endswith(".png"):
#         # now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

#         im = Image.open('WCEBleedGen_split82_seed42/train/Annotations/'+image_file_name)
#         new_width  = 256
#         new_height = 256
#         im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
#         image_file_name = image_file_name.replace("ann", "img")
#         im.save('WCEBleedGen_split82_seed42/train/rename/Annotations/' + image_file_name)
#         # im.save('F:\\GANs THESIS\\datasets\\IMAGE RESIZE AND MARGE\\new dataset\\' + now + '.jpg')
        
        
        
################## Split dataset for train validation and test ##################

# import splitfolders
# data_root = '/Resize'
# splitfolders.ratio(data_root, output="WCEBleedGen_split82_seed42", 
#                     seed=42, ratio=(.8, .2), 
#                     group_prefix=None) # default values
  
        
   
################## Rename images name form folder  ##################   
# for image_file_name in os.listdir('WCEBleedGen_split82_seed42/train/Annotations'):
   
#     if image_file_name.endswith(".png"):
#         # now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

#         im = Image.open('WCEBleedGen (updated)/Annotations/'+image_file_name)
#         image_file_name = image_file_name.replace("ann", "img")
#         im.save('WCEBleedGen_split82_seed42/train/rename/Annotations/' + image_file_name)
#         # im.save('WCEBleedGen_split82_seed42/train/rename/Annotations/' + now + '.jpg') 
 
   
    

################## Marge images form folder ##################

from PIL import Image
import os

for image_file_name in os.listdir('WCEBleedGen_split82_seed42/train/rename/Annotations'):
    
    if image_file_name.endswith(".png"):
        
        for second_image_file_name in os.listdir('WCEBleedGen_split82_seed42/train/bleeding'):
            if second_image_file_name.endswith(".png"):
                
                if image_file_name == second_image_file_name:
                    
                    
                    im = Image.open('WCEBleedGen_split82_seed42/train/bleeding/'+image_file_name)
                    im2 = Image.open('WCEBleedGen_split82_seed42/train/rename/Annotations/'+second_image_file_name)
                    new_im = Image.new('RGB', (512,256), (250,250,250))
                    
                    new_im.paste(im, (0,0))
                    new_im.paste(im2, (256, 0))
                    
                    new_im.save('WCEBleedGen_split82_seed42/train/marge_WCEBleedGen_split82_seed42/' + image_file_name)
                    












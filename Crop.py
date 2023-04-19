import matplotlib.pyplot as plt
from PIL import Image
import os

data_path = 'dataset/'

for dir in os.listdir(data_path):
    for classes in os.listdir(data_path+'/'+ dir):
        for file in os.listdir(data_path+'/'+dir+'/'+classes):
            fmt = file.split('.')

            if fmt[-1] == "jpg":
                img_path = data_path+'/'+dir+'/'+classes+'/'+file
                img = Image.open(img_path)
                width, height = img.size
                top_crop = 66
                bottom_crop = 20
                left_crop = 43
                right_crop = 43 
                box = (left_crop, top_crop, width-right_crop, height - bottom_crop)
                cropped_img = img.crop(box)
                cropped_img.save(img_path)

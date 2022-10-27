import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
from PIL import Image
import numpy as np
import math
import sys

path_bgrm = sys.argv[1]
#path_out = sys.argv[2]

import glob
paths = glob.glob(os.path.join(path_bgrm, '*.png'))
paths.sort()
print('本次执行检索到 '+str(len(paths))+' 张图像\n')
paths[0]

for root, dirs, files in os.walk(path_bgrm):
    print(files)
files[0]   #输出所有图片名称

path_bgrm + files[0]  #每张图片的绝对路径

#提取边缘
for imgpath in paths:
    imgname= os.path.splitext(os.path.basename(imgpath))[0]
    #print(imgpath)
    #img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    img_bgrm = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED)
#    print(cv2.split(img_bgrm))
    b,g,r, alpha = cv2.split(img_bgrm)
#     #图片转成矩阵
    alpha_mask = np.where(alpha==0,0,1)
     ##convert alpha to 0 and 255 only
    alpha2 = np.array(alpha_mask*255, dtype = "uint8")   #得到的矩阵
     #canny(): 边缘检测
    img1 = cv2.GaussianBlur(alpha2,(3,3),0)
    edges = cv2.Canny(img1, threshold1=30, threshold2=100)
    img=Image.fromarray(edges)
    cv2.imwrite(imgpath,edges)
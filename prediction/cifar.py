import numpy as np
from PIL import Image
import operator
from os import listdir
import sys
import pickle
import random

data ={}
list1 = []
list2 = []
list3 = []

def img_tra():
    for k in range(0,num):
        currentpath = folder + "/" + imglist[k]
        im = Image.open(currentpath)
        # width=im.size[0]
        # height=im.size[1]
        x_s = 32
        y_s = 32
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(folder_ad + "/" + str(imglist[k]))

def addWord(theIndex,word,adder):
    theIndex.setdefault(word,[]).append(adder)

def seplabel(fname):
    filestr = folder.split("/")[-1]
    label = filestr

    return label

def mkcf():
    global data
    global list1
    global list2
    global list3
    for k in range(0,num):
        currentpath = folder_ad + "/" + imglist[k]
        im = Image.open(currentpath)
        with open(binpath, 'a') as f:
            for i in range(0, 32):
                for j in range(0,32):
                    cl = im.getpixel((i,j))
                    list1.append(cl)
            for i in range(0,32):
                for j in range(0,32):
                    cl = im.getpixel((i,j))
                    list1.append(cl)
            for i in range(0,32):
                for j in range(0,32):
                    cl = im.getpixel((i,j))
                    list1.append(cl)
        list2.append(list1)
        list1 = []
        f.close()
        print("image"+str(k+1)+"saved.")
        list3.append(imglist[k].encode('utf-8'))
    arr2 = np.array(list2,dtype=np.uint8)
    data['batch_label'.encode('utf-8')] = 'testing batch 1 of 1'.encode('utf-8')
    data.setdefault('labels'.encode('utf-8'), label)
    data.setdefault('data'.encode('utf-8'), arr2)
    data.setdefault('filenames'.encode('utf-8'),list3)
    output = open(binpath, 'wb')
    pickle.dump(data,output)
    output.close()


folder = "G:/data/检测数据/5"
folder_ad = "G:/data/检测数据/5"
imglist = listdir(folder_ad)

num = len(imglist)
img_tra()
label = []
for i in range(0,num):
    label.append(seplabel(imglist[i]))
binpath = "G:/mine/fifth/realNVP-master/mydata/data_batch_5"

print(binpath)
mkcf()

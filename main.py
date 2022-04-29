# -*- coding: UTF-8 -*-
import tinify
import os
import os.path
import shutil
import sys

total = float(0)

# 递归遍历目录
def traversal_files(path):
    for dir in os.listdir(path):
        dir = os.path.join(path, dir)
        filetype = os.path.splitext(dir)[-1]
        if(filetype == ".png" or filetype == ".jpg"):
            print(dir,"...")
            source = tinify.from_file(dir)
            source.to_file(dir)
        # 判断当前目录是否为文件夹
        if os.path.isdir(dir):
            traversal_files(dir)

def getByteString(kb):
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)

def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
        global total
        total += kb
    except:
        print("传入的字节格式不对")
        return "Error"
    return getByteString(kb)

def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)

def file_size(path):
    for dir in os.listdir(path):
        dir = os.path.join(path, dir)
        filetype = os.path.splitext(dir)[-1]
        if(filetype == ".png" or filetype == ".jpg"):
            print(dir,",", getDocSize(dir))
        # 判断当前目录是否为文件夹
        if os.path.isdir(dir):
            file_size(dir)

if __name__ == '__main__':
    path = '/Users/zoulin/Desktop/supermonkey_null_safety/supermonkeyapp/assets'
    tinify.key = "GcY1lvGDZNp1t13dywTJBSYdn5pbH5C3"
    # traversal_files(path)
    file_size(path)
    print("图片总大小:" + getByteString(total))
    # print(p)
    


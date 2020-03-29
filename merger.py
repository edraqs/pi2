# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:48:28 2020

@author: ss180994
"""

import glob
import shutil
import os

dir_path = "./dataset/*/*.png"
save_path = "./dataset/save/"
files = glob.glob(dir_path)
print(files)
dirs = dict()

for file in files:
    try:
        dirs[file.split("\\")[1]].append(file)
    except:
        dirs[file.split("\\")[1]] = [file]

dir_to_merge = dict()
for dir in dirs.keys():
    dir_real_name = dir.split(' ')[0]
    try:
        dir_to_merge[dir_real_name].append(dir)
    except:
        dir_to_merge[dir_real_name] = [dir]

print(dir_to_merge)
for target_dir, merge_list in dir_to_merge.items():
    out = save_path + target_dir + "/"
    try:
        os.mkdir(out)
    except:
        pass

    print("out : " , out)
    i = 0
    for dir in merge_list:
        for file in dirs[dir]:
            try:
                shutil.copyfile(file, out + str(i) + file.split('\\')[-1])
            except Exception as e:
                print(e)
        i += 1
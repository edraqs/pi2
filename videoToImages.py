# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import filedialog as fd
import tkinter
import cv2
import os

def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    vidcap.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
    fps = vidcap.get(cv2.CAP_PROP_POS_FRAMES)
    vidcap.set(cv2.CAP_PROP_POS_AVI_RATIO,0)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 20/fps
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

def askFile():
    root = tkinter.Tk()
    root.withdraw()
    filename = fd.askopenfilename()
    return filename

def askDirectory():
    root = tkinter.Tk()
    root.withdraw()
    dir = fd.askdirectory()
    return dir

video_to_frames(askFile(), askDirectory())
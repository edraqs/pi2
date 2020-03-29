* videoToImages.py:
  samples a video file to multiple image files (used for making the dataset).  
* merger.py:
  Merges all folder with a similar name contained in a folder, this is to correct the result of videoToImages:  
  videoToImages creates a folder each time it is executed, resulting in multiple folder for only one item, merger fixes this by       getting all those images in one folder only.
* neural_network_keras
  * main.py
    Trains model on a dataset 
  * evaluate.py
    Code to launch live object recognition using opencv

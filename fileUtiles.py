#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:46:18 2020

@author: pankajsharma
"""
import os.path
from urllib import request as urllib2
from os import path;
class FileUtills:
    def __init__(self):
        print("Hello")
    def downloadORGetPath(self,imageUrl,imageId):
        if(path.exists("images/"+imageId+".jpg")):
            return "images/"+imageId+".jpg";
        else:
            filedata = urllib2.urlopen(imageUrl)
            datatowrite = filedata.read()
            with open("images/"+imageId+".jpg",'wb') as f:
                f.write(datatowrite);
            return "images/"+imageId+".jpg";    
                
#x = FileUtills();
#x.downloadORGetPath('https://firebasestorage.googleapis.com/v0/b/lost-and-found-dc2ae.appspot.com/o/lostItemsImages%2Fscaled_28154c2b-c52f-4e58-bfd6-0654994b2933991692850786096539.jpg%7D?alt=media&token=4dcb9147-8cbc-48c7-8aff-97d77e01e698','aaabb');                
            
        
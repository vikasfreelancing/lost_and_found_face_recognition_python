#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:19:45 2020

@author: vikas vashistha
"""

from mongoRepository import MongoRepository
from faceRecognition import FaceRecognition
from fileUtiles import FileUtills

class InitializeFounding:
    def __init__(self):
        pass
    def initializeFounding(self,itemId):
        self.mongo = MongoRepository();
        self.rec = FaceRecognition()
        self.fl = FileUtills()
        foundItem = self.mongo.getFoundItem(itemId)
        lostItems = self.mongo.getAllLostItems();
        self.createEncodings(lostItems,foundItem)
        #print(lostItems)
    def createEncodings(self,lostItems,foundItem):
        known_persons_ids = []
        known_person_Image_paths = []
        for item in lostItems:
            idx = str(item['_id']);
            indx = 0 
            for imageUrl in item['images']:
                known_persons_ids.append(idx)
                tempIdx = idx + str(indx);
                indx= indx + 1
                known_person_Image_paths.append(self.fl.downloadORGetPath(imageUrl,tempIdx))
        known_faces_encoding,final_ids = self.rec.createKnownMapping(known_person_Image_paths,known_persons_ids)
        uknown_image_url = self.fl.downloadORGetPath(foundItem['images'],str(foundItem['_id']))            
        print(known_persons_ids);
        print(known_person_Image_paths)
        matched_lost_item_id = self.rec.recognizeFace(uknown_image_url,known_faces_encoding,final_ids)
        print("Match image : {}".format(matched_lost_item_id))
        if(matched_lost_item_id!='Unknown face'):
            self.mongo.updateLostItem(matched_lost_item_id,str(foundItem['_id']))
            
#InitializeFounding("5e9d95ef9a6422140c09e044")
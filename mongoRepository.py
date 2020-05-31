#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:21:52 2020

@author: vikas vashistha
"""
from bson.objectid import ObjectId
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string


class MongoRepository:
    def __init__(self):
        self.client =  MongoClient("mongodb+srv://root:Angel11papa@cluster0-nugqv.mongodb.net")
        self.db=self.client.founding_wizard
        # Issue the serverStatus command and print the results
        serverStatusResult=self.db.command("serverStatus")
        #pprint(serverStatusResult)         
    def getAllLostItems(self):
        allItems = []
        items = self.db.lostItem.find({'isFound':False})
        for item in items:
            imageUrls = item['images']
            item['images']= imageUrls.split(',')[:-1]
            allItems.append(item)
        return allItems;
    
    def getFoundItem(self,itemId):
        return self.db.foundItem.find_one({'_id': ObjectId(itemId)})
    def updateLostItem(self,lostItemId,foundItemId):
        print(lostItemId,foundItemId);
        query = {'_id':ObjectId(lostItemId)}
        new_values = {"$set":{"isFound":True,"foundId":foundItemId}}
        self.db.lostItem.update_one(query,new_values)
#print(MongoRepository().getFoundItem("5e9d95ef9a6422140c09e044"))
            
        


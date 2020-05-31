#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:24:35 2020

@author: vikas vashistha
"""
import face_recognition;
class FaceRecognition:
    def __init__(self):
        print("hello")
    def recognizeFace(unknown_face_image,known_faces_encodings,known_face_ids) :  
        all_face_locations = face_recognition.face_locations(unknown_face_image,model='hog')
        #detect face encodings for all the faces detected
        all_face_encodings = face_recognition.face_encodings(unknown_face_image,all_face_locations) 
        #print the number of faces detected
        print('There are {} no of faces in this image'.format(len(all_face_locations)))
        
        
                

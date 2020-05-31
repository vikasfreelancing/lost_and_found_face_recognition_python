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
    def recognizeFace(self,image_url,known_faces_encodings,known_face_ids) :  
        unknown_face_image = face_recognition.load_image_file(image_url)
        all_face_locations = face_recognition.face_locations(unknown_face_image,model='hog')
        #detect face encodings for all the faces detected
        all_face_encodings = face_recognition.face_encodings(unknown_face_image,all_face_locations) 
        #print the number of faces detected
        print('There are {} no of faces in this image'.format(len(all_face_locations)))
        for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):
            #splitting the tuple to get the four position values of current face
            top_pos,right_pos,bottom_pos,left_pos = current_face_location
            #find all the matches and get the list of matches
            all_matches = face_recognition.compare_faces(known_faces_encodings, current_face_encoding)
           
            #string to hold the label
            id_of_person = 'Unknown face'
            
            #check if the all_matches have at least one item
            #if yes, get the index number of face that is located in the first index of all_matches
            #get the name corresponding to the index number and save it in name_of_person
            if True in all_matches:
                first_match_index = all_matches.index(True)
                id_of_person = known_face_ids[first_match_index]
        return id_of_person;
        
    def createKnownMapping(self,imageUrls,ids):
        print(len(ids))
        print(len(imageUrls))
        final_ids = []
        known_faces_encodings = []
        idx = 0
        for _image in imageUrls:
            temp_image = face_recognition.load_image_file(_image)
            all_face_locations = face_recognition.face_locations(temp_image,model='hog')
            if(len(all_face_locations)==0):
                idx+=1
                continue;
            temp_face_encodings = face_recognition.face_encodings(temp_image)[0]
            known_faces_encodings.append(temp_face_encodings)
            final_ids.append(ids[idx]);
            idx+=1
        return [known_faces_encodings,final_ids];    
            

        
                

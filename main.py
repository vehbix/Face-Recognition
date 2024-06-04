import face_recognition
import cv2
import numpy as np
import time 
import os
import json as js
import math
import datetime

def fac2_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)
    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + "%"
    else:
        value=(linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2)))*100
        return str(round(value, 2)) + "%"

class FaceRecognition:
    def __init__(self):
        self.face_recognitions = []
        self.face_encodings = []
        self.face_names = []
        self.known_face_encodings = []
        self.known_face_names = []
        self.process_current_frame = True
        self.pathFaces="faces"
        self.pathGelen="gelen"
        self.pathFind="find"
        self.encode_faces()

    def encode_faces(self):
        for image in os.listdir(self.pathFaces):
            face_image=face_recognition.load_image_file(self.pathFaces+"/"+image)
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
        print(self.known_face_names)

    def run_recognition(self):
            resimler=os.listdir(self.pathGelen)
            print(resimler)
            if len(resimler)==1:
                print("Resim yok")
                time.sleep(1)
                return True
            for dosya in resimler:
                if dosya==".stfolder":
                    continue
                resim = os.path.join(self.pathGelen, dosya)
            video_capture = cv2.VideoCapture(resim)
            video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)   
            ret, frame = video_capture.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1]

                #find all faces current frame
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)       
                self.face_names = []
                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown.jpg"
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        confidence = fac2_confidence(face_distances[best_match_index])
                        value=int(confidence.split(".")[0])
                        if value>90:
                            self.face_names.append(f'{name.split(".")[0]} {confidence}')
                            print(f'{name} {confidence} bulundu')
                        else:
                            name = "Unknown.jpg"
                            self.face_names.append("Unknown")
                    self.face_names.append("Unknown")
            self.process_current_frame = not self.process_current_frame
            

            #display annotations
            for (top, right, bottom, left), name2 in zip(self.face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name2, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

            now = datetime.datetime.now()   
            try:   
                string=str(now.strftime("%Y-%m-%d %H.%M.%S"))+" " + name  
            except:
                string=str(now.strftime("%Y-%m-%d %H.%M.%S"))+" Unknown.jpg"      
            print(string)
            
            cv2.imwrite(f"{self.pathFind}/{string}", frame)
            
            tel=os.listdir("telegram")
            for i in tel:
                os.remove(f"telegram/{i}")
            cv2.imwrite(f"telegram/{string}", frame)

            video_capture.release()
            cv2.destroyAllWindows()
            os.remove(resim)
            self.face_recognitions = []
            self.face_encodings = []
            self.face_names = []
            self.known_face_encodings = []
            self.known_face_names = []
            self.process_current_frame = True

            class FileInfoCollector:
                def __init__(self, directory):
                    self.pathFind = directory

                def collect_file_info(self):
                    # Create an empty dictionary to store the file information
                    file_info_dict = {}

                    # List all files in the 'find' directory
                    file_list = os.listdir(self.pathFind)

                    # Initialize a counter for naming the dictionary entries
                    counter = 1

                    # Iterate over each file in the list
                    for file_name in file_list:
                        # Skip the '.stfolder' and 'images.json' files
                        if file_name != ".stfolder" and file_name != "images.json":
                            # Extract the date, time, and name from the file name
                            date = file_name[:10]
                            timeS = file_name[10:19]
                            name = file_name[19:].split(".")[0]
                            path = file_name
                            
                            # Create a dictionary entry with the extracted information
                            entry_name = f"images{counter}"
                            file_info_dict[entry_name] = {
                                "date": date,
                                "time": timeS,
                                "name": name,
                                "path": path
                            }
                            
                            # Increment the counter for the next entry
                            counter += 1

                    # Define the path for the JSON file
                    json_file_path = os.path.join(self.pathFind, "images.json")

                    # Write the dictionary to the JSON file
                    with open(json_file_path, 'w') as json_file:
                        js.dump(file_info_dict, json_file, indent=4)

                    print(f"File information written to {json_file_path}")

            # Example usage:
            collector = FileInfoCollector("find")
            collector.collect_file_info()



            
if __name__ == "__main__":
    while True:    
        fr = FaceRecognition()  
        fr.run_recognition()
        time.sleep(1)
    

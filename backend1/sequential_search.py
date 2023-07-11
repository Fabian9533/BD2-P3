import time
import os
import numpy
import face_recognition
from queue import PriorityQueue 

def range_search(input_file, search_radius, working_directory, indexed_dictionary):
    img_path = working_directory + '/instance/uploads/' + input_file
    if not os.path.exists(img_path):
        print("No path")
        return []
    else:
        facial_image = face_recognition.load_image_file(img_path)
        face_enc = face_recognition.face_encodings(facial_image) 
        if len(face_enc) == 0:
            print("No face found")
            return []
        else:
            converted_face_enc = tuple(face_enc)
            search_results = []
            # gather info
            info_results = []
            print("Searching...")
            start_time = time.time()

            for dict_path in indexed_dictionary:
                first_array = numpy.array(list(map(float, indexed_dictionary[dict_path].strip("()").split(', '))))
                second_array = numpy.array(list(map(float, converted_face_enc[0])))
                distance_calculation = numpy.linalg.norm(first_array - second_array)
                if distance_calculation < search_radius:
                    search_results.append((dict_path, distance_calculation))
                    person_name = dict_path
                    info_results.append((person_name, round(distance_calculation,3)))
            end_time = time.time()
            print("Range search took " + str(round((end_time - start_time) * 1000)) + " ms.")
            print("Displaying results:")
            return info_results
        

def knn_search(input_file, num_neighbors, working_directory, indexed_dictionary):
    priority_queue = PriorityQueue(False)

    img_path = working_directory + '/instance/uploads/' + input_file
    if not os.path.exists(img_path):
        print("No path")
        return []
    else:
        facial_image = face_recognition.load_image_file(img_path)
        face_enc = face_recognition.face_encodings(facial_image) 
        if len(face_enc) == 0:
            print("No face found")
            return []
        else:
            converted_face_enc = tuple(face_enc)
            search_results = []

            info_results = []
            print("Searching...")
            start_time = time.time()
            for dict_path in indexed_dictionary:
                first_array = numpy.array(list(map(float, indexed_dictionary[dict_path].strip("()").split(', '))))
                second_array = numpy.array(list(map(float, converted_face_enc[0])))
                distance_calculation = numpy.linalg.norm(first_array - second_array)
                person_name = dict_path
                priority_queue.put((round(distance_calculation,3), person_name))
                info_results.append((round(distance_calculation,3),person_name))
            for i in range(num_neighbors):
                search_results.append(priority_queue.get())
            end_time = time.time()
            search_time = str(round((end_time - start_time) * 1000))
            print("Nearest neighbors search took " + search_time + " ms.")
            print("Displaying results:")
            return search_results, search_time




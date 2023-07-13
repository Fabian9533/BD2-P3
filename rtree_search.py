import face_recognition
import numpy
import time
import os


path_data = "data.json"

def KNN_SEARCH_RTree(input_file, num_neighbors, working_directory, mapped_dictionary, index):
      imagePath = working_directory + '/test_images/' + input_file
      if not os.path.exists(imagePath):
            print("No path")
            return []
      else:
        facial_image = face_recognition.load_image_file(imagePath)
        face_enc = face_recognition.face_encodings(facial_image) 
        if len(face_enc) == 0:
            print("No face found")
            return []
        else:
          converted_face_enc = tuple(face_enc[0])
          search_results = []
          print("Searching...")
          start_time = time.time()
          nearestNeighbors = list(index.nearest(coordinates=converted_face_enc, num_results=num_neighbors))
          finish_time = time.time()     
          current_count = 1
          for index in nearestNeighbors:
            indexed_item = mapped_dictionary[index]
            image_path = indexed_item[0]
            first_array = numpy.array(indexed_item[1])
            second_array = numpy.array(converted_face_enc[0])
            distance_calculation = numpy.linalg.norm(first_array - second_array)
            search_results.append((image_path, round(distance_calculation, 3)))
            if current_count > num_neighbors:
              break
            current_count += 1
          print("KNN Search RTree search took " + str(round((finish_time-start_time)*1000, 3)) + " ms.")
          print("Displaying results:")
          return search_results

def RANGE_SEARCH_RTree(input_file, search_radius, working_directory, index, mapped_dictionary):
      imagePath = working_directory + '/test_images/' + input_file
      if not os.path.exists(imagePath):
            print("No path")
            return []
      else:
            facial_image = face_recognition.load_image_file(imagePath)
            face_enc = face_recognition.face_encodings(facial_image) 
            if len(face_enc) == 0:
                  print("No face found")
                  return []
            else:
                  converted_face_enc = tuple(face_enc[0])
                  lower_bound = []
                  upper_bound = []
                  for point in converted_face_enc:
                        lower_bound.append(point - search_radius)
                        upper_bound.append(point + search_radius)
                  boundary = lower_bound + upper_bound
                  start_time = time.time()
                  range_search_results = [n for n in index.intersection(boundary)]
                  finish_time = time.time()
                  search_results = []
                  second_array = numpy.array(converted_face_enc[0])
                  prev_path = ""
                  for index in range_search_results:
                        indexed_item = mapped_dictionary[index]
                        image_path = indexed_item[0]
                        first_array = numpy.array(indexed_item[1])
                        distance_calculation = numpy.linalg.norm(first_array - second_array)
                        if distance_calculation < search_radius and image_path != prev_path:
                              search_results.append((image_path, round(distance_calculation, 3)))
                        prev_path = image_path
                        
                  print("Range Search RTree took " + str(round((finish_time-start_time)*1000, 3)) + " ms.")
                  print("Displaying results:")
                  return search_results

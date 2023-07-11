import face_recognition
import numpy
import random
import linecache as lc
import io

import shutil
import os
import json

num_samples = 5000
block_size = 1000
current_directory = os.getcwd() 
processed_image_path = current_directory + "/processed_dataset"
file_name = "processed_images.json"
directory_to_clean = processed_image_path


def processImageSet(limit):

    total_images = 0 

    if not os.path.exists(processed_image_path): 
        os.makedirs(processed_image_path)

    factor = 1
    counter = 0
    block_dictionary = {}
    face_encodings = {}
    dataset_directory_path = current_directory + "/dataset" 
    dataset_subdirectories = os.listdir(dataset_directory_path)

    for subdir in dataset_subdirectories: 
       
        if(total_images >= limit):
            memoryLoad(block_dictionary)
            return total_images, face_encodings

        subdir_path = dataset_directory_path + "/" + subdir
        for img in os.listdir(subdir_path): 
            if(total_images >= limit):
                memoryLoad(block_dictionary)
                return total_images, face_encodings

            img_path = subdir_path + "/" + img
            key = subdir + '/' + img
            face_img = face_recognition.load_image_file(img_path)
            face_encoding = face_recognition.face_encodings(face_img) 
            
            if len(face_encoding) != 0:
                new_face_encoding = tuple(face_encoding[0])
               
                if new_face_encoding not in block_dictionary:
                    block_dictionary[key] = str(new_face_encoding)
                    face_encodings[key] = str(new_face_encoding)
                    total_images += 1
                    print(counter)
                    counter += 1
                    if counter > block_size*factor:
                        print("counter")
                        factor += 1
                        memoryLoad(block_dictionary)
                else:
                    block_dictionary[key] += str(new_face_encoding)
                    face_encodings[key] = str(new_face_encoding)
                    total_images += 1
                    print(counter)
                    counter += 1
                    if counter > block_size*factor:
                        print("counter")
                        factor += 1
                        memoryLoad(block_dictionary)
                
            else: 
                print("no face found in: " + str(img_path))
    
    memoryLoad(block_dictionary)

    return total_images, face_encodings


def memoryLoad(block_dictionary):
    try:
        dictionary_path = processed_image_path + '/' + file_name
        with open(dictionary_path, 'a', encoding="utf-8") as file: 
            print("Data is: [face_image_path] -> face encoding")
            print("Loading data into new directory file...")
            for keyword in block_dictionary:
                file.write(json.dumps({keyword: block_dictionary[keyword]}, ensure_ascii=False))
                file.write("\n")
            file.close()
            print("Data successfully uploaded!")
        block_dictionary.clear()
        return 1
    except IOError:
        print("Problem reading: " + str(dictionary_path) + " path.")
        return 0


def generateDistances(N, distribution):
    result = []
    
    for i in range(1, N):
        aux_tuple = () 
        aux_tuple = random.sample(range(0, len(distribution)), 2)
        first_array = numpy.array(distribution[aux_tuple[0]])
        second_array = numpy.array(distribution[aux_tuple[1]])
        result.append(numpy.linalg.norm(first_array - second_array))
    return result


def clearProcessedImagesDirectory():
    if os.path.exists(directory_to_clean):
        shutil.rmtree(directory_to_clean)
    else:
        print("Files not found")

def loadBlockDictionary(block_dictionary, total):
    for i in range(1, total):
        PATH = current_directory + "/processed_dataset/processed_images.json"
        try:
            aux_line = lc.getline(PATH, i).rstrip()
            if aux_line != "":
                json_obj = json.load(io.StringIO(aux_line))
                key = list(json_obj.keys())
                value = tuple(json_obj.values())
                block_dictionary[key[0]] = value[0]
        except:
            print("There are no processed images")
            return 0
    return block_dictionary
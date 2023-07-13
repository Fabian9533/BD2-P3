import time
import os
import numpy
import face_recognition
import pandas as pd
#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA
from sklearn.neighbors import KDTree


def KDTREE(file_name, k, working_dir, block_dictionary):
    imgPath = working_dir + '/test_images/' + file_name
    if not os.path.exists(imgPath):
        print("No path")
        return []
    else:
        loaded_face = face_recognition.load_image_file(imgPath)

        face_enc = face_recognition.face_encodings(loaded_face)

        face_enc = numpy.array(face_enc)

        if len(face_enc) == 0:
            print("Not face found")
            return []
        else:

            existsFile = os.path.isfile(working_dir+'/KDTREE.csv')
            
            if not existsFile:
                print("creando csv ...")

                cols = [str(i) for i in range(128)]
                face_df = pd.DataFrame(columns=cols)
                img_df = pd.DataFrame(columns=["img"])

                for file_path in block_dictionary:
                    initial_array = numpy.array(list(map(float, block_dictionary[file_path].strip("()").split(', '))))
                    initial_array = pd.DataFrame(initial_array.reshape(1,-1), columns=list(cols))
                    face_df = pd.concat( [face_df, initial_array]) 
                    image_entry = pd.DataFrame(numpy.array([file_path]), columns=["img"])
                    img_df = pd.concat([img_df,image_entry])

                print("searching...")
                start_time = time.time()

                face_df["img"] = img_df
                face_df.to_csv(working_dir+'/KDTREE.csv',index=False, encoding='utf-8')    
                face_df.reset_index(drop=True, inplace=True)
                tree_instance = KDTree(face_df.iloc[:, 0:-1])
                distances, indices = tree_instance.query(face_enc, k)
                matches = []
                for i in range(len(distances[0])):
                    matches.append((round(distances[0][i],3),face_df.iloc[indices[0][i]].values.tolist()[-1]))
                end_time = time.time()
                
                time_elapsed = str(round((end_time - start_time) * 1000, 3))
                print("KNN Search KDtree took " + time_elapsed + " ms.")
                print("Displaying results:")
                return matches, time_elapsed
            else:
                print("searching...")
                start_time = time.time()

                face_df = pd.read_csv(working_dir+'/KDTREE.csv')
                face_df.reset_index(drop=True, inplace=True)
                tree_instance = KDTree(face_df.iloc[:, 0:-1])
                distances, indices = tree_instance.query(face_enc, k)
                matches = []

                for i in range(len(distances[0])):
                    matches.append((round(distances[0][i],3),face_df.iloc[indices[0][i]].values.tolist()[-1]))
                end_time = time.time()
                
                time_elapsed = str(round((end_time - start_time) * 1000, 3))
                print("KNN Search KDtree took " + time_elapsed + " ms.")
                print("Displaying results:")
                return matches, time_elapsed
from sequential_search import *
from image_processing import *
from rtree_search import *
from kdtree import *
from rtree import index
import os

cwd = os.getcwd() # current working directory
processed_images_path = cwd + "/processed_dataset"
filename = "processed_images.json"

class image_browser():
    total = 13175
    block_dictionary = {}
    indexed_dictionary = {}

    def __init__(self, limit, flag):
        if flag:
            self.PROCESS_IMAGES(limit)
        self.PROCESS_RTREE()
   

    def PROCESS_RTREE(self):
        p = self.load_rtree_properties()
        self.idx128d = index.Index('128d_index', properties=p)
     
        if(len(self.block_dictionary) == 0):
            self.block_dictionary = loadBlockDictionary(self.block_dictionary, self.total)
            if(len(self.block_dictionary) == 0):
                print("data has not been processed..")
                return 0
       
        items =  list(self.block_dictionary.items())
        counter = 1
        for item in items:
            val = tuple(numpy.array(list(map(float, item[1].strip("()").split(', ')))))
            self.idx128d.insert(counter, val)
            self.indexed_dictionary[counter] = (str(item[0]), val)
            counter += 1
    
    def load_rtree_properties(self):
        p = index.Property()
        p.dimension = 128 
        p.buffering_capacity = 4
        p.dat_extension = 'data'
        p.idx_extension = 'index'
        return p

    def PROCESS_IMAGES(self, limit):
        clearProcessedImagesDirectory()
        self.total, self.block_dictionary = processImageSet(limit)
        
    def RANGE_SEARCH_RTREE(self, file_name, radius):
        if hasattr(self, 'idx128d'):
            info = RANGE_SEARCH_RTree(file_name, radius, cwd, self.idx128d, self.indexed_dictionary)
            self.printing(info)
        else:
            pass
            

    def KNN_SEARCH_RTREE(self, file_name, k):
        print('KNN_SEARCH_TREE')
        if hasattr(self, 'idx128d'):
            info = KNN_SEARCH_RTree(file_name, k, cwd, self.indexed_dictionary, self.idx128d)
            self.printing(info)       
        else:
            pass

    def RANGE_SEARCH(self, file_name, radius):
        if(len(self.block_dictionary) == 0):
            self.block_dictionary = loadBlockDictionary(self.block_dictionary, self.total)
            if(len(self.block_dictionary) == 0):
                print("data has not been processed..")
                return []
        info = range_search(file_name, radius, cwd, self.block_dictionary)
        self.printing(info)
        return info
    
    def KNN_SEARCH(self, file_name, k):
        print('KNN_SEARCH')
        if(len(self.block_dictionary) == 0):
            self.block_dictionary = loadBlockDictionary(self.block_dictionary, self.total)
            if(len(self.block_dictionary) == 0):
                print("data has not been processed..")
                return []
        info, tiempo = knn_search(file_name, k, cwd, self.block_dictionary)
        self.printing(info)
        return info, tiempo

    def KDTREE(self, file_name, k):
        print('KDTREE')
        if(len(self.block_dictionary) == 0):
            self.block_dictionary = loadBlockDictionary(self.block_dictionary, self.total)
            if(len(self.block_dictionary) == 0):
                print("data has not been processed..")
                return []
        info, tiempo = KDTREE(file_name, k, cwd, self.block_dictionary)
        self.printing(info)  
        return info, tiempo

    def printing(self, info):
        counter = 0
        for key in info:
         
            print(str(counter) + ") -> (" + str(key[0]) + ", " + str(key[1]) + ")")
            counter += 1



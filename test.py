from main import *

cwd = os.getcwd() 
n = 12800

def test():
    smt = image_browser(n, False)
    print("N = ", n)
    smt.KNN_SEARCH("tom_cruise.jpeg", 8)
    #'''
    print()
    smt.KNN_SEARCH_RTREE("tom_cruise.jpeg", 8)
    print()
    smt.KDTREE("tom_cruise.jpeg", 8)
    #'''

test()
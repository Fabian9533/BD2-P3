from main import *

cwd = os.getcwd() 


def test():
    smt = some_class(14000, False)
    
    smt.KNN_SEARCH("Salma_Hayek.jpeg", 8)
   
    print()
    smt.KNN_SEARCH_RTREE("Salma_Hayek.jpeg", 8)
    print()
    smt.KDTREE("Salma_Hayek.jpeg", 8)

test()
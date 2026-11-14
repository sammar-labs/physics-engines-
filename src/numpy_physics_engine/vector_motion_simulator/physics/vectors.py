import numpy as np
def displacement(initial_position,final_position):
    initial=np.array(initial_position,dtype=float)
    final=np.array(final_position,dtype=float)
    return final-initial

def add_vectors(a,b):
    return np.array(a)+np.array(b)

def subtract_vectors(a,b):
    return np.array(a)-np.array(b)

def magnitude(vector):
    vector=np.array(vector,dtype=float)
    return np.sqrt(np.sum(vector**2))

def dot_product(a,b):
    return np.dot(a,b)
if __name__=="__main__":
    print(displacement([10,20],[50,80]))
import pickle
import os

def load_pkl(path_file):
    '''load_pkl using pickle
    path_file   : full path or file name with extension .pkl
    '''
    try:
        with open(path_file,'rb') as file_input:
            return pickle.load(file_input)
    except:
        path_file = os.path.join(os.getcwd(),'path_file')
        with open(path_file,'rb') as file_input:
            return pickle.load(file_input)
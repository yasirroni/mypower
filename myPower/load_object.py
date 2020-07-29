import pickle
def load_object(path_file):
    '''load_object using pickle
    path_file   : full path or file name with extension .pkl
    '''
    with open(path_file,'rb') as file_input:
        return pickle.load(file_input)
import pickle
def save_object(obj,path_file):
    '''save_object in binary format using pickle
    obj         : any object, i.e. [mypc]<class 'oct2py.io.Struct'>
    path_file   : full path or file name with extension .pkl
    '''
    with open(path_file,'wb') as file_output:
        pickle.dump(obj,file_output,pickle.HIGHEST_PROTOCOL)
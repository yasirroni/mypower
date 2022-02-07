import pickle

def save_pkl(inp,path_file=None):
    '''save in binary format using pickle
    inp         : any object, i.e. [mypc]<class 'oct2py.io.Struct'>
    path_file   : full path or file name with extension .pkl
    '''
    if path_file == None:
        import os
        path_file=os.path.join(os.getcwd(),'mypc.pkl')

    with open(path_file,'wb') as pkl:
        pickle.dump(inp,pkl,pickle.HIGHEST_PROTOCOL)
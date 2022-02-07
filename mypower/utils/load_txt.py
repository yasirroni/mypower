def load_txt(path):
    '''load_txt
    Return list of str. Used to get str from readable .txt file
    '''
    t = []
    with open(path,'r') as f:
        for l in f:
            t.append(l[:-1])
    return t
def str_in(path):
    '''str_in
    Return list of str.
    '''
    t = []
    with open(path,'r') as f:
        for l in f:
            t.append(l[:-1])
    return t
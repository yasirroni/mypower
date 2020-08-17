def count_nout(path):
    '''count_nout
    Count number of output of .m function.
    '''
    nout = 0
    status = 'NOT FUNCTION'
    with open(path, encoding='utf8') as f:
        for l in f: 
            if l[0] != 'f': #not function
                if status == 'NOT FUNCTION':
                    continue
            l = l.translate(str.maketrans('', '', '[]()')).split()
            try:
                l.remove('function')
            except:
                pass
            for s in l:
                if s == '...':
                    status = 'FUNCTION'
                    continue
                if s != '=':
                    nout += 1
                else:
                    return nout
    return nout
from myPower.api import get_index
def to_mypc(mypc):
    '''Make bus numbering start from 1
    Convenient for Octave indexing.
    '''
    mypc0 = copy.deepcopy(mypc)
    
    idx = get_index()

    if min(mypc['bus'][:,idx['BUS_I']])==1:
        return mypc
    
    mypc['bus'][:,idx['BUS_I']]=range(1,len(mypc['bus'][:,idx['BUS_I']]) + 1)
    
    mypc['branch'][:,idx['F_BUS']]=mypc['branch'][:,idx['F_BUS']] + 1
    mypc['branch'][:,idx['T_BUS']]=mypc['branch'][:,idx['T_BUS']] + 1
    
    mypc['gen'][:,idx['GEN_BUS']]=mypc['gen'][:,idx['GEN_BUS']] + 1
    
    return mypc
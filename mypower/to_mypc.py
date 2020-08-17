import copy
from .get_index import get_index

def to_mypc(mypc):
    '''Make bus numbering start from 1
    Convenient for Octave indexing.
    '''
    mypc_copy = copy.deepcopy(mypc)
    
    idx = get_index()

    if min(mypc_copy['bus'][:,idx['BUS_I']])==1:
        return mypc_copy
    
    mypc_copy['bus'][:,idx['BUS_I']]=range(1,len(mypc_copy['bus'][:,idx['BUS_I']]) + 1)
    
    mypc_copy['branch'][:,idx['F_BUS']]=mypc_copy['branch'][:,idx['F_BUS']] + 1
    mypc_copy['branch'][:,idx['T_BUS']]=mypc_copy['branch'][:,idx['T_BUS']] + 1
    
    mypc_copy['gen'][:,idx['GEN_BUS']]=mypc_copy['gen'][:,idx['GEN_BUS']] + 1
    
    return mypc_copy
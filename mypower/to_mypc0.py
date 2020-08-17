import copy
from .get_index import get_index

def to_mypc0(mypc):
    '''Make bus numbering start from 0
    Convenient for Python indexing.
    '''
    mypc_copy = copy.deepcopy(mypc)

    idx = get_index()

    if min(mypc_copy['bus'][:,idx['BUS_I']])==0:
        return mypc_copy
    
    mypc_copy['bus'][:,idx['BUS_I']]=range(len(mypc_copy['bus'][:,idx['BUS_I']]))
    
    mypc_copy['branch'][:,idx['F_BUS']]=mypc_copy['branch'][:,idx['F_BUS']] - 1
    mypc_copy['branch'][:,idx['T_BUS']]=mypc_copy['branch'][:,idx['T_BUS']] - 1
    
    mypc_copy['gen'][:,idx['GEN_BUS']]=mypc_copy['gen'][:,idx['GEN_BUS']] - 1
    
    return mypc_copy
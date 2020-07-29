import copy
from myPower.api import get_index

def to_mypc0(mypc):
    """Make bus numbering start from 0
    Convenient for Python indexing.
    """
    mypc0 =  copy.deepcopy(mypc)

    idx = get_index()

    if min(mypc0['bus'][:,idx['BUS_I']])==0:
        return mypc0
    
    mypc0['bus'][:,idx['BUS_I']]=range(len(mypc0['bus'][:,idx['BUS_I']]))
    
    mypc0['branch'][:,idx['F_BUS']]=mypc0['branch'][:,idx['F_BUS']] - 1
    mypc0['branch'][:,idx['T_BUS']]=mypc0['branch'][:,idx['T_BUS']] - 1
    
    mypc0['gen'][:,idx['GEN_BUS']]=mypc0['gen'][:,idx['GEN_BUS']] - 1
    
    return mypc0
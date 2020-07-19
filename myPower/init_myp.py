from oct2py import Oct2Py
import os

def init_myp(path='matpower'):
    if path == 'matpower':
        path=os.path.join(os.getcwd(),'matpower')
    myp = Oct2Py()
    myp.addpath(myp.genpath(path))
    return myp
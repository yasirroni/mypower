from oct2py import Oct2Py
import os

def oc_matpower(path_matpower='matpower',oc=None):
    if path_matpower == 'matpower':
        path_matpower=os.path.join(os.getcwd(),'matpower')
    if oc == None:
        oc = Oct2Py()
    oc.addpath(oc.genpath(path_matpower)) 
    return oc
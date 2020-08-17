from oct2py import Oct2Py
import os

def oc_addgenpath(path,oc=None):
    if oc == None:
        oc = Oct2Py()
    oc.addpath(oc.genpath(path))
    return oc

def oc_addpath(path,oc=None):
    if oc == None:
        oc = Oct2Py()
    oc.addpath(path)
    return oc

def oc_matpower(path_matpower='matpower',oc=None):
    if path_matpower == 'matpower':
        if os.path.isdir(os.path.join(os.path.dirname(__file__ ),path_matpower)):
            path_matpower = os.path.join(os.path.dirname(__file__ ),path_matpower)
        else:
            raise ValueError("""NO MATPOWER PATH FOUND!
PLEASE USE:
    oc = oc_matpower(path_matpower='/PATH/matpower')

ALTERNATIVELY, PLACE MATPOWER IN myPower PACKAGE. 
NAME THE FOLDER WITH 'matpower'. RESULT WILL BE:
    ...\\mypower\\api.py
    ...
    ...\\mypower\\matpower << here (whithout making new matpower folder)
    ...\\mypower\\matpower\\data
    ...\\mypower\\matpower\\lib""")
    if oc == None:
        oc = Oct2Py()
    oc.addpath(oc.genpath(path_matpower))
    return oc
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
    error_path = False
    if path_matpower == 'matpower':
        if os.path.isdir(os.path.join(os.path.dirname(__file__ ), path_matpower)):
            path_matpower = os.path.join(os.path.dirname(__file__ ), path_matpower)
        else:
            error_path = True
    elif not os.path.isdir(path_matpower):
        error_path = True
    
    if error_path:
        raise ValueError(
            "NO MATPOWER PATH FOUND!\n"
        """
            PLEASE USE:
                oc = oc_matpower(path_matpower='/PATH/TO/matpower')

            ALTERNATIVELY, PLACE MATPOWER IN myPower PACKAGE and use oc = oc_matpower(). 
            NAME THE FOLDER WITH 'matpower'. RESULT WILL BE:
                ...\\mypower\\__init__.py
                ...\\mypower\\matpower_api.py
                ...
                ...\\mypower\\matpower << here (whithout making new matpower folder)
                ...\\mypower\\matpower\\data
                ...\\mypower\\matpower\\lib
        """
    )
    if oc == None:
        oc = Oct2Py()
    oc.addpath(oc.genpath(path_matpower)) # add path to matpower
    return oc

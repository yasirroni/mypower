from oct2py import Oct2Py
import os

def oc_addgenpath(path, m=None):
    if oc == None:
        oc = Oct2Py()
    m.eval(f"addpath(genpath('{path}'))")
    return oc

def oc_addpath(path, m=None):
    if oc == None:
        oc = Oct2Py()
    m.addpath(path)
    return oc

def start_matpower(path_matpower='matpower', m=None):
    error_path = False
    if path_matpower == 'matpower':
        import matpower
        path_matpower = matpower.path_matpower
    elif path_matpower == 'mypower':
        path_matpower = os.path.dirname(os.path.abspath(__file__))
    elif not os.path.isdir(path_matpower):
        error_path = True
    
    if error_path:
        raise ValueError(
            "NO MATPOWER PATH FOUND!\n"
        """
            PLEASE USE:
                m = myp.start_matpower(path_matpower='/PATH/TO/MATPOWER')

            RECOMMENDED WAY TO INSTALL MATPOWER IS USING:

                pip install matpower

            ALTERNATIVELY, PLACE MATPOWER IN mypower PACKAGE and use:
                m = myp.start_matpower(path_matpower=mypower). 
        """
    )

    return oc_addgenpath(path_matpower)

from oct2py import Oct2Py
import os

def oc_addgenpath(path, m=None):
    if m == None:
        m = Oct2Py()
    m.eval(f"addpath(genpath('{path}'))")
    return m

def oc_addpath(path, m=None):
    if m == None:
        m = Oct2Py()
    m.addpath(path)
    return m

def start_matpower(path_matpower='matpower', m=None):
    path_matpower, error_path = check_path(path_matpower)
    
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
    else:
        return oc_addgenpath(path_matpower)

def check_path(path_matpower):
    if path_matpower == 'matpower':
        import matpower
        path_matpower = matpower.path_matpower
        error_path = False
    elif path_matpower == 'mypower':
        path_matpower = os.path.dirname(os.path.abspath(__file__))
        error_path = False
    elif not os.path.isdir(path_matpower):
        error_path = True
    
    return path_matpower, error_path
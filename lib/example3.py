import os
from init_myp import init_myp

myp = init_myp()
myp.addpath(myp.genpath(os.getcwd()))
myp.runpf()
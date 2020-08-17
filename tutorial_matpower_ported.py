# import
from mypower import pretty
from mypower.matpower_api import runpf
from mypower.oc_api import oc_matpower

# runpf with default nout = max_nout from matpower_api
result = runpf()
[MVAbase, bus, gen, branch, success, et] = result
print('runpf output: ',pretty(result))
print('runpf output type: ',type(result))

# runpf with default nout = 1 from api
oc = oc_matpower()
result = oc.runpf()
print('runpf output: ',pretty(result))
print('runpf output type: ',type(result))

"""Notes:
Path name is replaced for:
    @   : at_
    -   : _

If dir name already exist in python module, the dir name is revised:
    dirname     : _dirname
"""
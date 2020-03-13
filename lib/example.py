## to_ppc0
from pypower.api import case9
from to_ppc0 import to_ppc0
ppc=case9()
ppc=to_ppc0(ppc)
print(ppc)

## makeB_kron
from makeB_kron import makeB_kron
B,B0,B00,success=makeB_kron(ppc)
print(B,B0,B00,success)

## losses_kron_method
from losses_kron_method import losses_kron_method
from pypower.api import ppoption, runpf
from pypower.idx_gen import PG
ppopt = ppoption(PF_ALG=1,VERBOSE=0,OUT_ALL=0,OUT_ALL_LIM=0,OUT_V_LIM=0)
result,success = runpf(ppc,ppopt)
Pgen = result['gen'][:,PG]
PL,PL_Quadratic,PL_Linear,PL_Constant=losses_kron_method([B,B0,B00],result['baseMVA'],Pgen)
print(PL,PL_Quadratic,PL_Linear,PL_Constant)
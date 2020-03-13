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
from pypower.idx_brch import PF,PT
ppopt = ppoption(PF_ALG=1,VERBOSE=0,OUT_ALL=0,OUT_ALL_LIM=0,OUT_V_LIM=0)
result,success = runpf(ppc,ppopt)
PGen = result['gen'][:,PG]

PL_kron,PL_Quadratic,PL_Linear,PL_Constant=losses_kron_method([B,B0,B00],result['baseMVA'],PGen)
print(PL_kron,PL_Quadratic,PL_Linear,PL_Constant)
PL_NR = sum(result['branch'][:, PF] + result['branch'][:, PT]) # compute real power loss vector
print('Error Kron:',(PL_kron-PL_NR)/PL_NR)

## makeB_kron_slope
from makeB_kron_slope import makeB_kron_slope
slope_kron=makeB_kron_slope([B,B0],result['baseMVA'],PGen)
print(slope_kron)

## losses_kron_slope_method
from losses_kron_slope_method import losses_kron_slope_method
import copy
PL_ref=PL_kron
PGen_ref=copy.deepcopy(PGen)

PGen[0]=PGen[0]+PGen[1]*0.01+PGen[2]*0.01
PGen[1]=PGen[1]*0.99
PGen[2]=PGen[2]*0.99
print(PGen_ref)
print(PGen)
print(PGen-PGen_ref)

PL_slope_method=losses_kron_slope_method(slope_kron,PGen,PGen_ref,PL_ref)
print(PL_slope_method)

PL_kron,_,_,_=losses_kron_method([B,B0,B00],result['baseMVA'],PGen)
print(PL_kron)

print('Error PL_slope to PL_kron:',(PL_slope_method-PL_kron)/PL_kron)

ppopt = ppoption(PF_ALG=1,VERBOSE=0,OUT_ALL=0,OUT_ALL_LIM=0,OUT_V_LIM=0)
ppc['gen'][:,PG]=ppc['gen'][:,PG]*0.99
result,success = runpf(ppc,ppopt)
PL_NR = sum(result['branch'][:, PF] + result['branch'][:, PT])
print('Error PL_slope to PL_NR:',(PL_slope_method-PL_NR)/PL_NR)
print('Error PL_kron to PL_NR:',(PL_kron-PL_NR)/PL_NR)

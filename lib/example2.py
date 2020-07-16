## to_ppc0
from pypower.api import case9
from to_ppc0 import to_ppc0
from pypower.idx_bus import REF,BUS_TYPE,PD
from pypower.idx_gen import PG
from pypower.idx_brch import F_BUS,T_BUS,PF,PT
import copy

ppc=case9()
ppc=to_ppc0(ppc)
load_demand=sum(ppc['bus'][:,PD])
print('load_demand = ',load_demand)
PG_without_slack=sum(ppc['gen'][:,PG])
print('PG_without_slack = ',PG_without_slack)
for i,val in enumerate(ppc['bus'][:,BUS_TYPE].tolist()):
    if val == REF:
        slack_bus=i
        break
print('slack_bus = ',slack_bus)
branch_from_slack=[]
for i,val in enumerate(ppc['branch'][:,F_BUS].tolist()):
    if val == slack_bus:
        branch_from_slack.extend([i])
branch_to_slack=[]
for i,val in enumerate(ppc['branch'][:,T_BUS].tolist()):
    if val == slack_bus:
        branch_to_slack.extend([i])
print('\n')

## run pf
print('NR Method')
from pypower.api import ppoption, runpf
ppopt = ppoption(PF_ALG=1,VERBOSE=0,OUT_ALL=0,OUT_ALL_LIM=0,OUT_V_LIM=0)
result_nr,success = runpf(ppc,ppopt)
PGen = result_nr['gen'][:,PG]
PL_NR = sum(result_nr['branch'][:, PF] + result_nr['branch'][:, PT]) # compute real power loss vector

print('PL_NR = ',PL_NR)
print('PG_slack_NR = ',result_nr['gen'][slack_bus,PG])
print('PG_slack_NR = ',load_demand - PG_without_slack + PL_NR)
print(result_nr['branch'][:, PF])
print(result_nr['branch'][:, PT])
PG_slack_NR = 0
for i in branch_from_slack:
    PG_slack_NR = PG_slack_NR + result_nr['branch'][i, PF]
for i in branch_to_slack:
    PG_slack_NR = PG_slack_NR - result_nr['branch'][i, PT]
print('PG_slack_NR = ',PG_slack_NR)
print('\n')

## makeB_kron
print("Kron's Method")
from makeB_kron import makeB_kron
B,B0,B00,success=makeB_kron(ppc)
print(f'B = {B},\
    \nB0 = {B0},\
    \nB00 = {B00},\
    \nsuccess = {success}')

## losses_kron_method
from losses_kron_method import losses_kron_method
PG_Kron_ref=ppc['gen'][:,PG].tolist()
PG_Kron_ref[slack_bus] = load_demand - PG_without_slack
PL_kron,PL_Quadratic,PL_Linear,PL_Constant=losses_kron_method([B,B0,B00],ppc['baseMVA'],PG_Kron_ref)
print(f'PL_kron = {PL_kron},\
    \nPL_Quadratic = {PL_Quadratic},\
    \nPL_Linear = {PL_Linear},\
    \nPL_Constant = {PL_Constant}')
PG_Kron=copy.deepcopy(PG_Kron_ref)
PG_Kron[slack_bus]=PG_Kron[slack_bus] + PL_kron
PG_slack_Kron=PG_Kron[slack_bus]
print('Error Loss Kron = ',(PL_kron-PL_NR)/PL_NR)
print('Slack Missmatch Kron = ',(PG_slack_Kron-PG_slack_NR)/PG_slack_NR)
print('PG_slack_Kron = ',PG_slack_Kron)
print('\n')

## makeB_kron_slope
print("Linear Series Kron's Method (Kron's Slope Method)")
from makeB_kron_slope import makeB_kron_slope
slope_kron=makeB_kron_slope([B,B0],ppc['baseMVA'],PGen)
print('slope_kron = ',slope_kron)

## losses_kron_slope_method
from losses_kron_slope_method import losses_kron_slope_method
PG_Kron_ref=ppc['gen'][:,PG].tolist()
PG_Kron_ref[slack_bus] = load_demand - PG_without_slack
PL_Kron_ref,_,_,_=losses_kron_method([B,B0,B00],ppc['baseMVA'],PG_Kron_ref)
PG_Kron_slope=copy.deepcopy(PG_Kron_ref)
PG_Kron_slope[slack_bus] = PG_Kron_slope[slack_bus] + PL_Kron_ref
PL_Kron_slope=losses_kron_slope_method(slope_kron,PGen,PG_Kron_ref,PL_Kron_ref)
print('PL_Kron_slope',PL_Kron_slope)
PG_slack_Kron_slope = PG_Kron_ref[slack_bus] + PL_Kron_slope
print("Error Loss Kron's Slope Method = ",(PL_Kron_slope-PL_NR)/PL_NR)
print("Slack Missmatch Kron's Slope Method = ",(PG_slack_Kron_slope-PG_slack_NR)/PG_slack_NR)
print('PG_slack_Kron_slope = ',PG_slack_Kron_slope)
print('\n')
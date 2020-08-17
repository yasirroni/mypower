# Kron's Method Tutorial using myPower
'''Kron's Method Tutorial
Kron's Method is one of the most used linearization of AC power flow.
In this tutorial, you will be guided to make B matrix using Kron's Method and 
myPower original function, Kron's Slope Method. This work is under Apache 
License and act as pre-print of Kron's Slope Method publication (paper 
publication still on progress).

In this tutorial, we will use:

NRPF as Kron's Base
DCPF as evaluation target
It means that all losses are evaluated in evaluation target scenario (DCPF)
'''
                                                                                
## import library
import os
import copy

import mypower as myp
from mypower.oc_api import oc_matpower

## set MATPOWER case_name
case_name = 'case9'
print(case_name)

## myPower initialization
### start octave session for myPower
oc = oc_matpower()

### get index
idx = myp.get_index()
print(myp.pretty(idx))

### get slack generator index
mypc = oc.loadcase('case9')
mypc0 = myp.to_mypc0(mypc)
for bus_slack,val in zip(mypc0['bus'][:,idx['BUS_I']],mypc0['bus'][:,idx['BUS_TYPE']]):
    if val == idx['REF']:
        bus_slack = int(bus_slack)
        break
for num,val in enumerate(mypc0['gen'][:,idx['GEN_BUS']]):
    if int(val) == bus_slack:
        gen_slack = int(num)
        break
print(gen_slack)

## Newton Raphson Model (Also Kron's reference in making Kron's Coefficient)
### run nrpf
mypc_nr = oc.runpf(case_name)

### get losses for comparison
loss_nr = sum(mypc_nr['branch'][:, idx['PF']] + mypc_nr['branch'][:, idx['PT']])
print(loss_nr)

### get slack generator power for comparison
gen_PG_slack_nr = mypc_nr['gen'][gen_slack,idx['PG']]
print(gen_PG_slack_nr)

## DCPF Model (Also Kron's input in using Kron's Coefficient)
### set mpoption to dcpf
mpopt = oc.mpoption(model='DC')
print(myp.pretty(mpopt))

### run dcpf 
mypc_dc = oc.runpf(case_name,mpopt)

### get losses for comparison
loss_dc = sum(mypc_dc['branch'][:, idx['PF']] + mypc_dc['branch'][:, idx['PT']])
print(loss_dc)

### get slack generator power for comparison
gen_PG_slack_dc = mypc_dc['gen'][gen_slack,idx['PG']]
print(myp.pretty(gen_PG_slack_dc))

## Kron's Method Model (Also Kron's Slope reference in making Kron's Slope Coefficient)
### make B using Kron's Method
'''Note: mypc_kr is not Kron's pf output, but pf used to make B_kron'''
B_kron,mypc_kr = myp.makeB_kron(case_name,oc=oc)
print(myp.pretty(B_kron))

### get losses for comparison
#### total
B0_kron,B1_kron,B2_kron = B_kron['B0_kron'], B_kron['B1_kron'], B_kron['B2_kron']
loss_kr = myp.losses_kron(B0_kron,B1_kron,B2_kron,mypc_dc['gen'][:,idx['PG']],mypc_dc['baseMVA'])
print('loss_kr:',loss_kr)

#### individually
loss_kr0, loss_kr1, loss_kr2 = myp.losses_kron_detailed(B0_kron,B1_kron,B2_kron,mypc_dc['gen'][:,idx['PG']],mypc_dc['baseMVA'])
print('\tloss_kr0:',loss_kr0)
print('\tloss_kr1:',loss_kr1)
print('\tloss_kr2:',loss_kr2)

### get slack generator power for comparison
gen_PG_slack_kr = mypc_dc['gen'][gen_slack,idx['PG']] + loss_kr
print(gen_PG_slack_kr)

## Kron's Slope Model
### make B using Kron's Slope Method (Based on Taylor Series)
'''Note: mypc_krsl is not Kron's pf output, but pf used to make B_kron'''
B_kron_slope,mypc_krsl = myp.makeB_kron_slope(case_name,oc=oc)
print(myp.pretty(mypc_krsl['B_kron']))

### get losses for comparison
loss_krsl = myp.losses_kron_slope(B0_kron,B1_kron,B2_kron,B_kron_slope,mypc_krsl['B_kron']['PG_reff'],mypc_dc['gen'][:,idx['PG']],mypc_dc['baseMVA'])
print(loss_krsl)

### get slack generator power for comparison
gen_PG_slack_krsl = mypc_dc['gen'][gen_slack,idx['PG']] + loss_krsl
print(gen_PG_slack_krsl)

## Comparison
comparison = {
    'Losses': {
        'NRPF': loss_nr,
        'DCPF': loss_dc,
        'KRPF': loss_kr,
        'KRSLPF': loss_krsl
    },
    'Slack':{
        'NRPF': gen_PG_slack_nr,
        'DCPF': gen_PG_slack_dc,
        'KRPF': gen_PG_slack_kr,
        'KRSLPF': gen_PG_slack_krsl
    },
    'Losses Error':{
        'NRPF': (loss_nr - loss_nr) / loss_nr,
        'DCPF': (loss_dc - loss_nr) / loss_nr,
        'KRPF': (loss_kr - loss_nr) / loss_nr,
        'KRSLPF': (loss_krsl - loss_nr) / loss_nr
    },
    'Slack Error':{
        'NRPF': (gen_PG_slack_nr - gen_PG_slack_nr) / gen_PG_slack_nr,
        'DCPF': (gen_PG_slack_dc - gen_PG_slack_nr) / gen_PG_slack_nr,
        'KRPF': (gen_PG_slack_kr - gen_PG_slack_nr) / gen_PG_slack_nr,
        'KRSLPF': (gen_PG_slack_krsl - gen_PG_slack_nr) / gen_PG_slack_nr
    }
}
print(myp.pretty(comparison))
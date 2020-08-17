# import library
import os
import mypower as myp
from mypower.oc_api import oc_matpower

# start octave session for myPower
oc = oc_matpower()

# run power flow and get mypowercase
case_name = 'case9'
mypc = oc.runpf(case_name)
print(myp.pretty(mypc))

# save in str (can't be loaded automatically)
myp.save_str(mypc)

# save in pkl
myp.save_pkl(mypc,'mypc.pkl')

# delete mypc
del mypc

# load mypc
mypc = myp.load_pkl('mypc.pkl')

# get index
idx = myp.get_index()
print(myp.pretty(idx))

# get gen_PG from mypc
gen_PG = mypc['gen'][:,idx['PG']]
print(myp.pretty(gen_PG))

# convert to mypc0 for Python combatibility
mypc0 = myp.to_mypc0(mypc)
print(myp.pretty(mypc0['bus'][:,idx['BUS_I']]))

# revert to mypc for Octave compatibility
mypc = myp.to_mypc(mypc0)
print(myp.pretty(mypc['bus'][:,idx['BUS_I']]))

# setting mpopt
mpopt = oc.mpoption(model='DC')
print(myp.pretty(mpopt))

# using mpopt in runpf
mypc = oc.runpf(case_name,mpopt)
print(myp.pretty(mypc))
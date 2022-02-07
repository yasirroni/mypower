# import library
import os
import mypower as myp
import mypower.utils

# start octave session for mypower
m = myp.start_matpower()

# run power flow and get mypowercase
case_name = 'case9'
mypc = m.runpf(case_name)
print(myp.utils.pretty(mypc))

# save in str (can't be loaded automatically)
myp.utils.save_txt(mypc)

# save in pkl
myp.utils.save_pkl(mypc,'mypc.pkl')

# delete mypc
del mypc

# load mypc
mypc = myp.utils.load_pkl('mypc.pkl')

# get index
idx = myp.get_index()
print(myp.utils.pretty(idx))

# get gen_PG from mypc
gen_PG = mypc['gen'][:,idx['PG']]
print(myp.utils.pretty(gen_PG))

# convert to mypc0 for Python combatibility
mypc0 = myp.to_mypc0(mypc)
print(myp.utils.pretty(mypc0['bus'][:,idx['BUS_I']]))

# revert to mypc for Octave compatibility
mypc = myp.to_mypc(mypc0)
print(myp.utils.pretty(mypc['bus'][:,idx['BUS_I']]))

# setting mpopt
mpopt = m.mpoption(model='DC')
print(myp.utils.pretty(mpopt))

# using mpopt in runpf
mypc = m.runpf(case_name,mpopt)
print(myp.utils.pretty(mypc))
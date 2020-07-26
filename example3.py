# import library
import os
import myPower.api as myp
import myPower.matpower_api as mp

# start octave session for myPower
oc = myp.oc_matpower()

# run power flow and get mypowercase
mypc = oc.runpf()
print(myp.pretty(mypc))

# print in log
myp.save_str(mypc)

# save mypc
myp.save_object(mypc,'mypc.pkl')

# delete mypc
del mypc

# load mypc
mypc = myp.load_object('mypc.pkl')

# get index
idx = myp.get_index()
print(myp.pretty(idx))

# get gen_PG from mypc
gen_PG = mypc['gen'][:,idx['PG']]
print(myp.pretty(gen_PG))

# gen_PG in pu
baseMVA = mypc['baseMVA']
gen_PG_pu = gen_PG / baseMVA
print(gen_PG_pu)


# if __name__=='__main__':
#     from init_myp import init_myp
#     from myp_pretty import myp_pretty
#     from print_log import print_log
#     oc = init_myp()

#     idx_bus_list=idx_bus(oc=oc)
#     print(idx_bus_list)

    # mypc = runpf(oc=oc)
    # print(myp_pretty(mypc))
    # print_log(mypc)
    
    # mpopt = mpoption('pf.alg', 'FDXB', 'pf.tol', 1e-4,oc=oc)
    # print(myp_pretty(mpopt))
    # print_log(mpopt)
    
    # mypc = runpf('case30',mpopt,oc=oc)
    # print(myp_pretty(mypc))
    # print_log(mypc)
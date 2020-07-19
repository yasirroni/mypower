def runpf(*myp_arg,myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.runpf(*myp_arg)
    
def mpoption(*myp_arg,myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.mpoption(*myp_arg)

def loadcase(*myp_arg,myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.mpoption(*myp_arg)

def makeYbus(*myp_arg,myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.mpoption(*myp_arg)

def idx_bus(myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.idx_bus(nout=21)

def idx_brch(myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.idx_brch(nout=21)

def idx_cost(myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.idx_cost(nout=7)

def idx_gen(myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    return myp.idx_bus(nout=25)


if __name__=='__main__':
    from init_myp import init_myp
    from myp_pretty import myp_pretty
    from print_log import print_log
    myp = init_myp()

    idx_bus_list=idx_bus(myp=myp)
    print(idx_bus_list)

    # mypc = runpf(myp=myp)
    # print(myp_pretty(mypc))
    # print_log(mypc)
    
    # mpopt = mpoption('pf.alg', 'FDXB', 'pf.tol', 1e-4,myp=myp)
    # print(myp_pretty(mpopt))
    # print_log(mpopt)
    
    # mypc = runpf('case30',mpopt,myp=myp)
    # print(myp_pretty(mypc))
    # print_log(mypc)
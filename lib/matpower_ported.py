def runpf(*myp_arg,myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    mypc = myp.runpf(*myp_arg)
    return mypc

def mpoption(*myp_arg,myp=None):
    if myp == None:
        from init_myp import init_myp
        myp = init_myp()
    mpopt = myp.mpoption(*myp_arg)
    return mpopt

if __name__=='__main__':
    from init_myp import init_myp
    from myp_pretty import myp_pretty
    myp = init_myp()
    mypc = runpf(myp=myp)
    # print(myp_pretty(mypc))
    mpopt = mpoption('pf.alg', 'FDXB', 'pf.tol', 1e-4,myp=myp)
    # print(myp_pretty(mpopt))
    mypc = runpf('case30',mpopt,myp=myp)
    # print(myp_pretty(mypc))
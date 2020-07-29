def idx_cost(oc=None):
    if oc == None:
        from ..oc_matpower import oc_matpower
        oc = oc_matpower()
    return oc.idx_cost(nout=7)
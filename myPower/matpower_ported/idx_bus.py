def idx_bus(oc=None):
    if oc == None:
        from ..oc_matpower import oc_matpower
        oc = oc_matpower()
    return oc.idx_bus(nout=21)
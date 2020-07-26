def mpoption(*myp_arg,oc=None):
    if oc == None:
        from ..oc_matpower import oc_matpower
        oc = oc_matpower()
    return oc.mpoption(*myp_arg)
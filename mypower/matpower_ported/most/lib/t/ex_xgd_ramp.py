def ex_xgd_ramp(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.ex_xgd_ramp(*args,nout=nout)

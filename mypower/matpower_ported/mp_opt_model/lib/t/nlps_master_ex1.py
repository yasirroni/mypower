def nlps_master_ex1(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.nlps_master_ex1(*args,nout=nout)

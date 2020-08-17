def params_lin_constraint(*args,nout=6,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.params_lin_constraint(*args,nout=nout)

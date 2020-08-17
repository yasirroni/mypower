def params_quad_cost(*args,nout=4,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.params_quad_cost(*args,nout=nout)

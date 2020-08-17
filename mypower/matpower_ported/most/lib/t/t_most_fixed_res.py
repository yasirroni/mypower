def t_most_fixed_res(*args,nout=3,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_most_fixed_res(*args,nout=nout)

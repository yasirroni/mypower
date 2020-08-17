def t_most_30b_1_1_0_uc(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_most_30b_1_1_0_uc(*args,nout=nout)

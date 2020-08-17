def t_most_30b_3_1_17(*args,nout=2,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_most_30b_3_1_17(*args,nout=nout)

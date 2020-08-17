def most_ex4_dcopf_ss(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.most_ex4_dcopf_ss(*args,nout=nout)

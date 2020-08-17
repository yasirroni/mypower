def most_ex2_dcopf(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.most_ex2_dcopf(*args,nout=nout)

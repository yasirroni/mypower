def most_ex7_suc(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.most_ex7_suc(*args,nout=nout)

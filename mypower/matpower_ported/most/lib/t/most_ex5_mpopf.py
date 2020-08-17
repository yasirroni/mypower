def most_ex5_mpopf(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.most_ex5_mpopf(*args,nout=nout)

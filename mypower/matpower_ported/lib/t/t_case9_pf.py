def t_case9_pf(*args,nout=4,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_case9_pf(*args,nout=nout)

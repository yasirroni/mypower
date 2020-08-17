def t_psse_case3(*args,nout=1,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_psse_case3(*args,nout=nout)

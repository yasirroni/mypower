def t_case9_opf(*args,nout=6,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_case9_opf(*args,nout=nout)

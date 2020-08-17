def t_opf_tspopf_pdipm(*args,nout=1,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_opf_tspopf_pdipm(*args,nout=nout)

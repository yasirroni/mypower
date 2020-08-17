def t_opf_model_legacy(*args,nout=3,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_opf_model_legacy(*args,nout=nout)

def opf_model(*args,nout=0,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_model(*args,nout=nout)

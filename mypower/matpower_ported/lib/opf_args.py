def opf_args(*args,nout=17,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_args(*args,nout=nout)

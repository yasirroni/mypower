def opf_vlim_fcn(*args,nout=2,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_vlim_fcn(*args,nout=nout)

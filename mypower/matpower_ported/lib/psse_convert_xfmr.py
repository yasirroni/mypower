def psse_convert_xfmr(*args,nout=4,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.psse_convert_xfmr(*args,nout=nout)

def psse_convert_hvdc(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.psse_convert_hvdc(*args,nout=nout)

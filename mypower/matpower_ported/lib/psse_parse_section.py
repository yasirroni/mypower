def psse_parse_section(*args,nout=2,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.psse_parse_section(*args,nout=nout)

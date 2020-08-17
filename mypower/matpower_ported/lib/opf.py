def opf(*args,nout=11,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf(*args,nout=nout)

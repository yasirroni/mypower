def loadcase(*args,nout=7,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.loadcase(*args,nout=nout)

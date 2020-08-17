def runopf(*args,nout=8,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.runopf(*args,nout=nout)

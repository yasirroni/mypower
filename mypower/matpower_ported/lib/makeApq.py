def makeApq(*args,nout=5,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.makeApq(*args,nout=nout)
def runpf(*args,nout=6,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.runpf(*args,nout=nout)

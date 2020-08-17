def idx_bus(*args,nout=21,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.idx_bus(*args,nout=nout)

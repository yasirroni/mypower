def idx_gen(*args,nout=25,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.idx_gen(*args,nout=nout)

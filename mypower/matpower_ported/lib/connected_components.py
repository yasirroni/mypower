def connected_components(*args,nout=2,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.connected_components(*args,nout=nout)

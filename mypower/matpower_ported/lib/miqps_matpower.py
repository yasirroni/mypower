def miqps_matpower(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.miqps_matpower(*args,nout=nout)

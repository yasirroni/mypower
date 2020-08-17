def dSbus_dV(*args,nout=2,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.dSbus_dV(*args,nout=nout)

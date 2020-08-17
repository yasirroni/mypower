def case24_ieee_rts(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.case24_ieee_rts(*args,nout=nout)

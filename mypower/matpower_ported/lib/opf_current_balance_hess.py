def opf_current_balance_hess(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_current_balance_hess(*args,nout=nout)

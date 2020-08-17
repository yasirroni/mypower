def opf_legacy_user_cost_fcn(*args,nout=3,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_legacy_user_cost_fcn(*args,nout=nout)

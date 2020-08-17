def mpoption_info_ipopt(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.mpoption_info_ipopt(*args,nout=nout)

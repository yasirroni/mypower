def opf_nle_fcn1(*args,nout=2,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_nle_fcn1(*args,nout=nout)

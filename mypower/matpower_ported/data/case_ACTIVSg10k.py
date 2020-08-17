def case_ACTIVSg10k(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.case_ACTIVSg10k(*args,nout=nout)

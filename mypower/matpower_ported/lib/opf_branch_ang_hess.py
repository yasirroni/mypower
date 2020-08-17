def opf_branch_ang_hess(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.opf_branch_ang_hess(*args,nout=nout)

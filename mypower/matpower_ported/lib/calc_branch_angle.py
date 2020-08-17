def calc_branch_angle(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.calc_branch_angle(*args,nout=nout)

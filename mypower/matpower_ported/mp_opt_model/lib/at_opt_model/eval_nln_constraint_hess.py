def eval_nln_constraint_hess(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.eval_nln_constraint_hess(*args,nout=nout)

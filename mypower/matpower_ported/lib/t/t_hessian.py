def t_hessian(*args,nout=2,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_hessian(*args,nout=nout)

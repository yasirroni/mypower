def t_jacobian(*args,nout=2,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_jacobian(*args,nout=nout)

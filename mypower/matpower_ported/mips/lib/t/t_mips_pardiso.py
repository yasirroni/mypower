def t_mips_pardiso(*args,nout=2,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_mips_pardiso(*args,nout=nout)

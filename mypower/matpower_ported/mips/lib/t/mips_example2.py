def mips_example2(*args,nout=2,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.mips_example2(*args,nout=nout)

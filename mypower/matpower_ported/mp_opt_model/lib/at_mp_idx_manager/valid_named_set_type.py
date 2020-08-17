def valid_named_set_type(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.valid_named_set_type(*args,nout=nout)

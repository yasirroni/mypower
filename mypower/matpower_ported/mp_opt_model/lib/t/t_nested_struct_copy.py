def t_nested_struct_copy(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_nested_struct_copy(*args,nout=nout)

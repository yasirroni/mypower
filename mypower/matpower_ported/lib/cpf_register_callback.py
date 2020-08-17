def cpf_register_callback(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.cpf_register_callback(*args,nout=nout)

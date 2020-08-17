def cpf_qlim_event(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.cpf_qlim_event(*args,nout=nout)

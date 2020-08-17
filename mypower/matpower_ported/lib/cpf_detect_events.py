def cpf_detect_events(*args,nout=3,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.cpf_detect_events(*args,nout=nout)

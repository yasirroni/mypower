def varsets_cell2struct(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.varsets_cell2struct(*args,nout=nout)
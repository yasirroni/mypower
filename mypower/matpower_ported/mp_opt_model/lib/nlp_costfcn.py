def nlp_costfcn(*args,nout=3,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.nlp_costfcn(*args,nout=nout)

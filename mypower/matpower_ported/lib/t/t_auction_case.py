def t_auction_case(*args,nout=6,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_auction_case(*args,nout=nout)

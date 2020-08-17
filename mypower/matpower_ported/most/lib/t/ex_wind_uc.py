def ex_wind_uc(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.ex_wind_uc(*args,nout=nout)

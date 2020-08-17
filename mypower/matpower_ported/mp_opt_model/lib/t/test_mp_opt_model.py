def test_mp_opt_model(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.test_mp_opt_model(*args,nout=nout)

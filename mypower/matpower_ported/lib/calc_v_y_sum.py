def calc_v_y_sum(*args,nout=7,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.calc_v_y_sum(*args,nout=nout)

def feval_w_path(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.feval_w_path(*args,nout=nout)

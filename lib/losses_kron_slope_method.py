import numpy as np
def losses_kron_slope_method(slope_kron,PGen,PGen_ref,PL_ref):
    deltaPGen=(PGen-PGen_ref)
    PL=PL_ref+np.matmul(deltaPGen,slope_kron)
    return PL.tolist()
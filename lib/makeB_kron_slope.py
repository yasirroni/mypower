import numpy as np
def makeB_kron_slope(kronCoeffResult,baseMVA,PGen_ref):
    B=kronCoeffResult[0]
    B0=kronCoeffResult[1]
    PGen_ref=PGen_ref/baseMVA #convert to p.u.
    slope_kron=2*np.matmul(PGen_ref,B)+B0
    return slope_kron.tolist()
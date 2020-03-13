import numpy as np
def losses_kron_method(kronCoeffResult,baseMVA,PGen):
    """Compute losses based on Kron Method."""
    [B,B0,B00]=kronCoeffResult
    B=np.array(B)
    B0=np.array(B0)
    B00=np.array(B00)
    PGen=PGen/baseMVA #convert to p.u.
    PL_Quadratic=PGen.T.dot(B).dot(PGen)*baseMVA
    PL_Linear=B0.dot(PGen)*baseMVA
    PL_Constant=B00*baseMVA
    PL = PL_Quadratic+PL_Linear+PL_Constant #total power losses
    return PL.tolist(),PL_Quadratic.tolist(),PL_Linear.tolist(),PL_Constant.tolist()

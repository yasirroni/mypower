def losses_kron_method(kronCoeffResult,baseMVA,Pgen):
    """Compute losses based on Kron Method."""
    [B,B0,B00]=kronCoeffResult
    Pgen=Pgen/baseMVA #convert to p.u.
    PL_Quadratic=Pgen.T.dot(B).dot(Pgen)*baseMVA
    PL_Linear=B0.dot(Pgen)*baseMVA
    PL_Constant=B00*baseMVA
    PL = PL_Quadratic+PL_Linear+PL_Constant #total power losses
    return PL,PL_Quadratic,PL_Linear,PL_Constant

import numpy as np
def losses_kron(B0_kron,B1_kron,B2_kron,gen_PG_point,baseMVA):
    """Compute losses based on Kron's Method."""
    gen_PG_point_pu = np.array(gen_PG_point) / baseMVA #convert to p.u.
    B0_kron = np.array(B0_kron)
    B1_kron = np.array(B1_kron)
    B2_kron = np.array(B2_kron)
    # losses0 = B0_kron * baseMVA
    # losses1 = B1_kron.dot(gen_PG_point_pu) * baseMVA
    # losses2 = gen_PG_point_pu.T.dot(B2_kron).dot(gen_PG_point_pu) * baseMVA
    # losses = losses2 + losses1 + losses0 #total power losses
    return (B0_kron + B1_kron.dot(gen_PG_point_pu) + gen_PG_point_pu.T.dot(B2_kron).dot(gen_PG_point_pu)) * baseMVA

def losses_kron_detailed(B0_kron,B1_kron,B2_kron,gen_PG_point,baseMVA):
    """Compute losses based on Kron's Method."""
    gen_PG_point_pu = np.array(gen_PG_point) / baseMVA #convert to p.u.
    B0_kron = np.array(B0_kron)
    B1_kron = np.array(B1_kron)
    B2_kron = np.array(B2_kron)
    losses0 = B0_kron * baseMVA
    losses1 = B1_kron.dot(gen_PG_point_pu) * baseMVA
    losses2 = gen_PG_point_pu.T.dot(B2_kron).dot(gen_PG_point_pu) * baseMVA
    # losses = losses2 + losses1 + losses0 #total power losses
    return losses0, losses1, losses2
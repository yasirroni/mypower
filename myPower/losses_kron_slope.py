import numpy as np
from .losses_kron import losses_kron

def losses_kron_slope(B0_kron,B1_kron,B2_kron,B_kron_slope,PG_reff,PG_point,baseMVA):
    loss_kr = losses_kron(B0_kron,B1_kron,B2_kron,PG_point,baseMVA)
    return np.matmul((PG_reff - PG_point),B_kron_slope) + loss_kr

def losses_kron_slope_detailed(B0_kron,B1_kron,B2_kron,B_kron_slope,PG_reff,PG_point,baseMVA):
    loss_kr = losses_kron(B0_kron,B1_kron,B2_kron,PG_point,baseMVA)
    # loss_krsl = np.matmul((PG_reff - PG_point),B_kron_slope)
    return loss_kr, np.matmul((PG_reff - PG_point),B_kron_slope)
import numpy as np
from numpy import array, zeros, pi
from numpy.linalg import inv
from pypower.api import ppoption, makeYbus, runpf
from pypower.idx_bus import PD, QD, VM, VA, BUS_TYPE, BUS_I
from pypower.idx_gen import PG, QG, GEN_BUS

def makeB_kron(ppc,pf_alg=1):
    """
    Make B Kron or Kron Coefficient based on Arango Angarita,(2018). B Kron can be used to estimate power losses without redoing the power flow.
    Source: Arango Angarita, Dario & Urrego, Ricardo & Rivera, Sergio. (2018). Robust loss coefficients: application to power systems with solar and wind energy.
    """
    baseMVA = ppc['baseMVA']
    ppopt = ppoption(PF_ALG=pf_alg,VERBOSE=0,OUT_ALL=0,OUT_ALL_LIM=0,OUT_V_LIM=0)
    result,success = runpf(ppc,ppopt)
    if success != 1:
        B=[]
        B0=[]
        B00=[]
        PL=[]
        print("No Solution in Power Flow!")
        return B, B0, B00, PL, success
    Ybus, _, _ = makeYbus(baseMVA,ppc['bus'],ppc['branch'])
    Zb = inv(Ybus.toarray())
    Pgen = result['gen'][:,PG]/baseMVA
    Qgen = result['gen'][:,QG]/baseMVA
    Pdem = result['bus'][:,PD]/baseMVA
    Qdem = result['bus'][:,QD]/baseMVA
    vm = result['bus'][:,VM]
    theta = result['bus'][:,VA]*(pi/180)
    V = vm*(np.exp(1j*theta))
    nGen = np.size(Pgen)
    nBus = len(ppc['bus'][:,BUS_I])
    for sl,busType in zip(range(nBus),result['bus'][:,BUS_TYPE]):
        if busType==3:
            break
    cal = np.transpose([result['gen'][:,GEN_BUS],result['gen'][:,PG],result['gen'][:,QG]])
    Pgen[Pgen==0] = 0.000001/baseMVA
    nodGen = cal[:,GEN_BUS]
    VGEN = V[nodGen]
    ILK = np.array((Pdem-1j*Qdem)/np.conj(V))
    ID = np.sum(ILK)
    LK = ILK/ID
    T = np.matmul((Zb[sl,:]),LK.T)
    Zb1 = (np.array(Zb[sl,nodGen])).flatten()
    Zb2 = (np.array(Zb[sl,sl])).flatten()
    Zclave = np.hstack((Zb1,Zb2))
    C_a = -1*LK/T
    C_aa = np.transpose([C_a])
    C = C_aa*Zclave
    clave = np.arange(nGen)
    for i in range(nGen):
        C[nodGen[i],clave[i]] = 1+C[nodGen[i],clave[i]]
    PHI = np.zeros([nGen+1,nGen+1], dtype=complex)
    for k in range(nGen):
        F = 1j*(Qgen[k]/Pgen[k])
        PHI[k,k] = (1-F)/(np.conj(VGEN[k]))
    IO = -1*V[sl]/(Zb[sl,sl])
    PHI[nGen,nGen] = IO
    PHI = np.array(PHI)
    H = np.real(PHI.dot(C.T).dot(Zb.real).dot(np.conj(C)).dot(np.conj(PHI)))
    B = H[:nGen,:nGen]
    B0 = 2*H[nGen,:nGen]
    B00 = H[nGen,nGen]
    return B, B0, B00, success

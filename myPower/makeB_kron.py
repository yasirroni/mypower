import numpy as np
from numpy import array, zeros, pi
from numpy.linalg import inv

from get_index import get_index

def makeB_kron(mypc='case9',oc=None):
    """
    Make B Kron or Kron Coefficient based on Arango Angarita,(2018). B Kron can be used to estimate power losses without redoing the power flow.
    Source: Arango Angarita, Dario & Urrego, Ricardo & Rivera, Sergio. (2018). Robust loss coefficients: application to power systems with solar and wind energy.
    """

    if oc == None:
        import myPower.api as myp
        oc = myp.oc_matpower()

    if 'success' not in mypc:
        mypc=oc.runpf()

    if mypc['success'] != 1:
        B=[]
        B0=[]
        B00=[]
        PL=[]
        print("No Solution in Power Flow!")
        return B, B0, B00, PL, mypc['success']
    
    idx = get_index()
    baseMVA = mypc['baseMVA']
    
    Ybus = oc.makeYbus(mypc)
    Zb = inv(Ybus.toarray())

    gen_PG_pu = mypc['gen'][:,idx['PG']] / baseMVA
    gen_QG_pu = mypc['gen'][:,idx['QG']] / baseMVA
    bus_PD_pu = mypc['bus'][:,idx['PD']] / baseMVA
    bus_QD_pu = mypc['bus'][:,idx['QD']] / baseMVA
    bus_VM = mypc['bus'][:,idx['VM']]
    bus_VA_rad = mypc['bus'][:,idx['VA']] * (pi / 180)
    bus_voltage = bus_VM*(np.exp(1j*bus_VA_rad))
    number_of_gen = len(gen_PG_pu)
    number_of_bus = len(bus_PD_pu)
    for bus_slack,bus_BUS_TYPE in zip(range(number_of_bus),mypc['bus'][:,idx['BUS_TYPE']]):
        if bus_BUS_TYPE == 3:
            break
    
    return Ybus
    
    # cal = np.transpose([result['gen'][:,GEN_BUS],result['gen'][:,PG],result['gen'][:,QG]])
    # Pgen[Pgen==0] = 0.000001/baseMVA
    # nodGen = cal[:,GEN_BUS]
    # VGEN = V[nodGen]
    # ILK = np.array((Pdem-1j*Qdem)/np.conj(V))
    # ID = np.sum(ILK)
    # LK = ILK/ID
    # T = np.matmul((Zb[sl,:]),LK.T)
    # Zb1 = (np.array(Zb[sl,nodGen])).flatten()
    # Zb2 = (np.array(Zb[sl,sl])).flatten()
    # Zclave = np.hstack((Zb1,Zb2))
    # C_a = -1*LK/T
    # C_aa = np.transpose([C_a])
    # C = C_aa*Zclave
    # clave = np.arange(nGen)
    # for i in range(nGen):
    #     C[nodGen[i],clave[i]] = 1+C[nodGen[i],clave[i]]
    # PHI = np.zeros([nGen+1,nGen+1], dtype=complex)
    # for k in range(nGen):
    #     F = 1j*(Qgen[k]/Pgen[k])
    #     PHI[k,k] = (1-F)/(np.conj(VGEN[k]))
    # IO = -1*V[sl]/(Zb[sl,sl])
    # PHI[nGen,nGen] = IO
    # PHI = np.array(PHI)
    # H = np.real(PHI.dot(C.T).dot(Zb.real).dot(np.conj(C)).dot(np.conj(PHI)))
    # B = H[:nGen,:nGen]
    # B0 = 2*H[nGen,:nGen]
    # B00 = H[nGen,nGen]
    # return B.tolist(), B0.tolist(), B00.tolist(), success

    # Ybus, _, _ = makeYbus(baseMVA,ppc['bus'],ppc['branch'])
    # Zb = inv(Ybus.toarray())
    # Pgen = result['gen'][:,PG]/baseMVA
    # Qgen = result['gen'][:,QG]/baseMVA
    # Pdem = result['bus'][:,PD]/baseMVA
    # Qdem = result['bus'][:,QD]/baseMVA
    # vm = result['bus'][:,VM]
    # theta = result['bus'][:,VA]*(pi/180)
    # V = vm*(np.exp(1j*theta))
    # nGen = np.size(Pgen)
    # nBus = len(ppc['bus'][:,BUS_I])
    # for sl,busType in zip(range(nBus),result['bus'][:,BUS_TYPE]):
    #     if busType==3:
    #         break


# if mpopt==None:
    #     mpopt = myp.mpoption({
    #         'pf':{
    #             'alg':'NR'
    #         },
    #         'verbose':0,
    #         'out':{
    #             'all':0,
    #             'lim':{
    #                 'all':0,
    #                 'v':0
    #             }
    #         }
    #     })
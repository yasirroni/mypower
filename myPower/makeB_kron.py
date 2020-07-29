import numpy as np
import sys
from numpy import array, zeros, pi
from numpy.linalg import inv

from .get_index import get_index
from .to_mypc0 import to_mypc0

def makeB_kron(mypc='case9',mpopt=None,oc=None):
    '''
    Make B Kron or Kron Coefficient based on Arango Angarita,(2018). B Kron can be used to estimate power losses without redoing the power flow.
    Source: Arango Angarita, Dario & Urrego, Ricardo & Rivera, Sergio. (2018). Robust loss coefficients: application to power systems with solar and wind energy.
    
    Note    :
        1. Output mypc from makeB_kron is not Kron's pf output, but pf used to make B_kron
    '''

    if oc == None:
        import myPower.api as myp
        oc = myp.oc_matpower()

    if type(mypc) == str:
        if mpopt != None:
            mypc = oc.runpf(mypc,mpopt)
        else:
            mypc = oc.runpf(mypc)

        if mypc['success'] != 1:
            print("No Solution in Power Flow!")
            return None, mypc

    idx = get_index()

    baseMVA = mypc['baseMVA']
    if 'Ybus' not in mypc:
        mypc['Ybus'] = oc.makeYbus(mypc)
    if 'Zbus' not in mypc:
        mypc['Zbus'] = inv(mypc['Ybus'].toarray())

    mypc0 = to_mypc0(mypc)
    for bus_slack,val in zip(mypc0['bus'][:,idx['BUS_I']],mypc0['bus'][:,idx['BUS_TYPE']]):
        if val == idx['REF']:
            bus_slack = int(bus_slack)
            break
    
    gen_PG_slack = 0
    for key,val in zip(mypc0['gen'][:,idx['GEN_BUS']],mypc0['gen'][:,idx['PG']]):
        if key == bus_slack:
            gen_PG_slack += int(val)

    if int(gen_PG_slack) == 0:
        if mpopt != None:
            mypc = oc.runpf(mypc,mpopt)
        else:
            mypc = oc.runpf(mypc)
        mypc0 = to_mypc0(mypc)

    gen_PG_pu = mypc0['gen'][:,idx['PG']] / baseMVA
    gen_QG_pu = mypc0['gen'][:,idx['QG']] / baseMVA
    bus_PD_pu = mypc0['bus'][:,idx['PD']] / baseMVA
    bus_QD_pu = mypc0['bus'][:,idx['QD']] / baseMVA

    gen_PG_pu[gen_PG_pu == 0] = sys.float_info.epsilon

    bus_VM = mypc0['bus'][:,idx['VM']]
    bus_VA_rad = mypc0['bus'][:,idx['VA']] * (pi / 180)
    bus_voltage = bus_VM*(np.exp(1j*bus_VA_rad))
    
    cal = np.transpose([mypc0['gen'][:,idx['GEN_BUS']],mypc0['gen'][:,idx['PG']],mypc0['gen'][:,idx['QG']]])
    nod_gen = (cal[:,idx['GEN_BUS']]).astype(int)
    v_gen = bus_voltage[nod_gen]
    
    ILK = np.array((bus_PD_pu - 1j * bus_QD_pu) / np.conj(bus_voltage))
    ID = np.sum(ILK)
    LK = ILK / ID
    T = np.matmul(mypc0['Zbus'][bus_slack,:],LK.T)

    Zbus_1 = (np.array(mypc0['Zbus'][bus_slack,nod_gen])).flatten()
    Zbus_2 = (np.array(mypc0['Zbus'][bus_slack,bus_slack])).flatten()
    Zbus_clave = np.hstack((Zbus_1,Zbus_2))
    C = np.transpose([-1 * LK / T]) * Zbus_clave

    number_of_gen = len(gen_PG_pu)
    PHI =  np.zeros([number_of_gen + 1,number_of_gen + 1], dtype=complex)

    for i in range(number_of_gen):
        C[nod_gen[i],i] = 1 + C[nod_gen[i],i]

        F = 1j * (gen_QG_pu[i] / gen_PG_pu[i])
        PHI[i,i] = (1-F) / (np.conj(v_gen[i]))

    IO = -1 * bus_voltage[bus_slack] / (mypc0['Zbus'][bus_slack,bus_slack])
    PHI[number_of_gen,number_of_gen] = IO
    PHI = np.array(PHI)
    
    H = np.real(PHI.dot(C.T).dot(mypc0['Zbus'].real).dot(np.conj(C)).dot(np.conj(PHI)))
    
    mypc['B_kron'] = {
        'B0_kron' : H[number_of_gen,number_of_gen],
        'B1_kron' : 2*H[number_of_gen,:number_of_gen],
        'B2_kron' : H[:number_of_gen,:number_of_gen],
        'PG_reff' : mypc['gen'][:,idx['PG']]
    }

    return mypc['B_kron'], mypc
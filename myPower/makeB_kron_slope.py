import numpy as np
import sys
from numpy import array, zeros, pi
from numpy.linalg import inv

from .makeB_kron import makeB_kron
from .to_mypc0 import to_mypc0
def makeB_kron_slope(mypc='case9',mpopt=None,oc=None):
    '''Make B correction of original B Kron's Matrix
    The correction is based on Taylor Series and result of
    power generated by Kron's Method.

    Note    :
        1. Output mypc from makeB_kron is not Kron's pf output, but pf used to make B_kron
    '''
    if 'B_kron' not in mypc:
        B_kron,mypc = makeB_kron(mypc=mypc,mpopt=mpopt,oc=oc)

    mypc['B_kron']['B_kron_slope'] = kron2slope(B_kron['B1_kron'],B_kron['B2_kron'],B_kron['PG_reff'],mypc['baseMVA'])

    return mypc['B_kron']['B_kron_slope'], mypc

def kron2slope(B1_kron,B2_kron,PG_reff,baseMVA):
    '''Make B correction of original B Kron's Matrix
    The correction is based on Taylor Series and result of
    power generated by Kron's Method.
    
    Note:
        PG_reff : Generated power used in making B_kron in makeB_kron()
    '''
    B1_kron = np.array(B1_kron)
    B2_kron = np.array(B2_kron)

    PG_reff = PG_reff / baseMVA #convert to p.u.
    
    return 2 * np.matmul(PG_reff,B2_kron) + B1_kron
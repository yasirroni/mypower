from .get_index import get_index

def get_losses(mypc, idx=None):
    if idx is None:
        idx = get_index()
    losses_p = get_losses_p(mypc, idx=idx)
    losses_q = get_losses_q(mypc, idx=idx)
    return losses_p, losses_q

def get_losses_p(mypc, idx=None):
    if idx is None:
        idx = get_index()
    try:
        return sum(mypc['branch'][:, idx['PF']] + mypc['branch'][:, idx['PT']])
    except IndexError: # haven't run powerflow
        msg = "Please run power flow first before extracting losses."
        raise IndexError(msg)

def get_losses_q(mypc, idx=None):
    if idx is None:
        idx = get_index()
    try:
        return sum(mypc['branch'][:, idx['QF']] + mypc['branch'][:, idx['QT']])
    except IndexError: # haven't run powerflow
        msg = "Please run power flow first before extracting losses."
        raise IndexError(msg)
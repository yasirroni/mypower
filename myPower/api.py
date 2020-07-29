'''myPower.api
Pseudo package for all core functions of myPower.
Example:
    # import function individually into namespace
    from myPower.api import oc_matpower
    oc = oc_matpower

    # import all function
    import myPower.api as myp
    oc = myp.oc_matpower
'''

from __future__ import absolute_import

from .get_index import get_index
from .makeB_kron import makeB_kron
from .makeB_kron_slope import makeB_kron_slope
from .makeB_kron_slope import kron2slope
from .load_object import load_object
from .losses_kron import losses_kron
from .losses_kron import losses_kron_detailed
from .losses_kron_slope import losses_kron_slope
from .losses_kron_slope import losses_kron_slope_detailed
from .oc_matpower import oc_matpower
from .pretty import pretty
from .save_str import save_str
from .save_pkl import save_pkl
from .to_mypc import to_mypc
from .to_mypc0 import to_mypc0


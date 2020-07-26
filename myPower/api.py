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
from .load_object import load_object
from .oc_matpower import oc_matpower
from .pretty import pretty
from .save_str import save_str
from .save_object import save_object


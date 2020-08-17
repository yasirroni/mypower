# myPower
Supplementary function and port of [MATPOWER](https://github.com/MATPOWER/matpower) in Python. myPower stands for Matlab Python Ported MATPOWER.

## mypower/
Containing original myPower function.

## mypower/matpower_ported
Containing callable ported MATPOWER function with Oct2Py nout = max_nout.

Due MATPOWER folder naming, there is some changes in folder naming:

Path name is replaced for:

    @   : at_

    -   : _

If dir name already exist in python module, the dir name is revised:

    dirname     : _dirname

# Requirements
## Octave (Tutorial for Windows 10)
1. Download [octave](https://www.gnu.org/software/octave/download.html) zip.
2. Add new Environment Variable.

```
Variable name: OCTAVE_EXECUTABLE
Variable value: location:\\of\\octave\\bin\\octave-cli.exe
```

3. Restart computer to make 'os.environ' recognize the new path.
4. To test, open Command Prompt, run python, import oct2py.

```
python
import oct2py
```

## Library
myPower needs [numpy](https://github.com/numpy/numpy) and [oct2py](https://github.com/blink1073/oct2py) to be used.
```
pip install numpy oct2py
```

# Notable of functions
1. losses_kron: Compute losses based on Kron's coefficient
2. losses_kron_slope: Compute losses based on Taylor series of Kron's coefficient
3. makeB_kron: Make B based on Kron's method
4. makeB_kron_slope: Make first derivative of B Matrices of Kron method
5. to_mypc: Revert mypc indexing to start from 1 for octave compatibility
6. to_mypc0: Fix mypc bus indexing to start from 0 for Pyhton compatibility

# Usage
To use oct2py based MATPOWER, use:
```
from mypower.oc_api import oc_matpower

oc = oc_matpower()
mypc = oc.runpf()
```

To use myPower original function, use:
```
import mypower as myp

B_kron,mypc_kr = myp.makeB_kron(case_name,oc=oc)
```

To use MATPOWER ported (bridge) using oct2py with max nout, use:
```
from mypower.matpower_api import runpf

result = runpf()
[MVAbase, bus, gen, branch, success, et] = result
```

See tutorial for detailed example.

# Authors
* **Muhammad Yasirroni** - [yasirroni](https://github.com/yasirroni)

See also the list of [contributors](https://github.com/yasirroni/myPower/graphs/contributors) who participated in this project.

Feel free if you want to contribute.

# Acknowledgement
This repository was supported by [Faculty of Engineering, Universitas Gadjah Mada](https://ft.ugm.ac.id/en/) under the supervision of [Mr. Sarjiya](https://www.researchgate.net/profile/Sarjiya_Sarjiya)
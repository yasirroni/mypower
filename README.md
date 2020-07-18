# myPower
Supplementary function and port of [MATPOWER](https://github.com/MATPOWER/matpower) in Python.

## lib
Containing original myPower function

## matpower_ported
Containing callable ported MATPOWER function 

# Requirements
## Octave (Tutorial for Windows 10)
1. Download [octave](https://www.gnu.org/software/octave/download.html) zip.
2. Add new Environment Variable

```
Variable name: OCTAVE_EXECUTABLE
Variable value: location:\\of\\octave\\bin\\octave-cli.exe
```

3. Restart computer to make 'os.environ' recognize the new path.
4. To test, open Command Prompt, run python, import oct2py

```
python
import oct2py
```

## Library
myPower needs [numpy](https://github.com/numpy/numpy) to be used.
Some codes is dependent on [oct2py](https://github.com/blink1073/oct2py) and [PYPOWER](https://github.com/rwl/PYPOWER).

```
pip install numpy oct2py pypower
```
# List of functions
1. to_ppc0.py: Fix ppc bus for makeYbus, makeB, etc
2. makeB_kron.py: Make B based on Kron's method
3. losses_kron_method.py: Compute losses based on Kron's coefficient
4. makeB_kron_slope.py: Make first derivative of B Matrices of Kron method
5. losses_kron_slope_method.py: Compute losses based on Taylor series of Kron's coefficient

# Authors
* **Muhammad Yasirroni** - [yasirroni](https://github.com/yasirroni)

See also the list of [contributors](https://github.com/yasirroni/myPower/graphs/contributors) who participated in this project.

Feel free if you want to contribute.
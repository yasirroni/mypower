# myPower

Supplementary function and port of [MATPOWER](https://github.com/MATPOWER/matpower) in Python. myPower stands for Matlab Python Ported MATPOWER.

## Requirements

### Octave (Tutorial for Windows 10)

1. Download [octave](https://www.gnu.org/software/octave/download.html) zip.
2. Add new Environment Variable to execute `octave-cli`.

    Variable name: `OCTAVE_EXECUTABLE`

    Variable value: `location:\\of\\octave\\bin\\octave-cli.exe`

3. Restart computer to make 'os.environ' recognize the new path.
4. To test, open Command Prompt, run python, import oct2py.

    ```python
    import oct2py
    ```

### Library

myPower needs [numpy](https://github.com/numpy/numpy) and [oct2py](https://github.com/blink1073/oct2py) to be used.

```bash
pip install numpy oct2py
```

### Matpower

#### Windows (command prompt)

Note: It is assumed that `matpower` is located on `mypower/` subfolder (not repository root folder). Thus, use `cd mypower` if you are from repository root folder.

```bash
cd mypower
curl -L https://github.com/MATPOWER/matpower/archive/refs/tags/7.1.zip > matpower.zip
tar -xf matpower.zip
del matpower7.1.zip
```

## Notable of functions

1. losses_kron: Compute losses based on Kron's coefficient

2. makeB_kron: Make B based on Kron's method

3. to_mypc: Revert mypc indexing to start from 1 for octave compatibility

4. to_mypc0: Fix mypc bus indexing to start from 0 for Pyhton compatibility

## Usage

To use oct2py based MATPOWER, use:

```python
from mypower.oc_api import oc_matpower

oc = oc_matpower()
mypc = oc.runpf(nout=1) # nout specify number of returned variable from Octave
```

See tutorial for detailed example.

## Authors

* **Muhammad Yasirroni** - [yasirroni](https://github.com/yasirroni)

See also the list of [contributors](https://github.com/yasirroni/myPower/graphs/contributors) who participated in this project.

Feel free if you want to contribute.

## Acknowledgement

This repository was supported by [Faculty of Engineering, Universitas Gadjah Mada](https://ft.ugm.ac.id/en/) under the supervision of [Mr. Sarjiya](https://www.researchgate.net/profile/Sarjiya_Sarjiya)
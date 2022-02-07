# mypower

Supplementary function and port of [MATPOWER](https://github.com/MATPOWER/matpower) in Python, powered by octave via oct2py.

## Requirements

### Octave (Tutorial for Windows 10)

1. Download [octave](https://www.gnu.org/software/octave/download.html).

2. Install octave, write down the destination path.

3. Open Environment Variable. You can access it by pressing <kbd>Windows-Key</kbd>, type `edit the system environment variables`, and press <kbd>&#9166;Enter</kbd> to search.

4. Add new Environment Variable to execute `octave-cli`. The path is likely to be `C:\Program Files\octave-5.2.0-w64\mingw64\bin\octave-cli.exe`.

    Variable name: `OCTAVE_EXECUTABLE`

    Variable value: `location:\\of\\octave\\bin\\octave-cli.exe`

5. Restart computer to make `os.environ` recognize the new path.

### MATPOWER

The recommended way to install MATPOWER from python is using [matpower-pip](https://github.com/yasirroni/matpower-pip).

```plaintext
pip install matpower
```

If you already have MATPOWER installed, you can pass the path to mypower when starting matpower instance.

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

See also the list of [contributors](https://github.com/yasirroni/mypower/graphs/contributors) who participated in this project.

Feel free if you want to contribute.

## Acknowledgement

This repository was supported by [Faculty of Engineering, Universitas Gadjah Mada](https://ft.ugm.ac.id/en/) under the supervision of [Mr. Sarjiya](https://www.researchgate.net/profile/Sarjiya_Sarjiya)
# mypower

Supplementary function and port of [MATPOWER](https://github.com/MATPOWER/matpower) in Python, powered by octave via oct2py.

## Requirements

### Octave (Tutorial for Windows 10)

1. Download [octave](https://octave.org/download#ms-windows).

1. Install octave, and write down the installation destination path.

    ```plaintext
    C:\Program Files\octave-7.3.0-w64
    ```

1. From the installation destination path, find the **octave client path**, that is the path to `octave-cli.exe` under `mingw64\bin\` folder. Copy the path.

    ```plaintext
    C:\Program Files\octave-7.3.0-w64\mingw64\bin\octave-cli.exe
    ```

1. Open Environment Variable. You can access it by pressing Windows-Key, type `edit the system environment variables`, and press Enter to search.

1. Click `Environment Variables`.

1. Under `System variables`, click `New...`.

1. Fill the `Variable name` with `OCTAVE_EXECUTABLE`, and `Variable value` with the **octave client path**.

    Variable name: `OCTAVE_EXECUTABLE`

    Variable value: `C:\Program Files\octave-7.3.0-w64\mingw64\bin\octave-cli.exe`

1. Restart (not shutdown, but restart) the computer to make `os.environ` recognize the new path.

### oct2py

1. Install `oct2py` from python PyPI using a command prompt.

    ```shell
    pip install oct2py
    ```

1. Check `octave` and `oct2py` installation by running the below python code.

    ```python
    from oct2py import octave

    octave.path()
    ```

### MATPOWER

The recommended way to install MATPOWER from python is using [matpower-pip](https://github.com/yasirroni/matpower-pip).

```plaintext
pip install matpower
```

If you already have MATPOWER installed, you can pass the path to mypower when starting matpower instance.

## Usage

To use oct2py based MATPOWER, use:

```python
import mypower as myp

m = myp.start_matpower()
mypc = m.runpf(nout=1) # nout specify number of returned variable from Octave
```

See the tutorial for a detailed example.

## Citing `mypower`

We do request that publications derived from the use of `mypower`, explicitly acknowledge that fact by citing the appropriate paper(s) and the software mentioned in [MATPOWER publication](https://github.com/MATPOWER/matpower#citing-matpower) and the following citation:

> M. Yasirroni, Sarjiya, "mypower: Supplementary function and Python port of MATPOWER", GitHub, 2021. [Online]. Available: https://github.com/yasirroni/mypower.

If a journal publication from the author appears, it also needs to be cited.

## Authors

* **Muhammad Yasirroni** - [yasirroni](https://github.com/yasirroni)

See also the list of [contributors](https://github.com/yasirroni/mypower/graphs/contributors) who participated in this project.

Feel free if you want to contribute.

## Acknowledgment

This repository was supported by the [Faculty of Engineering, Universitas Gadjah Mada](https://ft.ugm.ac.id/en/) under the supervision of [Mr. Sarjiya](https://www.researchgate.net/profile/Sarjiya_Sarjiya)

<!--
This README can be printed using:

    pandoc README.md -o README.pdf
-->
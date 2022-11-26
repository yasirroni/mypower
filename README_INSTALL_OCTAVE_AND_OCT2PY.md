# Install Octave and oct2py

<!-- TODO: octave installation for ubuntu -->

## Octave for Windows 10

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

## oct2py

1. Install `oct2py` from python PyPI using a command prompt.

    ```shell
    pip install oct2py
    ```

1. Check `octave` and `oct2py` installation by running the below python code.

    ```python
    from oct2py import octave

    octave.path()
    ```

<!--
This README can be printed using:

    pandoc README_INSTALL_OCTAVE_AND_OCT2PY.md -o README_INSTALL_OCTAVE_AND_OCT2PY.pdf
-->

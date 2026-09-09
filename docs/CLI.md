# Command Line Interface

You can run READ from the command line using [python](https://www.python.org/downloads/)
or [uv](https://docs.astral.sh/uv/).

You can find all scripts in the `/scripts` folder.

> [!NOTE]
>
> Installing READ to your global environment will make all scripts globally available,
> nevertheless we recommend using uv even though it requires copying the scripts to the
> desired running location. However, this has the benefit that READ runs in an isolated
> environment!

## Usage with `uvx`

You can use READ with [uv](https://docs.astral.sh/uv/)
**without installing READ** or **running scripts** by using
[uvx](https://docs.astral.sh/uv/reference/cli/#uv-tool-run).

For example, instead of running the `tmt_chimerys.py` script, you can run:
```bash
uvx --python 3.13 --from imp-read tmt_chimerys <args>
```
Where `<args>` are the arguments that should be passed to `tmt_chimerys` (see below).

## Chimerys DIA

- Export Chimerys PSMs from Proteome Discoverer in tab-separated `.txt` format.
- \[Optionally\] Export Chimerys Proteins from Proteome Discoverer in tab-seperated `.txt` format.
- Set you desired parameters in `config.toml`.
- The scripts support both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when the scripts are run.
- The following steps are optional if you want to convert your `.raw` files manually:
  - Download ThermoRawFileParser from [here](https://github.com/CompOmics/ThermoRawFileParser/releases/tag/v1.4.5).
  - Convert your RAW file with:
    ```bash
    ThermoRawFileParser.exe -i RAW_FILE_NAME.raw
    ```
- Install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - We recommend and tested using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- **Option A (recommended): Running via [uv](https://docs.astral.sh/uv/).**
  - [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if it's not already installed on your system, e.g.:
    ```bash
    pip install uv
    ```
  - Run the script with:
    ```bash
    uv run tmt_chimerys.py -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini
    ```
  - _or_ if you also have proteins with:
    ```bash
    uv run tmt_chimerys.py -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini -p PROTEOME_DISCOVERER_Proteins.txt
    ```
  - To display all possible parameters run:
    ```bash
    uv run tmt_chimerys.py --help
    ```
- **Option B: Running via native python.**
  - Install python 3.12 or 3.13 from [here](https://www.python.org/downloads/).
  - Install READ with:
    ```bash
    pip install imp-read
    ```
  - Run READ with:
    ```bash
    tmt_chimerys -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini
    ```
  - _or_ if you also have proteins with:
    ```bash
    tmt_chimerys -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini -p PROTEOME_DISCOVERER_Proteins.txt
    ```
  - To display all possible parameters run:
    ```bash
    tmt_chimerys --help
    ```
- The result will be new files with name extension `_purity_tmt_quant` that are written out,
  containing purity and quantification values.
- Please refer to [OUTPUT.md](https://github.com/hgb-bin-proteomics/READ/blob/master/docs/OUTPUT.md) for a description of the new
  columns in the output file(s).

## Chimerys DDA

- Export Chimerys PSMs from Proteome Discoverer in tab-separated `.txt` format.
- \[Optionally\] Export Chimerys Proteins from Proteome Discoverer in tab-seperated `.txt` format.
- Set you desired parameters in `config.toml`.
- The scripts support both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when the scripts are run.
- The following steps are optional if you want to convert your `.raw` files manually:
  - Download ThermoRawFileParser from [here](https://github.com/CompOmics/ThermoRawFileParser/releases/tag/v1.4.5)
  - Convert your RAW file with:
    ```bash
    ThermoRawFileParser.exe -i RAW_FILE_NAME.raw
    ```
- Install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - We recommend and tested using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- **Option A (recommended): Running via [uv](https://docs.astral.sh/uv/).**
  - [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if it's not already installed on your system, e.g.:
    ```bash
    pip install uv
    ```
  - Run the script with:
    ```bash
    uv run tmt_chimerys_dda.py -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini
    ```
  - _or_ if you also have proteins with:
    ```bash
    uv run tmt_chimerys_dda.py -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini -p PROTEOME_DISCOVERER_Proteins.txt
    ```
  - To display all possible parameters run:
    ```bash
    uv run tmt_chimerys_dda.py --help
    ```
- **Option B: Running via native python.**
  - Install python 3.12 or 3.13 from [here](https://www.python.org/downloads/).
  - Install READ with:
    ```bash
    pip install imp-read
    ```
  - Run READ with:
    ```bash
    tmt_chimerys_dday -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini
    ```
  - _or_ if you also have proteins with:
    ```bash
    tmt_chimerys_dda -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini -p PROTEOME_DISCOVERER_Proteins.txt
    ```
  - To display all possible parameters run:
    ```bash
    tmt_chimerys_dda --help
    ```
- The result will be new files with name extension `_purity_tmt_quant` that are written out,
  containing purity and quantification values.
- Please refer to [OUTPUT.md](https://github.com/hgb-bin-proteomics/READ/blob/master/docs/OUTPUT.md) for a description of the new
  columns in the output file(s).

## Spectronaut

- Export matched precursors/the main report from Spectronaut in **semicolon-separated** `.csv` format.
  - If your result file is comma-separated you need to pass `-d ","` to the script.
- Set you desired parameters in `config.toml`.
- The scripts support both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when the scripts are run.
- The following steps are optional if you want to convert your `.raw` files manually:
  - Download ThermoRawFileParser from [here](https://github.com/CompOmics/ThermoRawFileParser/releases/tag/v1.4.5)
  - Convert your RAW file with:
    ```bash
    ThermoRawFileParser.exe -i RAW_FILE_NAME.raw
    ```
- Install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - We recommend and tested using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- **Option A (recommended): Running via [uv](https://docs.astral.sh/uv/).**
  - [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if it's not already installed on your system, e.g.:
    ```bash
    pip install uv
    ```
  - Run the script with:
    ```bash
    uv run tmt_spectronaut.py -s SPECTRA.mzML -i report.csv -c config.toml -t tmt18plex_default.ini
    ```
  - To display all possible parameters run:
    ```bash
    uv run tmt_spectronaut.py --help
    ```
- **Option B: Running via native python.**
  - Install python 3.12 or 3.13 from [here](https://www.python.org/downloads/).
  - Install READ with:
    ```bash
    pip install imp-read
    ```
  - Run READ with:
    ```bash
    tmt_spectronaut -s SPECTRA.mzML -i report.csv -c config.toml -t tmt18plex_default.ini
    ```
  - To display all possible parameters run:
    ```bash
    tmt_spectronaut --help
    ```
- The result will be new files with name extension `_purity_tmt_quant` that are written out,
  containing purity and quantification values.
- Please refer to [OUTPUT.md](https://github.com/hgb-bin-proteomics/READ/blob/master/docs/OUTPUT.md) for a description of the new
  columns in the output file(s).

## DIA-NN

- Use the `report.parquet` that you get from DIA-NN.
- Set you desired parameters in `config.toml`.
- The scripts support both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when the scripts are run.
- The following steps are optional if you want to convert your `.raw` files manually:
  - Download ThermoRawFileParser from [here](https://github.com/CompOmics/ThermoRawFileParser/releases/tag/v1.4.5)
  - Convert your RAW file with:
    ```bash
    ThermoRawFileParser.exe -i RAW_FILE_NAME.raw
    ```
- Install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - We recommend and tested using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- **Option A (recommended): Running via [uv](https://docs.astral.sh/uv/).**
  - [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if it's not already installed on your system, e.g.:
    ```bash
    pip install uv
    ```
  - Run the script with:
    ```bash
    uv run tmt_diann.py -s SPECTRA.mzML -i report.parquet -c config.toml -t tmt18plex_default.ini
    ```
  - To display all possible parameters run:
    ```bash
    uv run tmt_diann.py --help
    ```
- **Option B: Running via native python.**
  - Install python 3.12 or 3.13 from [here](https://www.python.org/downloads/).
  - Install READ with:
    ```bash
    pip install imp-read
    ```
  - Run READ with:
    ```bash
    tmt_diann -s SPECTRA.mzML -i report.parquet -c config.toml -t tmt18plex_default.ini
    ```
  - To display all possible parameters run:
    ```bash
    tmt_diann --help
    ```
- The result will be new files with name extension `_purity_tmt_quant` that are written out,
  containing purity and quantification values.
- Please refer to [OUTPUT.md](https://github.com/hgb-bin-proteomics/READ/blob/master/docs/OUTPUT.md) for a description of the new
  columns in the output file(s).

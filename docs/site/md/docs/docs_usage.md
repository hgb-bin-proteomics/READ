# Usage

- On Microsoft Windows READ can be run as a standalone executable or via python.
- Other operating systems are limited to python, please see below.
- Quick start with [uvx](https://docs.astral.sh/uv/reference/cli/#uv-tool-run):
  ```bash
  uvx --python 3.13 --from imp-read tmt_chimerys --help
  ```
  - Use `tmt_chimerys` for [Chimerys](https://www.msaid.de/chimerys) DIA result files.
  - Use `tmt_chimerys_dda` for [Chimerys](https://www.msaid.de/chimerys) DDA result files.
  - Use `tmt_spectronaut` for [Spectronaut](https://biognosys.com/software/spectronaut/) result files.
  - Use `tmt_diann` for [DIA-NN](https://github.com/vdemichev/DiaNN) result files.
- Runtime per RAW file is usually between 15-30 minutes.

## Usage with OpenMS

<div style="text-align: justify">

To use OpenMS quantification you will need a dedicated configuration file that can be generated via:

```bash
IsobaricAnalyzer -write_ini tmt18plex_default.ini
```

Alternatively, you can use the `tmt18plex_default.ini` file in the `config/` directory ➡️ see [here](https://github.com/hgb-bin-proteomics/READ/tree/master/config).

> [!WARNING]
> On Microsoft Windows you might have to unblock the
> downloaded `tmt18plex_default.ini` file for usage with READ either via its _Properties_ (right-click) or
> using [PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file).

> [!IMPORTANT]
> You might want to adapt the `tmt18plex_default.ini` file to your TMT lot. Please refer to the
> OpenMS [documentation](https://openms.de/documentation/html/TOPP_IsobaricAnalyzer.html)!

</div>

## Usage with the TMT Resolution GUI Tool

![TMT Resolution GUI Tool screenshot](https://github.com/hgb-bin-proteomics/TMT_Resolution_GUI/raw/master/Application/Screenshot.png)

<div style="text-align: justify">

You might also want to use the output of the Resolution GUI tool developed by Dina L. Bai, Tian Zhang _et al._[^1] as additional input for better quality control. Please refer to this repository for instructions: [https://github.com/hgb-bin-proteomics/TMT_Resolution_GUI](https://github.com/hgb-bin-proteomics/TMT_Resolution_GUI).

</div>

[^1]: Keele, G.R., Dou, Y., Kodikara, S.P. et al. Expanding the landscape of aging via orbitrap astral mass spectrometry and tandem mass tag integration. _Nat Commun_ 16, 4753 (2025). [https://doi.org/10.1038/s41467-025-60022-x](https://doi.org/10.1038/s41467-025-60022-x)

## Using the GUI

![GUI screenshot](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/gui.png)

<div style="text-align: justify">

We provide compiled standalone binaries for Microsoft Windows that offer a graphical user interface (GUI). Please download the executables from
[releases](https://github.com/hgb-bin-proteomics/READ/releases).

The source code for the built executables is available at [this repository](https://github.com/hgb-bin-proteomics/READ-GUI).

> [!IMPORTANT]
> Please note that using the GUI still requires installation of
> [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html)
> if quantification via OpenMS is enabled! Python is bundled with the application
> and is not required to be installed!

</div>

## Using the CLI

<div style="text-align: justify">

You can run READ from the command line using the [python](https://www.python.org/downloads/)
or [uv](https://docs.astral.sh/uv/) command line interface (CLI) as detailed below.

> [!IMPORTANT]
> Please note that RAW file input is only supported on Microsoft Windows-based systems!
> If you use another OS please convert your RAW files to `.mzML` beforehand!

> [!TIP]
> If you are using uv/uvx you can clear the uv cache after running READ with `uv cache clear`!

</div>

## Using the CLI: Chimerys DIA

- Export Chimerys PSMs from Proteome Discoverer in tab-separated `.txt` format.
- \[Optionally\] Export Chimerys Proteins from Proteome Discoverer in tab-seperated `.txt` format.
- Set you desired parameters in `config.toml`.
- READ supports both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when READ is run.
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
  - Run READ with:
    ```bash
    uvx --python 3.13 --from imp-read tmt_chimerys -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini
    ```
  - _or_ if you also have proteins with:
    ```bash
    uvx --python 3.13 --from imp-read tmt_chimerys -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini -p PROTEOME_DISCOVERER_Proteins.txt
    ```
  - To display all possible parameters run:
    ```bash
    uvx --python 3.13 --from imp-read tmt_chimerys --help
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
- Please refer to [Output](/docs/docs_output) for a description of the new
  columns in the output file(s).

## Using the CLI: Chimerys DDA

- Export Chimerys PSMs from Proteome Discoverer in tab-separated `.txt` format.
- \[Optionally\] Export Chimerys Proteins from Proteome Discoverer in tab-seperated `.txt` format.
- Set you desired parameters in `config.toml`.
- READ supports both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when READ is run.
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
  - Run READ with:
    ```bash
    uvx --python 3.13 --from imp-read tmt_chimerys_dda -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini
    ```
  - _or_ if you also have proteins with:
    ```bash
    uvx --python 3.13 --from imp-read tmt_chimerys_dda -s SPECTRA.mzML -i PROTEOME_DISCOVERER_PSMs.txt -c config.toml -t tmt18plex_default.ini -p PROTEOME_DISCOVERER_Proteins.txt
    ```
  - To display all possible parameters run:
    ```bash
    uvx --python 3.13 --from imp-read tmt_chimerys_dda --help
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
- Please refer to [Output](/docs/docs_output) for a description of the new
  columns in the output file(s).

## Using the CLI: Spectronaut

- Export matched precursors/the main report from Spectronaut in **semicolon-separated** `.csv` format.
  - If your result file is comma-separated you need to pass `-d ","` to READ.
- Set you desired parameters in `config.toml`.
- READ supports both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when READ is run.
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
  - Run READ with:
    ```bash
    uvx --python 3.13 --from imp-read tmt_spectronaut -s SPECTRA.mzML -i report.csv -c config.toml -t tmt18plex_default.ini
    ```
  - To display all possible parameters run:
    ```bash
    uvx --python 3.13 --from imp-read tmt_spectronaut --help
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
- Please refer to [Output](/docs/docs_output) for a description of the new
  columns in the output file(s).

## Using the CLI: DIA-NN

- Use the `report.parquet` that you get from DIA-NN.
- Set you desired parameters in `config.toml`.
- READ supports both `.raw` files and `.mzML` files as input, `.raw` files will be automatically
  converted to `.mzML` when READ is run.
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
  - Run READ with:
    ```bash
    uvx --python 3.13 --from imp-read tmt_diann -s SPECTRA.mzML -i report.parquet -c config.toml -t tmt18plex_default.ini
    ```
  - To display all possible parameters run:
    ```bash
    uvx --python 3.13 --from imp-read tmt_diann --help
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
- Please refer to [Output](/docs/docs_output) for a description of the new
  columns in the output file(s).

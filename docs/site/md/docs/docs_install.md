# Installation

<div style="text-align: justify">

**READ** can easily be installed via [PyPI](https://pypi.org/p/IMP-READ/) and run via the command line. We also provide executables with a graphical user interface for Microsoft Windows
which can be downloaded [here](https://github.com/hgb-bin-proteomics/READ/releases). In-depth information on how to install and run **READ** can be found below.

</div>

## Requirements

- Please install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - \[Recommended\] We tested READ using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- If you want to run READ via the command line/python, you need to either
  - install [python 3.12 or 3.13](https://www.python.org/downloads/),
  - _or_ install [uv](https://docs.astral.sh/uv/getting-started/installation/) (_highly recommended_).
- READ was tested with result files from
  - Cimerys `v4.7.0 (Proteome Discoverer 3.2)`,
  - DIA-NN `v2.2.0`, and
  - Spectronaut `v20.1.250624.92449`
- ...but READ should also work with result files from newer software versions!
- READ supports Thermo RAW files as input on Microsoft Windows-based systems, on other operating systems
  please convert your RAW files to `.mzML` format first!
  - \[Recommended\] We tested READ with RAW files converted with ThermoRawFileParser version [1.4.5](https://github.com/CompOmics/ThermoRawFileParser/releases/tag/v1.4.5)!
- We recommend at least 16GB of memory for running READ!

> [!IMPORTANT]
> - We generally recommend using [uv](https://docs.astral.sh/uv/) for running READ!
> - Please also refer to [Usage](/docs/docs_usage)
>   for more information on how to use READ with uv.

## Installation

You can install READ from [PyPI](https://pypi.org/p/IMP-READ/) via pip:

```bash
pip install imp-read
```

Or into your [uv](https://docs.astral.sh/uv/) project via:

```bash
uv add imp-read
```

Installation should not take longer than a few seconds!

<div style="text-align: justify">

> [!TIP]
> The recommended way of using READ is via [uvx](https://docs.astral.sh/uv/reference/cli/#uv-tool-run)
> which does not require installation of READ!<br>Please see [Usage](/docs/docs_usage)!

</div>

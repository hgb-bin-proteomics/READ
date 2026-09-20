# READ
_\[R\]eporter Ion \[E\]xtractor and \[A\]nnotation \[D\]irector_

<img src="https://github.com/hgb-bin-proteomics/READ/raw/master/docs/logo/logo_padded.png" align="left" width="200px" style="padding-right: 20px;"/>

<div style="text-align: justify">

**READ** is a python-based tool to orchestrate
TMTpro-18plex quantification for \[single cell\] DIA and DDA searches with
[Chimerys](https://www.msaid.de/chimerys),
[Spectronaut](https://biognosys.com/software/spectronaut/), and
[DIA-NN](https://github.com/vdemichev/DiaNN).

**READ** supports Thermo RAW files via [ThermoRawFileParser](https://github.com/compomics/ThermoRawFileParser) or [mzML](https://www.psidev.info/mzml) files, maps
identified precursors to their corresponding MS1 and MS2 spectra, and then quantifies PSMs and/or proteins. Quantification is done either natively, via [OpenMS](https://openms.de/) (recommended), or
the TMT Resolution GUI Tool \[[publication](https://doi.org/10.1038/s41467-025-60022-x)\] (see also [Usage](/docs/docs_usage)). Quantification is additionally quality controlled by optionally several filters including precursor co-isolation purity, reporter ion resolution,
minimum reporter signal, and minimum reporter signal-to-noise. Filtering behavior is easily controlled via a human-readable `.toml` configuration file.

**READ** can easily be installed via [PyPI](https://pypi.org/p/IMP-READ/) and run via the command line. We also provide executables with a graphical user interface for Microsoft Windows
which can be downloaded [here](https://github.com/hgb-bin-proteomics/READ/releases). In-depth information on how to install and run **READ** can be found in the [Installation](/docs/docs_install) section.

</div>

## Quick Start

Quick start with [uvx](https://docs.astral.sh/uv/reference/cli/#uv-tool-run):
```bash
uvx --python 3.13 --from imp-read tmt_chimerys --help
```
- Use `tmt_chimerys` for [Chimerys](https://www.msaid.de/chimerys) DIA result files.
- Use `tmt_chimerys_dda` for [Chimerys](https://www.msaid.de/chimerys) DDA result files.
- Use `tmt_spectronaut` for [Spectronaut](https://biognosys.com/software/spectronaut/) result files.
- Use `tmt_diann` for [DIA-NN](https://github.com/vdemichev/DiaNN) result files.

## Acknowledgements

We thank _Dasha Pototska_ for designing the READ logo!

## License

<div style="text-align: justify">

- The READ software and code are [MIT](https://github.com/hgb-bin-proteomics/READ/blob/master/LICENSE) licensed.
- The [READ logo](https://github.com/hgb-bin-proteomics/READ/tree/master/docs/logo) © 2026 by Dasha Pototska and Micha Birklbauer is licensed under
  [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).

</div>

## Citing

If you are using READ please cite the following publication:

- Manuscript in preparation
  ```text
  (wip)
  ```

# READ
_\[R\]eporter Ion \[E\]xtractor and \[A\]nnotation \[D\]irector_

<div style="text-align: justify">

**READ** is a python-based tool to orchestrate mass spectrometry-based
TMTpro-18plex protein quantification for \[single cell\] DIA and DDA searches with
[Chimerys](https://www.msaid.de/chimerys),
[Spectronaut](https://biognosys.com/software/spectronaut/), and
[DIA-NN](https://github.com/vdemichev/DiaNN).

**READ** supports Thermo RAW files via [ThermoRawFileParser](https://github.com/compomics/ThermoRawFileParser) or [mzML](https://www.psidev.info/mzml) files, maps
identified precursors to their corresponding MS1 and MS2 spectra, and then quantifies PSMs and/or proteins. Quantification is done either natively, via [OpenMS](https://openms.de/) (recommended), or
the TMT Resolution GUI Tool \[[publication](https://doi.org/10.1038/s41467-025-60022-x)\]. Quantification is additionally quality controlled by optionally several filters including precursor co-isolation purity, reporter ion resolution,
minimum reporter signal, and minimum reporter signal-to-noise. Filtering behavior is easily controlled via a human-readable `.toml` configuration file.

</div>

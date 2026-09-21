# Configuration

READ requires a configuration file in `.toml` format as input. An example READ
config file is given in the `config/` directory.
Please set the following parameters according to your needs in the `config.toml` file:

```toml
[METHOD]
# window size
window_size = 0.5
# window start (m/z)
window_start = 400.0
# window end (m/z)
window_end = 800.0
# window overlap
window_overlap = 0.0

[MATCHING]
# m/z tolerance for matching peaks in Dalton
mz_tolerance = 0.02
# retention time tolerance in seconds for matching identifications to MS2 spectra
rt_tolerance = 3.0
# retention time window in seconds that a MS1 and corresponding MS2 spectrum must be in
ms1_rt_window = 10.0

[ISOTOPES]
# whether precursor isotopes should be considered for purity calculation
consider_precursor_isotopes = true
# isotope match tolerance in Dalton
isotope_tolerance = 0.01
# maximum considered precursor charge
max_charge = 6

[FILTERING]
# precursor intensity fraction in the window to use as reference, only used for displaying some preliminary statistics
# for filtering use PROTEIN.min_purity
total_intensity_threshold = 0.7
# minimum relative intensity threshold compared to most intense peak in window to not be considered noise
noise_threshold = 0.1

[QUANTIFICATION]
# subtract the reporter noise from the reporter signal?
# if true, filtering by S/N should be turned off or thresholds set to 0.0
subtract_noise = true
# quantification method to use
# 1 = native
# 2 = OpenMS
# 3 = Resolution GUI
quantification_method = 2

[PROTEIN]
# Qvalue that should be used for filtering, only used for DIA-NN and Spectronaut
q_value = 0.01
# Normalized Chimerys Coefficient Threshold, anything below will be ignored, only applies to Chimerys
min_chimerys_coefficient = 1.0
# minimum average reporter S/N for a PSM to be considered for aggregation, only applies to Chimerys
min_avg_reporter_sn = 10.0
# minimum reporter resolution to be considered for aggregation
min_reporter_res = 45000.0
# minimum purity for a PSM to be considered for aggregation
min_purity = 0.7
# whether or not ambiguous protein groups should be filtered out, only used for DIA-NN and Spectronaut
keep_ambiguous_protein_groups = false

[CONDITIONS]
# please define your conditions here
# conditions should be given as condition name (without spaces) following an equal sign and then a list of TMT reporters
# see examples below
all = ["TMTpro-126",  "TMTpro-127N", "TMTpro-127C", "TMTpro-128N", "TMTpro-128C",
       "TMTpro-129N", "TMTpro-129C", "TMTpro-130N", "TMTpro-130C", "TMTpro-131N",
       "TMTpro-131C", "TMTpro-132N", "TMTpro-132C", "TMTpro-133N", "TMTpro-133C",
       "TMTpro-134N", "TMTpro-134C", "TMTpro-135N"]
cond1 = ["TMTpro-126",  "TMTpro-127N", "TMTpro-127C", "TMTpro-128N", "TMTpro-128C",
         "TMTpro-129N", "TMTpro-129C", "TMTpro-130N", "TMTpro-130C"]
cond2 = ["TMTpro-131N", "TMTpro-131C", "TMTpro-132N", "TMTpro-132C", "TMTpro-133N",
         "TMTpro-133C", "TMTpro-134N", "TMTpro-134C", "TMTpro-135N"]
# please define the min S/N thresholds per condition that should be used for protein aggregation here
# this should be sn_thresholds = map of thresholds for each condition
# see example below
sn_thresholds = { all = 0.0, cond1 = 10.0, cond2 = 10.0 }
# please define the min abundance thresholds per condition that should be used for protein aggregation here
# this should be s_thresholds = map of thresholds for each condition
# see example below (in this case -> no abundance thresholds)
# please not that the conditions have to be the same in sn_thresholds and s_thresholds
s_thresholds = { all = 0.0, cond1 = 0.0, cond2 = 0.0 }
```

## Method Parameters

The following parameters can be adjusted in the `[METHOD]` section:
- `window_size`:
  - Size of the isolation window in m/z (`float`).
- `window_start`:
  - Start of the mass (m/z) range for MS scans (`float`).
- `window_end`:
  - End of the mass (m/z) range for MS scans (`float`).
- `window_overlap`:
  - Size of the isolation window overlap in m/z (`float`).

> [!IMPORTANT]
>
> Please note that if a window file is provided to READ via `-w` or `--window` it will
> automatically override these parameters!

## Matching Parameters

The following parameters can be adjusted in the `[MATCHING]` section:
- `mz_tolerance`:
  - The m/z tolerance used for matching peaks in Dalton (`float`).
- `rt_tolerance`:
  - The retention time tolerance used for matching identifications to MS2 spectra in seconds (`float`).
- `ms1_rt_window`
  - The retention time window that a MS1 and corresponding MS2 spectrum must be in, in seconds (`float`).

> [!IMPORTANT]
>
> These parameters majorly control how identifications are matched to (precursor) peaks and MS spectra,
> usually the values in the default config file are a good selection!

## Isotope Parameters

The following parameters can be adjusted in the `[ISOTOPES]` section:
- `consider_precursor_isotopes`:
  - Whether precursor isotopes should be considered for precursor co-isolation purity calculation (`bool`).
- `isotope_tolerance`:
  - Tolerance used for identifying isotope peaks in Dalton (`float`).
- `max_charge`:
  - The maximum considered precursor charge when identifying isotope peaks (`int`).

## Filtering Parameters

The following parameters can be adjusted in the `[FILTERING]` section:
- `total_intensity_threshold`:
  - Parameter only used for logging some preliminary statistics, READ will display how many
    precursors pass this co-isolation purity value (`float`).
- `noise_threshold`:
  - The minimum relative intensity threshold compared to the most intense peak in the isolation window
    to not be considered noise, e.g. `0.1` denotes that any peak below 10% intensity of the most intense
    peak in the isolation window is considered noise (`float` between `[0, 1)`).

## Quantification Parameters

The following parameters can be adjusted in the `[QUANTIFICATION]` section:
- `subtract_noise`:
  - Whether the reporter noise should be subtracted from the reporter signal (`bool`).
  - **If this is set to `true` you should (probably) not apply any signal-to-noise filters!**
  - **Requires the output of the TMT Resolution GUI Tool as input for READ!**
- `quantification_method`:
  - Which quantification method to use (`int` between `[1, 3]`).
  - Can be `1` for native quantification,
    or `2` (recommended) for quantification with OpenMS (requires installation of OpenMS),
    or `3` for quantification based on the TMT Resolution GUI Tool (requires the output of
    the TMT Resolution GUI Tool as input for READ).

## Protein Filtering and Aggregation Parameters

The following parameters can be adjusted in the `[PROTEIN]` section:
- `q_value`:
  - The Qvalue that should be used for filtering (`float`).
  - Only used for DIA-NN and Spectronaut, Chimerys reports are assumed to be filtered/validated.
- `min_chimerys_coefficient`:
  - The minimum normalized Chimerys Coefficient, anything below will be ignored (`float`).
  - Only used for Chimerys.
- `min_avg_reporter_sn`:
  - The minimum average reporter S/N for a PSM to be considered for aggregation (`float`).
  - Only used for Chimerys.
- `min_reporter_res`:
  - The minimum reporter resolution for a reporter to be considered for aggregation (`float`).
  - **Requires the output of the TMT Resolution GUI Tool as input for READ to be applied! Otherwise parameter is ignored!**
- `min_purity`:
  - The minimum co-isolation purity for a PSM/precursor to be considered for aggregation (`float` between `[0, 1]`).
- `keep_ambiguous_protein_groups`:
  - Whether or not ambiguous protein groups should be filtered out (`bool`).
  - Only used for DIA-NN and Spectronaut.

## Condition Parameters

The `[CONDITIONS]` allows setup of different conditions based on the reporter ions.
Each condition should be given as the condition name (without spaces) followed by an equal sign
and then a list of TMT reporter ions, for example:

```toml
all = ["TMTpro-126",  "TMTpro-127N", "TMTpro-127C", "TMTpro-128N", "TMTpro-128C",
       "TMTpro-129N", "TMTpro-129C", "TMTpro-130N", "TMTpro-130C", "TMTpro-131N",
       "TMTpro-131C", "TMTpro-132N", "TMTpro-132C", "TMTpro-133N", "TMTpro-133C",
       "TMTpro-134N", "TMTpro-134C", "TMTpro-135N"]
```

This would define one condition called `all` which contains all reporter ions.

The following parameters can then be adjusted in the `[CONDITIONS]` section:
- `sn_thresholds`:
  - The minimum S/N thresholds per condition that should be applied for protein aggregation.
  - For example: `sn_thresholds = { all = 0.0 }` (no minimum S/N filter for condition `all`).
- `s_thresholds`:
  - The minimum abundance thresholds per condition that should be applied for protein aggregation.
  - For example: `s_thresholds = { all = 0.0 }` (no minimum abundance filter for condition `all`).

> [!TIP]
>
> Please also check the example config file for a better demonstration on how to set
> up different conditions!

## TMT Correction Factors

> [!IMPORTANT]
>
> You might also want to adapt the isotope correction factors for your TMT lot, you can do that in the `tmt18plex_default.ini` file.
> Please refer to the documentation site of OpenMS [here](https://openms.de/documentation/html/TOPP_IsobaricAnalyzer.html).

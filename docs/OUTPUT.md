# READ Output

The output you can expect after running READ depends on the version of READ you are running
(e.g. READ for Chimerys, READ for DIA-NN, etc.) and the input files - more specifically if you
supply a resolution file from the Resolution GUI Tool or not.

Below you can find a breakdown of all version and input combinations.

Please note, that columns containing a `{reporter}` placeholder exist once for every reporter
(so in total 18-times) with reporters being:

<details><summary>Expand to show reporter labels!</summary>
```text
TMTpro-126
TMTpro-127N
TMTpro-127C
TMTpro-128N
TMTpro-128C
TMTpro-129N
TMTpro-129C
TMTpro-130N
TMTpro-130C
TMTpro-131N
TMTpro-131C
TMTpro-132N
TMTpro-132C
TMTpro-133N
TMTpro-133C
TMTpro-134N
TMTpro-134C
TMTpro-135N
```
</details>

The Resolution GUI Tool output columns are:

<details><summary>Expand to show column names!</summary>
```text
```
</details>

## + Resolution GUI Tool Output

The following output will be produced by READ if a resolution file from the Resolution GUI Tool
is provided.

### READ for Chimerys DIA

#### PSM Table

Quantification:
- `Annotated {reporter}`:
  PSM-level reporter quantification (noise subtracted if specified).

PSM statistics:
- `Co-Isolation Purity`:
  Precursor co-isolation purity of the PSM.
- `Parsed MS2 Scan Number`:
  The scan number of the MS2 scan that the PSM was associated with.

Condition statistics:
- `Condition_S_{condition}`:
  Total signal for condition `{condition}`, e.g. sum of all signal for each reporter in the condition, guaranteed to be a float.
- `Condition_N_{condition}`:
  Total noise for condition `{condition}`, e.g. sum of all noise for each reporter in the condition, guaranteed to be a float.
- `Condition_SN_{condition}`:
  Total signal-to-noise for condition `{condition}`, e.g. `Condition_S_{condition}` divided by `Condition_N_{condition}`, guaranteed to be a float.

Annotated Resolution GUI Tool columns:
- `RESGUI_{colname}`:
  Annotated Resolution GUI Tool columns from the resolution file, where `{colname}` is the column name of each column in the file.

#### Protein Table

Quantification:
- `Annotated protein-level {reporter}`:
  Protein-level aggregated reporter quantification after filtering.

Reporter statistics per protein:
- `Annotated mean {reporter} S (unfiltered)`:
  Annotated mean reporter signal for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated mean {reporter} S (filtered)`:
  Annotated mean reporter signal for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated median {reporter} S (unfiltered)`:
  Annotated median reporter signal for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated median {reporter} S (filtered)`:
  Annotated median reporter signal for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated min {reporter} S (unfiltered)`:
  Annotated minimum reporter signal for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated min {reporter} S (filtered)`:
  Annotated minimum reporter signal for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated max {reporter} S (unfiltered)`:
  Annotated maximum reporter signal for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated max {reporter} S (filtered)`:
  Annotated maximum reporter signal for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated mean {reporter} S/N (unfiltered)`:
  Annotated mean reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated mean {reporter} S/N (filtered)`:
  Annotated mean reporter signal-to-noise for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated median {reporter} S/N (unfiltered)`:
  Annotated median reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated median {reporter} S/N (filtered)`:
  Annotated median reporter signal-to-noise for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated min {reporter} S/N (unfiltered)`:
  Annotated minimum reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated min {reporter} S/N (filtered)`:
  Annotated minimum reporter signal-to-noise for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated max {reporter} S/N (unfiltered)`:
  Annotated maximum reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated max {reporter} S/N (filtered)`:
  Annotated maximum reporter signal-to-noise for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated mean {reporter} resolution (unfiltered)`:
  Annotated mean reporter resolution for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated mean {reporter} resolution (filtered)`:
  Annotated mean reporter resolution for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated median {reporter} resolution (unfiltered)`:
  Annotated median reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated median {reporter} resolution (filtered)`:
  Annotated median reporter resolution for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated min {reporter} resolution (unfiltered)`:
  Annotated minimum reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated min {reporter} resolution (filtered)`:
  Annotated minimum reporter resolution for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.
- `Annotated max {reporter} resolution (unfiltered)`:
  Annotated maximum reporter signal-to-noise for the protein considering all `{reporter}` reporters, may be `NaN`.
- `Annotated max {reporter} resolution (filtered)`:
  Annotated maximum reporter resolution for the protein considering only `{reporter}` reporters that pass filtering, may be `NaN`.

PSM/Precursor statistics per protein:
- `Annotated mean purity`:
  Mean precursor co-isolation purity of all precursors associated with the protein, may be `NaN`.
- `Annotated median purity`:
  Median precursor co-isolation purity of all precursors associated with the protein, may be `NaN`.
- `Annotated number of PSMs (unfiltered)`:
  Total number of PSMs per protein, always a positive integer or zero.
- `Annotated number of PSMs (filtered)`:
  Number of PSMs that pass filtering, always a positive integer or zero.

## - Resolution GUI Tool Output

The following output will be produced by READ if a resolution file from the Resolution GUI Tool
is **NOT** provided.

### READ for Chimerys DIA

#### PSM Table

Quantification:
- `Annotated {reporter}`:
  PSM-level reporter quantification (noise subtracted if specified).

PSM statistics:
- `Co-Isolation Purity`:
  Precursor co-isolation purity of the PSM.
- `Parsed MS2 Scan Number`:
  The scan number of the MS2 scan that the PSM was associated with.

#### Protein Table

Quantification:
- `Annotated protein-level {reporter}`:
  Protein-level aggregated reporter quantification after filtering.

PSM/Precursor statistics per protein:
- `Annotated mean purity`:
  Mean precursor co-isolation purity of all precursors associated with the protein, may be `NaN`.
- `Annotated median purity`:
  Median precursor co-isolation purity of all precursors associated with the protein, may be `NaN`.
- `Annotated number of PSMs (unfiltered)`:
  Total number of PSMs per protein, always a positive integer or zero.
- `Annotated number of PSMs (filtered)`:
  Number of PSMs that pass filtering, always a positive integer or zero.

The following columns will be created but all values will be `NaN` and can be ignored:
<details><summary>Expand to show column names!</summary>
```text
Annotated mean {reporter} S (unfiltered)
Annotated mean {reporter} S (filtered)
Annotated median {reporter} S (unfiltered)
Annotated median {reporter} S (filtered)
Annotated min {reporter} S (unfiltered)
Annotated min {reporter} S (filtered)
Annotated max {reporter} S (unfiltered)
Annotated max {reporter} S (filtered)
Annotated mean {reporter} S/N (unfiltered)
Annotated mean {reporter} S/N (filtered)
Annotated median {reporter} S/N (unfiltered)
Annotated median {reporter} S/N (filtered)
Annotated min {reporter} S/N (unfiltered)
Annotated min {reporter} S/N (filtered)
Annotated max {reporter} S/N (unfiltered)
Annotated max {reporter} S/N (filtered)
Annotated mean {reporter} resolution (unfiltered)
Annotated mean {reporter} resolution (filtered)
Annotated median {reporter} resolution (unfiltered)
Annotated median {reporter} resolution (filtered)
Annotated min {reporter} resolution (unfiltered)
Annotated min {reporter} resolution (filtered)
Annotated max {reporter} resolution (unfiltered)
Annotated max {reporter} resolution (filtered)
```
</details>

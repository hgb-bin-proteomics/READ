# Example Data and Usage

Please download the example data from here: [pcloud](https://u.pcloud.link/publink/show?code=kZwSebJZHvmADbINd5yxry3WhPk5qQmg23mV).

Then extract the `example.zip` file and you should get the following contents:
- `20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw`
  - MS data, RAW file, DIA, 1 m/z isolation window.
- `config.toml`
  - The configuration for READ.
- `report.parquet`
  - DIA-NN report.
- `resolution.csv`
  - The resolution file produced from the TMT Resolution GUI Tool, see [here](https://github.com/hgb-bin-proteomics/TMT_Resolution_GUI).
- `tmt18plex_default.ini`
  - TMT lot configuration for OpenMS, see [here](https://openms.de/documentation/html/TOPP_IsobaricAnalyzer.html).

> [!IMPORTANT]
>
> This example assumes you are running the example on a Microsoft Windows PC. If you are not
> running Microsoft Windows you need to convert the RAW file to `.mzml` format and can only use the CLI!

> [!TIP]
>
> This example uses a DIA-NN report as input, but using Chimerys or Spectronaut works
> analogous!

## Requirements

- Please install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - We recommend and tested using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- If you want to run the READ command line interface examples, please install [uv](https://docs.astral.sh/uv/).
- If you want to run the READ graphical user interface examples, please download the executables from [here](https://github.com/hgb-bin-proteomics/READ/releases/latest).

## Example Usage of the GUI

- Launch the GUI via the `READ_Chimerys_DIA.exe` file.
- You will be presented with the following window:

![Example Screenshot Step 1](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_1.png)

- Select the following files:
  - diann: `report.parquet`
  - spectra: `20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw`
  - config: `config.toml`
  - ini_file: `tmt18plex_default.ini`
  - resolution: `resolution.csv`

![Example Screenshot Step 2](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_2.png)

- Then click the "Start" button.
- You will presented with "Running" window and a terminal should pop up.
- The terminal will run [ThermoRawFileParser](https://github.com/compomics/ThermoRawFileParser) and convert the RAW file to mzML format.

![Example Screenshot Step 3](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_3.png)

- After the conversion is done, the terminal will close automatically and another terminal should pop up.
- The terminal will run the [OpenMS IsobaricAnalyzer](https://openms.de/documentation/html/TOPP_IsobaricAnalyzer.html) to extract TMT reporter ion intensities.

![Example Screenshot Step 4](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_4.png)

- After the [OpenMS IsobaricAnalyzer](https://openms.de/documentation/html/TOPP_IsobaricAnalyzer.html) is done, the terminal will close automatically.
- The rest of the steps happen all within the "Running" window.
- You will see your configuration printed at the start.

![Example Screenshot Step 5](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_5.png)

- Then the precursor annotation is performed.
- You might see several `RuntimeWarning: Could not find a suitable MS1 spectrum for precursor` pop up throughout.
  - You can safely ignore these, some of the precursors might have been identified purely from their MS2 spectra without showing up in an MS1 scan.

![Example Screenshot Step 6](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_6.png)

- After that the protein annotation is performed.
- The application might seem unresponsive as nothing is printed to the "Running" window, however this is normal and the application is running in the background.
- The progress is sometimes not accurately reported in the GUI, please do not stop the application if you do not see progress - if there was an error it would pop up!
- The protein annotation might take a few minutes.

![Example Screenshot Step 7](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_7.png)

- Once the protein annotation is done the application finishes. You will get a pop up notification!

![Example Screenshot Step 8](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_8.png)

- The log in the "Finished" window should also say `Script finished successfully!` at the end. You can also scroll through the log.

![Example Screenshot Step 9](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_9.png)

This document is currently still a WIP!

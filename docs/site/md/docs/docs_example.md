# Example Data and Usage

Please download the example data from here: [pCloud](https://u.pcloud.link/publink/show?code=kZwSebJZHvmADbINd5yxry3WhPk5qQmg23mV).

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
> This example assumes you are running the example on a Microsoft Windows PC. If you are not
> running Microsoft Windows you need to convert the RAW file to `.mzml` format and can only use the CLI!

> [!TIP]
> This example uses a DIA-NN report as input, but using Chimerys or Spectronaut works
> analogous!

## Requirements

- Please install [OpenMS](https://openms.readthedocs.io/en/latest/about/installation.html).
  - We recommend and tested using OpenMS version [3.4.0](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/3.4.0/)!
- If you want to run the READ command line interface example, please install [uv](https://docs.astral.sh/uv/).
- If you want to run the READ graphical user interface example, please download the `READ_Chimerys_DIA.exe` executable from [here](https://github.com/hgb-bin-proteomics/READ/releases/latest).

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
- You will presented with the "Running" window and a terminal should pop up.
- The terminal will run [ThermoRawFileParser](https://github.com/compomics/ThermoRawFileParser) and convert the RAW file to `.mzML` format.

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
- The application might seem unresponsive as nothing is printed to the "Running" window, however **this is normal and the application is running in the background**.
- The progress is sometimes not accurately reported in the GUI, please do not stop the application if you do not see progress - if there was an error it would pop up!
- The protein annotation might take a few minutes.

![Example Screenshot Step 7](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_7.png)

- Once the protein annotation is done the application finishes. You will get a pop up notification!

![Example Screenshot Step 8](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_8.png)

- The log in the "Finished" window should also say `Script finished successfully!` at the end. You can also scroll through the log.

![Example Screenshot Step 9](https://github.com/hgb-bin-proteomics/READ/raw/master/docs/img/example/example_9.png)

- You will get a new `report_purity_tmt_quant.parquet` file annotated by READ. Please refer to [Output](/docs/docs_output) for details.

## Example Usage of the CLI

- Open a terminal in the folder where the example data is located.
- Run the following command:
  ```bash
  uvx --python 3.13 --from imp-read tmt_diann -s 20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw -i report.parquet -c config.toml -t tmt18plex_default.ini -r resolution.csv
  ```

::: details Expand to show example terminal output!
```text
C:\Users\Micha\Downloads\example>uvx --python 3.13 --from imp-read tmt_diann -s 20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw -i report.parquet -c config.toml -t tmt18plex_default.ini -r resolution.csv
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\pyopenms\__init__.py:41: UserWarning: Warning: OPENMS_DATA_PATH environment variable already exists. pyOpenMS will use it (C:\Program Files\OpenMS-3.4.1\share\OpenMS) to locate data in the OpenMS share folder (e.g., the unimod database), instead of the default (C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\pyopenms\share/OpenMS).
  warnings.warn(
{'window_size': 1.0, 'window_start': 400.0, 'window_end': 800.0, 'window_overlap': 0.0, 'mz_tolerance': 0.02, 'rt_tolerance': 3.0, 'rt_window': 10.0, 'threshold': 0.7, 'noise': 0.1, 'deisotope': True, 'isotope_tolerance': 0.01, 'max_charge': 6, 'subtract_noise': False, 'quantification_method': 2, 'q_value': 0.01, 'min_chimerys_coefficient': 0.0, 'min_avg_reporter_sn': 0.0, 'min_reporter_res': 45000.0, 'min_purity': 0.7, 'keep_pg': False, 'conditions': [{'name': 'H000Y000', 'reporters': ['TMTpro-126', 'TMTpro-127N', 'TMTpro-127C', 'TMTpro-129C', 'TMTpro-131C', 'TMTpro-133C'], 'sn': 20.0, 's': 0.0}, {'name': 'H100Y000', 'reporters': ['TMTpro-128N', 'TMTpro-128C', 'TMTpro-129N'], 'sn': 20.0, 's': 0.0}, {'name': 'H100Y010', 'reporters': ['TMTpro-130N', 'TMTpro-130C', 'TMTpro-131N'], 'sn': 20.0, 's': 0.0}, {'name': 'H100Y020', 'reporters': ['TMTpro-132N', 'TMTpro-132C', 'TMTpro-133N'], 'sn': 20.0, 's': 0.0}, {'name': 'H100Y100', 'reporters': ['TMTpro-134N', 'TMTpro-134C', 'TMTpro-135N'], 'sn': 20.0, 's': 0.0}]}
Found RAW file with name 20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw.
Converting using ThermoRawFileParser...
Downloading ThermoRawFileParser!
2026-10-21 16:53:40 INFO Started parsing 20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw
2026-10-21 16:53:47 INFO Processing 367660 MS scans
10% 20% 30% 40% 50% 60% 70% 80% 90% 100%

2026-10-21 16:58:39 INFO Finished parsing 20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.raw
2026-10-21 16:58:39 INFO Processing completed 0 errors, 0 warnings
Successfully converted file to 20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_ij8_53c75ng_1.mzML!
Total number of parsed spectra: 367660
Number of MS1 spectra: 6565
Number of MS2 spectra: 361095
Progress of 'loading mzML':
  Progress of 'loading spectra list':
  -- done [took 29.53 s (CPU), 29.56 s (Wall)] --
  Progress of 'loading chromatogram list':
  -- done [took 0.02 s (CPU), 0.01 s (Wall)] --
-- done [took 29.56 s (CPU), 29.59 s (Wall) @ 114.9 MiB/s] --
Selecting scans with activation mode: auto
Filtering by MS/MS(/MS) and activation mode:
  level 2: 361095 scans
Using MS-level 2 for quantification.
Calibration stats: Median distance of observed reporter ions m/z to expected position (up to 0.5 Th):
  ch 126  (~126.127): 0.0716347 Th [MSn impurity (within 0.002 Th): 1 windows|spectra]
  ch 127N (~127.124): 0.0378012 Th [MSn impurity (within 0.002 Th): 17 windows|spectra]
  ch 127C (~127.131): 0.0441135 Th [MSn impurity (within 0.002 Th): 22 windows|spectra]
  ch 128N (~128.128): -8.83457e-05 Th [MSn impurity (within 0.002 Th): 448 windows|spectra]
  ch 128C (~128.134): 6.71035e-05 Th [MSn impurity (within 0.002 Th): 443 windows|spectra]
  ch 129N (~129.131): 1.27344e-06 Th [MSn impurity (within 0.002 Th): 372 windows|spectra]
  ch 129C (~129.137): 0.00604562 Th [MSn impurity (within 0.002 Th): 190 windows|spectra]
  ch 130N (~130.134): -4.74365e-05 Th [MSn impurity (within 0.002 Th): 374 windows|spectra]
  ch 130C (~130.141): 7.74951e-05 Th [MSn impurity (within 0.002 Th): 477 windows|spectra]
  ch 131N (~131.138): -1.88525e-05 Th [MSn impurity (within 0.002 Th): 282 windows|spectra]
  ch 131C (~131.144): 0.00593494 Th [MSn impurity (within 0.002 Th): 222 windows|spectra]
  ch 132N (~132.141): -5.13037e-05 Th [MSn impurity (within 0.002 Th): 302 windows|spectra]
  ch 132C (~132.147): 5.83691e-05 Th [MSn impurity (within 0.002 Th): 397 windows|spectra]
  ch 133N (~133.144): -7.46094e-06 Th [MSn impurity (within 0.002 Th): 306 windows|spectra]
  ch 133C (~133.151): 0.00541227 Th [MSn impurity (within 0.002 Th): 264 windows|spectra]
  ch 134N (~134.148): -3.99121e-05 Th [MSn impurity (within 0.002 Th): 210 windows|spectra]
  ch 134C (~134.154): 2.39844e-05 Th [MSn impurity (within 0.002 Th): 243 windows|spectra]
  ch 135N (~135.151): -1.13281e-05 Th [MSn impurity (within 0.002 Th): 165 windows|spectra]

Impurities within the allowed reporter mass shift 0.002 Th have been found.They can be ignored if the spectra are m/z calibrated (see above), since only the peak closest to the theoretical position is used for quantification!
IsobaricQuantifier: skipped 73472 of 335770 selected scans due to lack of reporter information:
IsobaricQuantifier: channels with signal
  ch 126 : 19553 / 335770 (5%)
  ch 127N: 17684 / 335770 (5%)
  ch 127C: 18673 / 335770 (5%)
  ch 128N: 178127 / 335770 (53%)
  ch 128C: 180669 / 335770 (53%)
  ch 129N: 185350 / 335770 (55%)
  ch 129C: 53925 / 335770 (16%)
  ch 130N: 194259 / 335770 (57%)
  ch 130C: 190965 / 335770 (56%)
  ch 131N: 194077 / 335770 (57%)
  ch 131C: 60194 / 335770 (17%)
  ch 132N: 198606 / 335770 (59%)
  ch 132C: 197023 / 335770 (58%)
  ch 133N: 198979 / 335770 (59%)
  ch 133C: 68997 / 335770 (20%)
  ch 134N: 219870 / 335770 (65%)
  ch 134C: 220678 / 335770 (65%)
  ch 135N: 216313 / 335770 (64%)
IsobaricAnalyzer took 45.23 s (wall), 45.11 s (CPU), 2.16 s (system), 42.95 s (user); Peak Memory Usage: 4685 MB.
Reading consensusXML...: 100%|████████████████████████████████████████████████████████████████████████████| 262298/262298 [00:05<00:00, 46456.73it/s]
Reading Resolution GUI output...: 100%|███████████████████████████████████████████████████████████████████| 361095/361095 [00:08<00:00, 42896.03it/s]
Using OpenMS quantification!
Annotating DIA-NN result...:   0%|                                                                              | 1/101936 [00:00<3:00:31,  9.41it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 444.6158447265625 and retention time 2776.330755.
  warnings.warn(
Annotating DIA-NN result...:   0%|                                                                             | 110/101936 [00:00<03:55, 431.85it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.0429077148438 and retention time 2016.948081.
  warnings.warn(
Annotating DIA-NN result...:   1%|▋                                                                            | 829/101936 [00:01<02:44, 616.30it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.1349487304688 and retention time 2046.4074870000002.
  warnings.warn(
Annotating DIA-NN result...:   1%|▊                                                                           | 1029/101936 [00:01<02:39, 631.93it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0375366210938 and retention time 3614.091703000002.
  warnings.warn(
Annotating DIA-NN result...:   1%|▉                                                                           | 1224/101936 [00:02<02:38, 635.32it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 697.1078491210938 and retention time 2010.0715639999978.
  warnings.warn(
Annotating DIA-NN result...:   2%|█▏                                                                          | 1554/101936 [00:02<02:42, 619.63it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 669.9749145507812 and retention time 2243.916610000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 563.9306640625 and retention time 1575.444132.
  warnings.warn(
Annotating DIA-NN result...:   2%|█▎                                                                          | 1749/101936 [00:02<02:41, 620.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 636.6340942382812 and retention time 1912.047471.
  warnings.warn(
Annotating DIA-NN result...:   2%|█▎                                                                          | 1812/101936 [00:03<02:48, 593.17it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 756.084716796875 and retention time 2973.220468999998.
  warnings.warn(
Annotating DIA-NN result...:   3%|██                                                                          | 2797/101936 [00:04<02:45, 599.36it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 754.6127319335938 and retention time 3232.627113.
  warnings.warn(
Annotating DIA-NN result...:   3%|██▏                                                                         | 2917/101936 [00:04<02:49, 583.82it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 759.7081909179688 and retention time 2199.7739989999977.
  warnings.warn(
Annotating DIA-NN result...:   3%|██▎                                                                         | 3046/101936 [00:05<02:41, 611.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 584.060546875 and retention time 1958.490013000002.
  warnings.warn(
Annotating DIA-NN result...:   4%|██▋                                                                         | 3586/101936 [00:05<02:22, 692.42it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1806030273438 and retention time 3375.591649999998.
  warnings.warn(
Annotating DIA-NN result...:   4%|██▋                                                                         | 3656/101936 [00:06<02:28, 663.91it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 415.93316650390625 and retention time 2712.472674.
  warnings.warn(
Annotating DIA-NN result...:   4%|██▉                                                                         | 4006/101936 [00:06<02:22, 685.51it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 626.1463012695312 and retention time 2760.2467789999982.
  warnings.warn(
Annotating DIA-NN result...:   5%|███▍                                                                        | 4618/101936 [00:07<02:33, 633.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4464111328125 and retention time 3379.8466099999982.
  warnings.warn(
Annotating DIA-NN result...:   5%|███▌                                                                        | 4750/101936 [00:07<02:33, 632.00it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.68896484375 and retention time 2344.114002.
  warnings.warn(
Annotating DIA-NN result...:   5%|███▊                                                                        | 5138/101936 [00:08<02:39, 607.04it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 709.5986938476562 and retention time 2866.8788400000003.
  warnings.warn(
Annotating DIA-NN result...:   5%|████▏                                                                       | 5575/101936 [00:09<02:42, 593.51it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 784.6408081054688 and retention time 2195.7043639999983.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▏                                                                       | 5695/101936 [00:09<02:44, 585.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.080810546875 and retention time 2416.898247.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▎                                                                       | 5756/101936 [00:09<02:42, 591.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.400634765625 and retention time 3120.337807000002.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▍                                                                       | 5886/101936 [00:09<02:40, 596.61it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 652.6084594726562 and retention time 2330.9090359999977.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▍                                                                       | 6010/101936 [00:09<02:38, 606.01it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 737.1611328125 and retention time 3013.8384.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▋                                                                       | 6210/101936 [00:10<02:29, 639.28it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 777.81201171875 and retention time 2078.4594559999978.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▋                                                                       | 6335/101936 [00:10<02:56, 541.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 666.5943603515625 and retention time 2099.458933000002.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▊                                                                       | 6529/101936 [00:10<02:37, 605.35it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 787.6613159179688 and retention time 2295.514546000002.
  warnings.warn(
Annotating DIA-NN result...:   6%|████▉                                                                       | 6591/101936 [00:10<02:40, 593.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.0919799804688 and retention time 3763.0726510000018.
  warnings.warn(
Annotating DIA-NN result...:   7%|████▉                                                                       | 6651/101936 [00:10<02:44, 579.90it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 759.1204833984375 and retention time 2091.484897999998.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████                                                                       | 6849/101936 [00:11<02:30, 633.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0857543945312 and retention time 1580.968098.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4671630859375 and retention time 2928.875505.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████▏                                                                      | 6913/101936 [00:11<02:45, 574.28it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.452880859375 and retention time 2087.082435.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████▏                                                                      | 6972/101936 [00:11<02:54, 543.08it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 768.0474853515625 and retention time 2731.3210270000022.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████▏                                                                      | 7033/101936 [00:11<02:49, 560.32it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 713.1384887695312 and retention time 2945.4099690000003.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████▎                                                                      | 7090/101936 [00:11<02:53, 545.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1499633789062 and retention time 3575.4258569999997.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████▍                                                                      | 7355/101936 [00:12<02:29, 632.52it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0650634765625 and retention time 2350.775332999998.
  warnings.warn(
Annotating DIA-NN result...:   7%|█████▌                                                                      | 7483/101936 [00:12<02:30, 627.08it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.7147216796875 and retention time 3718.365255.
  warnings.warn(
Annotating DIA-NN result...:   8%|█████▉                                                                      | 8005/101936 [00:13<02:29, 628.07it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 616.2868041992188 and retention time 3011.057131000002.
  warnings.warn(
Annotating DIA-NN result...:   8%|██████                                                                      | 8131/101936 [00:13<02:35, 602.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4310913085938 and retention time 2754.8158660000017.
  warnings.warn(
Annotating DIA-NN result...:   8%|██████                                                                      | 8192/101936 [00:13<02:47, 558.20it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 663.0006103515625 and retention time 2116.4319469999978.
  warnings.warn(
Annotating DIA-NN result...:   8%|██████▏                                                                     | 8249/101936 [00:13<02:47, 560.55it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 738.1226806640625 and retention time 3221.947134.
  warnings.warn(
Annotating DIA-NN result...:   8%|██████▏                                                                     | 8369/101936 [00:13<02:42, 576.49it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 651.969482421875 and retention time 2420.418474.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.674560546875 and retention time 2021.2544929999979.
  warnings.warn(
Annotating DIA-NN result...:   8%|██████▎                                                                     | 8550/101936 [00:14<02:44, 567.30it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 618.9768676757812 and retention time 2853.629065000002.
  warnings.warn(
Annotating DIA-NN result...:   8%|██████▍                                                                     | 8608/101936 [00:14<02:44, 566.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 672.9688720703125 and retention time 1722.773302000002.
  warnings.warn(
Annotating DIA-NN result...:   9%|██████▍                                                                     | 8667/101936 [00:14<02:43, 572.02it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 616.5671997070312 and retention time 2252.151589000002.
  warnings.warn(
Annotating DIA-NN result...:   9%|██████▌                                                                     | 8797/101936 [00:14<02:31, 614.18it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 542.239990234375 and retention time 2134.910674000002.
  warnings.warn(
Annotating DIA-NN result...:   9%|██████▊                                                                     | 9064/101936 [00:14<02:26, 632.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 711.5606689453125 and retention time 2148.5670769999983.
  warnings.warn(
Annotating DIA-NN result...:   9%|██████▊                                                                     | 9195/101936 [00:15<02:28, 626.32it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 770.6179809570312 and retention time 2263.607196.
  warnings.warn(
Annotating DIA-NN result...:   9%|███████                                                                     | 9393/101936 [00:15<02:29, 619.82it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.12744140625 and retention time 2244.601236.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 794.0347290039062 and retention time 1961.7471310000021.
  warnings.warn(
Annotating DIA-NN result...:  10%|███████▎                                                                    | 9785/101936 [00:16<02:22, 647.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.3983764648438 and retention time 2937.3576869999997.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 670.0772705078125 and retention time 1780.092427000002.
  warnings.warn(
Annotating DIA-NN result...:  10%|███████▌                                                                   | 10209/101936 [00:16<02:12, 694.05it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 442.9090270996094 and retention time 2835.7387679999997.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4452514648438 and retention time 1589.459944999998.
  warnings.warn(
Annotating DIA-NN result...:  10%|███████▌                                                                   | 10349/101936 [00:17<02:22, 644.78it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 756.0194702148438 and retention time 2675.6893150000024.
  warnings.warn(
Annotating DIA-NN result...:  10%|███████▋                                                                   | 10482/101936 [00:17<02:21, 648.15it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 663.96923828125 and retention time 1941.9339850000022.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 715.599853515625 and retention time 2388.9270010000023.
  warnings.warn(
Annotating DIA-NN result...:  11%|████████▏                                                                  | 11068/101936 [00:18<02:32, 597.51it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 535.9348754882812 and retention time 3148.7048200000017.
  warnings.warn(
Annotating DIA-NN result...:  11%|████████▏                                                                  | 11128/101936 [00:18<02:36, 581.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 634.6470947265625 and retention time 2396.973331999998.
  warnings.warn(
Annotating DIA-NN result...:  11%|████████▏                                                                  | 11187/101936 [00:18<02:37, 576.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 765.6788330078125 and retention time 2373.970051000002.
  warnings.warn(
Annotating DIA-NN result...:  11%|████████▍                                                                  | 11526/101936 [00:18<02:16, 661.05it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.3692626953125 and retention time 2997.160642000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.438720703125 and retention time 3099.097848.
  warnings.warn(
Annotating DIA-NN result...:  11%|████████▌                                                                  | 11657/101936 [00:19<02:28, 608.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4654541015625 and retention time 2686.899607000002.
  warnings.warn(
Annotating DIA-NN result...:  12%|████████▋                                                                  | 11797/101936 [00:19<02:22, 632.08it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 560.598388671875 and retention time 2517.631189000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 706.8194580078125 and retention time 2416.475319.
  warnings.warn(
Annotating DIA-NN result...:  12%|████████▋                                                                  | 11861/101936 [00:19<02:27, 608.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 493.5804443359375 and retention time 2162.2935049999983.
  warnings.warn(
Annotating DIA-NN result...:  12%|████████▊                                                                  | 11923/101936 [00:19<02:27, 609.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 757.0590209960938 and retention time 2140.3039060000024.
  warnings.warn(
Annotating DIA-NN result...:  12%|█████████                                                                  | 12332/101936 [00:20<02:16, 657.58it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0974731445312 and retention time 2554.931206000002.
  warnings.warn(
Annotating DIA-NN result...:  12%|█████████                                                                  | 12398/101936 [00:20<02:21, 634.20it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 420.93304443359375 and retention time 3041.898058999998.
  warnings.warn(
Annotating DIA-NN result...:  13%|█████████▌                                                                 | 12975/101936 [00:21<02:04, 713.54it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 766.6570434570312 and retention time 2786.480751.
  warnings.warn(
Annotating DIA-NN result...:  13%|█████████▊                                                                 | 13348/101936 [00:21<02:00, 734.51it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9860229492188 and retention time 3111.836898.
  warnings.warn(
Annotating DIA-NN result...:  13%|█████████▉                                                                 | 13567/101936 [00:21<02:08, 686.56it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 774.7627563476562 and retention time 2561.195851999998.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▏                                                                | 13848/101936 [00:22<02:14, 653.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9210815429688 and retention time 2971.3534339999983.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 768.0316162109375 and retention time 3262.4575780000023.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▏                                                                | 13914/101936 [00:22<02:20, 626.58it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 673.6251831054688 and retention time 2112.2370929999997.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 461.906494140625 and retention time 2489.460778000002.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▎                                                                | 13978/101936 [00:22<02:28, 594.01it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 751.8721923828125 and retention time 2881.944991000002.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▍                                                                | 14112/101936 [00:22<02:19, 629.54it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 626.6305541992188 and retention time 1860.98478.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▍                                                                | 14243/101936 [00:23<02:21, 621.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 636.0603637695312 and retention time 1546.058236000002.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▌                                                                | 14310/101936 [00:23<02:18, 634.19it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 766.8316040039062 and retention time 1936.11498.
  warnings.warn(
Annotating DIA-NN result...:  14%|██████████▊                                                                | 14648/101936 [00:23<02:09, 671.97it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.7660522460938 and retention time 2629.253167000002.
  warnings.warn(
Annotating DIA-NN result...:  15%|██████████▉                                                                | 14855/101936 [00:24<02:13, 651.86it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4710693359375 and retention time 2376.2664589999977.
  warnings.warn(
Annotating DIA-NN result...:  15%|███████████                                                                | 15056/101936 [00:24<02:19, 624.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 609.9441528320312 and retention time 2819.630569999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 582.0325927734375 and retention time 1404.846652000002.
  warnings.warn(
Annotating DIA-NN result...:  15%|███████████▎                                                               | 15450/101936 [00:25<02:34, 559.05it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 556.0316772460938 and retention time 2026.3288009999978.
  warnings.warn(
Annotating DIA-NN result...:  15%|███████████▌                                                               | 15644/101936 [00:25<02:20, 615.58it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 793.7559814453125 and retention time 2174.492965000002.
  warnings.warn(
Annotating DIA-NN result...:  16%|███████████▋                                                               | 15838/101936 [00:25<02:21, 609.17it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.7025756835938 and retention time 2348.669931.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.6660766601562 and retention time 3611.984257999998.
  warnings.warn(
Annotating DIA-NN result...:  16%|████████████▎                                                              | 16731/101936 [00:27<02:13, 637.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 672.9779663085938 and retention time 2497.003212.
  warnings.warn(
Annotating DIA-NN result...:  17%|████████████▍                                                              | 16934/101936 [00:27<02:10, 652.29it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.448974609375 and retention time 2253.1077430000023.
  warnings.warn(
Annotating DIA-NN result...:  17%|████████████▌                                                              | 17066/101936 [00:27<02:09, 653.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 743.6263427734375 and retention time 1721.011692.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.3809204101562 and retention time 1725.534739999998.
  warnings.warn(
Annotating DIA-NN result...:  18%|█████████████▏                                                             | 17854/101936 [00:28<02:01, 692.48it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 756.8645629882812 and retention time 2964.7333439999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 778.7131958007812 and retention time 1795.923226999998.
  warnings.warn(
Annotating DIA-NN result...:  18%|█████████████▏                                                             | 17924/101936 [00:28<02:11, 639.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 553.9370727539062 and retention time 1864.839310000002.
  warnings.warn(
Annotating DIA-NN result...:  18%|█████████████▏                                                             | 17989/101936 [00:28<02:17, 611.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 557.9249267578125 and retention time 1717.916938999998.
  warnings.warn(
Annotating DIA-NN result...:  18%|█████████████▎                                                             | 18051/101936 [00:29<02:20, 594.98it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.062744140625 and retention time 2259.493672000002.
  warnings.warn(
Annotating DIA-NN result...:  18%|█████████████▌                                                             | 18466/101936 [00:29<02:07, 656.75it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 765.7489624023438 and retention time 2148.831112000002.
  warnings.warn(
Annotating DIA-NN result...:  18%|█████████████▋                                                             | 18596/101936 [00:29<02:11, 631.56it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 738.1271362304688 and retention time 2040.0666559999981.
  warnings.warn(
Annotating DIA-NN result...:  19%|██████████████▏                                                            | 19226/101936 [00:30<02:04, 662.18it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 652.005126953125 and retention time 1675.891714999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 586.9440307617188 and retention time 2479.524481000002.
  warnings.warn(
Annotating DIA-NN result...:  19%|██████████████▎                                                            | 19434/101936 [00:31<02:04, 662.76it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.0538940429688 and retention time 2805.746977000002.
  warnings.warn(
Annotating DIA-NN result...:  19%|██████████████▌                                                            | 19711/101936 [00:31<02:04, 660.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 787.0709228515625 and retention time 3062.9523120000003.
  warnings.warn(
Annotating DIA-NN result...:  19%|██████████████▌                                                            | 19778/101936 [00:31<02:12, 617.95it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 444.9087829589844 and retention time 2755.090756000002.
  warnings.warn(
Annotating DIA-NN result...:  20%|██████████████▋                                                            | 19903/101936 [00:31<02:18, 593.78it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 583.7869262695312 and retention time 2022.232668.
  warnings.warn(
Annotating DIA-NN result...:  20%|██████████████▊                                                            | 20182/101936 [00:32<01:59, 681.57it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 589.0528564453125 and retention time 2207.391871999998.
  warnings.warn(
Annotating DIA-NN result...:  20%|███████████████                                                            | 20454/101936 [00:32<02:02, 663.65it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 727.6375732421875 and retention time 2934.858675.
  warnings.warn(
Annotating DIA-NN result...:  20%|███████████████▏                                                           | 20587/101936 [00:32<02:04, 652.42it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.626953125 and retention time 2937.3576869999997.
  warnings.warn(
Annotating DIA-NN result...:  21%|███████████████▍                                                           | 21022/101936 [00:33<01:56, 692.39it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.448974609375 and retention time 2537.9574070000017.
  warnings.warn(
Annotating DIA-NN result...:  21%|███████████████▋                                                           | 21237/101936 [00:33<01:55, 700.45it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4426879882812 and retention time 2826.994323.
  warnings.warn(
Annotating DIA-NN result...:  21%|███████████████▋                                                           | 21377/101936 [00:34<02:07, 632.87it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 755.1426391601562 and retention time 1953.0100399999978.
  warnings.warn(
Annotating DIA-NN result...:  21%|████████████████                                                           | 21795/101936 [00:34<01:57, 682.84it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 518.5949096679688 and retention time 1770.793597999998.
  warnings.warn(
Annotating DIA-NN result...:  22%|████████████████▎                                                          | 22142/101936 [00:35<01:58, 674.63it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0880126953125 and retention time 3737.501551999998.
  warnings.warn(
Annotating DIA-NN result...:  22%|████████████████▌                                                          | 22490/101936 [00:35<01:56, 683.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 700.0065307617188 and retention time 2188.8649549999977.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 760.1703491210938 and retention time 2892.583561000002.
  warnings.warn(
Annotating DIA-NN result...:  22%|████████████████▊                                                          | 22840/101936 [00:36<02:03, 639.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 673.6580200195312 and retention time 2146.223433.
  warnings.warn(
Annotating DIA-NN result...:  23%|████████████████▉                                                          | 23039/101936 [00:36<02:03, 640.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 757.64794921875 and retention time 2459.184286000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 705.5928344726562 and retention time 2309.977863.
  warnings.warn(
Annotating DIA-NN result...:  23%|█████████████████                                                          | 23226/101936 [00:37<02:14, 584.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.483642578125 and retention time 3422.3291380000023.
  warnings.warn(
Annotating DIA-NN result...:  23%|█████████████████▏                                                         | 23418/101936 [00:37<02:15, 579.90it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.064208984375 and retention time 2601.640798000002.
  warnings.warn(
Annotating DIA-NN result...:  23%|█████████████████▎                                                         | 23558/101936 [00:37<02:03, 636.40it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 786.0787353515625 and retention time 2395.672011.
  warnings.warn(
Annotating DIA-NN result...:  23%|█████████████████▍                                                         | 23765/101936 [00:37<02:05, 624.08it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 638.107421875 and retention time 2077.754898.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 589.9443359375 and retention time 2564.439453.
  warnings.warn(
Annotating DIA-NN result...:  24%|█████████████████▋                                                         | 23966/101936 [00:38<02:07, 613.76it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 765.645751953125 and retention time 2569.609252000002.
  warnings.warn(
Annotating DIA-NN result...:  24%|█████████████████▋                                                         | 24029/101936 [00:38<02:08, 606.39it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 639.8015747070312 and retention time 2443.747750999998.
  warnings.warn(
Annotating DIA-NN result...:  24%|█████████████████▋                                                         | 24092/101936 [00:38<02:07, 611.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1987915039062 and retention time 3648.126910999998.
  warnings.warn(
Annotating DIA-NN result...:  24%|█████████████████▉                                                         | 24366/101936 [00:38<01:54, 677.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 692.1166381835938 and retention time 2161.202899000002.
  warnings.warn(
Annotating DIA-NN result...:  24%|█████████████████▉                                                         | 24434/101936 [00:38<02:04, 620.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 458.99200439453125 and retention time 3167.390848000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 755.7093505859375 and retention time 2535.588697000002.
  warnings.warn(
Annotating DIA-NN result...:  24%|██████████████████▏                                                        | 24687/101936 [00:39<02:08, 599.30it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.0308837890625 and retention time 2217.006126.
  warnings.warn(
Annotating DIA-NN result...:  24%|██████████████████▏                                                        | 24748/101936 [00:39<02:11, 585.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 762.0857543945312 and retention time 2705.815576999998.
  warnings.warn(
Annotating DIA-NN result...:  24%|██████████████████▎                                                        | 24808/101936 [00:39<02:11, 587.38it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 750.616943359375 and retention time 2091.444931000002.
  warnings.warn(
Annotating DIA-NN result...:  25%|██████████████████▍                                                        | 25008/101936 [00:39<01:59, 645.39it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 700.6651611328125 and retention time 2037.738348.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 690.844970703125 and retention time 2154.810160999998.
  warnings.warn(
Annotating DIA-NN result...:  25%|██████████████████▋                                                        | 25428/101936 [00:40<01:48, 704.25it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 745.1660766601562 and retention time 2522.8272220000017.
  warnings.warn(
Annotating DIA-NN result...:  25%|██████████████████▊                                                        | 25571/101936 [00:40<01:51, 681.96it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 734.1571655273438 and retention time 2463.3064950000003.
  warnings.warn(
Annotating DIA-NN result...:  25%|██████████████████▉                                                        | 25710/101936 [00:40<01:52, 678.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 651.0924072265625 and retention time 2777.367619999998.
  warnings.warn(
Annotating DIA-NN result...:  25%|███████████████████                                                        | 25988/101936 [00:41<01:52, 673.94it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 721.716796875 and retention time 1950.756469999998.
  warnings.warn(
Annotating DIA-NN result...:  26%|███████████████████▎                                                       | 26195/101936 [00:41<01:56, 649.09it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1168212890625 and retention time 3167.034907000002.
  warnings.warn(
Annotating DIA-NN result...:  26%|███████████████████▍                                                       | 26399/101936 [00:41<01:53, 663.10it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0804443359375 and retention time 2686.899607000002.
  warnings.warn(
Annotating DIA-NN result...:  26%|███████████████████▍                                                       | 26466/101936 [00:42<01:55, 650.81it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 479.5841979980469 and retention time 3016.7012179999983.
  warnings.warn(
Annotating DIA-NN result...:  26%|███████████████████▌                                                       | 26536/101936 [00:42<01:53, 665.02it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 698.0219116210938 and retention time 2146.363575.
  warnings.warn(
Annotating DIA-NN result...:  27%|███████████████████▉                                                       | 27026/101936 [00:42<01:48, 690.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.12060546875 and retention time 2703.9008689999982.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 412.5979919433594 and retention time 3014.192263999998.
  warnings.warn(
Annotating DIA-NN result...:  27%|███████████████████▉                                                       | 27096/101936 [00:43<02:00, 621.86it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0955200195312 and retention time 3222.250180000002.
  warnings.warn(
Annotating DIA-NN result...:  27%|████████████████████▏                                                      | 27370/101936 [00:43<02:02, 609.81it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 788.7420043945312 and retention time 2714.5094329999984.
  warnings.warn(
Annotating DIA-NN result...:  27%|████████████████████▏                                                      | 27433/101936 [00:43<02:05, 595.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 766.863037109375 and retention time 2365.4624500000023.
  warnings.warn(
Annotating DIA-NN result...:  27%|████████████████████▎                                                      | 27558/101936 [00:43<02:07, 584.90it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 779.6483764648438 and retention time 2782.3360439999997.
  warnings.warn(
Annotating DIA-NN result...:  27%|████████████████████▎                                                      | 27688/101936 [00:44<02:03, 601.26it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 480.60369873046875 and retention time 2986.984908.
  warnings.warn(
Annotating DIA-NN result...:  27%|████████████████████▍                                                      | 27749/101936 [00:44<02:04, 594.33it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 451.749755859375 and retention time 2755.1107279999983.
  warnings.warn(
Annotating DIA-NN result...:  27%|████████████████████▌                                                      | 27954/101936 [00:44<01:52, 654.75it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 791.3546142578125 and retention time 2605.8315119999997.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 624.9561767578125 and retention time 2243.716089.
  warnings.warn(
Annotating DIA-NN result...:  28%|████████████████████▋                                                      | 28165/101936 [00:44<01:50, 668.61it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.3947143554688 and retention time 2639.851708000002.
  warnings.warn(
Annotating DIA-NN result...:  28%|████████████████████▊                                                      | 28233/101936 [00:44<01:53, 649.84it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 649.2806396484375 and retention time 1601.4717930000002.
  warnings.warn(
Annotating DIA-NN result...:  28%|█████████████████████▏                                                     | 28715/101936 [00:45<01:46, 690.44it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.3983764648438 and retention time 3541.3943249999998.
  warnings.warn(
Annotating DIA-NN result...:  28%|█████████████████████▏                                                     | 28785/101936 [00:45<01:51, 655.90it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.1317749023438 and retention time 3418.063788.
  warnings.warn(
Annotating DIA-NN result...:  29%|█████████████████████▍                                                     | 29145/101936 [00:46<01:44, 697.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 491.60711669921875 and retention time 3071.9720899999984.
  warnings.warn(
Annotating DIA-NN result...:  29%|█████████████████████▌                                                     | 29356/101936 [00:46<01:45, 685.58it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 513.5914916992188 and retention time 3108.1991669999998.
  warnings.warn(
Annotating DIA-NN result...:  29%|█████████████████████▋                                                     | 29497/101936 [00:46<01:49, 663.50it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 786.7164916992188 and retention time 2565.508269.
  warnings.warn(
Annotating DIA-NN result...:  29%|█████████████████████▊                                                     | 29629/101936 [00:46<01:53, 638.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 753.7059936523438 and retention time 2508.050629000002.
  warnings.warn(
Annotating DIA-NN result...:  29%|█████████████████████▉                                                     | 29760/101936 [00:47<01:57, 614.04it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 410.9070739746094 and retention time 2723.079147.
  warnings.warn(
Annotating DIA-NN result...:  29%|█████████████████████▉                                                     | 29823/101936 [00:47<02:03, 582.12it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1051635742188 and retention time 2363.516788000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 767.855712890625 and retention time 2084.800957999998.
  warnings.warn(
Annotating DIA-NN result...:  30%|██████████████████████▏                                                    | 30094/101936 [00:47<01:53, 635.50it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4305419921875 and retention time 2852.464786999998.
  warnings.warn(
Annotating DIA-NN result...:  30%|██████████████████████▏                                                    | 30159/101936 [00:47<01:55, 620.58it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 664.830810546875 and retention time 2212.0553419999983.
  warnings.warn(
Annotating DIA-NN result...:  30%|██████████████████████▏                                                    | 30222/101936 [00:47<01:59, 599.45it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 763.0330200195312 and retention time 2040.196780000002.
  warnings.warn(
Annotating DIA-NN result...:  30%|██████████████████████▎                                                    | 30290/101936 [00:48<01:55, 620.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 735.6925048828125 and retention time 2529.134115.
  warnings.warn(
Annotating DIA-NN result...:  30%|██████████████████████▋                                                    | 30784/101936 [00:48<01:42, 694.68it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 703.0828857421875 and retention time 2709.7822770000002.
  warnings.warn(
Annotating DIA-NN result...:  30%|██████████████████████▊                                                    | 30994/101936 [00:49<01:42, 691.99it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.7322387695312 and retention time 2231.8421059999982.
  warnings.warn(
Annotating DIA-NN result...:  31%|███████████████████████▎                                                   | 31630/101936 [00:50<01:39, 707.07it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 746.614501953125 and retention time 2860.688857000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 703.6859130859375 and retention time 1991.014405999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 741.8130493164062 and retention time 2467.577068000002.
  warnings.warn(
Annotating DIA-NN result...:  31%|███████████████████████▍                                                   | 31774/101936 [00:50<01:49, 642.97it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 723.634033203125 and retention time 2233.570132999998.
  warnings.warn(
Annotating DIA-NN result...:  31%|███████████████████████▍                                                   | 31905/101936 [00:50<01:55, 604.30it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 724.1494750976562 and retention time 2781.999934999998.
  warnings.warn(
Annotating DIA-NN result...:  31%|███████████████████████▌                                                   | 32031/101936 [00:50<01:53, 613.84it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1593017578125 and retention time 3486.0935569999983.
  warnings.warn(
Annotating DIA-NN result...:  32%|███████████████████████▋                                                   | 32220/101936 [00:51<01:54, 609.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 764.6961669921875 and retention time 3037.3068859999976.
  warnings.warn(
Annotating DIA-NN result...:  32%|████████████████████████                                                   | 32669/101936 [00:51<01:49, 635.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 553.0364990234375 and retention time 2281.5275549999997.
  warnings.warn(
Annotating DIA-NN result...:  32%|████████████████████████▏                                                  | 32805/101936 [00:52<01:46, 651.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.1995239257812 and retention time 3288.4734580000018.
  warnings.warn(
Annotating DIA-NN result...:  32%|████████████████████████▏                                                  | 32871/101936 [00:52<01:49, 631.61it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4393920898438 and retention time 2924.6407309999977.
  warnings.warn(
Annotating DIA-NN result...:  33%|████████████████████████▍                                                  | 33224/101936 [00:52<01:38, 698.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.86865234375 and retention time 2412.685638.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.8504638671875 and retention time 1540.5083509999981.
  warnings.warn(
Annotating DIA-NN result...:  33%|████████████████████████▌                                                  | 33436/101936 [00:52<01:50, 619.57it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 783.708984375 and retention time 2048.7506280000002.
  warnings.warn(
Annotating DIA-NN result...:  33%|████████████████████████▋                                                  | 33503/101936 [00:53<01:48, 630.06it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.3680419921875 and retention time 2637.746037.
  warnings.warn(
Annotating DIA-NN result...:  33%|████████████████████████▋                                                  | 33567/101936 [00:53<01:54, 594.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 782.134521484375 and retention time 2261.508151000002.
  warnings.warn(
Annotating DIA-NN result...:  33%|████████████████████████▋                                                  | 33628/101936 [00:53<01:56, 585.82it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 765.0453491210938 and retention time 1834.060612000002.
  warnings.warn(
Annotating DIA-NN result...:  33%|█████████████████████████                                                  | 34113/101936 [00:54<01:44, 649.91it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 427.9210205078125 and retention time 2780.464975000002.
  warnings.warn(
Annotating DIA-NN result...:  34%|█████████████████████████▏                                                 | 34313/101936 [00:54<01:42, 658.98it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 686.1041259765625 and retention time 2533.116579.
  warnings.warn(
Annotating DIA-NN result...:  34%|█████████████████████████▋                                                 | 34939/101936 [00:55<01:39, 673.47it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 465.509521484375 and retention time 2485.2362449999982.
  warnings.warn(
Annotating DIA-NN result...:  34%|█████████████████████████▊                                                 | 35007/101936 [00:55<01:46, 630.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 675.8126220703125 and retention time 2201.45079.
  warnings.warn(
Annotating DIA-NN result...:  35%|██████████████████████████                                                 | 35345/101936 [00:55<01:47, 620.34it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 669.5743408203125 and retention time 2133.456804.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1448364257812 and retention time 3307.608549.
  warnings.warn(
Annotating DIA-NN result...:  35%|██████████████████████████                                                 | 35475/101936 [00:56<01:47, 617.16it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 744.095703125 and retention time 2546.167498000002.
  warnings.warn(
Annotating DIA-NN result...:  35%|██████████████████████████▎                                                | 35824/101936 [00:56<01:38, 673.49it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 733.6035766601562 and retention time 2858.48025.
  warnings.warn(
Annotating DIA-NN result...:  35%|██████████████████████████▍                                                | 35958/101936 [00:56<01:43, 634.54it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 781.1747436523438 and retention time 2843.862837.
  warnings.warn(
Annotating DIA-NN result...:  36%|██████████████████████████▊                                                | 36381/101936 [00:57<01:33, 698.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 774.7530517578125 and retention time 3326.602918999998.
  warnings.warn(
Annotating DIA-NN result...:  36%|██████████████████████████▉                                                | 36649/101936 [00:58<01:44, 622.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 747.7086791992188 and retention time 2552.549172.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 733.9927978515625 and retention time 2195.420479000002.
  warnings.warn(
Annotating DIA-NN result...:  36%|███████████████████████████                                                | 36847/101936 [00:58<01:43, 627.10it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 793.9916381835938 and retention time 2148.991291999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 759.1507568359375 and retention time 2898.984811999998.
  warnings.warn(
Annotating DIA-NN result...:  36%|███████████████████████████▎                                               | 37042/101936 [00:58<01:45, 614.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 684.6690673828125 and retention time 1654.824943999998.
  warnings.warn(
Annotating DIA-NN result...:  37%|███████████████████████████▍                                               | 37365/101936 [00:59<01:40, 641.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 455.593017578125 and retention time 3065.419534000002.
  warnings.warn(
Annotating DIA-NN result...:  37%|███████████████████████████▌                                               | 37496/101936 [00:59<01:41, 633.10it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 736.3051147460938 and retention time 2176.2987850000018.
  warnings.warn(
Annotating DIA-NN result...:  37%|███████████████████████████▋                                               | 37698/101936 [00:59<01:40, 641.89it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 634.70654296875 and retention time 1971.514558000002.
  warnings.warn(
Annotating DIA-NN result...:  37%|███████████████████████████▉                                               | 37896/101936 [01:00<01:40, 639.50it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 563.5320434570312 and retention time 2468.7582850000017.
  warnings.warn(
Annotating DIA-NN result...:  37%|███████████████████████████▉                                               | 38028/101936 [01:00<01:39, 644.40it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 764.6605834960938 and retention time 2280.537636.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 769.6380615234375 and retention time 2684.2860610000016.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▏                                              | 38367/101936 [01:00<01:35, 662.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 688.6321411132812 and retention time 2195.209486000002.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▎                                              | 38437/101936 [01:00<01:34, 672.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 776.7821655273438 and retention time 2660.9657730000004.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▎                                              | 38505/101936 [01:00<01:37, 650.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 700.5971069335938 and retention time 2760.671182000002.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▌                                              | 38788/101936 [01:01<01:32, 683.07it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 782.7876586914062 and retention time 2272.154536999998.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▋                                              | 38925/101936 [01:01<01:34, 664.97it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 712.1614379882812 and retention time 2278.139418.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▋                                              | 39065/101936 [01:01<01:34, 665.44it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 692.0610961914062 and retention time 1816.679607.
  warnings.warn(
Annotating DIA-NN result...:  38%|████████████████████████████▊                                              | 39202/101936 [01:01<01:34, 665.16it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.6267700195312 and retention time 2491.252635.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 780.6090087890625 and retention time 2044.50072.
  warnings.warn(
Annotating DIA-NN result...:  39%|████████████████████████████▉                                              | 39399/101936 [01:02<01:38, 634.91it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0857543945312 and retention time 1602.236950999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 692.1552124023438 and retention time 2798.8368439999977.
  warnings.warn(
Annotating DIA-NN result...:  39%|█████████████████████████████▏                                             | 39737/101936 [01:02<01:34, 659.68it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 715.0999755859375 and retention time 2418.632920000002.
  warnings.warn(
Annotating DIA-NN result...:  39%|█████████████████████████████▎                                             | 39804/101936 [01:02<01:37, 638.76it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 731.7011108398438 and retention time 2104.086948.
  warnings.warn(
Annotating DIA-NN result...:  40%|█████████████████████████████▋                                             | 40363/101936 [01:03<01:32, 665.74it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.8619384765625 and retention time 2565.498286999998.
  warnings.warn(
Annotating DIA-NN result...:  40%|█████████████████████████████▋                                             | 40430/101936 [01:03<01:39, 615.38it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 784.715087890625 and retention time 3071.4052110000002.
  warnings.warn(
Annotating DIA-NN result...:  40%|██████████████████████████████▏                                            | 41014/101936 [01:04<01:28, 690.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.689697265625 and retention time 2029.7068199999999.
  warnings.warn(
Annotating DIA-NN result...:  41%|██████████████████████████████▍                                            | 41298/101936 [01:05<01:27, 691.75it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 750.7468872070312 and retention time 2367.540865999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 632.6163330078125 and retention time 2409.691407.
  warnings.warn(
Annotating DIA-NN result...:  41%|██████████████████████████████▍                                            | 41368/101936 [01:05<01:33, 648.68it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 774.7071533203125 and retention time 2084.851405000002.
  warnings.warn(
Annotating DIA-NN result...:  41%|██████████████████████████████▊                                            | 41865/101936 [01:06<01:25, 699.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 761.0541381835938 and retention time 2797.082161000002.
  warnings.warn(
Annotating DIA-NN result...:  42%|███████████████████████████████▏                                           | 42369/101936 [01:06<01:22, 723.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 794.1035766601562 and retention time 2059.463757.
  warnings.warn(
Annotating DIA-NN result...:  42%|███████████████████████████████▍                                           | 42660/101936 [01:07<01:24, 705.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 629.5850830078125 and retention time 1609.8711559999979.
  warnings.warn(
Annotating DIA-NN result...:  42%|███████████████████████████████▍                                           | 42806/101936 [01:07<01:24, 703.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 783.7720947265625 and retention time 2176.562163.
  warnings.warn(
Annotating DIA-NN result...:  42%|███████████████████████████████▌                                           | 42877/101936 [01:07<01:29, 662.84it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.3980102539062 and retention time 3592.808143000002.
  warnings.warn(
Annotating DIA-NN result...:  42%|███████████████████████████████▊                                           | 43157/101936 [01:07<01:26, 675.76it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.7991333007812 and retention time 3194.6610079999978.
  warnings.warn(
Annotating DIA-NN result...:  42%|███████████████████████████████▊                                           | 43225/101936 [01:08<01:29, 653.76it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.2060546875 and retention time 3477.599860999998.
  warnings.warn(
Annotating DIA-NN result...:  43%|████████████████████████████████                                           | 43523/101936 [01:08<01:20, 722.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4760131835938 and retention time 2299.847364.
  warnings.warn(
Annotating DIA-NN result...:  43%|████████████████████████████████▏                                          | 43819/101936 [01:08<01:22, 704.05it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 777.688720703125 and retention time 3281.617366999998.
  warnings.warn(
Annotating DIA-NN result...:  43%|████████████████████████████████▎                                          | 43961/101936 [01:09<01:22, 703.73it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.8192138671875 and retention time 3680.040937000002.
  warnings.warn(
Annotating DIA-NN result...:  43%|████████████████████████████████▌                                          | 44176/101936 [01:09<01:23, 688.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4065551757812 and retention time 3082.094595.
  warnings.warn(
Annotating DIA-NN result...:  44%|████████████████████████████████▉                                          | 44798/101936 [01:10<01:29, 641.04it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 766.7940673828125 and retention time 2769.509164999998.
  warnings.warn(
Annotating DIA-NN result...:  45%|█████████████████████████████████▋                                         | 45777/101936 [01:11<01:20, 696.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 724.7689208984375 and retention time 3322.090762000002.
  warnings.warn(
Annotating DIA-NN result...:  45%|█████████████████████████████████▋                                         | 45847/101936 [01:11<01:25, 658.81it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4556274414062 and retention time 2945.873799.
  warnings.warn(
Annotating DIA-NN result...:  46%|██████████████████████████████████▎                                        | 46638/101936 [01:13<01:16, 722.68it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 729.0872192382812 and retention time 2335.563949999998.
  warnings.warn(
Annotating DIA-NN result...:  46%|██████████████████████████████████▍                                        | 46783/101936 [01:13<01:19, 692.67it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 764.5094604492188 and retention time 2979.668779999998.
  warnings.warn(
Annotating DIA-NN result...:  46%|██████████████████████████████████▌                                        | 46924/101936 [01:13<01:21, 678.74it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 743.6755981445312 and retention time 2231.581549000002.
  warnings.warn(
Annotating DIA-NN result...:  46%|██████████████████████████████████▋                                        | 47133/101936 [01:13<01:20, 681.67it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 790.1724243164062 and retention time 2287.036006999998.
  warnings.warn(
Annotating DIA-NN result...:  46%|██████████████████████████████████▊                                        | 47267/101936 [01:14<01:26, 634.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 717.1271362304688 and retention time 2520.56259.
  warnings.warn(
Annotating DIA-NN result...:  46%|██████████████████████████████████▊                                        | 47331/101936 [01:14<01:29, 613.47it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.7789306640625 and retention time 2493.402370000002.
  warnings.warn(
Annotating DIA-NN result...:  47%|██████████████████████████████████▉                                        | 47520/101936 [01:14<01:31, 597.84it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 789.6713256835938 and retention time 2036.061535999998.
  warnings.warn(
Annotating DIA-NN result...:  47%|███████████████████████████████████                                        | 47589/101936 [01:14<01:27, 622.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.127685546875 and retention time 3481.844715.
  warnings.warn(
Annotating DIA-NN result...:  47%|███████████████████████████████████                                        | 47715/101936 [01:14<01:32, 583.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 743.7888793945312 and retention time 2669.3060440000017.
  warnings.warn(
Annotating DIA-NN result...:  47%|███████████████████████████████████▎                                       | 48042/101936 [01:15<01:25, 628.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 762.662109375 and retention time 2138.225857000002.
  warnings.warn(
Annotating DIA-NN result...:  47%|███████████████████████████████████▍                                       | 48106/101936 [01:15<01:25, 628.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 767.737060546875 and retention time 1650.989002000002.
  warnings.warn(
Annotating DIA-NN result...:  47%|███████████████████████████████████▌                                       | 48251/101936 [01:15<01:19, 672.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 630.6062622070312 and retention time 1786.259173999998.
  warnings.warn(
Annotating DIA-NN result...:  48%|███████████████████████████████████▊                                       | 48664/101936 [01:16<01:18, 681.85it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 749.0617065429688 and retention time 3098.830516000002.
  warnings.warn(
Annotating DIA-NN result...:  48%|████████████████████████████████████                                       | 48930/101936 [01:16<01:23, 638.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 771.7734375 and retention time 2346.382353.
  warnings.warn(
Annotating DIA-NN result...:  48%|████████████████████████████████████                                       | 49067/101936 [01:16<01:20, 658.98it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 711.1492919921875 and retention time 3283.7670070000017.
  warnings.warn(
Annotating DIA-NN result...:  48%|████████████████████████████████████▏                                      | 49134/101936 [01:17<01:23, 630.00it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 450.9414367675781 and retention time 3233.152239.
  warnings.warn(
Annotating DIA-NN result...:  48%|████████████████████████████████████▏                                      | 49266/101936 [01:17<01:22, 635.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 709.1133422851562 and retention time 2380.0333429999982.
  warnings.warn(
Annotating DIA-NN result...:  48%|████████████████████████████████████▎                                      | 49404/101936 [01:17<01:21, 643.17it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4007568359375 and retention time 2614.388119999998.
  warnings.warn(
Annotating DIA-NN result...:  49%|████████████████████████████████████▌                                      | 49691/101936 [01:17<01:16, 681.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.447265625 and retention time 2537.9574070000017.
  warnings.warn(
Annotating DIA-NN result...:  49%|████████████████████████████████████▋                                      | 49899/101936 [01:18<01:20, 644.33it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1155395507812 and retention time 3026.886504.
  warnings.warn(
Annotating DIA-NN result...:  49%|████████████████████████████████████▊                                      | 49967/101936 [01:18<01:19, 653.87it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.664306640625 and retention time 2839.7205070000023.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 626.6184692382812 and retention time 2558.2834330000023.
  warnings.warn(
Annotating DIA-NN result...:  49%|████████████████████████████████████▊                                      | 50099/101936 [01:18<01:21, 634.64it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.1266479492188 and retention time 2499.715168000002.
  warnings.warn(
Annotating DIA-NN result...:  49%|████████████████████████████████████▉                                      | 50164/101936 [01:18<01:21, 637.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 741.024169921875 and retention time 2431.528272.
  warnings.warn(
Annotating DIA-NN result...:  49%|█████████████████████████████████████                                      | 50378/101936 [01:18<01:18, 657.57it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.004638671875 and retention time 2080.4187760000023.
  warnings.warn(
Annotating DIA-NN result...:  50%|█████████████████████████████████████▎                                     | 50656/101936 [01:19<01:17, 659.44it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 741.96435546875 and retention time 3568.7416660000017.
  warnings.warn(
Annotating DIA-NN result...:  50%|█████████████████████████████████████▎                                     | 50723/101936 [01:19<01:19, 641.64it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 760.138427734375 and retention time 3428.506203.
  warnings.warn(
Annotating DIA-NN result...:  50%|█████████████████████████████████████▎                                     | 50788/101936 [01:19<01:20, 631.85it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 591.0962524414062 and retention time 2745.2123839999977.
  warnings.warn(
Annotating DIA-NN result...:  50%|█████████████████████████████████████▌                                     | 51053/101936 [01:20<01:18, 649.82it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9860229492188 and retention time 2822.750890999998.
  warnings.warn(
Annotating DIA-NN result...:  50%|█████████████████████████████████████▊                                     | 51324/101936 [01:20<01:19, 633.55it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 411.9261169433594 and retention time 2960.8411939999983.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9916381835938 and retention time 2954.361706000002.
  warnings.warn(
Annotating DIA-NN result...:  50%|█████████████████████████████████████▊                                     | 51388/101936 [01:20<01:22, 614.12it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 470.6123046875 and retention time 3456.7444800000003.
  warnings.warn(
Annotating DIA-NN result...:  51%|██████████████████████████████████████                                     | 51663/101936 [01:20<01:16, 655.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 475.9380187988281 and retention time 3469.523488000002.
  warnings.warn(
Annotating DIA-NN result...:  51%|██████████████████████████████████████                                     | 51729/101936 [01:21<01:23, 602.92it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9916381835938 and retention time 3175.516393999998.
  warnings.warn(
Annotating DIA-NN result...:  51%|██████████████████████████████████████▌                                    | 52337/101936 [01:22<01:17, 637.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0955200195312 and retention time 2733.590221999998.
  warnings.warn(
Annotating DIA-NN result...:  52%|██████████████████████████████████████▋                                    | 52605/101936 [01:22<01:15, 649.36it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.8480834960938 and retention time 2480.329278.
  warnings.warn(
Annotating DIA-NN result...:  52%|██████████████████████████████████████▊                                    | 52740/101936 [01:22<01:17, 634.92it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1036987304688 and retention time 3635.3604809999997.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4558715820312 and retention time 3290.604043999998.
  warnings.warn(
Annotating DIA-NN result...:  52%|██████████████████████████████████████▊                                    | 52804/101936 [01:22<01:23, 587.60it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 425.924560546875 and retention time 2979.973963999998.
  warnings.warn(
Annotating DIA-NN result...:  52%|███████████████████████████████████████                                    | 53016/101936 [01:23<01:16, 642.14it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 452.9559631347656 and retention time 3050.534403.
  warnings.warn(
Annotating DIA-NN result...:  52%|███████████████████████████████████████▎                                   | 53450/101936 [01:23<01:10, 685.01it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.2108764648438 and retention time 3486.0935569999983.
  warnings.warn(
Annotating DIA-NN result...:  53%|███████████████████████████████████████▌                                   | 53735/101936 [01:24<01:10, 687.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4237060546875 and retention time 3179.775229000002.
  warnings.warn(
Annotating DIA-NN result...:  53%|███████████████████████████████████████▋                                   | 53961/101936 [01:24<01:06, 726.26it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 445.9366760253906 and retention time 2918.492575000002.
  warnings.warn(
Annotating DIA-NN result...:  54%|████████████████████████████████████████▌                                  | 55185/101936 [01:26<01:06, 703.49it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0545043945312 and retention time 3171.271345999998.
  warnings.warn(
Annotating DIA-NN result...:  54%|████████████████████████████████████████▋                                  | 55256/101936 [01:26<01:09, 670.39it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 494.0420227050781 and retention time 2961.253612000002.
  warnings.warn(
Annotating DIA-NN result...:  55%|████████████████████████████████████████▉                                  | 55611/101936 [01:26<01:06, 697.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4364013671875 and retention time 2006.3673119999999.
  warnings.warn(
Annotating DIA-NN result...:  56%|█████████████████████████████████████████▊                                 | 56883/101936 [01:28<01:08, 662.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 761.642333984375 and retention time 2059.263978.
  warnings.warn(
Annotating DIA-NN result...:  56%|██████████████████████████████████████████                                 | 57243/101936 [01:29<01:05, 677.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 667.9913330078125 and retention time 2673.11454.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▍                                | 57661/101936 [01:29<01:04, 685.25it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0098266601562 and retention time 3328.842916999998.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▌                                | 57795/101936 [01:30<01:09, 634.86it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.2008056640625 and retention time 3562.648242.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▌                                | 57859/101936 [01:30<01:10, 626.50it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4634399414062 and retention time 1853.378053999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 703.7205200195312 and retention time 2271.7449960000004.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▌                                | 57922/101936 [01:30<01:11, 611.87it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.6395263671875 and retention time 2584.6548900000003.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▋                                | 58050/101936 [01:30<01:10, 623.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.188720703125 and retention time 2801.5220999999997.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▊                                | 58115/101936 [01:30<01:09, 630.15it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1725463867188 and retention time 3503.111368000002.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▊                                | 58187/101936 [01:30<01:06, 655.79it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.42431640625 and retention time 3409.581448999998.
  warnings.warn(
Annotating DIA-NN result...:  57%|██████████████████████████████████████████▊                                | 58253/101936 [01:30<01:08, 636.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 421.924560546875 and retention time 2591.179233.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 768.79052734375 and retention time 2780.141016.
  warnings.warn(
Annotating DIA-NN result...:  57%|███████████████████████████████████████████                                | 58593/101936 [01:31<01:05, 661.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 632.5994262695312 and retention time 1967.252764000002.
  warnings.warn(
Annotating DIA-NN result...:  58%|███████████████████████████████████████████▎                               | 58798/101936 [01:31<01:06, 646.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4229736328125 and retention time 2563.4317369999976.
  warnings.warn(
Annotating DIA-NN result...:  58%|███████████████████████████████████████████▌                               | 59157/101936 [01:32<01:01, 700.32it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 626.8871459960938 and retention time 2860.064769.
  warnings.warn(
Annotating DIA-NN result...:  58%|███████████████████████████████████████████▋                               | 59434/101936 [01:32<01:03, 667.63it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4644775390625 and retention time 2529.457152.
  warnings.warn(
Annotating DIA-NN result...:  59%|███████████████████████████████████████████▉                               | 59716/101936 [01:33<01:01, 690.91it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 449.906494140625 and retention time 2727.5035690000022.
  warnings.warn(
Annotating DIA-NN result...:  59%|████████████████████████████████████████████                               | 59854/101936 [01:33<01:03, 665.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 417.58575439453125 and retention time 2725.204776.
  warnings.warn(
Annotating DIA-NN result...:  59%|████████████████████████████████████████████▎                              | 60145/101936 [01:33<01:03, 659.80it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4403686523438 and retention time 3060.8556970000022.
  warnings.warn(
Annotating DIA-NN result...:  59%|████████████████████████████████████████████▍                              | 60474/101936 [01:34<01:09, 599.32it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 794.1182250976562 and retention time 2977.686379999998.
  warnings.warn(
Annotating DIA-NN result...:  59%|████████████████████████████████████████████▌                              | 60535/101936 [01:34<01:12, 572.06it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 788.673828125 and retention time 2671.683607999998.
  warnings.warn(
Annotating DIA-NN result...:  59%|████████████████████████████████████████████▌                              | 60593/101936 [01:34<01:15, 550.17it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.7106323242188 and retention time 2839.7205070000023.
  warnings.warn(
Annotating DIA-NN result...:  60%|████████████████████████████████████████████▋                              | 60656/101936 [01:34<01:12, 571.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.112060546875 and retention time 3554.166132.
  warnings.warn(
Annotating DIA-NN result...:  60%|████████████████████████████████████████████▋                              | 60714/101936 [01:34<01:11, 573.65it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 714.1043090820312 and retention time 2271.795211999998.
  warnings.warn(
Annotating DIA-NN result...:  60%|████████████████████████████████████████████▋                              | 60772/101936 [01:34<01:12, 566.38it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 438.5662536621094 and retention time 2527.5347869999982.
  warnings.warn(
Annotating DIA-NN result...:  60%|████████████████████████████████████████████▊                              | 60900/101936 [01:35<01:07, 604.33it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 653.5903930664062 and retention time 3402.460342000002.
  warnings.warn(
Annotating DIA-NN result...:  60%|████████████████████████████████████████████▊                              | 60961/101936 [01:35<01:09, 588.77it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4929809570312 and retention time 3018.401467999998.
  warnings.warn(
Annotating DIA-NN result...:  60%|████████████████████████████████████████████▉                              | 61022/101936 [01:35<01:08, 593.40it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1556396484375 and retention time 3205.255312999998.
  warnings.warn(
Annotating DIA-NN result...:  60%|█████████████████████████████████████████████                              | 61295/101936 [01:35<01:02, 654.64it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 782.6513671875 and retention time 2947.9191840000003.
  warnings.warn(
Annotating DIA-NN result...:  61%|█████████████████████████████████████████████▍                             | 61819/101936 [01:36<01:05, 610.29it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 786.66259765625 and retention time 2752.662519.
  warnings.warn(
Annotating DIA-NN result...:  61%|█████████████████████████████████████████████▌                             | 61945/101936 [01:36<01:07, 590.96it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4566040039062 and retention time 2899.1651760000004.
  warnings.warn(
Annotating DIA-NN result...:  61%|█████████████████████████████████████████████▋                             | 62078/101936 [01:37<01:04, 622.77it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1614379882812 and retention time 3056.612397.
  warnings.warn(
Annotating DIA-NN result...:  61%|█████████████████████████████████████████████▊                             | 62212/101936 [01:37<01:01, 643.18it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 597.7864990234375 and retention time 2336.9751640000018.
  warnings.warn(
Annotating DIA-NN result...:  61%|██████████████████████████████████████████████                             | 62540/101936 [01:37<01:02, 634.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 791.8179931640625 and retention time 3009.864276.
  warnings.warn(
Annotating DIA-NN result...:  61%|██████████████████████████████████████████████                             | 62675/101936 [01:37<01:01, 639.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4221801757812 and retention time 2793.0222259999978.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▏                            | 62740/101936 [01:38<01:04, 612.14it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 605.9611206054688 and retention time 2638.8542700000003.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▏                            | 62802/101936 [01:38<01:04, 606.80it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 710.3319702148438 and retention time 2161.3262170000016.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▎                            | 62863/101936 [01:38<01:04, 605.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 778.8510131835938 and retention time 2539.984054000002.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▎                            | 62997/101936 [01:38<01:01, 632.10it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 670.0307006835938 and retention time 1861.187440999998.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▍                            | 63063/101936 [01:38<01:01, 628.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 786.7664794921875 and retention time 2650.45941.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▍                            | 63188/101936 [01:38<01:03, 612.96it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.1406860351562 and retention time 2631.3595510000023.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▌                            | 63250/101936 [01:38<01:05, 592.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 772.6970825195312 and retention time 2438.0591509999977.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▌                            | 63312/101936 [01:39<01:04, 599.13it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 756.69677734375 and retention time 1829.778739000002.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▋                            | 63438/101936 [01:39<01:05, 592.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.7656860351562 and retention time 3316.082187.
  warnings.warn(
Annotating DIA-NN result...:  62%|██████████████████████████████████████████████▊                            | 63568/101936 [01:39<01:04, 597.00it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 779.7052612304688 and retention time 1974.416119999998.
  warnings.warn(
Annotating DIA-NN result...:  63%|███████████████████████████████████████████████▏                           | 64185/101936 [01:40<00:59, 636.32it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.6034545898438 and retention time 2756.6398780000018.
  warnings.warn(
Annotating DIA-NN result...:  63%|███████████████████████████████████████████████▎                           | 64250/101936 [01:40<01:00, 626.28it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 764.7047729492188 and retention time 2318.7565609999983.
  warnings.warn(
Annotating DIA-NN result...:  63%|███████████████████████████████████████████████▌                           | 64678/101936 [01:41<00:54, 684.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 600.675048828125 and retention time 1669.2527560000021.
  warnings.warn(
Annotating DIA-NN result...:  64%|███████████████████████████████████████████████▊                           | 64950/101936 [01:41<00:55, 661.75it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.6549682617188 and retention time 3088.466266999998.
  warnings.warn(
Annotating DIA-NN result...:  64%|███████████████████████████████████████████████▉                           | 65158/101936 [01:41<00:55, 664.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.154296875 and retention time 2078.602459999998.
  warnings.warn(
Annotating DIA-NN result...:  64%|████████████████████████████████████████████████▏                          | 65496/101936 [01:42<00:55, 661.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 748.0650634765625 and retention time 1944.4911469999981.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 769.6070556640625 and retention time 1540.386493000002.
  warnings.warn(
Annotating DIA-NN result...:  65%|████████████████████████████████████████████████▍                          | 65901/101936 [01:43<00:54, 660.91it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 590.5582885742188 and retention time 2932.025635999998.
  warnings.warn(
Annotating DIA-NN result...:  65%|████████████████████████████████████████████████▌                          | 65968/101936 [01:43<00:58, 614.26it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1084594726562 and retention time 2950.116603.
  warnings.warn(
Annotating DIA-NN result...:  65%|████████████████████████████████████████████████▊                          | 66306/101936 [01:43<00:54, 652.38it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.40625 and retention time 3009.904258999998.
  warnings.warn(
Annotating DIA-NN result...:  65%|████████████████████████████████████████████████▉                          | 66436/101936 [01:43<00:56, 622.96it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 793.7246704101562 and retention time 1897.996837999998.
  warnings.warn(
Annotating DIA-NN result...:  65%|█████████████████████████████████████████████████                          | 66636/101936 [01:44<00:57, 618.54it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 734.6470336914062 and retention time 2076.13068.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 747.6993408203125 and retention time 2267.723806999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.6971435546875 and retention time 2735.738452999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 739.0074462890625 and retention time 2001.8205.
  warnings.warn(
Annotating DIA-NN result...:  65%|█████████████████████████████████████████████████                          | 66699/101936 [01:44<01:04, 543.13it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 775.7178344726562 and retention time 2148.911224999998.
  warnings.warn(
Annotating DIA-NN result...:  66%|█████████████████████████████████████████████████▌                         | 67319/101936 [01:45<00:53, 652.99it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 754.7647094726562 and retention time 2191.255558999998.
  warnings.warn(
Annotating DIA-NN result...:  66%|█████████████████████████████████████████████████▊                         | 67782/101936 [01:46<00:54, 628.87it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 745.0006713867188 and retention time 2518.586109.
  warnings.warn(
Annotating DIA-NN result...:  67%|█████████████████████████████████████████████████▉                         | 67846/101936 [01:46<00:54, 624.34it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 782.1806030273438 and retention time 1976.530836.
  warnings.warn(
Annotating DIA-NN result...:  67%|█████████████████████████████████████████████████▉                         | 67911/101936 [01:46<00:55, 613.01it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 761.1783447265625 and retention time 2746.149802000002.
  warnings.warn(
Annotating DIA-NN result...:  67%|██████████████████████████████████████████████████                         | 68107/101936 [01:46<00:56, 598.79it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.10009765625 and retention time 2508.240835000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.99365234375 and retention time 3503.111368000002.
  warnings.warn(
Annotating DIA-NN result...:  67%|██████████████████████████████████████████████████▎                        | 68365/101936 [01:47<00:55, 600.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 787.6172485351562 and retention time 2852.3946079999982.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 732.7592163085938 and retention time 1999.6307160000001.
  warnings.warn(
Annotating DIA-NN result...:  67%|██████████████████████████████████████████████████▌                        | 68696/101936 [01:47<00:51, 642.07it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 691.6746826171875 and retention time 2480.089024999998.
  warnings.warn(
Annotating DIA-NN result...:  68%|██████████████████████████████████████████████████▋                        | 68956/101936 [01:48<00:52, 623.94it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 649.6140747070312 and retention time 2282.0684610000003.
  warnings.warn(
Annotating DIA-NN result...:  68%|██████████████████████████████████████████████████▊                        | 69094/101936 [01:48<00:50, 655.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4452514648438 and retention time 1469.9487010000018.
  warnings.warn(
Annotating DIA-NN result...:  68%|██████████████████████████████████████████████████▉                        | 69161/101936 [01:48<00:49, 657.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 723.8401489257812 and retention time 2339.765595.
  warnings.warn(
Annotating DIA-NN result...:  68%|███████████████████████████████████████████████████▎                       | 69783/101936 [01:49<00:51, 626.77it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 665.6786499023438 and retention time 1497.2962619999998.
  warnings.warn(
Annotating DIA-NN result...:  69%|███████████████████████████████████████████████████▍                       | 69920/101936 [01:49<00:49, 642.73it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 779.1561279296875 and retention time 2518.776970000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 751.72119140625 and retention time 1870.163092999998.
  warnings.warn(
Annotating DIA-NN result...:  69%|███████████████████████████████████████████████████▍                       | 69985/101936 [01:49<00:50, 626.94it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0835571289062 and retention time 3362.8327200000003.
  warnings.warn(
Annotating DIA-NN result...:  69%|███████████████████████████████████████████████████▌                       | 70049/101936 [01:49<00:52, 613.12it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 681.1220092773438 and retention time 2533.096567000002.
  warnings.warn(
Annotating DIA-NN result...:  69%|███████████████████████████████████████████████████▋                       | 70324/101936 [01:50<00:48, 651.07it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 730.6834106445312 and retention time 2864.8397520000003.
  warnings.warn(
Annotating DIA-NN result...:  69%|███████████████████████████████████████████████████▉                       | 70655/101936 [01:50<00:48, 640.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 736.047607421875 and retention time 1559.350195999998.
  warnings.warn(
Annotating DIA-NN result...:  69%|████████████████████████████████████████████████████                       | 70720/101936 [01:50<00:51, 607.29it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 763.6574096679688 and retention time 2086.919566999998.
  warnings.warn(
Annotating DIA-NN result...:  69%|████████████████████████████████████████████████████                       | 70782/101936 [01:50<00:53, 578.66it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 772.0758056640625 and retention time 1678.677064000002.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▏                      | 70851/101936 [01:51<00:51, 605.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 773.137451171875 and retention time 2650.336531000002.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▏                      | 70922/101936 [01:51<00:48, 634.65it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 650.0927124023438 and retention time 2677.302139999998.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▍                      | 71207/101936 [01:51<00:44, 684.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4351196289062 and retention time 2601.640798000002.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▌                      | 71491/101936 [01:51<00:43, 696.20it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 562.9733276367188 and retention time 3459.347752000002.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▋                      | 71628/101936 [01:52<00:47, 642.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 724.6373901367188 and retention time 2229.341463.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▊                      | 71762/101936 [01:52<00:46, 642.97it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 431.00335693359375 and retention time 3099.270364000002.
  warnings.warn(
Annotating DIA-NN result...:  70%|████████████████████████████████████████████████████▊                      | 71827/101936 [01:52<00:48, 626.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 626.0272216796875 and retention time 2343.472999999998.
  warnings.warn(
Annotating DIA-NN result...:  71%|█████████████████████████████████████████████████████                      | 72105/101936 [01:52<00:43, 680.02it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1917114257812 and retention time 3226.499542999998.
  warnings.warn(
Annotating DIA-NN result...:  71%|█████████████████████████████████████████████████████▎                     | 72442/101936 [01:53<00:45, 651.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 726.1031494140625 and retention time 1746.4314289999982.
  warnings.warn(
Annotating DIA-NN result...:  71%|█████████████████████████████████████████████████████▍                     | 72584/101936 [01:53<00:42, 682.92it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1925048828125 and retention time 3439.326516.
  warnings.warn(
Annotating DIA-NN result...:  71%|█████████████████████████████████████████████████████▌                     | 72731/101936 [01:53<00:41, 696.79it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 763.6576538085938 and retention time 2201.964406000002.
  warnings.warn(
Annotating DIA-NN result...:  71%|█████████████████████████████████████████████████████▌                     | 72801/101936 [01:54<00:43, 671.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 773.0966796875 and retention time 1931.8912849999979.
  warnings.warn(
Annotating DIA-NN result...:  71%|█████████████████████████████████████████████████████▌                     | 72869/101936 [01:54<00:45, 641.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 748.0245361328125 and retention time 2679.900562000002.
  warnings.warn(
Annotating DIA-NN result...:  72%|█████████████████████████████████████████████████████▋                     | 72934/101936 [01:54<00:45, 642.28it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.7262573242188 and retention time 3367.0965790000023.
  warnings.warn(
Annotating DIA-NN result...:  72%|█████████████████████████████████████████████████████▊                     | 73136/101936 [01:54<00:43, 659.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 713.0508422851562 and retention time 1623.070866.
  warnings.warn(
Annotating DIA-NN result...:  73%|██████████████████████████████████████████████████████▌                    | 74193/101936 [01:56<00:41, 675.60it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 698.6083374023438 and retention time 2798.8668660000003.
  warnings.warn(
Annotating DIA-NN result...:  73%|██████████████████████████████████████████████████████▋                    | 74261/101936 [01:56<00:43, 629.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 599.56591796875 and retention time 1969.2039630000002.
  warnings.warn(
Annotating DIA-NN result...:  73%|██████████████████████████████████████████████████████▊                    | 74537/101936 [01:56<00:41, 667.26it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 667.6005249023438 and retention time 2299.132573000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 657.1038208007812 and retention time 1688.696269999998.
  warnings.warn(
Annotating DIA-NN result...:  73%|██████████████████████████████████████████████████████▉                    | 74604/101936 [01:56<00:42, 648.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 685.6294555664062 and retention time 2647.746988000002.
  warnings.warn(
Annotating DIA-NN result...:  74%|███████████████████████████████████████████████████████▏                   | 74946/101936 [01:57<00:40, 674.19it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 726.1271362304688 and retention time 1942.26456.
  warnings.warn(
Annotating DIA-NN result...:  74%|███████████████████████████████████████████████████████▌                   | 75578/101936 [01:58<00:38, 676.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 760.643310546875 and retention time 2223.173542000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 793.6384887695312 and retention time 2386.873855000002.
  warnings.warn(
Annotating DIA-NN result...:  74%|███████████████████████████████████████████████████████▋                   | 75646/101936 [01:58<00:42, 619.12it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 604.048095703125 and retention time 2198.9741520000002.
  warnings.warn(
Annotating DIA-NN result...:  74%|███████████████████████████████████████████████████████▋                   | 75710/101936 [01:58<00:43, 606.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 480.9449768066406 and retention time 3480.1508249999997.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.744384765625 and retention time 2703.9008689999982.
  warnings.warn(
Annotating DIA-NN result...:  74%|███████████████████████████████████████████████████████▊                   | 75838/101936 [01:58<00:45, 570.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 754.032470703125 and retention time 1899.9445330000021.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 732.13818359375 and retention time 2048.510346.
  warnings.warn(
Annotating DIA-NN result...:  74%|███████████████████████████████████████████████████████▊                   | 75901/101936 [01:58<00:45, 571.52it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.027587890625 and retention time 2403.900460000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 692.6732177734375 and retention time 2424.8913660000003.
  warnings.warn(
Annotating DIA-NN result...:  75%|███████████████████████████████████████████████████████▉                   | 75960/101936 [01:58<00:45, 574.84it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 606.9585571289062 and retention time 2409.570949999998.
  warnings.warn(
Annotating DIA-NN result...:  75%|███████████████████████████████████████████████████████▉                   | 76084/101936 [01:59<00:44, 580.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.6546630859375 and retention time 3432.961657000002.
  warnings.warn(
Annotating DIA-NN result...:  75%|████████████████████████████████████████████████████████                   | 76143/101936 [01:59<00:44, 580.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 552.595947265625 and retention time 2260.290043999998.
  warnings.warn(
Annotating DIA-NN result...:  75%|████████████████████████████████████████████████████████▏                  | 76323/101936 [01:59<00:44, 575.93it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 594.5345458984375 and retention time 1481.6323349999998.
  warnings.warn(
Annotating DIA-NN result...:  75%|████████████████████████████████████████████████████████▎                  | 76598/101936 [01:59<00:38, 664.36it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9658203125 and retention time 2193.635617000002.
  warnings.warn(
Annotating DIA-NN result...:  75%|████████████████████████████████████████████████████████▌                  | 76796/101936 [02:00<00:40, 622.23it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 792.0676879882812 and retention time 3205.215247000002.
  warnings.warn(
Annotating DIA-NN result...:  76%|████████████████████████████████████████████████████████▊                  | 77186/101936 [02:00<00:39, 621.15it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.13427734375 and retention time 1976.6208439999982.
  warnings.warn(
Annotating DIA-NN result...:  76%|████████████████████████████████████████████████████████▉                  | 77400/101936 [02:01<00:35, 688.06it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 694.6292724609375 and retention time 2075.927968000002.
  warnings.warn(
Annotating DIA-NN result...:  76%|█████████████████████████████████████████████████████████                  | 77541/101936 [02:01<00:35, 695.17it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 720.1616821289062 and retention time 2197.466701999998.
  warnings.warn(
Annotating DIA-NN result...:  76%|█████████████████████████████████████████████████████████▎                 | 77819/101936 [02:01<00:36, 666.26it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.0525512695312 and retention time 2140.544548999998.
  warnings.warn(
Annotating DIA-NN result...:  77%|█████████████████████████████████████████████████████████▍                 | 78017/101936 [02:02<00:37, 631.20it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.683837890625 and retention time 3456.338028.
  warnings.warn(
Annotating DIA-NN result...:  77%|█████████████████████████████████████████████████████████▌                 | 78225/101936 [02:02<00:35, 672.41it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 786.0698852539062 and retention time 2658.9235660000018.
  warnings.warn(
Annotating DIA-NN result...:  77%|█████████████████████████████████████████████████████████▋                 | 78429/101936 [02:02<00:38, 617.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 779.649169921875 and retention time 2858.752720000002.
  warnings.warn(
Annotating DIA-NN result...:  77%|█████████████████████████████████████████████████████████▊                 | 78492/101936 [02:02<00:38, 605.70it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4150390625 and retention time 3388.341958000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.7330932617188 and retention time 2078.602459999998.
  warnings.warn(
Annotating DIA-NN result...:  77%|█████████████████████████████████████████████████████████▊                 | 78553/101936 [02:03<00:40, 580.76it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 456.9195861816406 and retention time 2716.971961000002.
  warnings.warn(
Annotating DIA-NN result...:  77%|█████████████████████████████████████████████████████████▉                 | 78748/101936 [02:03<00:37, 623.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1597900390625 and retention time 3175.516393999998.
  warnings.warn(
Annotating DIA-NN result...:  77%|██████████████████████████████████████████████████████████                 | 78944/101936 [02:03<00:36, 636.15it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.8970336914062 and retention time 2780.2814929999977.
  warnings.warn(
Annotating DIA-NN result...:  78%|██████████████████████████████████████████████████████████▍                | 79485/101936 [02:04<00:33, 668.00it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 761.0442504882812 and retention time 2418.883624999998.
  warnings.warn(
Annotating DIA-NN result...:  78%|██████████████████████████████████████████████████████████▋                | 79762/101936 [02:04<00:32, 682.64it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.42919921875 and retention time 2763.2902390000017.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 792.6458740234375 and retention time 2495.4685499999996.
  warnings.warn(
Annotating DIA-NN result...:  78%|██████████████████████████████████████████████████████████▊                | 79898/101936 [02:05<00:34, 645.78it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 562.6307373046875 and retention time 1975.3675739999999.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 730.7314453125 and retention time 2269.749861.
  warnings.warn(
Annotating DIA-NN result...:  78%|██████████████████████████████████████████████████████████▊                | 79964/101936 [02:05<00:35, 627.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 699.6687622070312 and retention time 2953.858267999998.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████                | 80213/101936 [02:05<00:37, 584.54it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 503.5555114746094 and retention time 1753.734901000002.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████                | 80272/101936 [02:05<00:38, 564.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 758.7098388671875 and retention time 2457.087406000002.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████                | 80329/101936 [02:05<00:38, 554.44it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 625.6221313476562 and retention time 1875.8441539999978.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 773.6475219726562 and retention time 2314.580278000002.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▏               | 80385/101936 [02:05<00:39, 547.04it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 782.7116088867188 and retention time 2365.574755000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4607543945312 and retention time 3549.899254000002.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▏               | 80442/101936 [02:06<00:38, 552.94it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 792.7598266601562 and retention time 2265.813213.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▏               | 80498/101936 [02:06<00:38, 550.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.763671875 and retention time 1887.3749740000019.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▎               | 80692/101936 [02:06<00:35, 606.56it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.772216796875 and retention time 1953.270435.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▍               | 80816/101936 [02:06<00:34, 608.36it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1192626953125 and retention time 2342.272999000002.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▌               | 80881/101936 [02:06<00:34, 618.40it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 787.8782348632812 and retention time 3065.0169300000002.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▌               | 80943/101936 [02:06<00:35, 597.73it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 733.60595703125 and retention time 2352.5610330000004.
  warnings.warn(
Annotating DIA-NN result...:  79%|███████████████████████████████████████████████████████████▌               | 81003/101936 [02:07<00:35, 588.81it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 737.1444091796875 and retention time 2550.3594660000003.
  warnings.warn(
Annotating DIA-NN result...:  80%|███████████████████████████████████████████████████████████▊               | 81274/101936 [02:07<00:31, 660.38it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 683.9884033203125 and retention time 1842.164202.
  warnings.warn(
Annotating DIA-NN result...:  80%|███████████████████████████████████████████████████████████▉               | 81403/101936 [02:07<00:34, 590.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 794.7353515625 and retention time 2027.590453000002.
  warnings.warn(
Annotating DIA-NN result...:  80%|███████████████████████████████████████████████████████████▉               | 81463/101936 [02:07<00:36, 553.67it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.073486328125 and retention time 2540.104492999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 674.6190795898438 and retention time 1969.615591000002.
  warnings.warn(
Annotating DIA-NN result...:  80%|███████████████████████████████████████████████████████████▉               | 81520/101936 [02:07<00:37, 544.58it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 696.6089477539062 and retention time 2397.306670999998.
  warnings.warn(
Annotating DIA-NN result...:  80%|████████████████████████████████████████████████████████████               | 81576/101936 [02:07<00:37, 545.91it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 594.6160278320312 and retention time 2052.021061000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4096069335938 and retention time 2470.022421.
  warnings.warn(
Annotating DIA-NN result...:  80%|████████████████████████████████████████████████████████████▏              | 81764/101936 [02:08<00:34, 590.19it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.2427368164062 and retention time 2918.2895290000024.
  warnings.warn(
Annotating DIA-NN result...:  80%|████████████████████████████████████████████████████████████▎              | 81953/101936 [02:08<00:32, 607.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4186401367188 and retention time 3426.5992030000016.
  warnings.warn(
Annotating DIA-NN result...:  80%|████████████████████████████████████████████████████████████▎              | 82014/101936 [02:08<00:34, 579.57it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 540.598388671875 and retention time 2209.273524.
  warnings.warn(
Annotating DIA-NN result...:  81%|████████████████████████████████████████████████████████████▋              | 82434/101936 [02:09<00:28, 693.12it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 541.8525390625 and retention time 2300.6001.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.7296752929688 and retention time 1999.680793999998.
  warnings.warn(
Annotating DIA-NN result...:  81%|████████████████████████████████████████████████████████████▋              | 82504/101936 [02:09<00:30, 631.44it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 731.1209106445312 and retention time 2401.743811000002.
  warnings.warn(
Annotating DIA-NN result...:  81%|████████████████████████████████████████████████████████████▊              | 82713/101936 [02:09<00:29, 662.40it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0943603515625 and retention time 2818.5171910000017.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 694.0232543945312 and retention time 2218.5560419999983.
  warnings.warn(
Annotating DIA-NN result...:  81%|████████████████████████████████████████████████████████████▉              | 82780/101936 [02:09<00:30, 636.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 632.5966186523438 and retention time 2418.19887.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.7332763671875 and retention time 2478.493896.
  warnings.warn(
Annotating DIA-NN result...:  81%|█████████████████████████████████████████████████████████████              | 82973/101936 [02:10<00:32, 585.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 769.7430419921875 and retention time 2212.586989999998.
  warnings.warn(
Annotating DIA-NN result...:  82%|█████████████████████████████████████████████████████████████▍             | 83448/101936 [02:10<00:30, 608.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 790.8270874023438 and retention time 2448.733108999998.
  warnings.warn(
Annotating DIA-NN result...:  82%|█████████████████████████████████████████████████████████████▌             | 83640/101936 [02:11<00:30, 592.65it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 793.651611328125 and retention time 2778.163210999998.
  warnings.warn(
Annotating DIA-NN result...:  82%|█████████████████████████████████████████████████████████████▋             | 83845/101936 [02:11<00:28, 631.56it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 787.7249145507812 and retention time 1763.706199000002.
  warnings.warn(
Annotating DIA-NN result...:  82%|█████████████████████████████████████████████████████████████▋             | 83909/101936 [02:11<00:29, 615.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 712.004638671875 and retention time 2146.423497.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 572.7703857421875 and retention time 1649.980783000002.
  warnings.warn(
Annotating DIA-NN result...:  82%|█████████████████████████████████████████████████████████████▊             | 84037/101936 [02:11<00:29, 609.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 755.8701782226562 and retention time 2561.045013.
  warnings.warn(
Annotating DIA-NN result...:  83%|█████████████████████████████████████████████████████████████▉             | 84166/101936 [02:12<00:28, 624.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.09765625 and retention time 3311.849875999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 793.0770263671875 and retention time 2333.780440999998.
  warnings.warn(
Annotating DIA-NN result...:  85%|███████████████████████████████████████████████████████████████▌           | 86365/101936 [02:15<00:21, 714.16it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 769.1307983398438 and retention time 1878.728038999998.
  warnings.warn(
Annotating DIA-NN result...:  85%|███████████████████████████████████████████████████████████████▋           | 86504/101936 [02:15<00:24, 637.09it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.0650024414062 and retention time 2374.140529999998.
  warnings.warn(
Annotating DIA-NN result...:  85%|███████████████████████████████████████████████████████████████▊           | 86701/101936 [02:15<00:24, 620.79it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 768.655517578125 and retention time 2818.376881000002.
  warnings.warn(
Annotating DIA-NN result...:  85%|███████████████████████████████████████████████████████████████▊           | 86764/101936 [02:16<00:24, 609.49it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 762.19140625 and retention time 2684.215477000002.
  warnings.warn(
Annotating DIA-NN result...:  85%|███████████████████████████████████████████████████████████████▉           | 86826/101936 [02:16<00:25, 591.15it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.9969482421875 and retention time 2280.7179610000017.
  warnings.warn(
Annotating DIA-NN result...:  85%|███████████████████████████████████████████████████████████████▉           | 86890/101936 [02:16<00:25, 601.83it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.681396484375 and retention time 2650.509426.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 773.6298828125 and retention time 2986.42911.
  warnings.warn(
Annotating DIA-NN result...:  86%|████████████████████████████████████████████████████████████████▎          | 87421/101936 [02:17<00:23, 627.87it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 728.6611938476562 and retention time 2276.090428000002.
  warnings.warn(
Annotating DIA-NN result...:  86%|████████████████████████████████████████████████████████████████▌          | 87694/101936 [02:17<00:21, 664.46it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 710.6181030273438 and retention time 2020.810624000002.
  warnings.warn(
Annotating DIA-NN result...:  86%|████████████████████████████████████████████████████████████████▌          | 87762/101936 [02:17<00:22, 643.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 777.71875 and retention time 1938.2733499999981.
  warnings.warn(
Annotating DIA-NN result...:  86%|████████████████████████████████████████████████████████████████▌          | 87827/101936 [02:17<00:22, 623.28it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.8709716796875 and retention time 2916.1213480000024.
  warnings.warn(
Annotating DIA-NN result...:  86%|████████████████████████████████████████████████████████████████▋          | 87955/101936 [02:17<00:23, 605.90it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 768.6680297851562 and retention time 2580.263337.
  warnings.warn(
Annotating DIA-NN result...:  86%|████████████████████████████████████████████████████████████████▊          | 88151/101936 [02:18<00:21, 636.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4310913085938 and retention time 2559.1702800000003.
  warnings.warn(
Annotating DIA-NN result...:  87%|█████████████████████████████████████████████████████████████████          | 88364/101936 [02:18<00:19, 681.52it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 603.6815795898438 and retention time 1709.660395000002.
  warnings.warn(
Annotating DIA-NN result...:  87%|█████████████████████████████████████████████████████████████████▏         | 88565/101936 [02:18<00:21, 614.61it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 789.0505981445312 and retention time 1834.2209629999982.
  warnings.warn(
Annotating DIA-NN result...:  87%|█████████████████████████████████████████████████████████████████▌         | 89108/101936 [02:19<00:20, 639.36it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 772.72265625 and retention time 3326.582728000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.066162109375 and retention time 2287.096186000002.
  warnings.warn(
Annotating DIA-NN result...:  88%|█████████████████████████████████████████████████████████████████▉         | 89579/101936 [02:20<00:18, 655.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.1204833984375 and retention time 3028.966668.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 789.1679077148438 and retention time 2518.837632.
  warnings.warn(
Annotating DIA-NN result...:  88%|█████████████████████████████████████████████████████████████████▉         | 89645/101936 [02:20<00:19, 627.01it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 430.59051513671875 and retention time 2725.297194.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▍        | 90342/101936 [02:21<00:17, 646.12it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 742.0388793945312 and retention time 2599.220017000002.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▌        | 90407/101936 [02:21<00:18, 607.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1604614257812 and retention time 3350.096388.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1027221679688 and retention time 2860.939462000002.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▋        | 90690/101936 [02:22<00:16, 670.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 781.6221313476562 and retention time 1678.7171819999999.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 794.6544189453125 and retention time 2826.974170999998.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▊        | 90823/101936 [02:22<00:17, 632.97it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 745.9390869140625 and retention time 2127.5066460000003.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▊        | 90887/101936 [02:22<00:17, 618.52it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.7378540039062 and retention time 2620.78329.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▉        | 90958/101936 [02:22<00:17, 644.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 792.7000122070312 and retention time 3579.6437459999997.
  warnings.warn(
Annotating DIA-NN result...:  89%|██████████████████████████████████████████████████████████████████▉        | 91023/101936 [02:22<00:16, 645.39it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 790.06396484375 and retention time 2661.025953.
  warnings.warn(
Annotating DIA-NN result...:  90%|███████████████████████████████████████████████████████████████████▎       | 91441/101936 [02:23<00:15, 663.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 798.7353515625 and retention time 1936.2950470000021.
  warnings.warn(
Annotating DIA-NN result...:  90%|███████████████████████████████████████████████████████████████████▎       | 91508/101936 [02:23<00:16, 632.82it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 769.0606689453125 and retention time 3460.439719999998.
  warnings.warn(
Annotating DIA-NN result...:  90%|███████████████████████████████████████████████████████████████████▍       | 91711/101936 [02:23<00:15, 647.63it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 673.9827270507812 and retention time 1924.973029000002.
  warnings.warn(
Annotating DIA-NN result...:  90%|███████████████████████████████████████████████████████████████████▋       | 92068/101936 [02:24<00:13, 711.47it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 411.93316650390625 and retention time 2586.882498.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.9751586914062 and retention time 2610.146374000002.
  warnings.warn(
Annotating DIA-NN result...:  90%|███████████████████████████████████████████████████████████████████▊       | 92208/101936 [02:24<00:14, 669.72it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1351928710938 and retention time 3601.325118.
  warnings.warn(
Annotating DIA-NN result...:  91%|███████████████████████████████████████████████████████████████████▉       | 92350/101936 [02:24<00:13, 685.21it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 691.0907592773438 and retention time 2269.538935000002.
  warnings.warn(
Annotating DIA-NN result...:  91%|████████████████████████████████████████████████████████████████████▏      | 92642/101936 [02:25<00:13, 688.27it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 751.6888427734375 and retention time 2546.217627.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 600.1091918945312 and retention time 3176.6043310000023.
  warnings.warn(
Annotating DIA-NN result...:  91%|████████████████████████████████████████████████████████████████████▏      | 92712/101936 [02:25<00:13, 659.64it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 656.7100830078125 and retention time 1837.755790999998.
  warnings.warn(
Annotating DIA-NN result...:  91%|████████████████████████████████████████████████████████████████████▍      | 93069/101936 [02:25<00:13, 671.11it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4465942382812 and retention time 3827.373552.
  warnings.warn(
Annotating DIA-NN result...:  92%|████████████████████████████████████████████████████████████████████▊      | 93499/101936 [02:26<00:12, 688.51it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 771.812255859375 and retention time 3115.967452000002.
  warnings.warn(
Annotating DIA-NN result...:  92%|████████████████████████████████████████████████████████████████████▊      | 93568/101936 [02:26<00:12, 652.85it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 766.0736694335938 and retention time 2212.557025000002.
  warnings.warn(
Annotating DIA-NN result...:  92%|█████████████████████████████████████████████████████████████████████      | 93920/101936 [02:27<00:11, 668.42it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.0592041015625 and retention time 2607.957649000002.
  warnings.warn(
Annotating DIA-NN result...:  92%|█████████████████████████████████████████████████████████████████████▏     | 93988/101936 [02:27<00:12, 623.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 785.7141723632812 and retention time 2680.1232499999983.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 746.666748046875 and retention time 3030.8664430000017.
  warnings.warn(
Annotating DIA-NN result...:  92%|█████████████████████████████████████████████████████████████████████▏     | 94118/101936 [02:27<00:12, 606.65it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 707.647216796875 and retention time 2537.463520000002.
  warnings.warn(
Annotating DIA-NN result...:  92%|█████████████████████████████████████████████████████████████████████▎     | 94249/101936 [02:27<00:12, 619.79it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 673.0292358398438 and retention time 2012.1168559999978.
  warnings.warn(
Annotating DIA-NN result...:  93%|█████████████████████████████████████████████████████████████████████▍     | 94371/101936 [02:27<00:13, 577.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 653.0618286132812 and retention time 2267.210026000002.
  warnings.warn(
Annotating DIA-NN result...:  93%|█████████████████████████████████████████████████████████████████████▋     | 94643/101936 [02:28<00:11, 651.31it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 796.63330078125 and retention time 3377.7179680000017.
  warnings.warn(
Annotating DIA-NN result...:  93%|█████████████████████████████████████████████████████████████████████▋     | 94780/101936 [02:28<00:10, 665.37it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.6790771484375 and retention time 3462.729829000002.
  warnings.warn(
Annotating DIA-NN result...:  93%|█████████████████████████████████████████████████████████████████████▉     | 95058/101936 [02:28<00:10, 682.41it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 691.6064453125 and retention time 1629.331693999998.
  warnings.warn(
Annotating DIA-NN result...:  93%|██████████████████████████████████████████████████████████████████████     | 95269/101936 [02:29<00:09, 680.01it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 790.7056884765625 and retention time 2593.091985.
  warnings.warn(
Annotating DIA-NN result...:  94%|██████████████████████████████████████████████████████████████████████▏    | 95418/101936 [02:29<00:09, 681.43it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.104736328125 and retention time 2907.637767.
  warnings.warn(
Annotating DIA-NN result...:  94%|██████████████████████████████████████████████████████████████████████▍    | 95784/101936 [02:29<00:08, 713.98it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 767.03515625 and retention time 2216.8354120000017.
  warnings.warn(
Annotating DIA-NN result...:  94%|██████████████████████████████████████████████████████████████████████▌    | 95856/101936 [02:30<00:09, 655.71it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4221801757812 and retention time 2257.353904999998.
  warnings.warn(
Annotating DIA-NN result...:  94%|██████████████████████████████████████████████████████████████████████▋    | 96001/101936 [02:30<00:08, 674.55it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 524.5520629882812 and retention time 2676.6278260000017.
  warnings.warn(
Annotating DIA-NN result...:  95%|███████████████████████████████████████████████████████████████████████▏   | 96816/101936 [02:31<00:07, 682.59it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4440307617188 and retention time 2295.5844409999977.
  warnings.warn(
Annotating DIA-NN result...:  95%|███████████████████████████████████████████████████████████████████████▎   | 96885/101936 [02:31<00:07, 646.35it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 442.5893859863281 and retention time 2878.193182000002.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 778.7071533203125 and retention time 2433.857755999998.
  warnings.warn(
Annotating DIA-NN result...:  95%|███████████████████████████████████████████████████████████████████████▍   | 97081/101936 [02:32<00:07, 628.88it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 782.1782836914062 and retention time 2771.704447999998.
  warnings.warn(
Annotating DIA-NN result...:  96%|███████████████████████████████████████████████████████████████████████▋   | 97352/101936 [02:32<00:06, 660.55it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 508.6528625488281 and retention time 3437.80443.
  warnings.warn(
Annotating DIA-NN result...:  96%|███████████████████████████████████████████████████████████████████████▋   | 97419/101936 [02:32<00:07, 638.02it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1435546875 and retention time 2971.3534339999983.
  warnings.warn(
Annotating DIA-NN result...:  96%|███████████████████████████████████████████████████████████████████████▉   | 97749/101936 [02:33<00:06, 621.02it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 533.5995483398438 and retention time 1734.759345.
  warnings.warn(
Annotating DIA-NN result...:  96%|████████████████████████████████████████████████████████████████████████   | 97960/101936 [02:33<00:05, 673.25it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 797.891845703125 and retention time 2833.3730860000023.
  warnings.warn(
Annotating DIA-NN result...:  96%|████████████████████████████████████████████████████████████████████████▎  | 98312/101936 [02:33<00:05, 690.75it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.8751220703125 and retention time 2712.390352000002.
  warnings.warn(
Annotating DIA-NN result...:  97%|████████████████████████████████████████████████████████████████████████▍  | 98454/101936 [02:34<00:05, 668.62it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4087524414062 and retention time 3362.8327200000003.
  warnings.warn(
Annotating DIA-NN result...:  97%|████████████████████████████████████████████████████████████████████████▌  | 98588/101936 [02:34<00:05, 649.48it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 470.91229248046875 and retention time 2534.0880709999983.
  warnings.warn(
Annotating DIA-NN result...:  97%|████████████████████████████████████████████████████████████████████████▊  | 98935/101936 [02:34<00:04, 661.70it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 795.076416015625 and retention time 2831.238327.
  warnings.warn(
Annotating DIA-NN result...:  97%|████████████████████████████████████████████████████████████████████████▉  | 99071/101936 [02:35<00:04, 646.99it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 770.6452026367188 and retention time 2586.629301.
  warnings.warn(
Annotating DIA-NN result...:  98%|█████████████████████████████████████████████████████████████████████████▎ | 99563/101936 [02:35<00:03, 658.67it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4185180664062 and retention time 2100.163495999998.
  warnings.warn(
Annotating DIA-NN result...:  98%|█████████████████████████████████████████████████████████████████████████▎ | 99695/101936 [02:36<00:03, 616.24it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 799.6769409179688 and retention time 3218.0026690000022.
  warnings.warn(
Annotating DIA-NN result...:  98%|████████████████████████████████████████████████████████████████████████▌ | 100038/101936 [02:36<00:02, 665.90it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.4654541015625 and retention time 2453.023858000002.
  warnings.warn(
Annotating DIA-NN result...:  99%|████████████████████████████████████████████████████████████████████████▉ | 100489/101936 [02:37<00:02, 620.03it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 571.5955810546875 and retention time 2353.800825.
  warnings.warn(
Annotating DIA-NN result...:  99%|████████████████████████████████████████████████████████████████████████▉ | 100552/101936 [02:37<00:02, 589.35it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.1798095703125 and retention time 3090.596560999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 571.6185302734375 and retention time 1949.9206660000023.
  warnings.warn(
Annotating DIA-NN result...:  99%|█████████████████████████████████████████████████████████████████████████▏| 100900/101936 [02:37<00:01, 646.61it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 709.1407470703125 and retention time 2541.719547.
  warnings.warn(
Annotating DIA-NN result...:  99%|█████████████████████████████████████████████████████████████████████████▎| 101034/101936 [02:38<00:01, 655.22it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.0553588867188 and retention time 2678.050516999998.
  warnings.warn(
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 800.10205078125 and retention time 1802.378799.
  warnings.warn(
Annotating DIA-NN result...: 100%|█████████████████████████████████████████████████████████████████████████▊| 101599/101936 [02:39<00:00, 681.53it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 689.0303955078125 and retention time 2169.699490999998.
  warnings.warn(
Annotating DIA-NN result...: 100%|█████████████████████████████████████████████████████████████████████████▉| 101802/101936 [02:39<00:00, 649.07it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_spectronaut.py:488: RuntimeWarning: Could not find a suitable MS1 spectrum for precursor m/z 761.729736328125 and retention time 2161.566598999998.
  warnings.warn(
Annotating DIA-NN result...: 100%|██████████████████████████████████████████████████████████████████████████| 101936/101936 [02:39<00:00, 638.80it/s]
Total number of identifications: 101936
Total number of identifications with impure precursors: 79868
Total number of identifications with MS1 spectra not found: 539
Filtering precursors...: 100%|████████████████████████████████████████████████████████████████████████████| 101936/101936 [00:02<00:00, 37270.00it/s]
Annotating protein abundances...:   0%|                                                                                   | 0/101936 [00:00<?, ?it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:195: RuntimeWarning: Mean of empty slice
  _mean_reporter_s_f[k].append(float(np.nanmean(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:196: RuntimeWarning: All-NaN slice encountered
  _median_reporter_s_f[k].append(float(np.nanmedian(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:197: RuntimeWarning: All-NaN axis encountered
  _min_reporter_s_f[k].append(float(np.nanmin(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:198: RuntimeWarning: All-NaN axis encountered
  _max_reporter_s_f[k].append(float(np.nanmax(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:205: RuntimeWarning: Mean of empty slice
  _mean_reporter_sn_f[k].append(float(np.nanmean(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:206: RuntimeWarning: All-NaN slice encountered
  _median_reporter_sn_f[k].append(float(np.nanmedian(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:207: RuntimeWarning: All-NaN axis encountered
  _min_reporter_sn_f[k].append(float(np.nanmin(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:208: RuntimeWarning: All-NaN axis encountered
  _max_reporter_sn_f[k].append(float(np.nanmax(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:215: RuntimeWarning: Mean of empty slice
  _mean_reporter_res_f[k].append(float(np.nanmean(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:216: RuntimeWarning: All-NaN slice encountered
  _median_reporter_res_f[k].append(float(np.nanmedian(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:217: RuntimeWarning: All-NaN axis encountered
  _min_reporter_res_f[k].append(float(np.nanmin(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:218: RuntimeWarning: All-NaN axis encountered
  _max_reporter_res_f[k].append(float(np.nanmax(v)))
Annotating protein abundances...:   0%|                                                                         | 1/101936 [00:00<6:13:59,  4.54it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:190: RuntimeWarning: Mean of empty slice
  _mean_reporter_s[k].append(float(np.nanmean(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:191: RuntimeWarning: All-NaN slice encountered
  _median_reporter_s[k].append(float(np.nanmedian(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:192: RuntimeWarning: All-NaN axis encountered
  _min_reporter_s[k].append(float(np.nanmin(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:193: RuntimeWarning: All-NaN axis encountered
  _max_reporter_s[k].append(float(np.nanmax(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:200: RuntimeWarning: Mean of empty slice
  _mean_reporter_sn[k].append(float(np.nanmean(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:201: RuntimeWarning: All-NaN slice encountered
  _median_reporter_sn[k].append(float(np.nanmedian(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:202: RuntimeWarning: All-NaN axis encountered
  _min_reporter_sn[k].append(float(np.nanmin(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:203: RuntimeWarning: All-NaN axis encountered
  _max_reporter_sn[k].append(float(np.nanmax(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:210: RuntimeWarning: Mean of empty slice
  _mean_reporter_res[k].append(float(np.nanmean(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:211: RuntimeWarning: All-NaN slice encountered
  _median_reporter_res[k].append(float(np.nanmedian(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:212: RuntimeWarning: All-NaN axis encountered
  _min_reporter_res[k].append(float(np.nanmin(v)))
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\imp_read\tmt_diann.py:213: RuntimeWarning: All-NaN axis encountered
  _max_reporter_res[k].append(float(np.nanmax(v)))
Annotating protein abundances...:   3%|██                                                                     | 2922/101936 [00:13<08:31, 193.69it/s]C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\numpy\_core\fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
C:\Users\Micha\AppData\Local\uv\cache\archive-v0\nywT0YsjaUynW41W\Lib\site-packages\numpy\_core\_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
Annotating protein abundances...: 100%|█████████████████████████████████████████████████████████████████████| 101936/101936 [08:07<00:00, 209.24it/s]
        Run.Index                                                Run  ... Annotated number of PSMs (filtered) Filter:Is_Ambiguous_PG
0               0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   4                  False
1               0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   1                  False
2               0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                  14                  False
3               0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   0                  False
4               0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   0                  False
...           ...                                                ...  ...                                 ...                    ...
101931          0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   1                  False
101932          0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   1                  False
101933          0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   1                  False
101934          0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   4                  False
101935          0  20250920_Neo6A1_TH073_TT_THIDmulti005_DIA_mz1_...  ...                                   7                  False

[101133 rows x 635 columns]
```
:::

- You will get a new `report_purity_tmt_quant.parquet` file annotated by READ. Please refer to [Output](/docs/docs_output) for details.

#!/usr/bin/env python3
#
# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = [
#   "imp-read",
# ]
# ///

# DIA TMT QUANTIFICATION SPECTRONAUT [MULTI-FILE]
# 2025 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import os
import glob
from imp_read.tmt_chimerys import __get_resolution_gui_map
from imp_read.tmt_chimerys import __read_settings
from imp_read.tmt_chimerys import __convert
from imp_read.tmt_spectronaut import __read_spectra
from imp_read.tmt_chimerys import __get_consensusXML_df
from imp_read.tmt_chimerys import __get_consensusXML_map
from imp_read.tmt_spectronaut import __annotate_spectronaut_result
from imp_read.tmt_chimerys import __annotate_result_conditions
from imp_read.tmt_chimerys import __get_bool_from_value
from imp_read.tmt_spectronaut import __annotate_spectronaut_pgs
from imp_read.tmt_spectronaut import __remove_ambiguous_pg

CONFIG_FILE = "config.toml"
INI_FILE = "tmt18plex_default.ini"
RESOLUTION_FILE = "resolution.csv"
WINDOW_FILE = None
MAIN_REPORT = "report.csv"
SPECTRONAUT_SEP = ";"
# Verbose level where 0: ignore all warnings and errors, 1: raise warnings, and >= 2: raise errors
VERBOSE = 1


def main():
    mzml_files = [f for f in glob.glob("*.mzML")]
    file_prefixes = [os.path.splitext(f)[0] for f in mzml_files]
    print("Reading resolution.csv for all files...")
    resolution_gui_map = __get_resolution_gui_map(RESOLUTION_FILE)
    print("Sucessfully read resolution.csv for all files!")
    for nr, f in enumerate(file_prefixes):
        # try parsing window size just to check that it's correctly parsed
        # adjust if needed
        _ = float(f.split("DIA_mz")[1].split("_")[0].replace("c", "."))
        w = f.split("DIA_mz")[1].split("_")[0].replace("c", ".")
        # console log
        print("---------- STARTING ANALYSIS FOR ONE FILE ----------")
        print(f"file: {f}")
        print(f"window: {w}")
        # run tmt chimerys dda
        settings = __read_settings(CONFIG_FILE)
        settings["window_size"] = float(w)
        print("Used settings:")
        print(settings)
        if WINDOW_FILE is not None:
            print(f"Using windows from given windows file: {WINDOW_FILE}")
        args_spectra = __convert(f"{f}.mzML")
        spectra = __read_spectra(args_spectra)
        quantification_method = int(settings["quantification_method"])
        consensusXML_map = None
        if quantification_method != 1 and quantification_method != 3:
            consensusXML_df = __get_consensusXML_df(args_spectra, INI_FILE)
            consensusXML_map = __get_consensusXML_map(consensusXML_df)
        df = __annotate_spectronaut_result(
            spectronaut_filename=MAIN_REPORT,
            spectrum_filename=args_spectra,
            spectra=spectra,
            settings=settings,
            consensusXML_map=consensusXML_map,
            resolution_gui_map=resolution_gui_map,
            window_file=WINDOW_FILE,
            verbose=VERBOSE,
            spectronaut_sep=SPECTRONAUT_SEP,
        )
        df = __annotate_result_conditions(df, settings["conditions"])
        df = __annotate_spectronaut_pgs(df, settings)
        if not __get_bool_from_value(settings["keep_pg"]):
            df = __remove_ambiguous_pg(df)
        df.to_csv(
            f"{f}_purity_tmt_quant.csv",
            sep=",",
            index=False,
        )
        df.to_parquet(
            f"{f}_purity_tmt_quant.parquet",
            index=False,
        )
        # console log
        print("---------- FINISHED ANALYSIS FOR ONE FILE ----------")
        print(f"processed {nr + 1}/{len(file_prefixes)} files.")


if __name__ == "__main__":
    main()

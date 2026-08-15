#!/usr/bin/env python3

# DDA TMT QUANTIFICATION CHIMERYS
# 2025 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import pandas as pd

try:
    from gooey import Gooey  # pyright: ignore[reportMissingImports]
    from gooey import GooeyParser  # pyright: ignore[reportMissingImports]
except ImportError as _e:
    Gooey = None
    GooeyParser = None

from .tmt_chimerys import __read_settings
from .tmt_chimerys import __get_consensusXML_df
from .tmt_chimerys import __get_consensusXML_map
from .tmt_chimerys import __get_resolution_gui_map
from .tmt_chimerys import __read_spectra_by_scannumber
from .tmt_chimerys import __annotate_result_conditions
from .tmt_chimerys import __annotate_chimerys_protein_table
from .tmt_chimerys import __convert
from .tmt_chimerys_dda import __version
from .tmt_chimerys_dda import __annotate_chimerys_result


def main(argv=None) -> pd.DataFrame:
    if Gooey is None:
        raise ImportError("Gooey is needed but not installed!")

    @Gooey(
        encoding="utf-8",
        program_name=f"TMT Chimerys DDA {__version}",
        menu=[
            {
                "name": "Help",
                "items": [
                    {
                        "type": "Link",
                        "menuTitle": "Project Page",
                        "url": "https://github.com/hgb-bin-proteomics/TMT/",
                    }
                ],
            }
        ],
    )
    def _main(argv=None) -> pd.DataFrame:
        parser = GooeyParser(  # pyright: ignore[reportOptionalCall]
            prog="tmt_chimerys_dda.py",
            description="Calculates co-isolation purity for Chimerys DDA TMT PSMs and optionally quantifies them.",
            epilog="(c) Research Institute of Molecular Pathology, 2025",
        )
        req = parser.add_argument_group("Required", "Required Arguments.")
        req.add_argument(
            "-i",
            "--chimerys",
            dest="chimerys",
            required=True,
            help="Path/name of the Chimerys result file in tab-separated .txt format.",
            type=str,
            widget="FileChooser",
        )
        req.add_argument(
            "-s",
            "--spectra",
            dest="spectra",
            required=True,
            help="Path/name of the mass spectra file in mzML format.",
            type=str,
            widget="FileChooser",
        )
        req.add_argument(
            "-c",
            "--config",
            dest="config",
            required=True,
            help="Path/name of the config file.",
            type=str,
            widget="FileChooser",
        )
        opt = parser.add_argument_group("Optional", "Optional Arguments.")
        opt.add_argument(
            "-p",
            "--proteins",
            dest="proteins",
            required=False,
            default=None,
            help="Path/name of the Chimerys protein result file in tab-separated .txt format.",
            type=str,
            widget="FileChooser",
        )
        opt.add_argument(
            "-r",
            "--resolution",
            dest="resolution",
            required=False,
            default=None,
            help="Path/name of the resolution.csv file from the Resolution GUI file.",
            type=str,
            widget="FileChooser",
        )
        args = parser.parse_args(argv)
        settings = __read_settings(args.config)
        print("Read settings:")
        print(settings)
        args_spectra = __convert(args.spectra)
        spectra = __read_spectra_by_scannumber(args_spectra)
        quantification_method = int(settings["quantification_method"])
        consensusXML_map = None
        if quantification_method != 1 and quantification_method != 3:
            consensusXML_df = __get_consensusXML_df(args_spectra)
            consensusXML_map = __get_consensusXML_map(consensusXML_df)
        resolution_gui_map = None
        if args.resolution is not None:
            resolution_gui_map = __get_resolution_gui_map(args.resolution)
        df = __annotate_chimerys_result(
            filename=args.chimerys,
            spectrum_filename=args_spectra,
            spectra=spectra,
            settings=settings,
            consensusXML_map=consensusXML_map,
            resolution_gui_map=resolution_gui_map,
        )
        df.to_csv(
            args.chimerys.split(".txt")[0] + "_purity_tmt_quant.txt",
            sep="\t",
            index=False,
        )
        df = __annotate_result_conditions(df, settings["conditions"])
        df.to_csv(
            args.chimerys.split(".txt")[0] + "_purity_tmt_quant_conditions.txt",
            sep="\t",
            index=False,
        )
        if args.proteins is not None:
            proteins_df = __annotate_chimerys_protein_table(args.proteins, df, settings)
            proteins_df.to_csv(
                args.proteins.split(".txt")[0] + "_purity_tmt_quant.txt",
                sep="\t",
                index=False,
            )
        print("Script finished successfully!")
        return df

    return _main(argv)


if __name__ == "__main__":
    _ = main()

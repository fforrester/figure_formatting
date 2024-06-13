from matplotlib import rc
from matplotlib import rcParams
from matplotlib import cycler
from matplotlib.pyplot import locator_params
from matplotlib.ticker import AutoMinorLocator
from collections import OrderedDict
import numpy as np


# ---------------------------------------------------
# Color sets
# ---------------------------------------------------
# Standard tableau 11 set
tableau = OrderedDict(
    [
        ("blue", "#0072B2"),
        ("orange", "#E69F00"),
        ("vermilion","#D55E00"),
        ("reddish", "#CC79A7"),
        ("green", "#009E73"),
        ("skyblue", "#56B4E9"),
        ("pink","#FAAFE4"),
        ("brown","#CA9161"),
        ("yellow", "#F0E442"),
        ("black","#000000")

    ]
)


colors = {
    "bluey_green": {
        0: "#FFFFD9",
        1: "#EDF8B1",
        2: "#C7E9B4",
        3: "#7FCDBB",
        4: "#41B6C4",
        5: "#1D91C0",
        6: "#225EA8",
        7: "#253494",
        8: "#081D58",
    },
    
"pinky_purple": {
        0: "#FFF7F3",
        1: "#FDE0DD",
        2: "#FCC5C0",
        3: "#FA9FB5",
        4: "#F768A1",
        5: "#DD3497",
        6: "#AE017E",
        7: "#7A0177",
        8: "#49006A",
    },

"redy_orange": {
        0: "#FFFFCC",
        1: "FFEDA0",
        2: "FED976",
        3: "#FEB24C",
        4: "#FD8D3C",
        5: "#FC4E2A",
        6: "#E31A1C",
        7: "#BD0026",
        8: "#800026",
    },
    
"yellowy_green": {
        0: "#FFFFE5",
        1: "#F7FCB9",
        2: "#D9F0A3",
        3: "#ADDD8E",
        4: "#78C679",
        5: "#41AB5D",
        6: "#238443",
        7: "#006837",
        8: "#004529",
    },

    "blue": {
        0: "#B8E3F4",
        1: "#95D5EF",
        2: "#71C8EA",
        3: "#4EBAE4",
        4: "#2AACDF",
        5: "#1D91C0",
        6: "#1879A0",
        7: "#135E7C",
        8: "#0D4359",  
    },

       "yellow": {
        0: "#FFFAD6",
        1: "#FFF4AD",
        2: "#FFEF85",
        3: "#FFE95C",
        4: "#FFE433",
        5: "#FFDE0A",
        6: "#F0D005,
        7: "#CCB100",
        8: "#B89F00",  
    },
    
      "red": {
        0: "#F6B6B7",
        1: "#F29193",
        2: "#EE6D6F",
        3: "#EA484B",
        4: "#E31A1C",
        5: "#C9181B",
        6: "#A41316,
        7: "#800F11",
        8: "#5B0B0C",  
    },

     "grey": {
        0: "#D6D6D6",
        1: "#C2C2C2",
        2: "#ADADAD",
        3: "#999999",
        4: "#7F7F7F",
        5: "#707070",
        6: "#5C5C5C,
        7: "#474747",
        8: "#333333",  
    },
}

fontsize = 8
linewidth = 0.7

nearly_black = "#161616"
light_grey = "#EEEEEE"
lighter_grey = "#F5F5F5"
white = "#FFFFFF"

text_entries = [
    "font.size",
    "xtick.labelsize",
    "ytick.labelsize",
    "axes.labelsize",
    "axes.titlesize",
]

line_entries = [
    "xtick.major.width",
    "xtick.minor.width",
    "ytick.major.width",
    "ytick.minor.width",
    "lines.linewidth",
    "axes.linewidth"
]

formatting = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "DejaVu Sans"],
    "mathtext.fontset": "custom",
    "mathtext.rm": f"Helvetica",
    "mathtext.it": f"Helvetica:italic",
    "mathtext.bf": f"Helvetica",
    "font.size": fontsize,
    "axes.formatter.limits": (-3, 3),
    "axes.spines.bottom": True,
    "axes.spines.left": True,
    "axes.spines.right": True,
    "axes.spines.top": True,
    "xtick.major.pad": 3,
    "ytick.major.pad": 3,
    "ytick.color": nearly_black,
    "xtick.color": nearly_black,
    "xtick.labelsize": fontsize,
    "ytick.labelsize": fontsize,
    "ytick.major.size": 3,
    "ytick.minor.size": 1.5,
    "xtick.major.size": 3,
    "xtick.minor.size": 1.5,
    "xtick.major.width": linewidth,
    "xtick.minor.width": linewidth,
    "ytick.major.width": linewidth,
    "ytick.minor.width": linewidth,
    "axes.labelcolor": nearly_black,
    "legend.facecolor": white,
    "legend.fancybox": False,
    "legend.frameon": False,
    "savefig.bbox": "tight",
    "axes.facecolor": white,
    "axes.labelpad": 2,
    "axes.labelsize": fontsize,
    "axes.titlesize": fontsize,
    "axes.titlepad": 7,
    "axes.titlelocation": "left",
    "lines.markersize": 5.0,
    "lines.scale_dashes": False,
    "axes.linewidth": linewidth,
    "axes.formatter.useoffset": False,
    "lines.linewidth": linewidth,
    "figure.dpi": 127,
    "figure.figsize": (3.15, 1.95),
}  # Default size = landscape (8 cm width + golden ratio(1.618)


def square_ax(ax):
    ax.set_aspect(1.0 / ax.get_data_ratio())

def set_formatting(Dict: formatting = formatting, context=None) -> None:

    if context == "talk":
        formatting.update({k: 16 for k in text_entries})
        formatting.update({k: 1.4 for k in line_entries})
    for k, v in formatting.items():
        rcParams[k] = v

def set_palette(palette: OrderedDict = None) -> None:
    if palette is None:
        color_cycle = tableau.values()
    else:
        color_cycle = palette.values()
    rcParams['axes.prop_cycle'] = cycler(color=color_cycle)

def unspine():
    rcParams["axes.spines.right"] = False
    rcParams["axes.spines.top"] = False






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
        1: "#FFEDA0",
        2: "#FED976",
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
        0: "#85D2FF",
        1: "#5CC3FF",
        2: "#33B4FF",
        3: "#0AA5FF",
        4: "#008EE0",
        5: "#0072B2",
        6: "#005A8F",
        7: "#004166",
        8: "#00273D", 
        9: "#000D14"
    },

       "yellow": {
        0: "#FCFAD9",
        1: "#F9F4B4",
        2: "#F6EF8E",
        3: "#F3EA68",
        4: "#F0E442",
        5: "#EDDF1D",
        6: "#D0C311",
        7: "#AA9F0E",
        8: "#847C0B",
        9: "#5E5908"
    },
    
      "red": {
        0: "#F9C8C8",
        1: "#F5A3A3",
        2: "#F17E7E",
        3: "#ED5A5A",
        4: "#E93535",
        5: "#DC1919",
        6: "#B81414",
        7: "#931010",
        8: "#6E0C0C", 
        9: "#490808"
    },

    "orange": {
        0: "#FFECC2",
        1: "#FFDF99",
        2: "#FFD270",
        3: "#FFC547",
        4: "#FFB81F",
        5: "#E69F00",
        6: "#CC8B00",
        7: "#A37000",
        8: "#7A5400",  
        9: "#523800"
    },

     "grey": {
        0: "#D6D6D6",
        1: "#C2C2C2",
        2: "#ADADAD",
        3: "#999999",
        4: "#7F7F7F",
        5: "#707070",
        6: "#5C5C5C",
        7: "#474747",
        8: "#333333"  
    },

    "green": {
        0:"#99FFE4",
        1:"#70FFD9",
        2:"#47FFCE",    
        3:"#1FFFC3",
        4:"#00F5B4",
        5:"#00CC96",
        6:"#009E73",
        7:"#007A5A",
        8:"#00523C",
        9:"#00291E"
    },
    
    "reddish": {
        0:"#F9F0F5",
        1:"#EED3E2",
        2:"#E3B5CE",    
        3:"#D897BB",
        4:"#CC79A7",
        5:"#C15C94",
        6:"#B14380",
        7:"#94386B",
        8:"#762D55",
        9:"#592240"
    }
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






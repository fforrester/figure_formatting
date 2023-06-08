import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as transforms

def add_range_frames(ax, linewidth=None):
    # Hide the original spines and remember their line widths
    linewidths = []
    for spine in ax.spines.values():
        linewidths.append(spine.get_linewidth())
        spine.set_visible(False)

    # If no linewidth was provided, use the maximum linewidth of the original spines
    if linewidth is None:
        linewidth = max(linewidths)

    # Get the data limits
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    # Create new transforms
    transform_x = transforms.blended_transform_factory(ax.transData, ax.transAxes)
    transform_y = transforms.blended_transform_factory(ax.transAxes, ax.transData)

    # Draw the range frames
    ax.plot([xmin, xmax], [0, 0], color='black', transform=transform_x, clip_on=False, linewidth=linewidth)
    ax.plot([0, 0], [ymin, ymax], color='black', transform=transform_y, clip_on=False, linewidth=linewidth)

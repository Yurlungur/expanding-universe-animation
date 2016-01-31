#!/usr/bin/env python

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2016-01-31 14:48:32 (jmiller)>

# imports
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation

# global constants
NUM_ROWS=1
NUM_COLUMNS=2
NUM_SUBPLOTS=NUM_ROWS*NUM_COLUMNS
AXIS_BOUNDS = [-1,1]
MARKERSIZE=12.0

# The functions for the grid
def make_centred_grid(h):
    "Create grid centred on Earth with dots separated by distance h"
    

# set up the figure, axis, and plot elements
fig , axarr = plt.subplots(NUM_ROWS,NUM_COLUMNS)
lines = [None for ax in axarr]
for i,ax in enumerate(axarr):
    ax.set_xlim(AXIS_BOUNDS)
    ax.set_ylim(AXIS_BOUNDS)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    figlines[i] = [ax.plot([],[],'bo',ms=MARKERSIZE),
                   ax.plot([],[],'ro',ms=MARKERSIZE)]

def init():
    "Initialization function. Plot the background for each frame."
    for lines in figlines:
        for line in lines:
            line.set_data([],[])
    return figlines

plt.show()

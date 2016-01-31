#!/usr/bin/env python

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2016-01-31 17:22:38 (jmiller)>
# ======================================================================



# Preliminaries
# ======================================================================
# imports
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation

# global constants
NUM_ROWS=1
NUM_COLUMNS=2
NUM_SUBPLOTS=NUM_ROWS*NUM_COLUMNS
NUM_COLORS=2
AXIS_BOUNDS = [-1,1]
MARKERSIZE=12.0
STARTING_DISTANCE=0.25/2
NUM_TIMES=20
TIMES = np.linspace(1,3,NUM_TIMES)
DISTANCES = STARTING_DISTANCE * TIMES
FONTSIZE=16
FILENAME='expanding_universe_two_perspectives.mp4'
# ======================================================================



# utility functions
# ======================================================================
def symmetric_arange(xmax,dx):
    "Like arange, but missing first element"
    positive_out = np.arange(0,xmax,dx)
    negative_out = np.fliplr([-1*positive_out])[0]
    out = np.hstack((negative_out[:-1],positive_out))
    return out

def is_even(number):
    "Whether or not a number is odd. Returns false if number is not integer."
    return number % 2 == 0

def midpoint(length):
    """
    Given an array length, finds the index of the midpoint.
    Assumes array is odd.
    """
    return length/2
# ======================================================================



# The functions for the grid
# ======================================================================
def make_universe_grid(h):
    "Create a grid that does not contain Earth, with dots separated by h"
    x = symmetric_arange(AXIS_BOUNDS[1],
                         h)
    X,Y = np.meshgrid(x,x)
    return X,Y

def make_centered_grid(X,Y):
    "Center Earth based on universe grid"
    center_ix,center_iy = (midpoint(l) for l in X.shape)
    earth_ix,earth_iy = center_ix,center_iy
    earth_x = np.array([X[earth_ix,earth_iy]])
    earth_y = np.array([Y[earth_ix,earth_iy]])
    return earth_x,earth_y

def make_uncentered_grid(X,Y):
    "Place uncentered Earth based on universe grid"
    center_ix,center_iy = (midpoint(l) for l in X.shape)
    earth_ix,earth_iy = center_ix+1,center_iy+2
    earth_x = np.array([X[earth_ix,earth_iy]])
    earth_y = np.array([Y[earth_ix,earth_iy]])
    return earth_x,earth_y
    
# ======================================================================



# The plot
# ======================================================================
# set up the figure, axis, and plot elements
fig , axarr = plt.subplots(NUM_ROWS,NUM_COLUMNS,
                           figsize=(10,4))
for i,ax in enumerate(axarr):
    ax.set_xlim(AXIS_BOUNDS)
    ax.set_ylim(AXIS_BOUNDS)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
axarr[0].set_title('How it Looks from Earth',
                   fontsize=FONTSIZE)
axarr[1].set_title('How it Looks Elsewhere',
                   fontsize=FONTSIZE)
bg_centered, = axarr[0].plot([],[],'bo',ms=MARKERSIZE)
bg_uncentered, = axarr[1].plot([],[],'bo',ms=MARKERSIZE)
fg_centered, = axarr[0].plot([],[],'ro',ms=MARKERSIZE)
fg_uncentered, = axarr[1].plot([],[],'ro',ms=MARKERSIZE)

def init():
    "Initialization function. Plot the background for each frame."
    bg_centered.set_data([],[])
    bg_uncentered.set_data([],[])
    fg_centered.set_data([],[])
    fg_uncentered.set_data([],[])
    return bg_centered,bg_uncentered,fg_centered,fg_uncentered

def animate(i):
    "Animation function. This is called sequentially"
    h = DISTANCES[i]
    X,Y = make_universe_grid(h)
    cex,cey = make_centered_grid(X,Y)
    uex,uey = make_uncentered_grid(X,Y)
    x,y=X.flatten(),Y.flatten()
    bg_centered.set_data(x,y)
    fg_centered.set_data(cex,cey)
    bg_uncentered.set_data(x,y)
    fg_uncentered.set_data(uex,uey)
    return bg_centered,bg_uncentered,fg_centered,fg_uncentered
    
anim = animation.FuncAnimation(fig,animate,init_func=init,
                               frames=len(TIMES),
                               interval=60,
                               blit=True)

anim.save(FILENAME,
          extra_args=['-vcodec','libx264'])
# ======================================================================

# Expanding Universe Animation

Author: Jonah Miller (jonah.maxwell.miller@gmail.com)

Time-stamp: <2016-01-31 17:48:09 (jmiller)>

## Requirements

* python2 or python3, doesn't matter which. Note that I had trouble
  saving the animation in python3 because of a
  [known bug in numpy](https://github.com/matplotlib/matplotlib/issues/1891/). For
  this reason, the code uses python2 by default.
* matplotlib
* numpy
* ffmpeg

## Description

This is python code to generate an animation showing how the universe
expands. In the left frame, I show how the expansion of the universe
looks to us. The Earth is a red dot and all astronomical objects are
moving away from it. Nearer objects appear to be moving away from the
Earth less quickly than distant objects. (That's
[Hubble's law](https://en.wikipedia.org/wiki/Hubble's_law).)

In the right frame, I show how the expansion of the universe looks in
a different (arbitrary) reference frame. Again the Earth is a red
dot. The overall distance between each point in space is increasing at
a constant rate. This is the expanding universe we know and love.

A key point is that in an expanding universe, every point looks like
the center of an explosion, but there is no center. And there is no
explosion.

## Running

To generate the animation, just clone the repository, enter it, and
type `make`. This will generate an mp4 video and a gif.

To swap between python2 and python3, edit the `PYTHON` variable in the Makefile.

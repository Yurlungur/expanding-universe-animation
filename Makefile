# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2016-01-31 17:46:42 (jmiller)>

# file name
NAME=expanding_universe_two_perspectives
# should be version agnostic
# but matplotlib.animation has a bug in python3 for me
PYTHON=python2

default: all
all: mp4 gif
gif: ${NAME}.gif
mp4: ${NAME}.mp4

${NAME}.gif: ${NAME}.mp4
	convert $^ $@

${NAME}.mp4: expanding-universe-animation.py
	$(PYTHON) $^

clean:
	$(RM) ${NAME}.gif ${NAME}.mp4

.PHONY: default all gif mp4

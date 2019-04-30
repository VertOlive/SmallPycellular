import numpy as np
import png

WOLFRAMRULE = 90
RESOLUTIONSIZE = 2*2
IMAGESIZE = 50

def convertToPng(numpyList):
    pass ## TODO: Work in progress.

def main():
    image = np.zeros(np.shape(IMAGESIZE,IMAGESIZE), dtype=bool)
    image[0][(int)(IMAGESIZE/2)] = true

    for(y in range(0, IMAGESIZE)):
        for(x in range(0, IMAGESIZE)):
            pass ## TODO: Work in progress.


if(__name__ == "__main__"):
    main()

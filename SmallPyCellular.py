import numpy as np
from PIL import Image

WOLFRAMRULE = np.uint8(90)
RESOLUTIONSIZE = 4
IMAGESIZE = 100

def convertToPng(numpyList):
    size = numpyList.shape[::-1]
    databytes = np.packbits(numpyList, axis=1)
    Image.frombytes(mode='1', size=size, data=databytes).save("Cellular.png")

def main():
    ## Unpack bits rules.
    rulesList = np.unpackbits(WOLFRAMRULE)
    print(rulesList)
    ## Make blank cellular field buffer with one active cell.
    cellularField = np.zeros((IMAGESIZE, IMAGESIZE), dtype=bool)
    cellularField[0][int(IMAGESIZE/2) -1] = True

    ## Process rules
    for y in range(0, IMAGESIZE-1):
        for x in range(1, IMAGESIZE-1):
            value = int(cellularField[y][x-1])*1 + int(cellularField[y][x])*2 + int(cellularField[y][x+1])*4
            if(rulesList[value] == 1):
                cellularField[y+1][x] = True


    convertToPng(cellularField)

if(__name__ == "__main__"):
    main()

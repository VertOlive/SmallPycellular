import numpy as np
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("rule",
                    type=np.uint8,
                    help="Set the Wolfram rule from 0 to 255")
parser.add_argument("-r", "--random",
                    action="store_true",
                    help="Set ramdom patern of initial cells")
args = parser.parse_args()

WOLFRAMRULE = np.uint8(args.rule)
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
    rulesList= np.flip(rulesList)
    ## Make blank cellular field buffer..
    cellularField = np.zeros((IMAGESIZE, IMAGESIZE), dtype=bool)


    if(args.random == True):
        for i in range(0, IMAGESIZE):
            cellularField[0][i] = bool(np.random.randint(0,2))
    else:
        cellularField[0][int(IMAGESIZE/2) -1] = True

    ## Process rules
    for y in range(0, IMAGESIZE-1):
        for x in range(1, IMAGESIZE-1):
            value = int(cellularField[y][x-1])*4 + int(cellularField[y][x])*2 + int(cellularField[y][x+1])*1
            if(rulesList[value] == 1):
                cellularField[y+1][x] = True

    ## Create the image from the bufferd cellularField.
    convertToPng(cellularField)

if(__name__ == "__main__"):
    main()

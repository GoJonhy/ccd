import sys, os,getopt
import random
from bitstring import BitArray;

def CompressByte(symbol: bytes, index: int):
    newsymbol=0;
    if(index<=5):
        d = BitArray(symbol)
        aux=d.cut(6,2,count=1)
        for k in d.cut(6,2,count=1):
            newsymbol = k.bin
    else:
        d = BitArray(symbol)
        aux=d.cut(6,2,count=1)
        for k in d.cut(4,4,count=1):
            newsymbol = k.bin
    return newsymbol;

def main(argv):

    # Leitura de argumentos
    inputFileName = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile"])
    except getopt.GetoptError:
        print("fileEntropy.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('fileEntropy.py -i <inputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileName = arg

    stdout = os.fdopen(sys.stdout.fileno(), 'wb')

    inputFile = open(inputFileName, "rb")
    fileSize = os.stat(inputFileName).st_size
    size = 1
    byteTotal = 0
    byteDict = dict()
    betsize=0;bet=list();
    # Leitura byte a byte
    while True:
        byte = inputFile.read(size)
        if(int.from_bytes(byte, "big")!=0):
            print(CompressByte(byte,betsize))
            if(betsize==7):
                betsize=0;
            betsize+=1;
        byteTotal += 1
        
        if byteTotal >= fileSize:
            break

if __name__ == "__main__":
    main(sys.argv[1:])
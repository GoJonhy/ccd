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

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


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
    compressedByte=''
    while True:
        byte = inputFile.read(size)
        if(int.from_bytes(byte, "big")!=0):
            compressedByte+=CompressByte(byte,betsize)
            #print(compressedByte)
            if(betsize==7):
                betsize=0;
            betsize+=1;
        byteTotal += 1
        
        if byteTotal >= fileSize:
            break


    #print(bitstring_to_bytes(compressedByte))
    #print(int(compressedByte, 2).to_bytes(len(compressedByte) // 8, byteorder='big'));
    #print(bytes([int(i,2) for i in compressedByte]))
    stdout.write(bitstring_to_bytes(compressedByte))
    #stdout.write(int(compressedByte, 2).to_bytes(len(compressedByte) // 8, byteorder='big'));
if __name__ == "__main__":
    main(sys.argv[1:])
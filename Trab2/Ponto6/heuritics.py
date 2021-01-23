#!/bin/python3

import sys, getopt, os, secrets
import math
from integer import Integer
from operator import itemgetter
import math

def lerBytes(filePath :str,byteDict :dict , seqSize :int):
    inputFileSize = os.stat(filePath).st_size
    inputFile = open(filePath, "rb")
    curSize=0
    curByte = None
    curSeqSize=0
    seq = None
    while True:
        if( curSize >= inputFileSize):
            break
        curByte = inputFile.read(1)
        curSize+=1
        if seq == None:
            seq=curByte
        else:
            seq.join([seq,curByte])
        curSeqSize+=1
        # Verifica se Byte existe no dicionario
        if (curSeqSize == seqSize):
            symbol = byteDict.get(seq)
            if symbol == None:
                byteDict.update([(seq, 1)])
            else:
                symbol += 1
                byteDict.update([(seq, symbol)])
            seq = None
            curSeqSize=0

def createHeuristicDict(byteDict :dict,outputFileSize :int,stdout):
    outputSize=0
    # Organizar lista   
    sortedByteDict = {k: v for k, v in sorted(byteDict.items(), key=itemgetter(1))}.items()
    # Avançar estado de leitura
    for key, value in sortedByteDict:
        outputSize += 1
        stdout.write(key)
        # Verificar dimensao de saida
        if( outputSize >= outputFileSize):
            return
    
        

# Main 
def main(argv):
    # Leitura de argumentos
    try:
        opts, args = getopt.getopt(argv, "hi:s::", ["ifile", "outsize"])
    except getopt.GetoptError:
        print("fileEntropy.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('fileEntropy.py -i <inputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileDir = arg
        elif opt in ("-s", "--outsize"):
            size = float(arg)
    # Global Variables
    seqSize=4
    fileList=os.listdir(inputFileDir)
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    byteDict = dict()
    outputFileSize=32768
    # Obter dados
    for file in fileList:
        filePath=inputFileDir+'/'+file
        lerBytes(filePath,byteDict,seqSize)
    createHeuristicDict(byteDict,outputFileSize,stdout)

if __name__ == "__main__":
   main(sys.argv[1:])
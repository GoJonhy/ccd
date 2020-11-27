#!/bin/python3

import sys, getopt, os
import math


# Calculo de entropia para uma fonte de markov de 1 ordem
def entropyCalc1Markov(byte2DArray):
    entropy = 0
    countColum = [0] * 256
    countLines = [0] * 256
    line = 0
    for linha in byte2DArray:
        col = 0
        for sym in linha:
            countColum[col] += sym
            col += 1

            countLines[line] += sym

        line += 1
    
    counTotal = 0
    for v in countColum:
        counTotal += v

    line = 0
    for v in countColum:
        if(v != 0 and countLines[line] != 0):
            entropy += (v/counTotal) * math.log(1/(countLines[line]/counTotal), 2)
        line += 1

    return entropy

# Criar array auxiliar [linha|estado][coluna|simbolo]
def create2DArray():
    return [[0] * 256 for i in range(256)]

# Main 
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

    print ('Input file is "', inputFileName)

    # Obter ficheiro
    inputFile = open(inputFileName, "rb")
    fileSize = os.stat(inputFileName).st_size
    size = 1
    byteTotal = 0
    byte2DArray = create2DArray()

    # Leitura byte a byte
    byte = None
    while True:
        prev = byte
        byte = inputFile.read(size)

        if(prev != None):
            byte2DArray[int.from_bytes(prev, "big")][int.from_bytes(byte, "big")] += 1
        
        byteTotal += 1
        if byteTotal >= fileSize:
            break

    # Calculo de Entropia
    arr = [ [4, 2, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0]]
    entropia = entropyCalc1Markov(byte2DArray)

    ### Resultados ###
    print("\n")
    print("Entropia 1ª Ordem Markov: ", entropia)

if __name__ == "__main__":
   main(sys.argv[1:])
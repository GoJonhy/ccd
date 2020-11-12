#!/usr/bin/python3

import sys, getopt, os
from operator import itemgetter
import math


# Estima a entropia associada ao ficheiro com base nas contagens fornecidas
def entropyCount(symList, byteTotal: int) -> float:
    entropy = 0
    for sym in symList.items():
        prob = sym[1]/byteTotal
        entropy += prob * math.log(1/prob, 2)
    return entropy

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
    byteDict = dict()

    # Leitura byte a byte
    while True:
        piece = inputFile.read(size)

        symbol = byteDict.get(piece)
        if symbol == None:
            byteDict.update([(piece, 1)])
        else:
            symbol += 1
            byteDict.update([(piece, symbol)])
        byteTotal += 1
        if byteTotal >= fileSize:
            break

    # Organizar lista
    sortedByteDict = {k: v for k, v in sorted(byteDict.items(), key=itemgetter(1))}

    print(sortedByteDict)

    # Extimativa entropia com base a distribuiçao
    entropy = entropyCount(sortedByteDict, byteTotal)
    # Indicaç~ao de resultados
    print("Entropia: ", entropy)
    print("Numero de Simbolos: ", len(sortedByteDict))
    print("Simbolos mais frequentes: ")
    print(" 1º: ", int.from_bytes(sortedByteDict.popitem()[0], "big") )
    print(" 2º: ", int.from_bytes(sortedByteDict.popitem()[0], "big") )
    print(" 3º: ", int.from_bytes(sortedByteDict.popitem()[0], "big"))
    print(" 4º: ", int.from_bytes(sortedByteDict.popitem()[0], "big"))
    print(" 5º: ", int.from_bytes(sortedByteDict.popitem()[0], "big"))
    
if __name__ == "__main__":
   main(sys.argv[1:])




#!/usr/bin/python3

import sys, getopt, os
from operator import itemgetter
import math


# Estima a entropia associada ao ficheiro com base nas contagens fornecidas
def entropyCount(symList, byteTotal: int) -> float:
    entropy = 0
    for sym in symList:
        prob = sym[1]/byteTotal
        entropy += prob * math.log(1/prob, 2)
    return entropy

# Auto informaç~ao de um simbolo 
def selfInformation(prob: float) -> float:
    return math.log(1/prob, 2)


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

    print("\n")
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
    sortedByteDict = {k: v for k, v in sorted(byteDict.items(), key=itemgetter(1), reverse=True)}.items()

    # Sub conjunto de 50% 
    subConSym = []
    probSum = 0 
    half = byteTotal/2
    for k,v in sortedByteDict:
        if(probSum >= half):
            break
        else:
            subConSym.append(int.from_bytes(k, "big"))
            probSum += v
        


    # Compresao obtida
    newSize = 0
    for k,v in sortedByteDict:
        count = v
        newCode = selfInformation(count/byteTotal)
        newSize += count*newCode
    compObtida = byteTotal/newSize
        

    ### Resultados ###

    # Extimativa entropia com base a distribuiçao
    entropy = entropyCount(sortedByteDict, byteTotal)
    # Indicaç~ao de resultados
    print("Entropia: ", entropy)
    print("Numero de Simbolos: ", len(sortedByteDict))
    print("Simbolos mais frequentes: ")
    i = 0
    for k, v in sortedByteDict:
        if(i == 5):
            break
        i += 1

        print(i,"º: ", int.from_bytes(k, "big") )

    # Subconjunto desejado, mais que 50%
    print("Subconjunto com mais que 50% de probabilidade: ", subConSym)
    print("Soma probabilidade: ", probSum/byteTotal*100, "%")

    # Compress~ao obtida
    print("Compress~ao obtida: ", compObtida)

if __name__ == "__main__":
   main(sys.argv[1:])
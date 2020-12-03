#!/bin/python3

import sys, getopt, os, secrets
import math

# Posiçao de procura. Corresponde ao
def indexGenerator(fileSize):
    max = (fileSize-1)
    def generator():
        while True: 
            yield secrets.randbelow(max) 
    return generator

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

    # Obter ficheiro
    inputFile = open(inputFileName, "rb")
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    fileSize = os.stat(inputFileName).st_size
    outputSize = 0
    nextIndex = indexGenerator(fileSize)()

    # Leitura byte a byte
    curByte, nextByte = None, None
    while True:
        # Encontrar e escrever primeiro
        index = next(nextIndex)
        inputFile.seek(index)
        curByte = inputFile.read(1)
        stdout.write(curByte)

        # Avançar estado de leitura
        outputSize += 1
        cur = inputFile.tell()
        if( outputSize >= fileSize or cur > fileSize):
            break
            
    stdout.flush()
    stdout.close()


if __name__ == "__main__":
   main(sys.argv[1:])
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
    size = 6
    try:
        opts, args = getopt.getopt(argv, "hi:s:", ["ifile", "outsize"])
    except getopt.GetoptError:
        print("fileEntropy.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('fileEntropy.py -i <inputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileName = arg
        elif opt in ("-s", "--outsize"):
            size = float(arg)

    # Obter ficheiro
    inputFile = open(inputFileName, "rb")
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    fileSize = int(size * 1024)
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

        # Encontrar proxima ocorrencia e registar seu seguinte se existir
        while True:
            nextByte = inputFile.read(1)
            if(nextByte == curByte):
                stdout.write(nextByte)
                outputSize += 1
                break
            cur = inputFile.tell()
            if(cur >= fileSize):
                nextByte == None
                break

        # Verificar dimensao de saida
        if( outputSize >= fileSize):
            break
            
    stdout.flush()
    stdout.close()


if __name__ == "__main__":
   main(sys.argv[1:])
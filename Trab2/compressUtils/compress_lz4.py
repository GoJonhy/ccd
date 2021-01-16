#!/bin/python3

import sys, getopt, os, secrets
import math

import lz4.frame

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
        opts, args = getopt.getopt(argv, "hi:d:o", ["ifile", "outsize"])
    except getopt.GetoptError:
        print("fileEntropy.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('fileEntropy.py -i <inputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileName = arg
        elif opt in ("-d", "--dict"):
            dictFileName = arg
        elif opt in ("-o", "--ofile"):
            outputFileName = arg

    # Obter dados
    inputFile = open(inputFileName, "rb")
    dictFile = open(dictFileName, "rb")
    fileSize = os.stat(inputFileName).st_size
    dictSize = os.stat(inputFileName).st_size
    
    # Ler ficheiros
    fileData = inputFile.read(fileSize)
    dictData = inputFile.read(dictSize)

    # Simul
    # dict
    compressed_dict = lz4.frame.compress(dictData)
    # No dict
    compressed_data = lz4.frame.compress(fileData)
    # With dict
    compressed_data_with_dict = lz4.frame.compress(dictData + fileData)

    # Resultados
    compress_normal = len(compressed_data) 
    compress_dict = len(compressed_data_with_dict) - len(compressed_dict)
    compress_gain = compress_normal/compress_dict

    # Write output
    print(inputFileName)
    print("Original: ", fileSize)
    print("Normal: ", compress_normal)
    print("Dict: ", compress_dict)
    print("Gain: ", compress_gain)


if __name__ == "__main__":
   main(sys.argv[1:])
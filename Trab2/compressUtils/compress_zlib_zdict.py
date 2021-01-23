#!/bin/python3

import sys, getopt, os, secrets
import math

import zlib

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
    dictFileName = None
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
    if(dictFileName == None or dictFileName == "" or dictFileName == "-"):
        dictFile = b''
        dictSize = 0
        dictData = b''
    else:
        dictFile = open(dictFileName, "rb")
        dictSize = os.stat(dictFileName).st_size
        dictData = dictFile.read(dictSize)
    fileSize = os.stat(inputFileName).st_size
    
    # Ler ficheiros
    fileData = inputFile.read(fileSize)

    # Simul
    # No dict
    compress = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=zlib.MAX_WBITS, memLevel=9, strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(fileData)
    compressed_data += compress.flush()
    # With dict
    compress = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=zlib.MAX_WBITS, memLevel=9, strategy=zlib.Z_DEFAULT_STRATEGY, zdict=dictData)
    compressed_data_with_dict = compress.compress(fileData)
    compressed_data_with_dict += compress.flush()

    # Resultados
    compress_normal = len(compressed_data) 
    compress_dict = len(compressed_data_with_dict)
    compress_gain = compress_normal/compress_dict

    # Write output
    print("File: ", inputFileName , " : ", fileSize)
    print("Dic: ", dictFileName , " : ",  dictSize)
    print("Original: ", fileSize)
    print("Normal: ", compress_normal)
    print("Dict: ", compress_dict)
    print("Gain: ", compress_gain)
    print("")


if __name__ == "__main__":
   main(sys.argv[1:])
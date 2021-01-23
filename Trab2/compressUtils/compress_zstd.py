#!/bin/python3

import sys, getopt, os, secrets
import math

import zstandard as zstd

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
    # dict
    compress = zstd.ZstdCompressor(level=22)
    compressed_dict = compress.compress(dictData)
    # No dict
    compress = zstd.ZstdCompressor(level=22)
    compressed_data = compress.compress(fileData)
    # With dict
    compress = zstd.ZstdCompressor(level=22)
    compressed_data_with_dict = compress.compress(dictData + fileData)

    # Resultados
    compress_normal = len(compressed_data) 
    compress_combined =  len(compressed_data_with_dict) 
    compress_solo =  len(compressed_dict) 
    compress_dict = (len(compressed_data_with_dict) - len(compressed_dict))
    compress_gain = compress_normal/compress_dict

    # Write output
    print("File: ", inputFileName , " : ", fileSize)
    print("Dic: ", dictFileName , " : ",  dictSize)
    print("Original: ", fileSize)
    print("Combined: ", compress_combined)
    print("Solo dict: ", compress_solo)
    print("Normal: ", compress_normal)
    print("Dict: ", compress_dict)
    print("Gain: ", compress_gain)
    print("")


if __name__ == "__main__":
   main(sys.argv[1:])
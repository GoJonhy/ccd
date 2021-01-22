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
    dictSize = os.stat(dictFileName).st_size
    
    # Ler ficheiros
    fileData = inputFile.read(fileSize)
    dictData = dictFile.read(dictSize)

    # Simul
    # dict
    compress = zlib.compressobj()
    compressed_dict = compress.compress(dictData)
    compressed_dict += compress.flush()
    # No dict
    compress = zlib.compressobj()
    compressed_data = compress.compress(fileData)
    compressed_data += compress.flush()
    # With dict
    compress = zlib.compressobj()
    combined = dictData + fileData
    compressed_data_with_dict = compress.compress(combined)
    compressed_data_with_dict += compress.flush()

    # Resultados
    compress_normal = len(compressed_data) 
    compress_combined =  len(compressed_data_with_dict) 
    compress_solo =  len(compressed_dict) 
    compress_dict = len(compressed_data_with_dict) - len(compressed_dict)
    compress_gain = compress_normal/compress_dict

    ratio_normal = fileSize/compress_normal
    ratio_dict = fileSize/compress_dict

    # Write output
    print("File: ", inputFileName , " : ", fileSize)
    print("Dic: ", dictFileName , " : ",  dictSize)
    print("Original: ", fileSize)
    print("Dize Combined: ", len(combined))
    print("Combined: ", compress_combined)
    print("Solo dict: ", compress_solo)
    print("Normal: ", compress_normal)
    print("Dict: ", compress_dict)
    print("Gain: ", compress_gain)
    print("Ratio Normal: ", ratio_normal)
    print("Ratio Dict: ", ratio_dict)
    print("")


if __name__ == "__main__":
   main(sys.argv[1:])
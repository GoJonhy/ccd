#!/bin/python3

import sys, getopt, os, secrets
import math

import zstandard as zstd

# Main 
def main(argv):
    # Leitura de argumentos
    inputFileName = ''
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

    # Obter dados
    inputFile = open(inputFileName, "rb")
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    fileSize = os.stat(inputFileName).st_size
    dictSize = int(size * 1024)

    # Ler ficheiros
    bytes_obj = inputFile.read(fileSize)
    samples = [bytes_obj[i:i+1] for i in range(len(bytes_obj))]

    # dict
    zdict = zstd.train_dictionary(dictSize, samples, level=22)



    # Write output
    stdout.write(zdict)

    stdout.flush()
    stdout.close()


if __name__ == "__main__":
   main(sys.argv[1:])
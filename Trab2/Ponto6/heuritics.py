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

def lerBytes(fileSize,inputFile,byteDict ,seqSize,stdout):
    nextIndex = indexGenerator(fileSize)()
    curByte, nextByte = None, None
    curSeqSize=0
    seq = ''
    while True:
        # Encontrar e escrever primeiro
        index = next(nextIndex)
        inputFile.seek(index)
        curByte = inputFile.read(1)
        outputSize = 0
        # Verifica se Byte existe no dicionario
        
        if (curSeqSize<=seqSize):
            seq+=str(curByte)
            curSeqSize+=1
        else:
            curSeqSize=0
            symbol = byteDict.get(seq)
            if symbol == None:
                byteDict.update([(seq, 1)])
            else:
                symbol += 1
            byteDict.update([(seq, symbol)])

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

# Main 
def main(argv):
    # Leitura de argumentos
    inputFileDir = ''
    size=1
    seqSize=1
    fileSize = int(size * 1024)
    try:
        opts, args = getopt.getopt(argv, "hi:s::", ["ifile", "outsize"])
    except getopt.GetoptError:
        print("fileEntropy.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('fileEntropy.py -i <inputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileDir = arg
        elif opt in ("-s", "--outsize"):
            size = float(arg)

    # Obter dados
    fileList=os.listdir(inputFileDir)
    bytesdict = dict()
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    for file in fileList :
        filePath=inputFileDir+'/'+file
        inputFile = open(filePath, "rb")
        fileSize = os.stat(filePath).st_size
        #fileData = inputFile.read(fileSize)
        lerBytes(fileSize,inputFile,bytesdict,seqSize,stdout)
    


if __name__ == "__main__":
   main(sys.argv[1:])
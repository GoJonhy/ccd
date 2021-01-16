#!/bin/python3

import sys, getopt, os, secrets

# Lança dado
def dado():
    return secrets.randbelow(6)+1

# Main 
def main(argv):
    # Leitura de argumentos
    try:
        opts, args = getopt.getopt(argv, "hn:")
    except getopt.GetoptError:
        print("-n <number>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("-n <number>")
            sys.exit()
        elif opt in ("-n"):
            number = int(arg)

    # Obter ficheiro
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    outputSize = 0

    # Escrita byte a byte
    br = False
    while True:

        val, rep = dado(), dado()

        outputSize += rep

        if( outputSize >= number):
            rep = (outputSize - number)
            br = True

        for i in range(rep):
            stdout.write(val.to_bytes(1, byteorder="big"))
        
        if(br == True):
            break


            
    stdout.flush()
    stdout.close()


if __name__ == "__main__":
   main(sys.argv[1:])
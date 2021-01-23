#!/bin/sh

clear
rm results*.txt

for file in ./files/*
do
  python3 ../../compressUtils/compress_zlib.py -i "$file" -d "files/dict_reduced_lenac_32kiB.txt" >> results_zlib.txt
done

for file in ../files/*
do
  python3 ../../compressUtils/compress_zlib_zdict.py -i "$file" -d "files/dict_reduced_lenac_32kiB.txt" >> results_zlib_zdict.txt
done

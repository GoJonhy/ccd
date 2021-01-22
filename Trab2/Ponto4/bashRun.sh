#!/bin/sh

clear
rm results*.txt

for file in ../Ponto1/files2/*
do
  python3 ../compressUtils/compress_zlib.py -i "$file" -d "./files/dict_reduced_32kiB.txt" >> results_zlib.txt
done

for file in ../Ponto1/files2/*
do
  python3 ../compressUtils/compress_zlib_zdict.py -i "$file" -d "./files/dict_reduced_32kiB.txt" >> results_zlib_zdict.txt
done

for file in ../Ponto1/files2/*
do
  python3 ../compressUtils/compress_lz4.py -i "$file" -d "./files/dict_reduced_32kiB.txt" >> results_lz4.txt
done

for file in ../Ponto1/files2/*
do
  python3 ../compressUtils/compress_zstd.py -i "$file" -d "./files/dict_reduced_32kiB.txt" >> results_zstd.txt
done

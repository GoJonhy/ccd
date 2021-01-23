#!/bin/sh

clear
rm results*.txt

for file in ../Ponto1/files/*
do
  python3 ../compressUtils/compress_zstd_zdict.py -i "$file" -d "./dict/dictionary" >> results_zstd.txt
done

for file in ../Ponto5/input/*
do
  python3 ../compressUtils/compress_zstd_zdict.py -i "$file" -d "./dict/dictionary2" >> results_zstd2.txt
done

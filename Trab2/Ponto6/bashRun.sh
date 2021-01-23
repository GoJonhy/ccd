#!/bin/sh

clear
rm results*.txt

for file in ./inputs/*
do
  python3 ../compressUtils/compress_zlib.py -i "$file" >> results_zlib.txt
done

for file in ./inputs/*
do
  python3 ../compressUtils/compress_zlib_zdict.py -i "$file" >> results_zlib_zdict.txt
done

for file in ./inputs/*
do
  python3 ../compressUtils/compress_lz4.py -i "$file" >> results_lz4.txt
done

for file in ./inputs/*
do
  python3 ../compressUtils/compress_zstd.py -i "$file" >> results_zstd.txt
done

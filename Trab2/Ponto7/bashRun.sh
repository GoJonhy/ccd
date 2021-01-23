#!/bin/sh

clear
rm results*.txt

for file in ./files/enron_mail_inbox/*
do
  python3 ../compressUtils/compress_zlib.py -i "$file" -d "./heuritic_dict.txt" >> results_zlib_enron_mail.txt
done

for file in ./files/enron_mail_inbox/*
do
  python3 ../compressUtils/compress_zlib_zdict.py -i "$file" -d "./heuritic_dict.txt" >> results_zlib_zdict_enron_mail.txt
done

for file in ./files/enron_mail_inbox/*
do
  python3 ../compressUtils/compress_lz4.py -i "$file" -d "./heuritic_dict.txt" >> results_lz4_enron_mail.txt
done

for file in ./files/enron_mail_inbox/*
do
  python3 ../compressUtils/compress_zstd.py -i "$file" -d "./heuritic_dict.txt" >> results_zstd_enron_mail.txt
done

# ----------

for file in ../Ponto1/files/*
do
  python3 ../compressUtils/compress_zlib.py -i "$file" -d "./heuritic_dict.txt" >> results_zlib_Ponto1_files.txt
done

for file in ../Ponto1/files/*
do
  python3 ../compressUtils/compress_zlib_zdict.py -i "$file" -d "./heuritic_dict.txt" >> results_zlib_zdict_Ponto1_files.txt
done

for file in ../Ponto1/files/*
do
  python3 ../compressUtils/compress_lz4.py -i "$file" -d "./heuritic_dict.txt" >> results_lz4_Ponto1_files.txt
done

for file in ../Ponto1/files/*
do
  python3 ../compressUtils/compress_zstd.py -i "$file" -d "./heuritic_dict.txt" >> results_zstd_Ponto1_files.txt
done
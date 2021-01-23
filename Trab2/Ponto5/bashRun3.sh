#!/bin/bash
clear
rm results3/*

python3 ../compressUtils/compress_zlib.py -i "./input/target_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/azores.poi_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/kodim23.png_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/lenac.bmp_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results3/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg3333.txt_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg3333.html_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib.txt

python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/target_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/azores.poi_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/kodim23.png_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/lenac.bmp_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results3/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/pg3333.txt_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/pg3333.html_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zlib_dict.txt

python3 ../compressUtils/compress_lz4.py  -i "./input/target_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/azores.poi_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/kodim23.png_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/lenac.bmp_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results3/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/pg3333.txt_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/pg3333.html_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_lz4.txt

python3 ../compressUtils/compress_zstd.py -i "./input/target_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/azores.poi_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/kodim23.png_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/lenac.bmp_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results3/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/pg3333.txt_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zstd.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg3333.html_1kiB.txt" -d "./dicts/dict_pg1000.txt_32kiB.txt" >> results3/results_zstd.txt


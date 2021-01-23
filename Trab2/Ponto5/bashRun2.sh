#!/bin/bash
clear
rm results2/*



python3 ../compressUtils/compress_zlib.py -i "./input/target_1kiB.txt" -d "./dict2/dict_estimation_32kiB.txt" >> results2/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/azores.poi_1kiB.txt" -d "./dict2/dict_azores.poi_estimation.txt" >> results2/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/kodim23.png_1kiB.txt" -d "./dict2/dict_kodim23.png_estimation.txt" >> results2/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/lenac.bmp_1kiB.txt" -d "./dict2/dict_lenac.bmp_estimation.txt" >> results2/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results2/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg3333.txt_1kiB.txt" -d "./dict2/dict_pg3333.txt_estimation.txt" >> results2/results_zlib.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg3333.html_1kiB.txt" -d "./dict2/dict_pg3333.html_estimation.txt" >> results2/results_zlib.txt

python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/target_1kiB.txt" -d "./dict2/dict_estimation_32kiB.txt" >> results2/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/azores.poi_1kiB.txt" -d "./dict2/dict_azores.poi_estimation.txt" >> results2/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/kodim23.png_1kiB.txt" -d "./dict2/dict_kodim23.png_estimation.txt" >> results2/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/lenac.bmp_1kiB.txt" -d "./dict2/dict_lenac.bmp_estimation.txt" >> results2/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results2/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/pg3333.txt_1kiB.txt" -d "./dict2/dict_pg3333.txt_estimation.txt" >> results2/results_zlib_dict.txt
python3 ../compressUtils/compress_zlib_zdict.py  -i "./input/pg3333.html_1kiB.txt" -d "./dict2/dict_pg3333.html_estimation.txt" >> results2/results_zlib_dict.txt

python3 ../compressUtils/compress_lz4.py  -i "./input/target_1kiB.txt" -d "./dict2/dict_estimation_32kiB.txt" >> results2/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/azores.poi_1kiB.txt" -d "./dict2/dict_azores.poi_estimation.txt" >> results2/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/kodim23.png_1kiB.txt" -d "./dict2/dict_kodim23.png_estimation.txt" >> results2/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/lenac.bmp_1kiB.txt" -d "./dict2/dict_lenac.bmp_estimation.txt" >> results2/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results2/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/pg3333.txt_1kiB.txt" -d "./dict2/dict_pg3333.txt_estimation.txt" >> results2/results_lz4.txt
python3 ../compressUtils/compress_lz4.py  -i "./input/pg3333.html_1kiB.txt" -d "./dict2/dict_pg3333.html_estimation.txt" >> results2/results_lz4.txt

python3 ../compressUtils/compress_zstd.py -i "./input/target_1kiB.txt" -d "./dict2/dict_estimation_32kiB.txt" >> results2/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/azores.poi_1kiB.txt" -d "./dict2/dict_azores.poi_estimation.txt" >> results2/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/kodim23.png_1kiB.txt" -d "./dict2/dict_kodim23.png_estimation.txt" >> results2/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/lenac.bmp_1kiB.txt" -d "./dict2/dict_lenac.bmp_estimation.txt" >> results2/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/pg1000.txt_1kiB.txt" -d "./dict2/dict_pg1000.txt_estimation.txt" >> results2/results_zstd.txt
python3 ../compressUtils/compress_zstd.py -i "./input/pg3333.txt_1kiB.txt" -d "./dict2/dict_pg3333.txt_estimation.txt" >> results2/results_zstd.txt
python3 ../compressUtils/compress_zlib.py -i "./input/pg3333.html_1kiB.txt" -d "./dict2/dict_pg3333.html_estimation.txt" >> results2/results_zstd.txt


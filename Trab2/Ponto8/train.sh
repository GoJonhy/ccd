#!/bin/bash
clear
rm dict/*

python3 ../compressUtils/train_zstd.py -i "./samples/sample.txt" -s32 >> ./dict/dict_samples_max_32kiB.txt

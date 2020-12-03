#!/bin/sh

rm results/*

python3 geradorDados.py -n 716288 >> "results/dados.txt"
zstd -f "results/dados.txt" -o "results/dados.zst" 2>> "results/results.txt"
python3 ../exe1/exercicio1.py -i "results/dados.txt" 1>> "results/results.txt"
python3 ../exe2/exercicio2.py -i "results/dados.txt" 1>> "results/results.txt"

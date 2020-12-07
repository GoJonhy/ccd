#!/bin/sh

rm results/* comp/* comp_results.txt results_ordem1.txt results_ordem2.txt

python3 main.py -p 0 > "results/dados0.txt"
python3 main.py -p 0.1 > "results/dados0.1.txt"
python3 main.py -p 0.2 > "results/dados0.2.txt"
python3 main.py -p 0.4 > "results/dados0.4.txt"
python3 main.py -p 0.6 > "results/dados0.6.txt"
python3 main.py -p 0.8 > "results/dados0.8.txt"
python3 main.py -p 1 > "results/dados1.txt"

for file in results/*
do
  echo "$file"

  my_array=($(echo $file| tr "/" "\n"))
  newfile="comp-${my_array[1]}"

  python3 ../exe1/exercicio1.py -i $file >> "results_ordem1.txt"

  python3 ../exe2/exercicio2.py -i $file >> "results_ordem2.txt"

  zstd -f "$file" -o "comp/$newfile.zst" 2>>  "comp_results.txt"
done
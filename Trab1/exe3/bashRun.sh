#!/bin/sh

rm ordem1/* ordem2/* comp/* results*.txt compOrdem1/* compOrdem2/*


for file in ../files/*
do
  echo "$file"
  my_array=($(echo $file| tr "/" "\n"))
  newfile="estimation-${my_array[2]}"

  python3 estimativaOrdem1.py -i "$file" >> "ordem1/$newfile"
  python3 ../exe1/exercicio1.py -i "ordem1/$newfile" >> "results3_1.txt"

  python3 estimativaOrdem2.py -i "$file" >> "ordem2/$newfile"
  python3 ../exe2/exercicio2.py -i "ordem2/$newfile" >> "results3_2.txt"

  zstd -f "$file" -o "comp/$newfile.zst"
  zstd -f "ordem1/$newfile" -o "compOrdem1/$newfile.zst"
  zstd -f "ordem2/$newfile" -o "compOrdem2/$newfile.zst"

done


#!/bin/bash
clear
rm results/*


for file in ./files/*
do
  my_array=($(echo $file| tr "/" "\n"))
  newfile="${my_array[2]}"

  python3 ../Ponto1/estimativaOrdem2.py -i $file -s1 > "results/${newfile}_1kiB.txt"
done

mv  results/*.txt input

# dict
for file in ./files/*
do
  my_array=($(echo $file| tr "/" "\n"))
  newfile="${my_array[2]}"

  head --bytes 32768 $file > "./dicts/dict_${newfile}_32kiB.txt"
done

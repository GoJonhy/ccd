#!/bin/bash
clear
rm dict2/*


for file in ./files/*
do
  my_array=($(echo $file| tr "/" "\n"))
  newfile="${my_array[2]}"

  python3 ../Ponto1/estimativaOrdem2.py -i $file -s1 > "dict2/dict_${newfile}_estimation.txt"
done

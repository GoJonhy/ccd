#!/bin/sh

rm results1.txt

for file in ../files/*
do
  python3 exercicio1.py -i "$file" >> results1.txt
done

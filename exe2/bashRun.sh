#!/bin/sh

for file in ../files/*
do
  python3 exercicio2.py -i "$file" >> results2.txt
done

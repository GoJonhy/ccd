#!/bin/bash

rm files/*

file="34767-0.txt";

  python3 estimativaOrdem2.py -i $file -s0.1 >> "files/target_0.1kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.2 >> "files/target_0.2kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.3 >> "files/target_0.3kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.4 >> "files/target_0.4kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.5 >> "files/target_0.5kiB.txt"

  python3 estimativaOrdem2.py -i $file -s1 >> "files/target_1kiB.txt"
  python3 estimativaOrdem2.py -i $file -s2 >> "files/target_2kiB.txt"
  python3 estimativaOrdem2.py -i $file -s3 >> "files/target_3kiB.txt"
  python3 estimativaOrdem2.py -i $file -s4 >> "files/target_4kiB.txt"
  python3 estimativaOrdem2.py -i $file -s5 >> "files/target_5kiB.txt" 
  python3 estimativaOrdem2.py -i $file -s6 >> "files/target_6kiB.txt" 

  python3 estimativaOrdem2.py -i $file -s10 >> "files/target_10kiB.txt" 
  python3 estimativaOrdem2.py -i $file -s20 >> "files/target_20kiB.txt" 
  python3 estimativaOrdem2.py -i $file -s32 >> "files/target_32kiB.txt" 


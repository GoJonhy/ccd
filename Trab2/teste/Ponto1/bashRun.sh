#!/bin/bash

rm files/*

file="34767-0.txt";

  python3 estimativaOrdem2.py -i $file -s0.05 >> "files/target_0.05kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.1 >> "files/target_0.1kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.2 >> "files/target_0.2kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.3 >> "files/target_0.3kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.4 >> "files/target_0.4kiB.txt"
  python3 estimativaOrdem2.py -i $file -s0.5 >> "files/target_0.5kiB.txt"
  python3 estimativaOrdem2.py -i $file -s1 >> "files/target_1kiB.txt"


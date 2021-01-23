#!/bin/bash

rm inputs/*

cat  "files/target_0.05kiB.txt" "files/target_0.1kiB.txt" "files/target_0.2kiB.txt" "files/target_0.3kiB.txt" "files/target_0.4kiB.txt" "files/target_0.5kiB.txt" "files/target_1kiB.txt" > "inputs/0.05-1kib.txt"
cat  "files/target_1kiB.txt" "files/target_0.5kiB.txt" "files/target_0.4kiB.txt" "files/target_0.3kiB.txt" "files/target_0.2kiB.txt" "files/target_0.1kiB.txt" "files/target_0.05kiB.txt" > "inputs/1-0.5kib.txt"

# 0.5 0.4 1 0.3 0.2 0.1 0.05
cat  "files/target_0.5kiB.txt" "files/target_0.4kiB.txt" "files/target_1kiB.txt" "files/target_0.3kiB.txt" "files/target_0.2kiB.txt" "files/target_0.1kiB.txt" "files/target_0.05kiB.txt" > "inputs/ordem3.txt"
# 0.5 0.4 1 0.3 0.1 0.05 0.2 
cat  "files/target_0.5kiB.txt" "files/target_0.4kiB.txt" "files/target_1kiB.txt" "files/target_0.3kiB.txt" "files/target_0.1kiB.txt" "files/target_0.05kiB.txt" "files/target_0.2kiB.txt" > "inputs/ordem4.txt"
#  0.4 1 0.3 0.1 0.05 0.2 0.5
cat  "files/target_0.4kiB.txt" "files/target_1kiB.txt" "files/target_0.3kiB.txt" "files/target_0.1kiB.txt" "files/target_0.05kiB.txt" "files/target_0.2kiB.txt" "files/target_0.5kiB.txt"  > "inputs/ordem5.txt"

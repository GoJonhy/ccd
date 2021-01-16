#!/bin/sh

rm  partial/* partial_gzip/* partial_zstd/*


target="../../exe3/ordem1/estimation-34767-0.txt"

cat $target | head -c 71629 > "partial/71629.txt"
cat $target | head -c 179072 > "partial/179072.txt"
cat $target | head -c 358144 > "partial/358144.txt"
cat $target | head -c 537216 > "partial/537216.txt"
cat $target | head -c 716288 > "partial/716288.txt"

for file in partial/*
do
  echo "$file"
  my_array=($(echo $file| tr "/" "\n"))
  newfile="partial_gzip/${my_array[1]}.gz"

  gzip -c -k  "$file" > $newfile

done

cd partial_gzip/
ls -la > results.txt
cd ..

for file in partial/*
do
  echo "$file"
  my_array=($(echo $file| tr "/" "\n"))
  newfile="partial_zstd/${my_array[1]}.zz"

  zstd -f "$file" -o $newfile

done

cd partial_zstd/
ls -la > results.txt
cd ..
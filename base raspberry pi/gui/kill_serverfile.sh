#!/bin/sh
s=$(ps -ef | grep servertosend.py) 

echo $s
y=0 

sub=" " 

y=$(expr index "$s" "$sub")

a=$y
#echo $a
i=0 
z="" 
c=" " 

for a in $s 
do
 #echo $a
 i=` expr $i + 1 `
 #echo $i
 if [ $i -eq 2 ] ;
 then
  echo $a
  z=$a
 fi done
#echo 1
echo $z 


sudo kill $z

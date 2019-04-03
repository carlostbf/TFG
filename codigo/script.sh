#!/bin/bash
for i in {1..5}	
do	
	for j in {1..34}
	do
	  echo -n "$i," >> modelo_MOVISTAR.csv
	done
	echo $i >> modelo_MOVISTAR.csv
done
printf "fasta\tline_1\tline_2\tfourfold_sites\tfourfold_diff\n" > fourfold.txt
for i in *.fa; do 
	python fourfold_anynumber.py $i >> fourfold.txt
done

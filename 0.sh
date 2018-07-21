for i in {1..3};do
	for j in {1..9};do
		a="2018 "$i" "$j" "
		b="2018 0"$i" 0"$j" "
		echo $b
		sed -i "s/$a/$b/g" yang.txt
	done
done


for m in {1..9};do
	t="2017 12 "$m" "
	q="2017 12 0"$m" "
	sed -i "s/$t/$q/g" yang.txt
done

for m in {1..9};do
	t="2017 11 "$m" "
	q="2017 11 0"$m" "
	sed -i "s/$t/$q/g" yang.txt
done

for m in {1..3};do
	k="2018 "$m" "
	p="2018 0"$m" "
	sed -i "s/$k/$p/g" yang.txt
done

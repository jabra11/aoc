for i in *.py
do 
    in=in/$(ls $i | rg -o "\d\d").txt
    day=${i%.py}
    printf "%s:\n%s\n\n" $day $(python3 $i $in)
done;

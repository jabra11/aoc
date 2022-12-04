for i in *.py
do 
    printf "%s:\n%s\n\n" ${i%.py} $(python3 $i "in/$(ls $i | rg -o "\d\d").txt");
done;

for i in *.py
do 
    printf "running %s" "python3 $i in/$(ls $i | rg -o "\d\d").txt"
    printf "%s:\n%s\n\n" ${i%.py} "$(python3 $i "in/$(ls $i | rg -o "\d\d").txt")";
done;

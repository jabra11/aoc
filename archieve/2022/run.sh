for i in *.py
do 
    python3 $i in/$(ls $i | rg -o "\d\d").txt;
done;

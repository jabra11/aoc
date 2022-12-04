day=$@
year="2022"

if [[ "$day" == "" ]]
then
    echo "enter the day (1-25)!"
    exit
fi

cookie=$AOCCOOK
url="https://adventofcode.com/$year/day/$day/input"

day_pretty=$(printf %02d $day)
out="in/$day_pretty.txt"

cookie_censored=$(printf $cookie | cut -c1-8)'...'

printf "fetching input from %s with cookie %s\n" $url $cookie_censored

input=$(curl -sfb "session="$cookie $url)
if [[ $? -eq 0 ]]
then
    echo "writing input to $out"
    echo "$input" > $out
else
    printf "failed to fetch input!\n"
    exit
fi

arch="archieve/$year/in/$day_pretty.txt"
if [[ ! -f $arch ]]; then
    echo "copying to ${arch%$day_pretty.txt}"
    cp $out $arch
fi
echo "done"

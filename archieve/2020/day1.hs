part1 = do
    inputs <- lines <$> readFile "../etc/data.txt"
    let nums = map read inputs :: [Int]
    let result = head [a*b | a <- nums, b <- nums, a+b == 2020]
    print result
    

part2 = do
    inputs <- lines <$> readFile "../etc/data.txt"
    let nums = map read inputs :: [Int]
    let result = head [a*b*c | a <- nums, b <- nums, c <- nums, a+b+c == 2020]
    print result

main :: IO ()
main = do
    part1
    part2

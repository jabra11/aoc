def is_valid(cur, n):
    return n - cur >= 1 and n - cur <= 3

def get_paths(graph, node, cache):
    if len(graph[node]) < 1:
        return 1

    if node not in cache:
        ctr = 0
        for i in graph[node]:
            ctr += get_paths(graph, i, cache)

        cache[node] = ctr
    return cache[node]
    
    
def solve(ratings, head):
    i = len(ratings)-1
    m = {}
    while i >= 0:
        if not ratings[i] in m:
            m[ratings[i]] = []
            for j in range(1,4):
                if ratings[i] - j in ratings:
                    m[ratings[i]].append(ratings[i] - j)
        i -= 1

    for key in m:
        print("{}: {}".format(key, m[key]))

    cache = {}
    return get_paths(m, head,cache)



def main():
    ratings = []
    ratings.append(0)
    for i in open('etc/data.txt').read().splitlines():
        ratings.append(int(i))

    ratings.append(max(ratings)+3)
    ratings = sorted(ratings)

    print(solve(ratings, max(ratings)))

    

main()

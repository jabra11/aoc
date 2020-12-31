#include <bits/stdc++.h>
#include <fmt/format.h>

using i64 = std::int64_t;
using u64 = std::uint64_t;

std::vector<std::string> get_input()
{
    auto file = std::ifstream("../etc/data.txt");

    auto res = std::vector<std::string>();

    std::string tmp;
    while (std::getline(file, tmp))
    {
        res.push_back(tmp);
    }
    return res;
}

int main()
{
}

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

struct bagnet
{
    std::string bag;
    uint64_t count;
    uint64_t multiplier = 1;
};

int main()
{
    auto rules = get_input();
    auto graph = std::map<std::string, std::vector<bagnet>>();

    for (std::string_view rule : rules) 
    {
        auto ins = std::vector<bagnet>();

        auto split_point = rule.find(" contain ");
        auto main = rule.substr(0, split_point);
        auto inside = rule.substr(split_point+9);
        main = main.substr(0, main.find(" bags"));

        if (inside == "no other bags.")
        {
            graph.insert(std::make_pair(main, std::vector<bagnet>()));
            continue; 
        }
        inside = inside.substr(0, inside.size()-1);
        auto pos = 0ULL;

        bool keep = true;
        while (keep)
        {
            auto tmp = inside.find(", ", pos);
            if (tmp == std::string::npos)
                keep = false;

            auto s = inside.substr(pos, tmp-pos);

            auto num = std::stoll(std::string(s.substr(0, s.find_first_of(' ', 1))));
            s = s.substr(s.find_first_of(' ', 1)+1);

            if (auto pos = s.find(" bags"); pos != std::string::npos)
            {
                s = s.substr(0, pos);
            }
            else
            {
                s = s.substr(0, s.find(" bag"));
            }

            ins.push_back(bagnet{std::string(s), static_cast<uint64_t>(num)});
            pos = tmp+2;
        }

        graph.insert(std::make_pair(main, ins));
    }

    std::uint64_t total = 0;
    auto s = std::stack<bagnet>();
    s.push({"shiny gold", 1, 1});

    while (!s.empty())
    {
        auto cur = s.top();
        s.pop();
        auto childs = graph[cur.bag];

        for (auto& c : childs)
        {
            total += cur.multiplier * c.count;
            c.multiplier = cur.multiplier * c.count;
            s.push(c);
        }
    }

    fmt::print("total = {}\n", total);
}

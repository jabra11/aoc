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
    auto rules = get_input();
    auto graph = std::multimap<std::string, std::vector<std::string>>();

    for (std::string_view rule : rules) 
    {
        auto end_pos = rule.find("contain"); 
        auto primary = std::string(rule.substr(0, end_pos-2));
        auto secondaries = std::vector<std::string>();

        if (rule.find("no") != std::string::npos)
        {
            graph.insert(std::make_pair(primary, secondaries));
            continue;
        }

        auto start_pos = rule.find_first_of(' ', end_pos);
        start_pos = rule.find_first_of(' ', start_pos);

        while (true) 
        {
            end_pos = rule.find_first_of(',', start_pos+1);
            if (end_pos == std::string::npos)
            {
                start_pos = rule.find_first_of(' ', start_pos+1);
                auto last = rule.substr(start_pos+1, rule.size());

                if (last[last.size()-2] == 's')
                    last = last.substr(0, last.size()-2);
                else
                    last = last.substr(0, last.size()-1);

                secondaries.emplace_back(last);
                break;
            }
            else
            {
                auto current = rule.substr(start_pos+1, end_pos-start_pos-1);
                if (current[current.size()-1] == 's')
                    current = current.substr(0, current.size()-1);

                current = current.substr(current.find_first_of(' ', 1));
                current = current.substr(1);
                fmt::print("current = {}\n", current);

                secondaries.emplace_back(current);
                start_pos = end_pos+1;
            }
        }
        graph.insert(std::make_pair(primary, secondaries));
    }

    auto parents = std::set<std::string>();
    parents.insert("shiny gold bag");

    std::uint64_t ctr=1;
    for (auto& i : graph)
    {
        fmt::print("{}. {}\n", ctr++, i.first);
        fmt::print("childs : ");
        for (auto& s : i.second)
            fmt::print("{}, ", s);

        std::cout << '\n';
    }

    while (true)
    {
        ctr = parents.size();
        for (auto& i : graph)
        {
            for (auto& j : parents)
            {
                auto found = std::find(i.second.begin(), i.second.end(), j);
                if (found != i.second.end())
                {
                    if (!parents.contains(i.first))
                    {
                        parents.insert(i.first);
                        fmt::print("found {}th parent: {} -> {}\n", 
                                    parents.size()-1, i.first, j);
                    }
                }
            }
        }
        if (parents.size() == ctr)
        {
            fmt::print("found {} parents\n", parents.size()-1);
            return 0;
        }
    }
}

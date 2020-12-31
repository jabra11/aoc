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
        auto end_pos = rule.find("contain"); 
        auto primary = std::string(rule.substr(0, end_pos-2));
        auto secondaries = std::vector<bagnet>();

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
                auto last = rule.substr(start_pos+1, rule.size());

                if (last[last.size()-2] == 's')
                    last = last.substr(0, last.size()-2);
                else
                    last = last.substr(0, last.size()-1);

                std::uint64_t number = std::stoi(std::string(last.substr(0, last.find_first_of(' ', 1))));
                last = last.substr(last.find_first_of(' ', 1));
                last = last.substr(1);

                //fmt::print("last = {}, amount = {}\n", last, number);


                secondaries.push_back({std::string(last), number});
                break;
            }
            else
            {
                auto current = rule.substr(start_pos+1, end_pos-start_pos-1);
                if (current[current.size()-1] == 's')
                    current = current.substr(0, current.size()-1);

                std::uint64_t number = std::stoi(std::string(current.substr(0, current.find_first_of(' ', 1))));

                current = current.substr(current.find_first_of(' ', 1));
                current = current.substr(1);

                //fmt::print("current = {}, amount = {}\n", current, number);

                secondaries.push_back({std::string(current), number});
                start_pos = end_pos+1;
            }
        }
        graph.insert(std::make_pair(primary, secondaries));
    }

    std::uint64_t total = 0;
    
    auto s = std::stack<bagnet>();
    s.push({"shiny gold bag", 1, 1});

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

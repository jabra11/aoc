cmake_minimum_required(VERSION 3.16)
project(aoc)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(src
    src/1.cpp
    #src/2.cpp
    #src/3.cpp
    #src/4.cpp
    #src/4.cpp
    #src/5.cpp
    #src/6.cpp
    #src/7.cpp
    #src/8.cpp
    #src/9.cpp
    )


find_package(benchmark REQUIRED)
find_package(fmt REQUIRED)

add_executable(aoc ${src})

target_link_libraries(aoc
                    benchmark::benchmark
                    fmt::fmt
                    )

if (${CMAKE_BUILD_TYPE} STREQUAL "Debug")
    target_precompile_headers(aoc PUBLIC /usr/include/c++/12.2.0/x86_64-pc-linux-gnu/bits/stdc++.h)
endif()

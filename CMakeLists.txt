cmake_minimum_required(VERSION 3.20)

project(txtDesk VERSION 0.1.0 LANGUAGES CXX)

option(TXTDESK_BUILD_TESTS "Build txtDesk tests" ON)

add_executable(txtdesk
    src/main.cc
)

target_compile_features(txtdesk PRIVATE cxx_std_20)
target_include_directories(txtdesk PRIVATE
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
)

if(CMAKE_CXX_COMPILER_ID MATCHES "Clang|GNU")
    target_compile_options(txtdesk PRIVATE -Wall -Wextra -Wpedantic)
elseif(MSVC)
    target_compile_options(txtdesk PRIVATE /W4)
endif()

if(TXTDESK_BUILD_TESTS)
    include(CTest)
endif()

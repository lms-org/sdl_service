cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCES
    "src/sdl_service.cpp"
    "src/interface.cpp"
)

set(HEADERS
    "include/sdl_service/sdl_service.h"
)

#set compiler flags
if((${CMAKE_CXX_COMPILER_ID} STREQUAL "Clang") OR (${CMAKE_CXX_COMPILER_ID} STREQUAL "GNU"))
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra -Wreturn-type -Wpedantic ")
endif()

include_directories(include)
add_library(sdl_service SHARED ${SOURCES} ${HEADERS})
target_link_libraries(sdl_service PRIVATE ${CONAN_LIBS})

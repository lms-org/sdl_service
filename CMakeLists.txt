set(SOURCES
    "src/sdl_service.cpp"
    "src/interface.cpp"
)

set(HEADERS
    "include/sdl_service/sdl_service.h"
)

include_directories(
        include
        /usr/local/include
)
add_library(sdl_service SHARED ${SOURCES} ${HEADERS})
target_link_libraries(sdl_service PRIVATE lmscore SDL2)

#include "sdl_service/sdl_service.h"

namespace sdl_service {

bool SdlService::init() {
    // Initialize SDL2 Video subsystem
    if(SDL_Init(SDL_INIT_VIDEO | SDL_INIT_NOPARACHUTE) != 0) {
        logger.error("SDL_init") << SDL_GetError();
        return false;
    }

    return true;
}

void SdlService::destroy() {
    SDL_Quit();
}

} // namespace sdl_service

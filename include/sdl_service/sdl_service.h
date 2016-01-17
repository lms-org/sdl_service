#ifndef SDL_SERVICE_H
#define SDL_SERVICE_H

#include <SDL2/SDL.h>
#include <lms/service.h>

namespace sdl_service {

/**
 * @brief LMS service sdl_service
 **/
class SdlService : public lms::Service {
public:
    bool init() override;
    void destroy() override;
};

} // namespace sdl_service

#endif // SDL_SERVICE_H

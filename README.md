# sdl_service
Initializes the Video subsystem of SDL2. This service must be enabled when
[sdl_image_renderer](https://github.com/lms-org/sdl_image_renderer) is used.

## Dependencies
- SDL2

### Ubuntu
```
sudo apt-get install libsdl2-2.0-0 libsdl2-dev
```

### OS X (Homebrew)
```
brew install sdl2
```

## XML Config

```xml
<service>
    <name>sdl_service</name>
</service>
```


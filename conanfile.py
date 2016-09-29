from conans import ConanFile, CMake

class SdlServiceConan(ConanFile):
    name = "lms_sdl_service"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    exports = "src/*","include/*","CMakeLists.txt","README.md"
    requires = "SDL2_image/2.0.1@lasote/stable","lms/2.0@lms/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include",src="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")
        self.copy("*.so", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["lms_sdl_service"]
        self.copy("*.so",dst="bin")

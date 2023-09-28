from conans import ConanFile, CMake

class ConanProduct(ConanFile):
    name = "cppfront_cmake"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "txt" 
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    default_user = "local"
    default_channel = "testing"
    scm = {
        "type": "git",
        "url": "https://github.com/goszpeti/cppfront_cmake.git",
        "revision": "004ffc50b408939dbda9d2eadeb647e1461589d0",
        "verify_ssl": False, 
        "submodule": "recursive"
    }
    
    def configure(self):
        return super().configure()

    def build_requirements(self):
        self.tool_requires("cmake/3.27.5")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = str(self.settings.build_type).upper()
        cmake.definitions["CMAKE_CXX_STANDARD"] = str(self.settings.compiler.cppstd)
        cmake.configure()
        cmake.build()
        cmake.install()

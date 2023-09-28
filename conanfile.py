import os
import sys
from pathlib import Path

from conans import ConanFile, CMake, tools
# from conan import tools
class ConanProduct(ConanFile):
    name = "gclp"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "txt" 
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    default_user = "local"
    default_channel = "testing"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }
    
    def configure(self):
        return super().configure()

    def build_requirements(self):
        self.tool_requires("cmake/3.27.5")
        self.tool_requires("cppfront_cmake/0.1.0@local/testing")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = str(self.settings.build_type).upper()
        cmake.definitions["CMAKE_CXX_STANDARD"] = str(self.settings.compiler.cppstd)
        # --warn-uninitialized
        cmake.configure()
        cmake.build()
        cmake.install()

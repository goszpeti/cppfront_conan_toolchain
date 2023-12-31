

cmake_minimum_required(VERSION 3.23.0 FATAL_ERROR)

# Disable extensions here and require the chosen CMAKE_CXX_STANDARD (coming from Conan)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPERIMENTAL_CXX_MODULE_CMAKE_API aa1f7df0-828a-4fcd-9afc-2dc80491aca7)

if(NOT DEFINED CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 17)
endif()

# Use shared libraries from current directory on Linux (same behavior as on Windows)
SET(CMAKE_INSTALL_RPATH "$ORIGIN")

project(GCLP VERSION 0.1.0)

# check for conan
message(STATUS "Including Conan build info")

if(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
elseif(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/../conanbuildinfo.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/../conanbuildinfo.cmake)
elseif(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo_multi.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo_multi.cmake)
elseif(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/../conanbuildinfo_multi.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/../conanbuildinfo_multi.cmake)
else()
    message(FATAL_ERROR "Conan build info can't be found.")
endif()

set(gtest_search_mode CONFIG)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

if(CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
    # enable multicore compilation
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /MP")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP")
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
    # compile with /Z7 to avoid pdb generation and integrate debug symbols
    string(REGEX REPLACE "/Z[iI7]" "" CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /Z7")
    string(REGEX REPLACE "/Z[iI7]" "" CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
    set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO} /Z7")

    string(REGEX REPLACE "/Z[iI7]" "" CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG}")
    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /Z7")
    string(REGEX REPLACE "/Z[iI7]" "" CMAKE_C_FLAGS_RELWITHDEBINFO "${CMAKE_C_FLAGS_RELWITHDEBINFO}")
    set(CMAKE_C_FLAGS_RELWITHDEBINFO "${CMAKE_C_FLAGS_RELWITHDEBINFO} /Z7")
endif()

# Enable project folder structure for Visual Studio IDE
set_property(GLOBAL PROPERTY USE_FOLDERS true)

# some settings need to be set explicitly for QNX
if(UNIX)
    set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
    set(CMAKE_INSTALL_RPATH_USE_LINK_PATH ON)
    set(CMAKE_SKIP_BUILD_RPATH OFF)
endif(UNIX)

add_subdirectory(src)
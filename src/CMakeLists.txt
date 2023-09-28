find_package(cppfront REQUIRED)

add_executable(conan_explorer)

target_sources(conan_explorer
    PUBLIC
    main.cpp2
    utils.h2
)

install(TARGETS conan_explorer)

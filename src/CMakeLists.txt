find_package(cppfront REQUIRED)

add_executable(conan_explorer)

target_sources(conan_explorer
    PUBLIC
    main.cpp2
    utils.h2
)

# target_sources(main
#   PUBLIC
#     FILE_SET all_my_modules TYPE CXX_MODULES FILES
#     #BASE_DIRS ${CMAKE_BINARY_DIR}/_cppfront 
#     utils.mpp
# )

# target_link_libraries(main PRIVATE utils)

install(TARGETS conan_explorer)

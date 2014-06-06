cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

set( CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR} )
find_package(LIBVLC REQUIRED)

set(SOURCE_FILE_LIST src/foo.c)

include_directories( ${LIBVLC_INCLUDE_DIR} )

add_library(foo_plugin SHARED
  # EXCLUDE_FROM_ALL
  ${SOURCE_FILE_LIST})

message("LIBVLCCORE_LIBRARY ${LIBVLCCORE_LIBRARY}")
message("LIBVLC_LIBRARY ${LIBVLC_LIBRARY}")

target_link_libraries(foo_plugin ${LIBVLC_LIBRARY} ${LIBVLCCORE_LIBRARY})

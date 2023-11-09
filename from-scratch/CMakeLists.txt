cmake_minimum_required(VERSION 3.13)

include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)
set(PICO_PLATFORM rp2040)
set(PICO_BOARD pico_w)

set(CMAKE_C_COMPILER arm-none-eabi-gcc)
#set(CMAKE_FIND_ROOT_PATH )
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
#set(CMAKE_FIND_ROOT_PATH )

project(blink_steve C CXX ASM)
pico_sdk_init()

add_executable(blink_steve
        blink_steve.c
        )

target_link_libraries(blink_steve
        pico_stdlib              # for core functionality
        pico_cyw43_arch_none     # we need Wifi to access the GPIO, but we don't need anything else
        )

# create map/bin/hex file etc.
pico_add_extra_outputs(blink_steve)

# add url via pico_set_program_url
pico_set_program_url(blink_steve "https://ste.vework.org/picow_blink_has_no_content_and_doesnt_exist")

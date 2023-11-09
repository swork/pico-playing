#! /bin/sh

PICO_SDK_PATH=${PICO_SDK_PATH:-/Users/steve/Code/pico/pico-sdk}
export PICO_SDK_PATH

cd `dirname $0`
rm -rf build
cmake -S . -B build
make -C build
echo "\nBuild products in `pwd`:"
ls -lt build


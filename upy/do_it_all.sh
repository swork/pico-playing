#! /bin/sh

cat <<EOF
1. Install mpremote (pip install mpremote, maybe in a venv)
2. Get a micropython, like from https://micropython.org/download/?mcu=rp2040
3. Do the USB/BOOTSEL thing to install that micropython .uf2; wait 5s
4. mpremote cp blinkie.py :main.py

Building uPy from source was no big deal, so do that to know what
is actually running.

Potholes abound. Don't make assumptions. Consider just writing straight
to the metal in C.
EOF

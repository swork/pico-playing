/**
 * Copyright (c) 2022 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"

const unsigned short saahcsb_on[] =  { 200, 100, 100, 200, 250, 200, 200 };
const unsigned short saahcsb_off[] = {  50,  25,  25,  50, 250,  50, 800 };
const unsigned char cycle_len = sizeof(saahcsb_on) / sizeof(saahcsb_on[0]);

int main() {
    stdio_init_all();
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed");
        return -1;
    }
    while (true) {
        for (int i=0; i<cycle_len; ++i) {
            cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
            sleep_ms(saahcsb_on[i]);
            cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
            sleep_ms(saahcsb_off[i]);
        }
    }
}

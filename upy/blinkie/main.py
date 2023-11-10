from machine import Pin, Timer, lightsleep

instance = None  # placeholder, see below

def tick(timer):
    global instance
    idx = (instance.n // 2) % len(instance.gvr_on)
    if instance.n % 2:
        instance.led.off()
        timer.init(period=instance.gvr_off[idx],
                   mode=Timer.ONE_SHOT,
                   callback=tick)
    else:
        instance.led.on()
        timer.init(period=instance.gvr_on[idx],
                   mode=Timer.ONE_SHOT,
                   callback=tick)
    instance.n += 1
    if instance.n >= len(instance.gvr_on) * 2:
        instance.n = 0

class Guido_von_Rossum_on_a_pin():
    gvr_on  = [ 175, 150, 150, 125, 150, ]
    gvr_off = [  25, 100,  50,  25, 800, ]

    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        self.n = 0
        self.timer = Timer()

def start():
    global instance
    tick(instance.timer)

def stop():
    global instance
    instance.timer.deinit()

# special string "LED" is GPIO_25 on Pico, but arranges to
# twiddle the cyw's WL_GPIO_0 on Pico_W
instance = Guido_von_Rossum_on_a_pin("LED")

if __name__ == '__main__':
    start()

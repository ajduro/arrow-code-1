led.enable(True)

def on_forever():
    led.plot(2, 0)
    led.plot(2, 1)
    led.plot(2, 2)
    led.plot(2, 3)
    led.plot(2, 4)
    led.plot(1, 3)
    led.plot(0, 2)
    led.plot(3, 3)
    led.plot(4, 2)
basic.forever(on_forever)

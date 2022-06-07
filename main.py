def on_button_pressed_a():
    global roll
    roll = randint(0, 5)
    counts[roll] = counts[roll] + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    counts[0] = 0
    counts[1] = 0
    counts[2] = 0
    counts[3] = 0
    counts[4] = 0
    counts[5] = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

roll = 0
counts: List[number] = []
counts = [0, 0, 0, 0, 0, 0]

def on_forever():
    led.plot(0, counts[0]-1)
    led.plot(1, counts[1]-1)
    led.plot(2, counts[2]-1)
    led.plot(3, counts[3]-1)
    led.plot(4, counts[4]-1)
    led.plot(5, counts[5]-1)
basic.forever(on_forever)

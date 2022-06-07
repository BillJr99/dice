input.onButtonPressed(Button.A, function () {
    roll = randint(0, 5)
    counts[roll] = counts[roll] + 1
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    counts[0] = 0
    counts[1] = 0
    counts[2] = 0
    counts[3] = 0
    counts[4] = 0
    counts[5] = 0
})
let roll = 0
let counts: number[] = []
counts = [
0,
0,
0,
0,
0,
0
]
basic.forever(function () {
    led.plot(0, counts[0] - 1)
    led.plot(1, counts[1] - 1)
    led.plot(2, counts[2] - 1)
    led.plot(3, counts[3] - 1)
    led.plot(4, counts[4] - 1)
    led.plot(5, counts[5] - 1)
})

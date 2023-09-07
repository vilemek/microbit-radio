radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 99) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            `)
        radio.sendNumber(98)
    }
    if (receivedNumber == 98) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            . . . . .
            `)
        radio.sendNumber(100)
    }
    if (receivedNumber == 100) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.A, function () {
    letter += 1
    basic.showString(convertToText(letter))
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("" + convertToText(letter))
    letter = 0
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
	
})
let letter = 0
radio.setGroup(1)
radio.sendNumber(99)

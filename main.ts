radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (ready == 0) {
        if (receivedNumber == 99) {
            led.plot(4, 1)
            radio.sendNumber(98)
        }
        
        if (receivedNumber == 98) {
            led.plot(4, 2)
            radio.sendNumber(100)
        }
        
        if (receivedNumber == 100) {
            led.plot(4, 3)
            basic.pause(1000)
            basic.clearScreen()
            radio.sendNumber(100)
            ready = 1
        }
        
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (pos == 0) {
        if (letter0 <= 90) {
            basic.clearScreen()
            letter0 += 1
            basic.showString(String.fromCharCode(letter0))
        } else {
            letter0 = 64
        }
        
    } else if (pos == 1) {
        if (letter1 <= 90) {
            basic.clearScreen()
            letter1 += 1
            basic.showString(String.fromCharCode(letter1))
        } else {
            letter1 = 64
        }
        
    } else if (pos == 2) {
        if (letter2 <= 90) {
            basic.clearScreen()
            letter2 += 1
            basic.showString(String.fromCharCode(letter2))
        } else {
            letter2 = 64
        }
        
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString(String.fromCharCode(letter0) + String.fromCharCode(letter1) + String.fromCharCode(letter2))
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (pos < 16) {
        pos += 1
        basic.clearScreen()
    } else {
        pos = 0
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (letter0 == 64) {
        letter0 = lettern
    }
    
    if (letter1 == 64) {
        letter1 = lettern
    }
    
    if (letter2 == 64) {
        letter2 = lettern
    }
    
    radio.sendString(String.fromCharCode(letter0) + String.fromCharCode(letter1) + String.fromCharCode(letter2))
})
let pos = 0
let ready = 0
led.plot(4, 0)
radio.setGroup(1)
radio.sendNumber(99)
let lettern = 32
let letter0 = 64
let letter1 = 64
let letter2 = 64
let letter3 = 64
let letter4 = 64
let letter5 = 64
let letter6 = 64
let letter7 = 64
let letter8 = 64
let letter9 = 64
let letterA = 64
let letterB = 64
let letterC = 64
let letterD = 64
let letterE = 64
let letterF = 64

def on_received_number(receivedNumber):
    global ready
    if ready == 0:
        if receivedNumber == 99:
            led.plot(4, 1)
            radio.send_number(98)
        if receivedNumber == 98:
            led.plot(4, 2)
            radio.send_number(100)
        if receivedNumber == 100:
            led.plot(4, 3)
            basic.pause(1000)
            basic.clear_screen()
            radio.send_number(100)
            ready = 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global letter0, letter1, letter2, letter3, letter4, letter5, letter6, letter7, letter8, letter9, letterA, letterB, letterC, letterD, letterE, letterF
    if pos == 0:
        if letter0 <= 90:
            basic.clear_screen()
            letter0 += 1
            basic.show_string(String.from_char_code(letter0))
        else:
            letter0 = 64
    elif pos == 1:
        if letter1 <= 90:
            basic.clear_screen()
            letter1 += 1
            basic.show_string(String.from_char_code(letter1))
        else:
            letter1 = 64
    elif pos == 2:
        if letter2 <= 90:
            basic.clear_screen()
            letter2 += 1
            basic.show_string(String.from_char_code(letter2))
        else:
            letter2 = 64
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string(String.from_char_code(letter0) + String.from_char_code(letter1) + String.from_char_code(letter2))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global pos
    if pos < 16:
        pos += 1
        basic.clear_screen()
    else:
        pos = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global letter0, letter1, letter2, letter3, letter4, letter5, letter6, letter7, letter8, letter9, letterA, letterB, letterC, letterD, letterE, letterF
    if letter0 == 64:
        letter0 = lettern
    if letter1 == 64:
        letter1 = lettern
    if letter2 == 64:
        letter2 = lettern
    radio.send_string((String.from_char_code(letter0)) + (String.from_char_code(letter1)) + (String.from_char_code(letter2)))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

pos = 0
ready = 0
led.plot(4, 0)
radio.set_group(1)
radio.send_number(99)
lettern = 32
letter0 = 64
letter1 = 64
letter2 = 64
letter3 = 64
letter4 = 64
letter5 = 64
letter6 = 64
letter7 = 64
letter8 = 64
letter9 = 64
letterA = 64
letterB = 64
letterC = 64
letterD = 64
letterE = 64
letterF = 64
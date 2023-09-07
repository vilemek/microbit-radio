def on_received_number(receivedNumber):
    global ready
    if ready == 0:
        if receivedNumber == 99:
            led.plot(4, 1)
            radio.send_number(98)
        if receivedNumber == 98:
            led.plot(4,2)
            radio.send_number(100)
        if receivedNumber == 100:
            led.plot(4,3)
            basic.pause(1000)
            basic.clear_screen()
            radio.send_number(100)
            ready = 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global letter0
    if pos == 0:
        if letter0 <= 90:
            basic.clear_screen()
            letter0 += 1
            basic.show_string(String.from_char_code(letter0))
        else:
            letter0 = 64
    else if pos == 1:
        if letter1 <= 90:
            basic.clear_screen()
            letter1 += 1
            basic.show_string(String.from_char_code(letter1))
        else:
            letter1 = 64
    else if 
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string(String.from_char_code(letter0))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global pos
    if pos < 16:
        pos += 1
    else:
        pos = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if letter0 == 64:
        letter0 = 32
    if letter1 == 64:
        letter1 = 32
    if letter2 == 64:
        letter2 = 32
    if letter3 == 64:
        letter3 = 32
    if letter4 == 64:
        letter4 == 32
    if letter5 == 64:
        letter5 == 32
    if letter6 == 64:
        letter6 == 32
    if letter7 == 64:
        letter7 == 32
    if letter8 == 64:
        letter8 = 32
    if letter9 == 64:
        letter9 = 32
    if letterA == 64:
        letterA = 32
    if letterB == 64:
        letterB = 32
    if letterC == 64:
        letterC = 32
    if letterD == 64:
        letterD = 32
    if letterE == 64:
        letterE = 32
    if letterF == 64:
        letterF = 32


    radio.send_string(String.from_char_code(letter0))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

pos = 0
ready = 0
led.plot(4, 0)
radio.set_group(1)
radio.send_number(99)
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
ready = 0
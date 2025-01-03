# #klavye

# import serial
# import keyboard

# arduino_port = 'COM7'
# baud_rate = 9600

# ser = serial.Serial(arduino_port, baud_rate)

# while True:
#     gelen_veri = ser.readline().decode('utf-8').strip()  # Gelen veriyi oku

#     if gelen_veri == "sag":
#         keyboard.release('a')
#         keyboard.release('w')
#         keyboard.press('d')
#         print("Sağa dön")
#     elif gelen_veri == "sol":
#         keyboard.release('d')
#         keyboard.release('w')
#         keyboard.press('a')
#         print("Sola dön")
#     elif gelen_veri == "ileri":
#         keyboard.release('a')
#         keyboard.release('d')
#         keyboard.press('w')
#     else:
#         keyboard.release('a')
#         keyboard.release('d')
#         keyboard.release('w')
#         print("serbest")

#joystick

import serial
import vgamepad as vg
import time

arduino_port = 'COM7'
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

gamepad = vg.VX360Gamepad()

i = 0

while True:
    gelen_veri = ser.readline().decode('utf-8').strip()

    if gelen_veri == "sag":
        gamepad.left_joystick(x_value=150767, y_value=0)
        gamepad.update()
        print("Sağa dön")
    elif gelen_veri == "sol":
        gamepad.left_joystick(x_value=-150767, y_value=0) 
        gamepad.update()
        print("Sola dön")
    elif gelen_veri == "ileri":
        gamepad.left_joystick(x_value=0, y_value=0)
        gamepad.update()
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
        time.sleep(0.5)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
        print("İleri git")
    else:
        gamepad.left_joystick(x_value=0, y_value=0)
        gamepad.update()

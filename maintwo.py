import serial
import vgamepad as vg
import time

arduino_port = 'COM7'
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

gamepad = vg.VX360Gamepad()

max_value = 200767 
scale_factor = 20000 

while True:
    try:
        gelen_veri = ser.readline().decode('utf-8').strip()
        if gelen_veri.isdigit() or (gelen_veri.startswith('-') and gelen_veri[1:].isdigit()):
            ivme_x = int(gelen_veri)
            joystick_x = int((ivme_x / scale_factor) * max_value)
            gamepad.left_joystick(x_value=joystick_x, y_value=0)
            gamepad.update()
            
            print(f"X Eksen Değeri: {ivme_x}, Joystick X: {joystick_x}")

        if gelen_veri == "0":
            gamepad.left_joystick(x_value=0, y_value=0)
            gamepad.update()
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.5)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            print("İleri git")
    except ValueError:
        print(f"Hata!: {gelen_veri}")

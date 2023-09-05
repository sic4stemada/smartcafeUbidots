from __future__ import division
import time
import Adafruit_PCA9685
import requests

# Inisialisasi PCA9685 menggunakan alamat default (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Atur frekuensi PWM ke 60Hz (baik untuk servos).
pwm.set_pwm_freq(60)

TOKEN = "BBFF-dsPG7gaq7lQdbxAJaYApcnIxbTEVHh"
DEVICE_LABEL = "motodc"
VARIABLE_LABEL = "meja1"

def get_button_status():
    url = "https://industrial.api.ubidots.com/api/v1.6/devices/motodc/meja1/"
    headers = {"X-Auth-Token": TOKEN}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["last_value"]["value"]

# Configure min dan max servo pulse lengths
servo_min = 150  # Panjang pulsa minimum (0 derajat)
servo_max = 600  # Panjang pulsa maksimum (180 derajat)

# Menghitung panjang pulsa untuk 60 derajat
target_degrees = 60
target_pulse = int(servo_min + (target_degrees / 180.0 * (servo_max - servo_min)))

print('Moving servo on channel 0...')
try:
    while True:
        button_status = get_button_status()

        print("Button Status:", button_status)
        
        if button_status == 1:
            time.sleep(4)
            pwm.set_pwm(12, 0, target_pulse)
            time.sleep(1)
            pwm.set_pwm(12, 0, servo_min)
            time.sleep(1)
            
            time.sleep(6)
            pwm.set_pwm(8, 0, target_pulse)
            time.sleep(1)
            pwm.set_pwm(8, 0, servo_min)
            time.sleep(1)
            
            time.sleep(9)
            pwm.set_pwm(4, 0, target_pulse)
            time.sleep(1)
            pwm.set_pwm(4, 0, servo_min)
            time.sleep(1)
            
            time.sleep(12)
            pwm.set_pwm(2, 0, target_pulse)
            time.sleep(1)
            pwm.set_pwm(2, 0, servo_min)
            time.sleep(1)

            
        elif button_status == 0:
            pwm.set_pwm(0, 0, servo_min)
            time.sleep(1)
except KeyboardInterrupt:
    # Tangani jika pengguna menekan Ctrl-C
    pwm.set_pwm(0, 0, 0)  # Pastikan servo dimatikan sebelum keluar

# Bersihkan GPIO saat selesai
pwm.set_pwm(0, 0, 0)

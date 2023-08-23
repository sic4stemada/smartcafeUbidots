import RPi.GPIO as GPIO
import time
import requests

# Konfigurasi pin motor DC
servoPIN = 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

# Fungsi untuk menggerakkan motor maju
p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(2.5)

TOKEN = "BBFF-dsPG7gaq7lQdbxAJaYApcnIxbTEVHh"
DEVICE_LABEL = "motodc"
VARIABLE_LABEL = "servo1"  # Ganti dengan variabel tombol yang sudah Anda buat di Ubidots

def get_button_status():
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{VARIABLE_LABEL}/"
    headers = {"X-Auth-Token": TOKEN}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["last_value"]["value"]

try:
    while True:
        button_status = get_button_status()
        print("Button Status:", button_status)
        
        if button_status == 1:
            p.ChangeDutyCycle(5)
            time.sleep(2)
            p.ChangeDutyCycle(8)
            time.sleep(2)
            p.ChangeDutyCycle(5)
            time.sleep(2)
        elif button_status == 0:
            time.sleep(1)  # Menghentikan motor jika tombol off

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

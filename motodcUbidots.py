import RPi.GPIO as GPIO
import time 
import requests

# Konfigurasi pin motor DC
in1 = 23
in2 = 24
en = 25

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

# Fungsi untuk menggerakkan motor maju
def motor_maju():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

# Fungsi untuk menggerakkan motor mundur
def motor_mundur():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

# Fungsi untuk menghentikan motor
def motor_berhenti():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

# Mengatur PWM
p = GPIO.PWM(en, 20)
p.start(25)

TOKEN = "BBFF-dsPG7gaq7lQdbxAJaYApcnIxbTEVHh"
DEVICE_LABEL = "motodc"
VARIABLE_LABEL = "meja1"  # Variabel tombol yang sudah Anda buat

 # Time delay for stopping

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
            time.sleep(1)
            motor_maju()
            print("bubuk 1")
            time.sleep(1)
            motor_berhenti()
            print("mandek 1")
            time.sleep(3)

            motor_maju()
            print("air")
            time.sleep(1)
            motor_berhenti()
            print("mandek 2")
            time.sleep(5)

            motor_maju()
            print("toping")
            time.sleep(1)
            motor_berhenti()
            print("mandek 3")
            time.sleep(2)

        elif button_status == 0:
            motor_berhenti()
            print("berhenti")

            #mundur 

             #motor_mundur()
             #print("bubuk 1")
             #time.sleep(1)
             #motor_berhenti()
             #print("mandek 1")
             #time.sleep(2)

             #motor_mundur()
             #print("air")
             #time.sleep(1)
             #motor_berhenti()
             #print("mandek 2")
             #time.sleep(2)

             #motor_mundur()
             #print("toping")
             #time.sleep(1)
             #motor_berhenti()
             #print("mandek 3")
             #time.sleep(3)

            # motor_maju()
            # time.sleep(1)


            # motor_maju()
            # print("kopi 2")
            # time.sleep(1)
            # motor_berhenti
            # time.sleep(1)
            # motor_mundur()
            # print("mundur")
            # time.sleep(1)
            # motor_maju()
            # print("kopi 2")
            # time.sleep(1)
            # motor_berhenti()
            # print("air")
            # time.sleep(5)

            # motor_mundur()
            # print("mundur banyu")
            # time.sleep(1)
            # motor_berhenti()
            # print("air")
            # time.sleep(5)

            # motor_maju()
            # print("kopi 1")
            # time.sleep(2)
            # motor_mundur()
            # print("mundur banyu")
            # time.sleep(1)
            # motor_berhenti()
            # print("air")
            # time.sleep(5)

            # motor_maju()
            # print("kopi 1")
            # time.sleep(1)
            # motor_mundur()
            # print("mundur banyu")
            # time.sleep(1)
            # motor_berhenti()
            # print("air")
            # time.sleep(5)

            # motor_maju()
            # print("toping")
            # time.sleep(3)
            # motor_berhenti()
            # print("meja 1")
            # time.sleep(2)

except KeyboardInterrupt:
    p.stop()
    print("udah")
    GPIO.cleanup()

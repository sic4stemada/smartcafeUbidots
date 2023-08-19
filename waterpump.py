import RPi.GPIO as GPIO
import time

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
pump_pin = 18  # Ganti dengan nomor pin GPIO yang Anda gunakan
GPIO.setup(pump_pin, GPIO.OUT)


# Hidupkan pompa air
GPIO.output(pump_pin, GPIO.HIGH)
print("Pompa air dihidupkan.")
time.sleep(20)  # Atur berapa lama pompa harus dihidupkan

# Matikan pompa air
GPIO.output(pump_pin, GPIO.LOW)
print("Pompa air dimatikan.")

# Bersihkan GPIO saat selesai
GPIO.cleanup()
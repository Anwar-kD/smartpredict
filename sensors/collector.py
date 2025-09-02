import random
import time

def read_temperature():
    # Simule la lecture d’un capteur de température
    return round(20 + random.uniform(-2, 2), 2)

def read_humidity():
    # Simule la lecture d’un capteur d’humidité
    return round(50 + random.uniform(-5, 5), 2)

if __name__ == "__main__":
    while True:
        temp = read_temperature()
        hum = read_humidity()
        print(f"Temp: {temp}°C | Humidity: {hum}%")
        time.sleep(5)

import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB0', 115200)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        print(decoded_bytes)
        with open("test_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),decoded_bytes])
    except KeyboardInterrupt:
        print("File writing canceled")
        break
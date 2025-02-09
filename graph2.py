import serial
import time
import csv

# Serial port settings (update COM port accordingly)
ser = serial.Serial('COM10', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

# Open CSV file
filename = "Accelerometer_data.csv"
with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "X", "Y", "Z"])  # Header

    while True:
        try:
            line = ser.readline().decode().strip()
            if line:
                data = line.split(",")
                timestamp = time.strftime("%Y%m%d%H%M%S")  # Formatted timestamp
                writer.writerow([timestamp] + data)
                print(f"Data logged: {timestamp}, {data}")
        except KeyboardInterrupt:
            print("Data collection stopped.")
            break
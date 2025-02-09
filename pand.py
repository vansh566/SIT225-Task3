import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Load CSV File (Update filename if needed)
df = pd.read_csv("Accelerometer_data.csv")

# 🔹 If Timestamp column is missing, create a time index
df['Timestamp'] = pd.RangeIndex(start=0, stop=len(df), step=1)

# 🔹 Plot acceleration data
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['X'], label="X-axis Acceleration", color="red")
plt.plot(df['Timestamp'], df['Y'], label="Y-axis Acceleration", color="green")
plt.plot(df['Timestamp'], df['Z'], label="Z-axis Acceleration", color="blue")

# 🔹 Customize Graph
plt.xlabel("Data Point Index (Simulated Time)")
plt.ylabel("Acceleration (g)")
plt.title("Accelerometer Data Over Time")
plt.legend()
plt.grid()
plt.show()
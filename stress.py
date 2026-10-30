import os
import time

print("--- STARTING QA STRESS TEST ---")
time.sleep(1)

for i in range(1, 11):
    filename = f"report_{i}.txt"

    with open(filename, "w") as file:
        file.write(f"Sistem status: OK. Log nunber {i}\n")
    print(f"Generated: {filename}")
    time.sleep(0.3)
print("--- STRESS TEST FINISHED SUCCESSFULLY ---")


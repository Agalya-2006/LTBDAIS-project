import urllib.request
import urllib.parse
import time
import random

THINGSPEAK_WRITE_KEY = "NTRW0FX2XWO0WXRN"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

CYCLE_SECONDS = 24

def send_to_thingspeak(current, voltage, frequency, power_factor):
    params = {
        "api_key": THINGSPEAK_WRITE_KEY,
        "field1": current,
        "field2": voltage,
        "field3": frequency,
        "field4": power_factor,
    }
    url = THINGSPEAK_URL + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            body = response.read().decode("utf-8")
            return body  # ThingSpeak returns the entry number, or "0" if it failed
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

def normal_reading():
    return (
        round(random.uniform(70, 95), 2),
        round(random.uniform(225, 235), 2),
        round(random.uniform(49.8, 50.2), 2),
        round(random.uniform(0.88, 0.96), 2),
    )

def rain_reading():
    return (
        round(random.uniform(55, 70), 2),
        round(random.uniform(150, 170), 2),
        round(random.uniform(49.2, 49.7), 2),
        round(random.uniform(0.60, 0.70), 2),
    )

def tree_fall_reading():
    return (
        round(random.uniform(2, 8), 2),
        round(random.uniform(100, 125), 2),
        round(random.uniform(49.5, 50.0), 2),
        round(random.uniform(0.45, 0.55), 2),
    )

def overload_reading():
    return (
        round(random.uniform(150, 199), 2),
        round(random.uniform(160, 180), 2),
        round(random.uniform(49.5, 50.0), 2),
        round(random.uniform(0.60, 0.70), 2),
    )

phases = [
    ("NORMAL", normal_reading, CYCLE_SECONDS),
    ("RAIN FAULT", rain_reading, CYCLE_SECONDS),
    ("NORMAL", normal_reading, CYCLE_SECONDS),
    ("TREE FALL", tree_fall_reading, CYCLE_SECONDS),
    ("NORMAL", normal_reading, CYCLE_SECONDS),
    ("OVERLOAD", overload_reading, CYCLE_SECONDS),
]

print("=" * 50)
print("LTBDAIS Cloud Sensor Simulator (ThingSpeak)")
print("Sending readings to ThingSpeak every 16 seconds")
print("(ThingSpeak free tier limit: 1 update per 15 sec)")
print("Press CTRL+C to stop")
print("=" * 50)

phase_index = 0

try:
    while True:
        phase_name, reading_fn, duration = phases[phase_index % len(phases)]
        print(f"\n--- Phase: {phase_name} ---")
        elapsed = 0
        while elapsed < duration:
            current, voltage, frequency, power_factor = reading_fn()
            result = send_to_thingspeak(current, voltage, frequency, power_factor)
            print(f"[{phase_name}] current={current}, voltage={voltage} -> ThingSpeak entry: {result}")
            time.sleep(16)
            elapsed += 16
        phase_index += 1
except KeyboardInterrupt:
    print("\nSimulator stopped.")
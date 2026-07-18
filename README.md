# LTBDAIS — LT Line Break Detection and Auto Isolation System

SIH 2025 project built for KSEBL (Kerala State Electricity Board) under Disaster Management theme.

---

## What this project does

When a power line breaks due to rain, tree fall, or overload, this system detects it automatically and isolates the affected line — without anyone manually switching it off.

---

## How it works

1. ESP32 reads current and voltage from real sensors every 16 seconds
2. Data is sent to ThingSpeak cloud via WiFi
3. Spring Boot backend reads the cloud data automatically
4. Machine learning model identifies the fault type
5. Affected line is isolated and an email alert is sent
6. Dashboard shows live fault status

---

## Tech used

- React (frontend dashboard)
- Spring Boot Java (backend)
- Python Flask + RandomForest (ML model)
- MySQL (database)
- ThingSpeak (cloud)
- ESP32 + ACS712 + ZMPT101B (hardware)

---

## Fault types detected

- Rain → voltage drops → VOLTAGE_SAG
- Tree fall → current drops to zero → LINE_BREAK
- Overload → current too high → OVERLOAD

---

## Hardware setup

- ESP32 WROOM 38 pin board
- ACS712 5A current sensor (GPIO 36)
- ZMPT101B voltage sensor (GPIO 39)
- Relay module for auto isolation
- LED and buzzer for visual/audio alert

---

## How to run

**Backend:**
cd ltbdais-backend/ltbdais-backend
mvnw spring-boot:run

**ML service:**
cd ltbdais-ml
python app.py

**Frontend:**
cd ltbdais-frontend
npm install
npm run dev

Open `localhost:5173` in browser.

---

## About

Developed by Agalya M
ECE, VSB Engineering College, Karur
Batch 2024–2028

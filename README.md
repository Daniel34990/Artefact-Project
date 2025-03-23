# 🚗 Smart Remote Car with Automatic QR Code Navigation

Welcome to the **Smart Remote Car** project!  
This repository contains the code, system design, and documentation for a hybrid remote-controlled and autonomous vehicle that navigates using QR code markers.

---

## 🎯 Project Goals

This project was developed to build a smart car capable of:

- 🕹️ Manual control through a wireless remote interface
- 🤖 Autonomous driving mode using QR code recognition
- 🔍 Real-time QR code detection and interpretation
- 🧠 Driving decisions based on dynamic QR marker data
- 📊 QR data logging and analysis for behavior tracking

---

## 🧱 System Architecture

### 🔩 Hardware Components

- **Microcontroller**: Raspberry Pi (or compatible board)
- **Camera module**: For QR code scanning (OpenCV-compatible)
- **Motor drivers + DC motors**: For movement control
- **Chassis**: Thin wooden board custom-cut to fit the Pi and mount components
- **Wireless module**: For remote control via browser or mobile
- **Aruco markers & mounts**: For tracking and scene awareness  
---

### 💻 Software Stack

- 📷 **QR Code detection** using OpenCV (`cv2`)
- 🧭 **Path planning** and decision-making logic (Python)
- 🌐 **Web interface** for manual control (HTML/CSS/JavaScript)
- 📡 **Socket communication** for real-time commands

---

## 📹 Demo Video

📽️ **Project Demonstration**  

![Smart Remote Car Demo](./README-src/ProjectVideo.gif)


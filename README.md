# CompTIA Network+ Study Suite & Subnetting Toolkit

A standalone, GUI-based Python study and calculation suite built with standard `tkinter`. Designed to prepare students for the CompTIA Network+ certification exam through interactive summaries, progressive flashcard drills, an exam simulator, a searchable glossary, and a dedicated hand-calculation subnetting engine.

---

## Features

### 1. Core Study Suite (`network_study_beginner.py` - Build 1.2.1)
* **10 Comprehensive Chapter Modules:** Covers the OSI & TCP/IP stack, common & uncommon port numbers, cabling & infrastructure hardware, IPv4/IPv6 architecture, core network services (DNS, DHCP, NTP), CompTIA 7-step troubleshooting, wireless standards (802.11a/b/g/n/ac/ax) & security (WPA3/SAE), virtualization & cloud models (IaaS/PaaS/SaaS), network defense-in-depth, and operational management (SNMPv3, Syslog, disaster recovery).
* **Binary Leading-Bit Rule:** Integrates the binary derivation method for Class A–E network boundaries into Chapter 4.
* **Interactive Flashcard Engine:** Built-in 60-question flashcard bank (5–6 per chapter) with automated reshuffling, a progress tracker (`Card X of Y`), and visual completion alerts.
* **Exam Simulator:** Practice mode supporting both a 20-question randomized quick quiz and a 50-question full exam simulation with instant scoring, feedback, and answer explanations.
* **Searchable Glossary:** 35+ core terms and acronyms with instant live filtering and a dedicated definition viewer.
* **Theme Support:** One-click toggle between Dark Mode and Light Mode.

### 2. Ultimate Subnetting Calculator (`ultimate_subnet_calc.py` - Build 1.0.1)
* **Core Details & Binary Breakdown:** Analyzes any IPv4 address and CIDR prefix (e.g., `192.168.1.50/26`), outputting IP class, network type (RFC 1918 private, public, APIPA, loopback), wildcard mask, usable host range, and full 32-bit padded binary strings.
* **Subnet Slicer / Generator:** Divides any parent network into smaller subnets with an interactive table displaying Network IDs, host ranges, and broadcast addresses.
* **Hand Calculations Tab:** Step-by-step educational breakdown demonstrating the CompTIA "Magic Number" (Block Size) method, identifying the interesting octet, multiples, and broadcast calculation.
* **Theme Support:** Full Dark Mode and Light Mode styling across all widgets, tables, and text frames.

---

## Requirements

* **Python 3.8+**
* **Tkinter** (included with standard Python installations on Windows and macOS; install via `sudo pacman -S tk` on Arch Linux or `sudo apt install python3-tk` on Debian/Ubuntu).
* No third-party pip dependencies required.

---

## Usage

### Run the Study Suite
```bash
python3 network_study_beginner.py

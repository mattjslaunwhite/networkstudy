# CompTIA Network+ Study Suite

A standalone, GUI-based Python study application built with standard `tkinter`. Designed to prepare students for the CompTIA Network+ certification exam through interactive chapter summaries, progressive flashcard drills, an exam simulator, and a searchable glossary.

---

## Features

* **10 Comprehensive Chapter Modules:** Covers the OSI & TCP/IP stack, common & uncommon port numbers, cabling & infrastructure hardware, IPv4/IPv6 architecture, core network services (DNS, DHCP, NTP), CompTIA 7-step troubleshooting, wireless standards (802.11a/b/g/n/ac/ax) & security (WPA3/SAE), virtualization & cloud models (IaaS/PaaS/SaaS), network defense-in-depth, and operational management (SNMPv3, Syslog, disaster recovery).
* **Binary Leading-Bit Rule:** Integrates the binary derivation method for Class A–E network boundaries into Chapter 4.
* **Interactive Flashcard Engine:** Built-in 60-question flashcard bank (5–6 per chapter) with automated reshuffling, a progress tracker (`Card X of Y`), and visual completion alerts.
* **Exam Simulator:** Practice mode supporting both a 20-question randomized quick quiz and a 50-question full exam simulation with instant scoring, feedback, and answer explanations.
* **Searchable Glossary:** 35+ core terms and acronyms with instant live filtering and a dedicated definition viewer.
* **Theme Support:** One-click toggle between Dark Mode and Light Mode.

---

## Requirements

* **Python 3.8+**
* **Tkinter** (included with standard Python installations on Windows and macOS; install via `sudo pacman -S tk` on Arch Linux or `sudo apt install python3-tk` on Debian/Ubuntu).
* No third-party pip dependencies required.

---

## Usage

```bash
python3 network_study_beginner.py

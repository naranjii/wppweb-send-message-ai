# 🤖 wppweb-send-message-ai

[![License](https://img.shields.io/github/license/naranjii/wppweb-send-message-ai?style=flat-square)](https://github.com/naranjii/wppweb-send-message-ai/blob/main/LICENSE)
[![Issues](https://img.shields.io/github/issues/naranjii/wppweb-send-message-ai?style=flat-square)](https://github.com/naranjii/wppweb-send-message-ai/issues)
[![Last Commit](https://img.shields.io/github/last-commit/naranjii/wppweb-send-message-ai?style=flat-square)](https://github.com/naranjii/wppweb-send-message-ai/commits)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=flat-square)

---

## 📦 About

**`wppweb-send-message-ai`** is a lightweight automation tool written in Python using **Selenium** to send messages through WhatsApp Web.

---

## ✅ Current Features

- 🟢 Send WhatsApp messages through automated browser
- 🧪 Simple architecture, ready for integration with AI message sources, content array, et.
- 🔁 Can be looped or scheduled via external tools (e.g., `cron`, `schedule`, or tray GUIs*)
- 📂 Clean and extendable module structure

---

## 🔜 *Planned Features

- 🚀 Connect to a local Ollama-based API for AI-generated content
- 🧠 Serve messages from agents with memory/context
- 🔒 Improve headless support and session persistence
- ⏰ Native scheduling via config file or backend service

---

## ⚙️ Installation & Usage

```bash
git clone https://github.com/naranjii/wppweb-send-message-ai.git
cd wppweb-send-message-ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

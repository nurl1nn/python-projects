# QR Code Generator 🔳

A simple command-line tool that generates QR codes for URLs, WiFi networks, and vCards (contacts).

## Features

- 🌐 **URL** — Generate a QR code for any website link
- 📶 **WiFi** — Generate a scannable WiFi QR code (no password typing needed)
- 👤 **vCard** — Generate a contact QR code (name, phone, email)

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library

Install dependencies:

```bash
pip install qrcode[pil]
```

## How to Run

```bash
python qr_code_generator.py
```

## How to Use

1. Run the script
2. Choose what you want to create: `wifi` / `url` / `vcard`
3. Enter the required information
4. The QR code is saved as a `.png` file in the same directory

## Example

```
What do you want to create? wifi/url/vCard
wifi
Add your wifi name: MyNetwork
Add your password: 12345678
```

Scan the generated QR code with your phone — it will connect automatically!

## Supported Types

| Type  | What it does |
|-------|-------------|
| URL   | Opens a website when scanned |
| WiFi  | Connects to WiFi automatically when scanned |
| vCard | Adds a contact to your phone when scanned |

## Author
Nurlan — [github.com/nurl1nn](https://github.com/nurl1nn)

# NyxInjector v1.2
Advanced XSS, Shadow Injection & RAT Framework by Yashbhardwaj0101

## Features
- Multiple XSS & Shadow DOM payloads
- AI Payload Optimizer
- Built-in RAT Generator
- Auto-Exploitation mode

## Installation
```bash
git clone https://github.com/Yashbhardwaj0101/NyxInjector.git
cd NyxInjector
pip3 install requests
#usage
python3 nyx_injector.py --help
python3 nyx_injector.py -t https://target.com/search --auto --optimize
python3 nyx_injector.py --rat

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Now install freely
pip install requests

# Run your script
python3 nyx_injector.py

# Deactivate 
## add some new
python3 nyx_injector.py -t https://target.com --full-takeover
python3 nyx_injector.py -t https://target.com --all

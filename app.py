#!/usr/bin/env python3
import os
import subprocess
import sys

# Ensure npm in PATH (Windows Conda fix)
os.environ['PATH'] = os.environ.get('PATH', '') + os.pathsep + os.path.join(sys.executable, '..', 'Library', 'bin')

print("n8n launching via Node...")
try:
    subprocess.call(["n8n", "start"], cwd=os.path.dirname(__file__))
except FileNotFoundError:
    print("n8n not found—reinstall via npm.")
    subprocess.call(["npm", "install", "-g", "n8n"])
    subprocess.call(["n8n", "start"], cwd=os.path.dirname(__file__))

from flask import Flask
import sys
import os

# Add the parent directory to the path to import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

# This is the entry point for Vercel
# Vercel will automatically detect this as a Flask app
if __name__ == "__main__":
    app.run()
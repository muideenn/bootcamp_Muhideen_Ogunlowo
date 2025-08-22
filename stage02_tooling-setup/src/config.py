from pathlib import Path
from dotenv import load_dotenv
import os

def load_env(dotenv_path: str = ".env"):
    load_dotenv(dotenv_path)

def get_key(name: str, default=None):
    return os.getenv(name, default)
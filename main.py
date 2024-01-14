# main.py
import sys
import os

# Add generators to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'generators'))

from generators.file_creator import create_300_files

if __name__ == "__main__":
    create_300_files()

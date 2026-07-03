"""
EcoTwin AI - Main Entry Point
This module initializes the platform and serves as the primary execution script.
"""

import sys
import os

# Ensure the src directory is in the system path for absolute imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """
    Main function to initialize and run the EcoTwin AI platform.
    """
    print("==================================================")
    print("              Welcome to EcoTwin AI               ")
    print(" An Intelligent Digital Twin for Sustainable Cities")
    print("==================================================")
    print("\nSystem Initialization successful.")
    print("All core modules will be orchestrated from here.")

if __name__ == "__main__":
    main()
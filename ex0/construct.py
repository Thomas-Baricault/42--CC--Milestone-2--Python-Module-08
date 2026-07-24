import os
import site
import sys

if __name__ == "__main__":
    if sys.prefix == getattr(sys, "base_prefix", sys.prefix):
        print("MATRIX STATUS: You're still plugged in")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate   # On Windows")
        print()
        print("Then run this program again")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])

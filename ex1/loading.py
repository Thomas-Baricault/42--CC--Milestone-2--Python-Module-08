from importlib import import_module

if __name__ == "__main__":
    print()
    print("OPERATOR STATUS: Loading programs...")
    print()

    print("Checking dependencies:")
    all_ok = True
    for pkg, usage in [
        ("pandas", "Data manipulation"),
        ("requests", "Network access"),
        ("matplotlib", "Visualization"),
        ("numpy", "Data manipulation")
    ]:
        try:
            version = getattr(import_module(pkg), "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {usage} ready")
        except ImportError:
            all_ok = False
            print(f"[KO] Missing {pkg} - Install it with 'pip install {pkg}'")
    print()

    if all_ok is False:
        print("Please install all required dependencies individually or run",
              "'pip install -r requirements.txt'")
    else:
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd

        print("Analyzing Matrix data...")
        n = 1000
        data = pd.DataFrame(np.random.uniform(-1, 1, size=(n, 2)),
                            columns=["x", "y"])

        print(f"Processing {n} data points...")
        plt.scatter(data["x"], data["y"])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Random 2D points")

        print("Generating visualization...")
        path = "matrix_analysis.png"
        plt.savefig(path)
        print()

        print("Analysis complete!")
        print(f"Results saved to: {path}")

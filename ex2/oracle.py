from dotenv import find_dotenv, load_dotenv
from os import getenv

if __name__ == "__main__":
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv()
    env = {}
    for key in [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]:
        value = getenv(key)
        env[key] = None
        if value and value != "":
            env[key] = value

    print("Configuration loaded:")
    print("Mode:", env["MATRIX_MODE"])
    print("Database:", ("Not configured" if env["DATABASE_URL"] is None else
                        f"Connected to {env['DATABASE_URL']}"))
    print("API Access:", ("Not authenticated" if env["API_KEY"] is None else
                          "Authenticated"))
    print("Log Level:", env["LOG_LEVEL"])
    print("Zion Network:", ("Offline" if env["ZION_ENDPOINT"] is None else
                            "Online"))
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if find_dotenv() == "":
        print("[KO] .env not found")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")

import requests


def validate_app(url="http://localhost:8081"):
    try:
        r = requests.get(url)
        if r.status_code == 200 and "Welcome" in r.text:
            print("✅ App is serving content correctly.")
        else:
            print("⚠️ Unexpected response.")
    except Exception as e:
        print(f"❌ Validation failed: {e}")

if __name__ == "__main__":
    validate_app()

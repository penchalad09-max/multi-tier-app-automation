import requests


def validate_app(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and "App is running" in response.text:
            print("✅ App is serving content correctly.")
        else:
            print("⚠️ Unexpected response.")
    except Exception as e:
        print(f"❌ Validation failed: {e}")


if __name__ == "__main__":
    validate_app("http://localhost:8081")

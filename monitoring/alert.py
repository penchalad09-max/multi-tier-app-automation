import psutil
import datetime

LOG_FILE = "system_alerts.log"

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def check_cpu(threshold=80):
    usage = psutil.cpu_percent(interval=1)
    if usage > threshold:
        log_message(f"⚠️ High CPU usage detected: {usage}%")
    else:
        log_message(f"✅ CPU usage normal: {usage}%")

def check_memory(threshold=80):
    usage = psutil.virtual_memory().percent
    if usage > threshold:
        log_message(f"⚠️ High Memory usage detected: {usage}%")
    else:
        log_message(f"✅ Memory usage normal: {usage}%")

def check_disk(threshold=80):
    usage = psutil.disk_usage('/').percent
    if usage > threshold:
        log_message(f"⚠️ High Disk usage detected: {usage}%")
    else:
        log_message(f"✅ Disk usage normal: {usage}%")

if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk()

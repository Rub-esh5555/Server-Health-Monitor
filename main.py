import psutil
import time
import os
import platform
from datetime import datetime
import logging


os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_server_health():

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage(os.getcwd())

    return cpu, memory, disk


def display_server_health():

    while True:

        os.system("cls" if os.name == "nt" else "clear")

        cpu, memory, disk = get_server_health()

        print("=" * 50)
        print("       SERVER HEALTH MONITORING SYSTEM")
        print("=" * 50)

        print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        print("Operating System:", platform.system())

        print("CPU Usage:", cpu, "%")

        print("RAM Usage:", memory.percent, "%")

        print("Disk Usage:", disk.percent, "%")


        logging.info(f"CPU Usage: {cpu}%")

        logging.info(f"RAM Usage: {memory.percent}%")

        logging.info(f"Disk Usage: {disk.percent}%")


        print("-" * 50)

        print("SERVER STATUS")

        if cpu >= 80:
            print("WARNING: High CPU Usage!")
            logging.warning("High CPU Usage detected!")
        else:
            print("CPU Status: Normal")

        if memory.percent >= 80:
            print("WARNING: High RAM Usage!")
            logging.warning("High RAM Usage detected!")
        else:
            print("RAM Status: Normal")

        if disk.percent >= 90:
            print("WARNING: Low Disk Space!")
            logging.warning("Low Disk Space detected!")
        else:
            print("Disk Status: Normal")

        print("=" * 50)

        time.sleep(2)


if __name__ == "__main__":

    try:
        display_server_health()

    except KeyboardInterrupt:
        print("\nMonitoring stopped successfully.")
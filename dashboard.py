
import streamlit as st
import psutil
import time
import platform
from datetime import datetime

st.set_page_config(
    page_title="Server Health Monitor",
    page_icon="🖥️",
    layout="wide"
)

st.title("🖥️ Server Health Monitoring System")
st.write("Real-time system health monitoring dashboard")

st.sidebar.header("Monitoring Settings")
refresh_time = st.sidebar.slider(
    "Refresh interval (seconds)",
    min_value=2,
    max_value=10,
    value=3
)

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk_path = "C:\\" if platform.system() == "Windows" else "/"
disk = psutil.disk_usage(disk_path)

st.subheader("System Overview")
st.caption("Last updated: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{cpu}%")

with col2:
    st.metric("RAM Usage", f"{memory.percent}%")

with col3:
    st.metric("Disk Usage", f"{disk.percent}%")

st.divider()
st.subheader("Server Status")

if cpu >= 80:
    st.error("⚠️ High CPU Usage!")
else:
    st.success("✅ CPU Status: Normal")

if memory.percent >= 80:
    st.error("⚠️ High RAM Usage!")
else:
    st.success("✅ RAM Status: Normal")

if disk.percent >= 90:
    st.error("⚠️ Low Disk Space!")
else:
    st.success("✅ Disk Status: Normal")

st.divider()
st.subheader("System Information")
st.write("CPU Cores:", psutil.cpu_count())
st.write("Total RAM:", round(memory.total / (1024**3), 2), "GB")
st.write("Total Disk:", round(disk.total / (1024**3), 2), "GB")

if st.button("Refresh Dashboard"):
    st.rerun()

st.caption("Developed using Python, Streamlit and psutil")
time.sleep(refresh_time)
st.rerun()
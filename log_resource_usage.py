import psutil

# 현재 CPU 사용량 및 메모리 사용량을 출력
def log_resource_usage(step):
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    print(f"[{step}] CPU Usage: {cpu_percent}%")
    print(f"[{step}] Memory Usage: {memory_info.percent}% ({memory_info.used / (1024 ** 2):.2f} MiB / {memory_info.total / (1024 ** 2):.2f} MiB)\n")

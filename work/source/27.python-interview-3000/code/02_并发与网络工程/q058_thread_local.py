import threading
import time

local_data = threading.local()


def worker(name: str) -> None:
    local_data.value = name  # 每个线程写自己的副本
    time.sleep(0.1)
    print(f"{threading.current_thread().name} 读到自己的 value: {local_data.value}")


if __name__ == "__main__":
    threads = [threading.Thread(target=worker, args=(f"worker-{i}",)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

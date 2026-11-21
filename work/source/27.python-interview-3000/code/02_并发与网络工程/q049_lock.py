import threading

counter = 0
N_THREADS = 8
N_INCR = 100_000


def unsafe_increment() -> None:
    global counter
    for _ in range(N_INCR):
        counter += 1  # 非原子: 读-加-写


lock = threading.Lock()


def safe_increment() -> None:
    global counter
    for _ in range(N_INCR):
        with lock:
            counter += 1


if __name__ == "__main__":
    threads = [threading.Thread(target=unsafe_increment) for _ in range(N_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("无锁结果(通常小于期望值):", counter)

    counter = 0
    threads = [threading.Thread(target=safe_increment) for _ in range(N_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("加锁结果:", counter)

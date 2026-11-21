import threading

results: list[int] = []
lock = threading.Lock()


def append_is_atomic() -> None:
    for i in range(10_000):
        results.append(i)  # list.append 原子, 无锁也安全


counter = 0


def compound_not_atomic() -> None:
    global counter
    for _ in range(10_000):
        counter += 1  # 复合操作, 有竞态


if __name__ == "__main__":
    threads = [threading.Thread(target=append_is_atomic) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("append 无锁结果:", len(results), "(正确)")

    threads = [threading.Thread(target=compound_not_atomic) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("+= 无锁结果:", counter, "(期望 40000, 可能偏小)")

import random
import threading
import time


def run_system(locked: bool, seconds: float = 0.5) -> int:
    accounts = {"a": 100000, "b": 100000}
    lock = threading.Lock()
    violations = [0]

    def check_invariant() -> None:
        while not stop.is_set():
            if locked:
                with lock:
                    total = accounts["a"] + accounts["b"]
            else:
                total = accounts["a"] + accounts["b"]  # 无锁读可能撕裂
            if total != 200000:
                violations[0] += 1
            time.sleep(0.001)

    def mover() -> None:
        rng = random.Random(threading.get_ident())
        while not stop.is_set():
            amount = rng.randint(1, 50)
            if locked:
                with lock:
                    accounts["a"] -= amount
                    accounts["b"] += amount
            else:
                # 无锁: 读-改-写被 GIL 切换打散, 总额读数漂移
                a = accounts["a"]
                if a >= amount:
                    accounts["a"] = a - amount
                    accounts["b"] += amount

    stop = threading.Event()
    checker = threading.Thread(target=check_invariant)
    movers = [threading.Thread(target=mover) for _ in range(4)]
    checker.start()
    for m in movers:
        m.start()
    time.sleep(seconds)
    stop.set()
    checker.join()
    for m in movers:
        m.join()
    return violations[0]


if __name__ == "__main__":
    bad = run_system(locked=False)
    good = run_system(locked=True)
    print(f"无锁版本: 检测到 {bad} 次不变量破坏")
    print(f"加锁版本: 检测到 {good} 次不变量破坏")
    assert good == 0

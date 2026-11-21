import threading

class Config:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:            # 第一次检查:无锁快路径
            with cls._lock:                  # 只有一个线程能进来
                if cls._instance is None:    # 双检:防竞态重复创建
                    cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    results = []
    barrier = threading.Barrier(4)

    def worker():
        barrier.wait()                       # 4 线程同时起跑,放大竞态
        results.append(Config() is Config())

    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("all same instance:", all(results), "checks:", len(results))

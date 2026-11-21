import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:          # 双重检查,减少锁开销
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config):
        self.config = config               # 注意:每次都会执行

if __name__ == "__main__":
    a = Singleton("dev")
    b = Singleton("prod")
    print(a is b)          # True
    print(a.config)        # prod,__init__ 被第二次调用覆盖了

    threads = [threading.Thread(target=Singleton, args=("t",)) for _ in range(8)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(Singleton._instance is b)

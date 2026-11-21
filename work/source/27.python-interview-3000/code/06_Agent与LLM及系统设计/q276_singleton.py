import threading


class Singleton:
    """线程安全的 __new__ 单例,面试高频写法。"""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # 双重检查
                    cls._instance = super().__new__(cls)
        return cls._instance


def test():
    a = Singleton()
    b = Singleton()
    print(a is b)  # True


if __name__ == "__main__":
    test()

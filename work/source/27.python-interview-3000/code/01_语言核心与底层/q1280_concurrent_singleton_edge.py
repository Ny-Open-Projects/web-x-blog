import subprocess
import sys
import threading


class Registry:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def init(self, fail_first=False):
        with Registry._lock:
            if getattr(self, "_ok", False):
                return "already"
            if fail_first:
                raise RuntimeError("init failed, instance kept for retry")
            self._ok = True
            return "initialized"


CHILD_SRC = """
import threading
class R:
    _i = None
    _l = threading.Lock()
    def __new__(cls):
        if cls._i is None:
            with cls._l:
                if cls._i is None:
                    cls._i = super().__new__(cls)
        return cls._i
print(id(R()))
"""

if __name__ == "__main__":
    inst = Registry()
    try:
        inst.init(fail_first=True)
    except RuntimeError as e:
        print("first attempt:", e)
    print("second attempt:", inst.init())     # 幂等 init 可重试

    p1 = subprocess.run([sys.executable, "-c", CHILD_SRC],
                        capture_output=True, text=True)
    p2 = subprocess.run([sys.executable, "-c", CHILD_SRC],
                        capture_output=True, text=True)
    print("child ids:", p1.stdout.strip(), p2.stdout.strip(),
          "<- 不同进程,单例各建一份")

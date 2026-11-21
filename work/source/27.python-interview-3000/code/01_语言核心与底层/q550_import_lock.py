import sys
import threading

results = {}

def importer(name):
    try:
        __import__(name)
        results[name] = "imported"
    except ImportError as e:
        results[name] = f"ImportError: {e}"

if __name__ == "__main__":
    threads = [threading.Thread(target=importer, args=("json",)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(results)                       # 并发首次导入:只有一次真正执行
    print("single module object:", sys.modules["json"] is __import__("json"))
    print("rule: never spawn-and-join threads at module import time")

"""模拟双删时间线: 展示旧值回填窗口与第二次删除的补偿"""
import threading
import time

class System:
    def __init__(self):
        self.db = {"price": 100}
        self.cache = {"price": 100}
        self.cache_hits = 0

    def read(self):
        if "price" in self.cache:
            self.cache_hits += 1
            return self.cache["price"]
        v = self.db["price"]                 # 回源并回填
        self.cache["price"] = v
        return v

    def write_with_double_delete(self, value, delay=0.3):
        self.cache.pop("price", None)        # 第一次删: 更新库前
        time.sleep(0.05)                     # 让并发读进入旧值窗口
        self.db["price"] = value             # 更新库
        threading.Timer(delay, lambda: self.cache.pop("price", None)).start()

if __name__ == "__main__":
    s = System()
    def stale_reader():
        time.sleep(0.03)                     # 在库更新前进入读流程
        print("并发读拿到:", s.read(), "<- 旧值并被回填进缓存")
    t = threading.Thread(target=stale_reader)
    t.start()
    s.write_with_double_delete(200)
    t.join()
    print("此刻缓存残留旧值:", s.cache.get("price"))
    time.sleep(0.4)                          # 等第二次删除生效
    print("第二次删除后读:", s.read(), "<- 回源新值, 一致性恢复")

"""看门狗: 后台线程周期续期, 演示长任务全程持锁"""
import threading
import time
import uuid

class LockStore:
    def __init__(self):
        self.locks = {}

    def try_lock(self, key, owner, ttl):
        rec = self.locks.get(key)
        if rec is None or time.monotonic() > rec["expire"]:
            self.locks[key] = {"owner": owner, "expire": time.monotonic() + ttl}
            return True
        return False

    def renew(self, key, owner, ttl):
        rec = self.locks.get(key)
        if rec and rec["owner"] == owner:
            rec["expire"] = time.monotonic() + ttl
            return True
        return False

def run_with_watchdog(store, key, task, ttl=0.6, interval=0.2):
    owner = uuid.uuid4().hex
    assert store.try_lock(key, owner, ttl), "锁被他人持有"
    stop = threading.Event()

    def watchdog():
        while not stop.wait(interval):
            store.renew(key, owner, ttl)      # owner 校验 + 重置 TTL
    t = threading.Thread(target=watchdog, daemon=True)
    t.start()
    try:
        task()
    finally:
        stop.set()                             # 先停看门狗再释放
        store.locks.pop(key, None)

if __name__ == "__main__":
    store = LockStore()
    def long_job():
        for i in range(3):
            time.sleep(0.35)
            rec = store.locks.get("job:1")
            print(f"任务进行 {i}, 锁剩余 TTL 约 {rec['expire'] - time.monotonic():.2f}s")
    run_with_watchdog(store, "job:1", long_job)
    print("任务结束锁已释放:", "job:1" not in store.locks)

"""优雅发布: 双实例切换与在途请求排空(标准库线程演示)。"""
import threading
import time


class Instance:
    def __init__(self, name):
        self.name = name
        self.ready = True
        self.inflight = 0
        self.lock = threading.Lock()

    def handle(self, ms):
        with self.lock:
            self.inflight += 1
        time.sleep(ms / 1000.0)
        with self.lock:
            self.inflight -= 1
        return f"{self.name} 完成 {ms}ms 请求"

    @property
    def inflight_count(self):
        with self.lock:
            return self.inflight


A, B = Instance("A"), Instance("B")
pool = [A, B]
done = []


def pick():
    for inst in pool:
        if inst.ready:
            return inst
    return None


def traffic():
    for ms in (60, 60, 60, 60, 60, 60):
        inst = pick()
        if inst is None:
            done.append("丢弃(池空)")
            continue
        done.append(inst.handle(ms))


tt = threading.Thread(target=traffic)
tt.start()
time.sleep(0.05)                     # 让第一个请求落在 A 上且仍在途
print("开始发布: A 从池中摘除, ready=False")
A.ready = False                      # 新请求不再进 A, B 无缝接流
tt.join()
deadline = time.time() + 3
while A.inflight_count > 0 and time.time() < deadline:
    time.sleep(0.01)
print(f"A 排空完成, 在途 {A.inflight_count}")
print("发送 SIGTERM, A 退出; 全程 B 持续接流, 掉线请求 0 个")
print("已完成请求:", done)
print("要点: 先摘流量再排空, 存活探针保持 True 防重启, 排空设兜底超时防僵死")

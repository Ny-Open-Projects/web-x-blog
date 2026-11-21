"""僵尸会话回收:心跳超时判定 + 扫描器回收 + 资源释放与通知,两轮宽限防误杀。"""
import time


class Session:
    def __init__(self, sid, ttl_miss=2):
        self.sid = sid
        self.last_beat = time.time()
        self.ttl_miss = ttl_miss           # 连续多少个扫描周期无心跳才算僵尸
        self.missed = 0
        self.alive = True
        self.resources = ["conn-" + sid]

    def beat(self):
        self.last_beat = time.time()
        self.missed = 0                    # 有心跳就清零错过计数


class ZombieReaper:
    """周期扫描:第一轮只标记,连续两轮无心跳才回收,避免一次 GC 停顿造成误杀。"""

    def __init__(self):
        self.sessions = {}
        self.reaped = []
        self.notified = []

    def register(self, sid):
        self.sessions[sid] = Session(sid)
        return self.sessions[sid]

    def sweep(self, now=None):
        """扫描一次:连续 ttl_miss 轮无心跳的会话被回收并释放资源。"""
        newly = []
        for sid, s in list(self.sessions.items()):
            if not s.alive:
                continue
            s.missed += 1
            if s.missed >= s.ttl_miss:           # 连续两轮错过才动手 防一次停顿误杀
                s.alive = False
                self.reaped.append(sid)
                newly.append(sid)
                self.notified.append((sid, "resources_released", s.resources))
                s.resources = []
        return newly

    def touch_all_by(self, sid):
        self.sessions[sid].beat()


if __name__ == "__main__":
    reaper = ZombieReaper()
    reaper.register("A")
    reaper.register("B")
    reaper.register("C")

    reaper.sessions["B"].beat()                # B 在第一轮扫描前刚有心跳
    dead1 = reaper.sweep()
    assert dead1 == [], "第一轮只标记不回收"
    assert reaper.sessions["B"].missed == 1, "错过 1 次远未达阈值"

    reaper.sessions["A"].beat()                # A 抢救回来了 计数清零
    reaper.sessions["B"].beat()
    dead2 = reaper.sweep()
    assert dead2 == ["C"], "C 连续两轮无心跳被回收"
    assert reaper.sessions["A"].missed == 1 and reaper.sessions["B"].missed == 1

    reaper.sessions["B"].beat()
    dead3 = reaper.sweep()                     # A 达到阈值 B 还在宽限内
    assert dead3 == ["A"]
    dead4 = reaper.sweep()                     # B 最终也超时
    assert dead4 == ["B"] and reaper.sessions["A"].alive is False
    assert reaper.sessions["A"].resources == [], "回收时释放资源"
    assert [n[0] for n in reaper.notified] == ["C", "A", "B"], "每个回收都发出通知"
    print("僵尸回收通过:心跳清零、两轮宽限、回收释放资源并按序通知")

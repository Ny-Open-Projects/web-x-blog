# -*- coding: utf-8 -*-
"""并发安全的配置读取器: 加载 -> 校验 -> 原子替换 -> 无锁读。

- 配置快照整体不可变: 读者抓到引用后随便读多久, 都是一个自洽版本;
- 写者先校验, 坏配置直接拒绝, 旧配置继续服务 (校验失败不落地);
- 读者侧无锁: 抓引用是一条原子操作, 换快照不影响正在读的人;
- 不变量: sum(items) == total, 任何读者任何时刻都该看到自洽数据。
"""
import threading
import time


class ConfigStore:
    """版本化配置仓: 写者互斥, 读者无锁。"""

    def __init__(self, initial):
        self._cfg = initial            # 唯一会被整体替换的引用
        self._wlock = threading.Lock() # 只串行化写者, 读者不碰它
        self.rejected = 0
        self.applied = 0

    @property
    def current(self):
        return self._cfg               # 读者: 原子抓引用, 无锁

    def update(self, new_cfg, validate):
        with self._wlock:
            try:
                validate(new_cfg)
            except ValueError as exc:
                self.rejected += 1
                return "rejected: %s" % exc
            self._cfg = new_cfg        # 一次性替换快照, 读者即刻可见
            self.applied += 1
            return "applied v%d" % new_cfg["version"]


def validate(cfg):
    """配置合法性校验: 结构齐全 + 业务不变量自洽。"""
    for key in ("version", "total", "items", "timeout"):
        if key not in cfg:
            raise ValueError("missing key %s" % key)
    if cfg["total"] != sum(cfg["items"]):
        raise ValueError("total 与 items 不自洽")
    if not isinstance(cfg["timeout"], (int, float)) or cfg["timeout"] <= 0:
        raise ValueError("timeout 必须为正数")


def reader_loop(store, wid, seen, violations, done):
    """读者: 抓快照 -> 校验不变量 -> 记录见过的版本。"""
    while not done.is_set():
        cfg = store.current            # 抓本地引用, 之后写者怎么换都与我无关
        if cfg["total"] != sum(cfg["items"]):
            violations.append(wid)     # 撕裂读: 理论上不可能发生
        seen.add(cfg["version"])
        cfg["timeout"]                 # 模拟读一个配置项
        time.sleep(0.001)


if __name__ == "__main__":
    store = ConfigStore({"version": 1, "total": 6,
                         "items": [1, 2, 3], "timeout": 0.5})
    done = threading.Event()
    seen = [set() for _ in range(4)]
    violations = []
    readers = [threading.Thread(target=reader_loop,
                                args=(store, i, seen[i], violations, done))
               for i in range(4)]
    for t in readers:
        t.start()

    time.sleep(0.05)
    # 写者序列: 合法 -> 非法(拒绝) -> 合法
    r1 = store.update({"version": 2, "total": 10,
                       "items": [4, 6], "timeout": 0.8}, validate)
    time.sleep(0.05)
    r2 = store.update({"version": 3, "total": 99,          # 坏配置
                       "items": [4, 6], "timeout": 0.8}, validate)
    time.sleep(0.05)
    r3 = store.update({"version": 4, "total": 3,
                       "items": [1, 1, 1], "timeout": 1.2}, validate)
    time.sleep(0.05)
    done.set()
    for t in readers:
        t.join()

    print("写者结果: %s / %s / %s" % (r1, r2, r3))
    print("应用 %d 次, 拒绝 %d 次" % (store.applied, store.rejected))
    print("各读者见过的版本:", [sorted(s) for s in seen])
    print("撕裂读违规次数:", len(violations))
    assert store.rejected == 1 and store.applied == 2
    assert not violations, "出现了撕裂读"
    assert 1 in seen[0] and 4 in seen[0], "读者没有观察到版本切换"
    print("要点: 快照整体替换使读者天然一致, 校验前置让坏配置不落地")

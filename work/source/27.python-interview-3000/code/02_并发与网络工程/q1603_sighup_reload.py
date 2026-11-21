"""SIGHUP 热加载: 信号安全与原子替换。

- 信号处理器只做一件事: 置位标志。重活(读文件、解析)留给主循环,
  处理器里做 IO 是给未来埋雷;
- 配置文件用 tmp + os.replace 原子上线, 读者永远看到完整文件;
- 配置对象整体替换(不可变快照), 工作线程读一次引用就够, 无锁;
- 信号不排队: 连发两个 SIGHUP 可能合并成一次, Event 语义天然防抖。
"""
import json
import os
import signal
import tempfile
import threading
import time

CONFIG_PATH = os.path.join(tempfile.gettempdir(), "q1603_config.json")


def write_config(data):
    tmp = CONFIG_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f)
    os.replace(tmp, CONFIG_PATH)             # 原子替换: 不存在半截文件


class HotReloader:
    def __init__(self):
        write_config({"rate": 10})
        with open(CONFIG_PATH) as f:
            self.current = json.load(f)      # 整体替换的不可变快照
        self.reload_requested = threading.Event()
        self.versions = 0

    def on_sighup(self, signum, frame):
        self.reload_requested.set()          # 信号处理器只置位

    def reload_if_requested(self):
        if self.reload_requested.is_set():
            self.reload_requested.clear()
            with open(CONFIG_PATH) as f:
                self.current = json.load(f)  # 原子引用替换
            self.versions += 1
            return True
        return False


def main():
    reloader = HotReloader()
    signal.signal(signal.SIGHUP, reloader.on_sighup)   # 只能在主线程装

    seen = set()
    stop = threading.Event()

    def worker():
        while not stop.is_set():
            rate = reloader.current["rate"]  # 读一次快照引用, 无锁无撕裂
            seen.add(rate)
            time.sleep(0.02)

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(2)]
    for t in threads:
        t.start()
    time.sleep(0.1)                          # 稳定期: 保证初版配置被采样到
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline and 10 not in seen:
        time.sleep(0.02)                     # 确定性同步: 初值确认已被读

    print("初版配置 rate =", reloader.current["rate"])
    for new_rate in (20, 30):
        write_config({"rate": new_rate})
        os.kill(os.getpid(), signal.SIGHUP)  # 自我投递: 模拟运维 kill -HUP
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline and not reloader.reload_if_requested():
            time.sleep(0.01)
        # 等工作线程确认采样到这一版, 再进入下一版(否则窗口太窄会被跳过)
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline and new_rate not in seen:
            time.sleep(0.02)
        print("热加载后 rate =", reloader.current["rate"])

    stop.set()
    for t in threads:
        t.join(timeout=1)

    print("工作线程见过的 rate 集合:", sorted(seen))
    assert seen == {10, 20, 30}, "三轮配置都应被工作线程看到, 且无中间态"
    assert reloader.versions == 2, "两次 SIGHUP 各完成一次重载"
    print("结论: 信号只当门铃, 重载走主循环; 原子替换让读者永远只见完整配置")


if __name__ == "__main__":
    main()

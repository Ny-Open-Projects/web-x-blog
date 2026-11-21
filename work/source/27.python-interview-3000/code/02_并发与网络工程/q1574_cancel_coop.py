"""跨线程取消协作: 取消标志 + 检查点 + 不可中断区。

Python 的 Thread 没有 kill: 取消必须是协作式的。
- cancel() 只置位 Event, 从不强行打断;
- 工作循环在每个"检查点"查询标志, 在安全点及时退出;
- 必须完整执行的关键区标注为不可中断区, 检查点放在区外。
"""
import threading
import time


class CancellableJob:
    def __init__(self, total):
        self.cancel_evt = threading.Event()
        self.processed = 0
        self.total = total
        self.finished_cleanly = False

    def cancel(self):
        self.cancel_evt.set()               # 只置位, 不打断

    def run(self):
        try:
            for i in range(self.total):
                if self.cancel_evt.is_set():        # 检查点 1: 循环边界
                    return
                # ---- 不可中断区: 模拟"写到一半的账本", 必须完整 ----
                time.sleep(0.02)
                self.processed += 1
                # ---- 区外恢复检查点 ----
                if self.cancel_evt.is_set():        # 检查点 2: 区结束立刻查
                    return
        finally:
            self.finished_cleanly = True


def main():
    job = CancellableJob(total=200)
    t = threading.Thread(target=job.run, name="worker")
    t.start()
    time.sleep(0.15)                    # 让它先跑一会儿
    print("发起取消, 已处理:", job.processed)
    job.cancel()
    t.join(timeout=2)
    print("线程存活:", t.is_alive(), "干净退出:", job.finished_cleanly,
          "最终处理:", job.processed)
    assert not t.is_alive() and job.finished_cleanly, "取消后应尽快干净退出"
    assert job.processed < job.total, "不应跑完全量"

    # 对照: 循环里没有任何检查点, cancel 置位也停不下来, 只能等它自然结束
    runaway_done = threading.Event()

    def runaway():
        n = 0
        while n < 30:                   # 没有任何取消检查
            time.sleep(0.01)
            n += 1
        runaway_done.set()

    t2 = threading.Thread(target=runaway, daemon=True)
    t2.start()
    print("对照: 无检查点的循环对取消标志免疫, 只能等它自然结束")
    assert runaway_done.wait(timeout=2)
    print("结论: 取消协议 = 置位方只置位 + 执行方定期自查 + 关键区整体执行")


if __name__ == "__main__":
    main()

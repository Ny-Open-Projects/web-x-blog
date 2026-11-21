import random
import threading
import time

barrier = threading.Barrier(3, timeout=1.0)  # 3 个线程一组, 最多等 1 秒


def phase_worker(name: str, slow: bool = False) -> None:
    for phase in range(3):
        delay = 2.0 if slow and phase == 1 else random.uniform(0.05, 0.15)
        time.sleep(delay)
        print(f"{name} 完成阶段 {phase}")
        try:
            barrier.wait()  # 集合点: 全员到齐才进下一阶段
        except threading.BrokenBarrierError:
            print(f"{name} 阶段 {phase} 栅栏失效, 整组退出")
            return


if __name__ == "__main__":
    print("--- 正常场景 ---")
    ts = [threading.Thread(target=phase_worker, args=(f"w{i}",)) for i in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()

    print("--- 超时场景: w9 太慢, 全组 broken ---")
    barrier2 = threading.Barrier(3, timeout=0.5)

    def worker2(name: str, slow: bool) -> None:
        try:
            for phase in range(2):
                if slow:
                    time.sleep(1.5)  # 远超栅栏超时
                barrier2.wait()
            print(f"{name} 全部完成")
        except threading.BrokenBarrierError:
            print(f"{name} 检测到栅栏失效, 中止")

    ts = [
        threading.Thread(target=worker2, args=("a", False)),
        threading.Thread(target=worker2, args=("b", False)),
        threading.Thread(target=worker2, args=("slow", True)),
    ]
    for t in ts:
        t.start()
    for t in ts:
        t.join()

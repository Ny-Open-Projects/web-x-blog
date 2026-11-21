# -*- coding: utf-8 -*-
"""CAS 思想与丢失更新: 无保护的读改写会丢更新, CAS 循环靠提交校验自愈。

- CPython 不暴露硬件 CAS, 这里用一个极小锁只保护 "比较并交换" 这一步,
  它在语义上就是 compare_and_swap 原语的替身;
- CAS 循环: 读旧值 -> 计算新值 -> 提交时校验预期值, 失败就重来;
- 对照组: 裸的 counter += 1 在字节码层面是三步, 线程切换会让更新蒸发。
"""
import sys
import threading

sys.setswitchinterval(1e-6)           # 极小切换间隔, 迫使字节码高频交错
TOTAL_THREADS = 4
ITERS = 20000
TOTAL = TOTAL_THREADS * ITERS


def racy_incr(cell):
    for _ in range(ITERS):
        cell[0] += 1                      # 读 加 写 三步, 中途可被打断


class CasCell:
    """用最小锁模拟原子 CAS 原语。"""

    def __init__(self, value):
        self._value = value
        self._atomic = threading.Lock()
        self.retries = 0

    def read(self):
        return self._value                # GIL 下单项读是原子的

    def compare_and_swap(self, expected, new):
        with self._atomic:                # 只包住比较交换这一瞬
            if self._value == expected:
                self._value = new
                return True
            return False

    def incr(self):
        while True:
            cur = self.read()
            if self.compare_and_swap(cur, cur + 1):
                return
            self.retries += 1             # 预期值失效, 别人抢先了, 重来


def main():
    # 对照组: 裸读改写, 多轮尝试直到捕捉到丢失更新
    lost = 0
    racy_final = None
    for _ in range(3):
        racy = [0]
        ts = [threading.Thread(target=racy_incr, args=(racy,))
              for _ in range(TOTAL_THREADS)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        racy_final = racy[0]
        if racy_final != TOTAL:
            lost = TOTAL - racy_final
            break
    print("裸读改写结果: %d / %d, 丢失 %d 次更新" % (racy_final, TOTAL, lost))
    assert racy_final != TOTAL, "高频交错下裸读改写必然丢失更新"

    # 实验组: CAS 循环
    cell = CasCell(0)

    def cas_worker():
        for _ in range(ITERS):
            cell.incr()

    ts = [threading.Thread(target=cas_worker) for _ in range(TOTAL_THREADS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print("CAS 循环结果:", cell.read(), "因冲突重试次数:", cell.retries)
    assert cell.read() == TOTAL, "CAS 提交校验保证不丢更新"

    print("结论: 正确性不靠运气靠校验, 预期值不符就重来, 这就是乐观并发")


if __name__ == "__main__":
    main()

import os
import threading
import time
from typing import Optional

# 故障注入开关: RACE_HOOK=1 时放大竞态窗口
HOOK = os.environ.get("RACE_HOOK") == "1"


def transfer(accounts: dict, src: str, dst: str, amount: int) -> bool:
    if accounts[src] >= amount:          # 检查
        if HOOK:
            time.sleep(0.001)            # 注入: 放大 check 与 act 之间的窗口
        accounts[src] -= amount          # 动作
        accounts[dst] += amount
        return True
    return False


def one_round(threads: int = 3) -> Optional[dict]:  # 3.9 需 Optional, dict | None 运行时 TypeError
    accounts = {"a": 100, "b": 0}
    ts = [
        threading.Thread(target=transfer, args=(accounts, "a", "b", 100))
        for _ in range(threads)
    ]
    # 随机延迟启动, 增加打断模式多样性
    for t in ts:
        t.start()
        time.sleep(0.0001 if not HOOK else 0)
    for t in ts:
        t.join()
    if accounts["a"] < 0 or accounts["b"] > 100:
        return accounts  # 不变量被破坏: 余额为负 = 复现超取
    return None


def stress(rounds: int = 300) -> tuple:
    for i in range(rounds):
        bad = one_round()
        if bad is not None:
            return i, bad
    return None, None


if __name__ == "__main__":
    print(f"注入开关: {HOOK}")
    round_no, accounts = stress()
    if round_no is None:
        print("未复现 (多跑几轮或开启 RACE_HOOK=1)")
    else:
        print(f"第 {round_no} 轮复现! 账户状态: {accounts} → 超取竞态实锤")
    print("修复方法: transfer 全程持锁, 消除 check 与 act 之间的窗口")

---
title: [Q2658] CAS 的 ABA 问题:值回来了,世界却换过了
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2658 · CAS 的 ABA 问题:值回来了,世界却换过了

> 难度:★★★★ | 标签:CAS, ABA, 版本号

**问**:CAS 只比较值相等,如果值被改走又改回来,提交会发生什么?

**答**:发生 ABA 问题:账户 100 元,A 读到快照;期间 B 取走 30 又存回 30,余额回到 100 但发生过两次动账;A 的纯值 CAS 检查 100 == 100 通过,提交成功,却把 B 的动账台账整个覆盖——账面余额没错,审计记录凭空消失。版本号 CAS 每次提交把 version +1,A 校验的是 version,值回来了版本对不上,照样拒绝。

- ABA 的危害不在值,而在"值相同的两个时刻之间世界已经不同";

- 纯值 CAS 适合无历史语义的开关量,一切带台账、带引用、带链表节点的场景都会中招;

- 通用解是版本戳:值与版本打包,或者干脆用不可变对象整体替换;

- 无锁栈的节点复用是最经典的 ABA 现场 popped 节点被回收到栈顶,指针值相同而节点已换。

```python
# file: code/02_并发与网络工程/q2658_aba.py
# -*- coding: utf-8 -*-
"""CAS 的 ABA 问题: 值回来了, 世界却换过了。

- 只比对值的 CAS: A 读到 100, 期间 B 取走又存回 100, A 的提交照样成功;
- 被覆盖掉的不只是余额, 还有 B 留下的台账(movements), 审计直接失真;
- 版本号 CAS: 每次提交 version +1, 值回来了版本对不上, 照样拒绝。
"""
import copy


def cas_by_value(acct, expect_balance, new_balance, new_movements):
    """只认余额的 CAS: 余额没变就允许覆盖。"""
    if acct["balance"] == expect_balance:
        acct["balance"] = new_balance
        acct["movements"] = new_movements
        return True
    return False


def cas_by_version(acct, expect_version, new_balance, new_movements):
    """版本号 CAS: 版本对不上就拒绝, 强制重读重算。"""
    if acct["version"] == expect_version:
        acct["balance"] = new_balance
        acct["movements"] = new_movements
        acct["version"] += 1
        return True
    return False


def play_b(acct):
    """并发方 B: 取走 30 又存回 30, 余额回到原值, 台账 +2。"""
    ok1 = cas_by_version(acct, acct["version"], acct["balance"] - 30,
                         acct["movements"] + 1)
    ok2 = cas_by_version(acct, acct["version"], acct["balance"] + 30,
                         acct["movements"] + 1)
    return ok1 and ok2


if __name__ == "__main__":
    # 阶段一: A 读快照后休眠, B 完成"取走又存回", A 用纯值 CAS 提交
    acct = {"balance": 100, "movements": 0, "version": 0}
    snap = copy.copy(acct)               # A 的快照: balance=100
    assert play_b(acct)                  # B: 100 -> 70 -> 100, version 0 -> 2
    print("B 操作后: balance=%(balance)s, movements=%(movements)s, "
          "version=%(version)s" % acct)
    ok = cas_by_value(acct, snap["balance"], 120, snap["movements"] + 1)
    print("A 用纯值 CAS 提交(给客户加 20 并记一笔): 成功=%s" % ok)
    print("纯值 CAS 后: balance=%(balance)s, movements=%(movements)s" % acct)
    print("审计失真: 明明发生过 3 次动账, 台账只剩 1 次")

    # 阶段二: 同样的剧情, 换版本号 CAS
    acct2 = {"balance": 100, "movements": 0, "version": 0}
    snap2_version = acct2["version"]     # A 记住的是版本, 不只是余额
    assert play_b(acct2)
    ok2 = cas_by_version(acct2, snap2_version, 120, 1)
    print("A 用版本号 CAS 提交: 成功=%s (version 已是 %d)"
          % (ok2, acct2["version"]))
    print("版本号 CAS 拒绝陈旧提交, 强制 A 重读最新状态再重算")
```

**追问**:1) 版本号方案为什么能挡住 ABA?——它把"状态是否变过"从值域搬到单调递增的版本域,回拨不可能。2) Python 里有真实的 ABA 风险吗?——GIL 让单字节码原子,但"读-判断-写"跨多个字节码的组合操作照样存在 ABA 窗口。3) 底层机制:经典 ABA 现场长什么样?——无锁栈的 pop 读到栈顶节点 A 后被挂起,其他线程 pop 掉 A 又 push 回一个复用同地址的新节点,指针值相同而节点已换,比对照样通过;Python 层没有裸指针 CAS,但对共享 dict/对象字段的"读-比较-写"组合是同构问题。4) 生产陷阱?——把"值没变"当"什么都没发生",审计台账被静默覆盖;版本检查与写入仍是两步,要用锁或整体替换不可变对象封住窗口;拿 uuid/时间戳当版本号,碰撞与回拨都会复活 ABA。

---

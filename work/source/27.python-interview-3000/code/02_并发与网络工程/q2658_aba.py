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

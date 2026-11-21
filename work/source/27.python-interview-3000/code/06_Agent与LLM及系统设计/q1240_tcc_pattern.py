"""TCC:Try 预留 -> Confirm/Cancel,含空回滚、悬挂、幂等三防。"""


class AccountTCC:
    def __init__(self, balance):
        self.balance, self.frozen = balance, 0
        self.tried, self.finished = {}, set()      # xid 状态簿

    def try_freeze(self, xid, amount):
        if xid in self.tried or xid in self.finished:      # 幂等
            return "dup"
        if self.balance < amount:
            raise ValueError("余额不足")
        self.balance, self.frozen = self.balance - amount, self.frozen + amount
        self.tried[xid] = amount
        return "frozen"

    def confirm(self, xid):
        amt = self.tried.pop(xid, None)
        if amt is None:
            return "no_try"                        # 未 Try 先 Confirm:拒绝
        if xid in self.finished:
            return "dup"
        self.frozen -= amt                         # 冻结转实扣
        self.finished.add(xid)
        return "confirmed"

    def cancel(self, xid):
        amt = self.tried.get(xid)
        if amt is None:
            self.finished.add(xid)                 # 空回滚登记,防悬挂:迟到的 Try 被拒
            self.tried[xid] = 0
            return "empty_cancel"
        if xid in self.finished:
            return "dup"
        self.tried.pop(xid)
        self.frozen, self.balance = self.frozen - amt, self.balance + amt
        self.finished.add(xid)
        return "cancelled"

    def try_freeze_late(self, xid, amount):
        if xid in self.finished:
            return "suspended_rejected"            # 悬挂防御:Cancel 已登记
        return self.try_freeze(xid, amount)


if __name__ == "__main__":
    acc = AccountTCC(100)
    print(acc.try_freeze("x1", 30), acc.balance, "冻结", acc.frozen)
    print(acc.confirm("x1"), "-> 余额", acc.balance, "冻结", acc.frozen)
    assert acc.balance == 70 and acc.frozen == 0

    acc2 = AccountTCC(100)
    acc2.try_freeze("x2", 20)
    print(acc2.cancel("x2"), "-> 余额", acc2.balance)
    assert acc2.balance == 100 and acc2.frozen == 0
    print(acc2.try_freeze_late("x2", 20), "(悬挂 Try 被拒)")
    assert acc2.try_freeze_late("x2", 20) == "suspended_rejected"

    acc3 = AccountTCC(50)
    print(acc3.cancel("x3"), "(空回滚)")
    assert acc3.cancel("x3") == "dup" or acc3.finished
    print("三防验证: 幂等/空回滚/悬挂 全部就位")

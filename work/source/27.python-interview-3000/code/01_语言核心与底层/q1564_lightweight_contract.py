

def require(condition, message):
    """前置条件:违反 = 调用方的 bug,ValueError。"""
    if not condition:
        raise ValueError(message)


def ensure(condition, message):
    """后置条件:违反 = 实现者的 bug,RuntimeError。"""
    if not condition:
        raise RuntimeError("internal invariant broken: " + message)


class Ledger:
    def __init__(self, balances):
        self.balances = dict(balances)
        self._check_invariant()

    def _check_invariant(self):
        ensure(all(v >= 0 for v in self.balances.values()), "余额不得为负")
        ensure(set(self.balances) == {"alice", "bob"}, "账户集合固定")

    def transfer(self, src, dst, amount):
        require(amount > 0, "amount 必须为正, got %s" % amount)
        require(src in self.balances and dst in self.balances,
                "账户必须存在, got %r/%r" % (src, dst))
        before = sum(self.balances.values())
        self.balances[src] -= amount
        self.balances[dst] += amount
        self._check_invariant()                  # 状态转换后的不变量
        ensure(sum(self.balances.values()) == before, "转账不得创造或销毁金额")
        return self.balances[src], self.balances[dst]


if __name__ == "__main__":
    ledger = Ledger({"alice": 100, "bob": 50})
    print("transfer 30:", ledger.transfer("alice", "bob", 30))
    print("balances   :", ledger.balances)

    for bad in [("alice", "bob", 0), ("ghost", "bob", 5), ("alice", "bob", 999)]:
        try:
            ledger.transfer(*bad)
        except (ValueError, RuntimeError) as err:
            print("%s: %s" % (type(err).__name__, err))

    print("total intact:", sum(ledger.balances.values()) == 150)

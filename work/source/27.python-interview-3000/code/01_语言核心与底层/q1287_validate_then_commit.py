

def transfer(accounts, src, dst, amount):
    # 第一阶段:只读校验,不动任何状态
    if src not in accounts or dst not in accounts:
        raise KeyError("unknown account: %r" % (src if src not in accounts else dst))
    if amount <= 0:
        raise ValueError("amount must be positive, got %r" % (amount,))
    if accounts[src] < amount:
        raise ValueError("insufficient funds in %s: %d < %d"
                         % (src, accounts[src], amount))
    # 第二阶段:提交,极简赋值
    accounts[src] -= amount
    accounts[dst] += amount
    return accounts[src], accounts[dst]


if __name__ == "__main__":
    accounts = {"a": 100, "b": 50}
    print("ok transfer:", transfer(accounts, "a", "b", 30), accounts)
    snapshot = dict(accounts)
    for bad in (("a", "c", 10), ("a", "b", -5), ("a", "b", 1000)):
        try:
            transfer(accounts, bad[0], bad[1], bad[2])
        except (KeyError, ValueError) as e:
            print(type(e).__name__, "->", e,
                  "| state untouched:", accounts == snapshot)

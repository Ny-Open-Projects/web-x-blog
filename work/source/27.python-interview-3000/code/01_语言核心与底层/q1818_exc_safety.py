"""异常安全层级:基本保证与强保证的回滚实现。"""


class Account:
    def __init__(self, balance):
        self.balance = balance


class Bomb:
    """到账环节会崩溃的记账系统,用于演示回滚。"""

    def __init__(self):
        self._balance = 0
        self.armed = False

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if self.armed:
            raise RuntimeError("记账系统崩溃")
        self._balance = value


def transfer_strong(src, dst, amount):
    """强保证:要么全部生效,要么像没发生过。"""
    if amount > src.balance:
        raise ValueError("余额不足")
    src.balance -= amount
    try:
        dst.balance += amount
    except BaseException:
        src.balance += amount      # 回滚第一步
        raise


def transfer_broken(src, dst, amount):
    """反例:中途失败不回滚,总和不变量被破坏。"""
    if amount > src.balance:
        raise ValueError("余额不足")
    src.balance -= amount
    raise RuntimeError("到账环节崩溃")


if __name__ == "__main__":
    a, b = Account(100), Account(50)
    transfer_strong(a, b, 30)
    print("成功转账:", a.balance, b.balance, "总和:", a.balance + b.balance)

    a2, bomb = Account(100), Bomb()
    bomb.armed = True
    try:
        transfer_strong(a2, bomb, 30)
    except RuntimeError as e:
        print("到账失败:", e, "| 回滚后源账户:", a2.balance)
    print("强保证下总和守恒:", a2.balance + bomb.balance)

    a3, b3 = Account(100), Account(50)
    try:
        transfer_broken(a3, b3, 30)
    except RuntimeError:
        print("反例后总和(被破坏):", a3.balance + b3.balance)

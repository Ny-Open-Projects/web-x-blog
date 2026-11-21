def withdraw(balance: int, amount: int) -> int:
    assert amount > 0, "amount must be positive"    # python -O 下被剥离
    if amount > balance:
        raise ValueError("insufficient funds")      # 业务规则必须用异常
    return balance - amount

if __name__ == "__main__":
    print(withdraw(100, 30))
    print("assertions enabled:", __debug__)
    try:
        withdraw(100, -1)
    except AssertionError as e:
        print("assert fired:", e)
    print("with -O the assert vanishes and -1 passes the first check")

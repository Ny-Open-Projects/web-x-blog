

def load_user_profile(user_id, db):
    # 边界层:外部输入,完整校验,可行动的错误消息
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive int, got %r" % (user_id,))
    record = db.get(user_id)
    if record is None:
        raise KeyError("user %d not found" % user_id)
    return record


def internal_apply_discount(record, rate):
    # 内部层:契约已由上游保证,仅断言不变量
    assert 0 < rate < 1, "internal invariant broken, rate=%r" % (rate,)
    return record["price"] * (1 - rate)


if __name__ == "__main__":
    db = {1: {"name": "a", "price": 100.0}}
    print("profile:", load_user_profile(1, db))
    print("discounted:", internal_apply_discount(db[1], 0.2))
    for bad in (lambda: load_user_profile("1", db),
                lambda: load_user_profile(2, db)):
        try:
            bad()
        except (ValueError, KeyError) as e:
            print(type(e).__name__, "->", e)

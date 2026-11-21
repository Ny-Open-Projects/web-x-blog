from datetime import date

def rfm_score(orders, today=None):
    """orders: list of (uid, order_date, amount)"""
    today = today or date(2026, 11, 1)
    agg = {}
    for uid, d, amt in orders:
        r, f, m = agg.get(uid, (None, 0, 0.0))
        days = (today - d).days
        agg[uid] = (min(r, days) if r is not None else days,
                    f + 1, m + amt)
    # 打分:R 越小分越高,F/M 越大分越高(此处用固定阈值, 生产用分位数)
    result = {}
    for uid, (r, f, m) in agg.items():
        r_s = 3 if r <= 7 else (2 if r <= 30 else 1)
        f_s = 3 if f >= 3 else (2 if f >= 2 else 1)
        m_s = 3 if m >= 500 else (2 if m >= 100 else 1)
        seg = (r_s, f_s, m_s)
        label = {(3, 3, 3): "重要价值", (1, 1, 1): "流失",
                 (3, 1, 1): "新客户"}.get(seg, "一般")
        result[uid] = {"R": r, "F": f, "M": m, "score": seg, "label": label}
    return result

if __name__ == "__main__":
    orders = [("u1", date(2026, 10, 30), 600.0),
              ("u1", date(2026, 10, 25), 100.0),
              ("u2", date(2026, 6, 1), 30.0),
              ("u3", date(2026, 10, 31), 50.0)]
    for uid, info in rfm_score(orders).items():
        print(uid, info)

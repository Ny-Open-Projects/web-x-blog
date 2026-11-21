"""用纯函数模拟数仓分层:每层只依赖下一层,输入输出明确。"""

def ods_to_dwd(raw_rows):
    """清洗:去重 + 过滤非法,一行一个事件。"""
    seen, dwd = set(), []
    for r in raw_rows:
        key = (r["order_id"], r["uid"])
        if key in seen or r["amount"] <= 0:
            continue
        seen.add(key)
        dwd.append({"order_id": r["order_id"], "uid": r["uid"],
                    "amount": r["amount"], "dt": r["dt"]})
    return dwd

def dwd_to_dws(dwd_rows):
    """按用户按天汇总。"""
    agg = {}
    for r in dwd_rows:
        k = (r["uid"], r["dt"])
        amt, cnt = agg.get(k, (0.0, 0))
        agg[k] = (amt + r["amount"], cnt + 1)
    return [{"uid": u, "dt": d, "amt": a, "cnt": c} for (u, d), (a, c) in agg.items()]

def dws_to_ads(dws_rows):
    """应用层:直接可用的报表行。"""
    return sorted(dws_rows, key=lambda r: -r["amt"])[:3]

if __name__ == "__main__":
    raw = [{"order_id": 1, "uid": "u1", "amount": 100, "dt": "2026-11-01"},
           {"order_id": 1, "uid": "u1", "amount": 100, "dt": "2026-11-01"},
           {"order_id": 2, "uid": "u2", "amount": 50, "dt": "2026-11-01"}]
    dwd = ods_to_dwd(raw)
    dws = dwd_to_dws(dwd)
    ads = dws_to_ads(dws)
    print("ODS", len(raw), "-> DWD", len(dwd), "-> DWS", dws, "-> ADS", ads)

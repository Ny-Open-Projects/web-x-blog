"""新老用户判定:设备指纹归一与首活日口径"""
try:
    import pandas as pd
except ImportError:
    pd = None

EVENTS = [
    # date, user_id, device_id
    ("2025-06-01", "u1", "d1"),
    ("2025-06-01", "u2", "d2"),
    ("2025-06-02", "u9", "d1"),   # 同设备换了账号,应归一为老用户
    ("2025-06-02", "u2", "d2"),
    ("2025-06-02", "u3", "d3"),
    ("2025-06-03", "u3", "d3"),
]


def stdlib_version(rows):
    first_seen, daily = {}, {}
    for date, uid, dev in rows:
        key = dev  # 以设备指纹为主键,同设备多账号视为同人
        first_seen.setdefault(key, date)
        daily.setdefault(date, []).append(key)
    for date in sorted(daily):
        old = sum(1 for k in daily[date] if first_seen[k] < date)
        new = len(daily[date]) - old
        print(f"{date}  新 {new}  老 {old}")


if pd is None:
    print("标准库降级:设备口径新老判定")
    stdlib_version(EVENTS)
else:
    df = pd.DataFrame(EVENTS, columns=["date", "user_id", "device_id"])
    first = df.groupby("device_id")["date"].min().rename("first_seen")
    df = df.merge(first, on="device_id")
    df["is_new"] = df["date"] == df["first_seen"]
    daily = df.groupby(["date", "is_new"]).size().unstack(fill_value=0)
    daily.columns = ["old", "new"] if set(daily.columns) == {False, True} else daily.columns
    print(daily)

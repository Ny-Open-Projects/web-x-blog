try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:用 zoneinfo 看 DST 偏移变化")
    try:
        from zoneinfo import ZoneInfo
        from datetime import datetime
        for label, dt in [("春跳前", datetime(2026, 3, 29, 1, 30)), ("秋回拨", datetime(2026, 10, 25, 2, 30))]:
            print(label, dt.replace(tzinfo=ZoneInfo("Europe/Berlin")).utcoffset())
    except Exception as e:
        print("zoneinfo 不可用:", e)
else:
    naive = pd.Series(pd.to_datetime(["2026-03-29 02:30", "2026-10-25 02:30"]))
    # 春季不存在的时间:前移;秋季重复的时间:明确选择其一
    handled = naive.dt.tz_localize("Europe/Berlin", nonexistent="shift_forward", ambiguous="NaT")
    print(handled)
    utc = naive.dt.tz_localize(
        "Europe/Berlin", nonexistent="shift_forward", ambiguous=True
    ).dt.tz_convert("UTC")
    print("转 UTC 后:", utc.tolist())

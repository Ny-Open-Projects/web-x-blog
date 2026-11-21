try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    holidays = {"2026-01-01", "2026-01-02", "2026-01-03"}
    workdays = []
    from datetime import date, timedelta
    d = date(2026, 1, 1)
    while len(workdays) < 3:
        if d.weekday() < 5 and d.isoformat() not in holidays:
            workdays.append(d.isoformat())
        d += timedelta(days=1)
    print("前 3 个工作日:", workdays)
else:
    from pandas.tseries.offsets import CustomBusinessDay
    # 1 月 1 日至 3 日放假,1 月 10 日周六调休上班
    cbd = CustomBusinessDay(
        holidays=["2026-01-01", "2026-01-02", "2026-01-03"],
        weekmask="Mon Tue Wed Thu Fri Sat" if False else "Mon Tue Wed Thu Fri",
    )
    days = pd.bdate_range("2026-01-01", periods=3, freq=cbd)
    print(days.date.tolist())
    # 单独演示调休:把 2026-01-10 周六设为工作日
    cbd2 = CustomBusinessDay(weekmask="Mon Tue Wed Thu Fri Sat", holidays=["2026-01-01"])
    d = pd.Timestamp("2026-01-09") + cbd2
    print("周五加一个工作日 ->", d.date, d.day_name())

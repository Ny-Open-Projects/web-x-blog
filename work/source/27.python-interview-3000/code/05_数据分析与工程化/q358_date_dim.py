from datetime import date, timedelta

def build_date_dim(start, end):
    rows = []
    d = start
    while d <= end:
        rows.append({
            "date_key": d.isoformat().replace("-", ""),
            "date": d.isoformat(),
            "year": d.year, "month": d.month,
            "week_of_year": d.isocalendar()[1],
            "weekday": d.weekday(),               # 0=周一
            "is_weekend": d.weekday() >= 5,
        })
        d += timedelta(days=1)
    return rows

if __name__ == "__main__":
    dim = build_date_dim(date(2026, 10, 30), date(2026, 11, 1))
    assert len(dim) == 3
    assert all(r["is_weekend"] is False or r["weekday"] >= 5 for r in dim)
    for r in dim:
        print(r)

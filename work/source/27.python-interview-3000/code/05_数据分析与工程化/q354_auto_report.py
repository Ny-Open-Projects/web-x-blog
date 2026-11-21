import csv
import os
from datetime import date

def fetch_metrics(data_date):
    """生产上为参数化 SQL 查询结果表;此处模拟。"""
    return [["gmv", 10000], ["uv", 800], ["pay_rate", 0.12]]

def render_csv(metrics, data_date, path):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["metric", "value", "date"])
        for name, val in metrics:
            w.writerow([name, val, data_date])

def validate(metrics):
    names = {m[0] for m in metrics}
    required = {"gmv", "uv", "pay_rate"}
    missing = required - names
    if missing:                        # 缺指标就告警,不发空表
        raise ValueError(f"missing metrics: {missing}")
    return True

if __name__ == "__main__":
    today = date.today().isoformat()
    metrics = fetch_metrics(today)
    validate(metrics)
    render_csv(metrics, today, f"report_{today}.csv")
    print("report ready:", f"report_{today}.csv")
    os.remove(f"report_{today}.csv")

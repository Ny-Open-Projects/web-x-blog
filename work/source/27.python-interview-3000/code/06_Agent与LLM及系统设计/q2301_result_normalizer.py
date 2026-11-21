"""工具结果归一:时区统一 UTC 单位统一 SI 货币统一基准,异构工具结果可合并。"""
from datetime import datetime, timedelta, timezone


def norm_time(ts_epoch_s, tz_offset_hours):
    base = datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=ts_epoch_s)
    local = base.astimezone(timezone(timedelta(hours=tz_offset_hours)))
    return {"utc": base.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "local": local.strftime("%Y-%m-%dT%H:%M:%S%z")}


UNIT_TO_MB = {"KB": 1.0 / 1024.0, "MB": 1.0, "GB": 1024.0}
FX_TO_CNY = {"CNY": 1.0, "USD": 7.2}


def norm_size(value, unit):
    return round(value * UNIT_TO_MB[unit], 2)


def norm_price(value, currency):
    return round(value * FX_TO_CNY[currency], 2)


def merge_rows(rows):
    out = {}
    for r in rows:
        row = {"size_mb": norm_size(r["size"], r["unit"]),
               "price_cny": norm_price(r["price"], r["currency"]),
               "ts_utc": norm_time(r["ts"], r.get("tz", 0))["utc"]}
        key = r["item"]
        if key in out:
            out[key]["price_cny"] = round(out[key]["price_cny"] + row["price_cny"], 2)
            out[key]["size_mb"] = round(out[key]["size_mb"] + row["size_mb"], 2)
        else:
            out[key] = row
    return out


if __name__ == "__main__":
    rows = [
        {"item": "存储", "size": 512, "unit": "KB", "price": 10, "currency": "USD", "ts": 3600, "tz": 8},
        {"item": "存储", "size": 2, "unit": "GB", "price": 30, "currency": "CNY", "ts": 0, "tz": 0},
        {"item": "带宽", "size": 1, "unit": "GB", "price": 5, "currency": "USD", "ts": 1800, "tz": -5},
    ]
    merged = merge_rows(rows)
    assert merged["存储"]["size_mb"] == 2048.5, "KB 与 GB 统一到 MB"
    assert merged["存储"]["price_cny"] == 72.0 + 30.0, "USD 与 CNY 统一到 CNY"
    assert merged["存储"]["ts_utc"] == "2026-01-01T01:00:00Z", "本地时刻统一成 UTC"
    t = norm_time(1800, -5)
    assert t["utc"] == "2026-01-01T00:30:00Z"
    assert t["local"] == "2025-12-31T19:30:00-0500", "西五区本地串带偏移量可读"
    print("结果归一通过:时区统一 单位统一 货币统一 异构工具结果可合并")

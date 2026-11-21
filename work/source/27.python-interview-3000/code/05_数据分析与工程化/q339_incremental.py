import json
import os

STATE = "watermark.json"

def read_watermark(default="1970-01-01T00:00:00"):
    if os.path.exists(STATE):
        return json.load(open(STATE)).get("watermark", default)
    return default

def fetch_incremental(source_rows, watermark):
    """模拟按更新时间拉增量,生产上对应 SQL: WHERE updated_at > watermark"""
    return sorted(
        [r for r in source_rows if r["updated_at"] > watermark],
        key=lambda r: r["updated_at"],
    )

def apply_upsert(rows, table):
    for r in rows:
        table[r["id"]] = r             # 唯一键 upsert 兜底乱序重复

if __name__ == "__main__":
    source = [
        {"id": 1, "updated_at": "2026-11-01T01:00:00"},
        {"id": 2, "updated_at": "2026-11-01T02:00:00"},
        {"id": 1, "updated_at": "2026-11-01T03:00:00"},   # 同键更新
    ]
    table = {}
    wm = read_watermark()
    inc = fetch_incremental(source, wm)
    apply_upsert(inc, table)
    if inc:                             # 处理成功后才推进水位
        new_wm = inc[-1]["updated_at"]
        json.dump({"watermark": new_wm}, open(STATE, "w"))
    print("rows:", table, "watermark:", read_watermark())
    os.remove(STATE)

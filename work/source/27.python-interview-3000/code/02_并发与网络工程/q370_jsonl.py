"""JSON Lines 写入与流式读取统计。"""
import json


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")  # 一行一对象


def stream_stats(path):
    """逐行流式统计,内存占用与文件大小无关。"""
    total, bad, levels = 0, 0, {}
    with open(path, encoding="utf-8") as f:
        for line in f:  # 惰性迭代,不整读内存
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                rec = json.loads(line)
                # 合法 JSON 不一定是对象(裸字符串/数组/数字), 先校验再取字段
                if not isinstance(rec, dict):
                    bad += 1  # 非对象行按坏行隔离,不中断
                    continue
                levels[rec.get("level", "?")] = levels.get(rec.get("level", "?"), 0) + 1
            except json.JSONDecodeError:
                bad += 1  # 坏行隔离计数,不中断
    return total, bad, levels


if __name__ == "__main__":
    recs = [
        {"ts": "2026-11-01T10:00:00", "level": "INFO", "msg": "start"},
        {"ts": "2026-11-01T10:00:01", "level": "ERROR", "msg": "db down"},
        "这不是合法 JSON 行",  # 模拟写坏的行(裸字符串, JSON 合法但不是对象)
    ]
    write_jsonl("/tmp/app.jsonl", recs)
    print(stream_stats("/tmp/app.jsonl"))

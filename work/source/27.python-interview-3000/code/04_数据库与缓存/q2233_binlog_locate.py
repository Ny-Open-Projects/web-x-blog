"""误操作恢复的 binlog 定位: 纯概念模拟, 找事务边界取前镜像"""
events = [
    {"pos": 100, "ts": "10:00:01", "sql": "BEGIN"},
    {"pos": 120, "ts": "10:00:01", "sql": "UPDATE accounts SET balance=900 WHERE id=1",
     "before": {"id": 1, "balance": 1000}, "after": {"id": 1, "balance": 900}},
    {"pos": 180, "ts": "10:00:02", "sql": "COMMIT"},
    {"pos": 200, "ts": "10:01:00", "sql": "UPDATE accounts SET balance=0 WHERE id=1",
     "before": {"id": 1, "balance": 900}, "after": {"id": 1, "balance": 0}},   # 误操作
    {"pos": 260, "ts": "10:01:01", "sql": "COMMIT"},
    {"pos": 280, "ts": "10:02:00", "sql": "UPDATE accounts SET balance=5 WHERE id=2",
     "before": {"id": 2, "balance": 7}, "after": {"id": 2, "balance": 5}},
]

def locate(events, bad_ts):
    hits = [e for e in events if e["ts"] == bad_ts and "accounts" in e["sql"]]
    if not hits:
        return None
    pos = hits[0]["pos"]
    begin = max(e["pos"] for e in events if e["pos"] <= pos and e["sql"] == "BEGIN")
    commit = min(e["pos"] for e in events if e["pos"] > pos and e["sql"] == "COMMIT")
    return begin, commit

seg = locate(events, "10:01:00")
print("误操作事务边界: pos %d 到 %d" % seg)
bad = [e for e in events if e["ts"] == "10:01:00"][0]
b = bad["before"]
print("前镜像:", b, "-> 反向修复 SQL: UPDATE accounts SET balance=%d WHERE id=%d"
      % (b["balance"], b["id"]))
print("四步: 定位边界 取前镜像 隔离回放校验 幂等修复加审计, row 格式才有完整镜像")

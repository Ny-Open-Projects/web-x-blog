"""SCAN 断点续扫: 保存 cursor 让全量遍历任务可恢复"""
import json

def scan_once(store_keys, cursor, count=5):
    idx = cursor if cursor else 0           # cursor 0 表示从头开始
    chunk = store_keys[idx:idx + count]
    nxt = idx + count
    if nxt >= len(store_keys):
        nxt = 0
    return chunk, nxt

store = sorted("key:%04d" % i for i in range(100))

def scan_job(state=None):
    """全量遍历任务: cursor 进度可外部持久化, 崩溃后从断点续扫"""
    cursor = state.get("cursor", 0) if state else 0
    seen = set(state.get("seen", [])) if state else set()
    rounds = 0
    while True:
        chunk, cursor = scan_once(store, cursor)
        seen.update(chunk)
        rounds += 1
        if rounds == 7 and state is None:    # 首次运行模拟第 7 轮崩溃
            print(f"  第 {rounds} 轮后崩溃, 已处理 {len(seen)} 键, 保存 cursor={cursor}")
            return {"cursor": cursor, "seen": sorted(seen)}
        if cursor == 0:
            return {"cursor": 0, "seen": sorted(seen), "done": True}

s1 = scan_job()
print("断点状态样例:", json.dumps({"cursor": s1["cursor"], "seen_n": len(s1["seen"])}))
s2 = scan_job(state=s1)                      # 用保存的状态续扫
print(f"续扫完成: done={s2.get('done')}, 去重后键数 {len(set(s2['seen']))}, "
      f"覆盖全集: {set(s2['seen']) == set(store)}")
print("要点: cursor 是 opaque 数值, 只能续用不能解读; 遍历期间键可能增删, 结果可能重复需去重")
print("生产形态: cursor 与已处理集合落到 redis hash 或 DB, 定时任务每轮推进一段")

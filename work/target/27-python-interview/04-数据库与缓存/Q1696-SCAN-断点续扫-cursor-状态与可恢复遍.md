---
title: [Q1696] SCAN 断点续扫: cursor 状态与可恢复遍历
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1696 · SCAN 断点续扫: cursor 状态与可恢复遍历

> 难度:★★☆☆ | 标签:Redis, 遍历

**问**:用 SCAN 全量遍历上亿个 key,任务跑到一半挂了怎么办?

**答**:把 cursor 当作可持久化的进度水位:每轮 SCAN 返回新 cursor,任务把 cursor 连同已处理状态落到存储,恢复时从保存的 cursor 继续而不是从头再来。三个语义要牢记:cursor 是不透明数值,只能续用不能解读其含义;遍历期间集合会变化,结果可能重复也可能遗漏,消费端必须容忍(去重、配合定期重扫);cursor 持续推进直到再次返回 0 表示完整一圈。生产形态是定时任务每轮推进一段存进度,配合 HSCAN/SSCAN 清理大集合时同样适用,这是大 key 治理的标准工装。

```python
# file: code/04_数据库与缓存/q1696_scan_resume.py
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
```

**追问**:
- SCAN 期间大 key 被删除会怎样?——游标可能跳过或重复返回某些键,任务层面用"多扫几圈加对账"兜底,不能假设单圈精确。
- COUNT 参数是什么语义?——每轮的期望扫描量而非精确值,整个遍历的时间复杂度与集合大小无关,只与桶数相关。

---

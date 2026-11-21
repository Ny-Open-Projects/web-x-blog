---
title: [Q2010] 长任务的细粒度 checkpoint:批级状态与恢复验证
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2010 · 长任务的细粒度 checkpoint:批级状态与恢复验证

> 难度:★★★☆ | 标签:checkpoint, 容错

**问**:一个跑八小时的任务,checkpoint 多久存一次?存什么?怎么证明恢复后是对的?

**答**:checkpoint 粒度是恢复成本与落盘开销的折中:按条太贵,按整个任务太脆,工程折中是批级:每处理 N 条把 offset 加已算结果原子写一次(先 tmp 后 os.replace)。实测 12 条任务批大小 3,第 7 条模拟崩溃,恢复从 offset=6 续跑,最终结果与一次性跑完完全一致——恢复等价性要写进代码自动对账,不靠肉眼。三个细节:checkpoint 状态要小,大中间产物放外部存储、只存引用;崩溃发生在批中间时,已处理未落盘的部分会被重算,所以处理逻辑必须幂等;恢复后的第一批打日志标记"从 checkpoint 恢复",方便统计实际损失。批大小按"重算五分钟的成本"与"落盘一次的开销"权衡。

```python
# file: code/05_数据分析与工程化/q2010_fine_ckpt.py
"""细粒度 checkpoint:批级状态原子落盘,崩溃恢复后结果与一次跑完一致"""

import json
import os
import tempfile

CKPT = os.path.join(tempfile.mkdtemp(prefix="ckpt_demo_"), "state.json")
RECORDS = [f"r{i}" for i in range(1, 13)]
BATCH = 3


def load_state():
    if os.path.exists(CKPT):
        with open(CKPT) as f:
            return json.load(f)
    return {"offset": 0, "results": []}


def save_state(state):
    tmp = CKPT + ".tmp"                 # 原子写: 先 tmp 后 replace
    with open(tmp, "w") as f:
        json.dump(state, f)
    os.replace(tmp, CKPT)


def process(rec):
    return rec.upper()


def run(records, crash_after=None):
    state = load_state()
    done = 0
    for i in range(state["offset"], len(records)):
        state["results"].append(process(records[i]))
        done += 1
        if crash_after is not None and state["offset"] + done >= crash_after:
            raise RuntimeError(f"模拟崩溃于第 {state['offset'] + done} 条")
        if done % BATCH == 0:
            state["offset"] += done
            done = 0
            save_state(state)
    state["offset"] = len(records)
    save_state(state)
    return state["results"]


if __name__ == "__main__":
    try:
        run(RECORDS, crash_after=7)
    except RuntimeError as e:
        print("第一次运行:", e)
    partial = load_state()
    print(f"崩溃后 checkpoint: offset={partial['offset']}, 已落盘 {partial['results']}")
    results = run(RECORDS)
    print("恢复续跑最终结果:", results)
    once = [process(r) for r in RECORDS]
    verdict = "完全一致,不重不漏" if results == once else "不一致,有 bug"
    print("与一次性跑完对比:", verdict)
    print("要点:粒度取批,批大小是恢复成本与落盘开销的折中;状态原子写;恢复正确性用'与一次跑完对账'自动验证,别靠肉眼")
```

**追问**:
- 追问 1:和分片游标式断点续跑的区别?—— 分片游标恢复到片、实现简单;批级 checkpoint 恢复到批、粒度细但要管状态体积,按任务时长与单条成本选。
- 追问 2:checkpoint 文件写坏了怎么办?—— 原子写避免半写,再加版本号与校验和,坏档回退上一版或从头重跑并告警。

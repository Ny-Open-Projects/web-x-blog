---
title: [Q7668] Agent 记忆库膨胀检索退化复盘：越存越"记不住"
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7668 · Agent 记忆库膨胀检索退化复盘：越存越"记不住"

难度：P6-P7 | 标签：Agent、记忆系统、事故复盘

**问**：长期记忆 Agent 运行半年，记忆条数从 1 万涨到 80 万，同期"应回忆起关键偏好"的评测准确率从 92% 掉到 61%。复盘：为什么记忆越多反而越记不住？这条退化链的每个环节怎么修？

**答**：结论：退化链是"**只写不清 + 检索无治理**"：① 重复与过期记忆堆积——同一事实以不同措辞写入 N 次，检索时旧版本与新版本同场竞争；② 无淘汰——记忆只有增没有删，召回池被陈旧与噪声污染；③ 检索质量随库容下降——HNSW 检索本身不受库容影响（近似度可控），退化主要来自**排序**：top-k 里噪声占比上升，关键记忆排不进前 k。修复是"写入口径 + 记忆生命周期 + 检索排序"三段治理，本质是把记忆库当数据资产管理（Q2292 分级存储是结构视角，本卡是生命周期视角）。

取舍与实战：
1. 写入口径：写入前先检索——语义近似（cos > 0.92）且主体一致的存量为**更新合并**而非新插入，带来源与时间戳；条目结构化（主体-谓词-值 + 置信度）优于全文段落，天然可合并去重。
2. 生命周期：每条记忆带 TTL/置信度衰减——被命中即增强（ reinforcement），长期未命中且与近期行为矛盾则降级待清理；定期跑"记忆审计作业"（Q7135 清扫思路）：矛盾检测、孤儿清理、合并。
3. 检索排序修复：召回后重排（recency + 频次 + 置信度加权），关键偏好类记忆置顶；top-k 按"注入预算"（Q2566）截断而不是固定 k=10。
4. 评测是退化检测器：固定一组"应回忆"用例定期跑（写入 → 隔 N 轮 → 检索验证），准确率跌破基线即告警——本卡事故就是没有这个回归集，半年才被发现。

```python
"""记忆生命周期治理：写入合并 + 置信度衰减 + 检索重排（标准库演示）"""
from dataclasses import dataclass, field
import time


@dataclass
class Memory:
    subject: str          # 主体（用户/项目）
    pred: str             # 谓词（偏好/事实）
    value: str
    confidence: float = 0.8
    last_hit: float = field(default_factory=time.monotonic)
    hits: int = 0

def write_memory(store: dict[str, Memory], m: Memory, sim_threshold: float = 0.92):
    """写入前先检索：主体+谓词相同即合并更新，而非新插入"""
    key = f"{m.subject}|{m.pred}"
    old = store.get(key)
    if old and old.value != m.value:
        store[key] = Memory(m.subject, m.pred, m.value,
                            confidence=max(m.confidence, old.confidence))
    elif not old:
        store[key] = m
    return store

def rerank(cands: list[Memory], k: int = 5) -> list[Memory]:
    """召回后重排：置信度 × 近期命中衰减"""
    now = time.monotonic()
    scored = sorted(cands,
                    key=lambda m: m.confidence * (1 + m.hits) / (1 + (now - m.last_hit) / 86400),
                    reverse=True)
    return scored[:k]

store: dict[str, Memory] = {}
store = write_memory(store, Memory("u1", "editor", "vim"))
store = write_memory(store, Memory("u1", "editor", "neovim"))   # 合并更新
assert len(store) == 1 and store["u1|editor"].value == "neovim"
top = rerank(list(store.values()), k=3)
print("合并去重 OK, top:", [m.value for m in top])
```

**追问 1**：为什么"结构化条目"比"全文段落"更能抵抗膨胀？
**提示**：段落式记忆的"同一事实不同措辞"在向量空间距离不稳定（近似判断不可靠），去重失败率高；主体-谓词-值的键控结构让合并成为精确操作（key 相等即合并），膨胀源头被掐断。

**追问 2**：记忆置信度衰减会不会把"低频但关键"的记忆错杀？
**提示**：会——所以衰减要区分"类型"：偏好类低频但稳定应长 TTL，任务类短 TTL；错杀兜底是软删除（降级归档不物理删除，Q1408 归档思路），用户行为矛盾时可回捞。

## 背诵要点
- 退化链：只写不清（重复措辞）+ 无淘汰 + top-k 噪声占比上升；修 HNSW 没用，治排序与写入。
- 写入口径：先检索后写入，主体-谓词键控合并（结构化优于段落），带来源时间戳。
- 生命周期：命中增强、长期未命中降级、定期审计合并矛盾；"应回忆"评测集是退化告警器。

## 复盘追问
- 如何设计"应回忆"评测集的采样，使它能覆盖半年内各时段写入的记忆？
- 记忆合并的冲突策略（新旧值矛盾时信谁）如何结合来源可靠性加权？

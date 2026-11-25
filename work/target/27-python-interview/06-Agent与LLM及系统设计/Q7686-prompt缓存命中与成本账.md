---
title: [Q7686] prompt 缓存命中与成本账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7686 · prompt 缓存：命中一半输入半价，但你要先会"摆内容"

难度：P6 ｜ 标签：成本工程、prompt 缓存、上下文设计
基线：Anthropic prompt caching（写入 1.25×、命中 0.1×，5 分钟 TTL 滑动）；OpenAI 自动前缀缓存（命中 0.5×，隐式无标记）。

**问**：长系统提示 + RAG 文档的对话服务，账单显示输入 token 只有 20% 命中缓存。为什么命中率这么低？prompt 缓存的成本模型（写入溢价、命中折扣、TTL）怎么影响设计？

**答**：**结论**：prompt 缓存是**前缀精确匹配**：只有请求开头的连续相同 token 段能命中，命中率低的结构性原因几乎都是"**动态内容混进了前缀**"——时间戳、用户 ID、检索文档插在系统提示后面、每次都变的 few-shot。设计原则是**分层摆位**：静态最前（系统提示/工具定义）→ 半静态（few-shot 模板）→ 动态最后（检索结果/用户输入）。成本模型决定策略：Anthropic 写入 1.25×、命中 0.1×——**重用次数 ≥2 才划算**（1.25× 写一次 + n×0.1× < n×1× 的分界在 n≈2）；TTL 5 分钟滑动刷新，意味着**间隔短的高频会话**收益最大，低频长尾请求基本白写入。OpenAI 的自动前缀缓存无写入溢价、命中半价，但同样要求前缀稳定，且对 ≤1024 token 的前缀无效。

**取舍**：缓存设计与多租户/个性化的冲突：每个租户一个系统提示 → 前缀全不同 → 命中归零。解法是**模板公共化**——把租户差异收敛到尾部的少量 token（变量注入），让公共前缀最大化；代价是 prompt 表达力受限（差异只能通过变量表达）。另一取舍：动态检索文档若放中间，会"截断"后续所有内容的缓存资格——宁可牺牲文档排前的相关性收益，也要把动态段推到尾部。

**实战**：摆位与命中率账（标准库模拟）：

```python
# prompt 缓存账：摆位决定命中率，写入溢价决定划算分界
from dataclasses import dataclass

@dataclass
class CacheModel:
    write_premium: float   # 写入倍率 (Anthropic 1.25)
    hit_rate_mult: float   # 命中倍率 (Anthropic 0.1)
    ttl_s: int = 300

ANTHROPIC = CacheModel(1.25, 0.1)
OPENAI = CacheModel(1.0, 0.5)      # 无写入溢价，自动前缀缓存

def break_even_uses(m: CacheModel) -> float:
    """重用 n 次: n*0.1*+1.25 < n*1 -> n > 1.25/0.9"""
    return m.write_premium / (1 - m.hit_rate_mult)

print(f"Anthropic 写入 1.25x/命中 0.1x -> 重用 >{break_even_uses(ANTHROPIC):.2f} 次才划算")
print(f"OpenAI 无写入溢价/命中 0.5x -> 任何重用都划算\n")

# 摆位账：动态内容位置 vs 可缓存 token 数
def layout_tokens(sys_t: int, shots_t: int, rag_t: int, user_t: int,
                  dynamic_in_middle: bool) -> tuple[int, int]:
    """返回 (总 token, 可缓存 token)。动态段截断其后所有缓存资格。"""
    total = sys_t + shots_t + rag_t + user_t
    if dynamic_in_middle:            # RAG 插在中间（反模式）
        cacheable = sys_t            # 只有系统提示可命中
    else:                            # 动态全在尾部（正确摆位）
        cacheable = sys_t + shots_t
    return total, cacheable

total_good, cache_good = layout_tokens(2000, 800, 3000, 300, False)
total_bad, cache_bad = layout_tokens(2000, 800, 3000, 300, True)
print(f"正确摆位: {cache_good}/{total_good} 可缓存（{(cache_good/total_good)*100:.0f}%）")
print(f"RAG 插中间: {cache_bad}/{total_bad} 可缓存（命中率崩到 {(cache_bad/total_bad)*100:.0f}%）\n")

# 月度账：50% vs 90% 命中率的差异
IN_PRICE, daily_tokens, cacheable_ratio = 2.5 / 1e6, 200_000_000, 0.62
for hit in (0.2, 0.5, 0.9):
    cost = daily_tokens * cacheable_ratio * (
        (1 - hit) * 1 + hit * ANTHROPIC.hit_rate_mult) * IN_PRICE
    cost += daily_tokens * (1 - cacheable_ratio) * IN_PRICE
    print(f"命中率 {hit*100:.0f}% -> 输入月费 {cost*30:,.0f} 元")
```

**追问 1**：TTL 5 分钟滑动刷新对会话型应用意味着什么？
提示：每次请求刷新 TTL，秒级间隔的多轮对话全程命中；间隔超 5 分钟的会话每次都要重写入（1.25×）——低频场景要么放弃缓存要么缩短前缀。

**追问 2**：工具定义（tools）应该放前缀的哪个位置？为什么？
提示：紧跟系统提示且**保持 JSON 序列化稳定**——工具列表动态增删会立刻击穿缓存；版本化的工具集（固定排序、禁止动态注入时间戳）是缓存的先决条件。

**追问 3**：怎么度量缓存的真实收益而不被账单口径骗？
提示：看供应商返回的 `cache_read_input_tokens`/`cache_creation_input_tokens` 明细，计算"有效折扣率 = 节省金额/理论全价"；只看总 token 数会把写入溢价算漏。

## 背诵要点
1. 前缀精确匹配是铁律：动态内容（时间戳/RAG/租户变量）必须放尾部，插中间就截断其后所有缓存资格。
2. 成本模型决定策略：Anthropic 写 1.25×/命中 0.1×（重用 >1.25 次才划算，TTL 5 分钟滑动）；OpenAI 无写入溢价/命中 0.5×。
3. 度量看明细字段（cache_read/creation tokens）算有效折扣率，别只看总 token；工具集要版本化固定排序防击穿。

## 复盘追问
1. 你们的 prompt 里有哪些"不知不觉混进前缀"的动态内容（时间戳？A/B 标记？租户名）？是谁的代码写进去的？
2. 多租户模板公共化改造做过吗？租户差异收敛到变量后，产品侧有没有抱怨过"个性化能力受限"？

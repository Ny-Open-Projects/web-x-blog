---
title: [Q7534] System Prompt 瘦身：每 token 的行为价值与缓存结构
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7534 · 8K token 的 System Prompt：怎么瘦身才不砍到骨头？

> 难度:★★★ | 标签:成本工程, Prompt 优化, prefix caching

**问**：System prompt 越写越长（人设 + 规则 + few-shot + 工具说明 8K token），成本和延迟都扛不住。瘦身的实测方法是什么？哪些 token 绝对不能删？"每 token 行为价值"怎么量化？prefix caching 与 prompt 结构怎么配合？

**答**：结论：system prompt 是**每请求重复计费**的最贵常量——8K token 在 10 QPS 下每天就是数万美元级账单。瘦身纪律三步：① 段分类审计（安全/工具 schema = 不可删的 essential；约束类高保护；描述性文字优先删）；② **删一段测一次**——每删一段跑黄金集回归，质量不降才保留删除；③ 结构对齐缓存——稳定前缀（system + 工具 schema）启用 prefix caching，动态内容放后缀，缓存命中价约 1/10。

机理与实战：
- **每 token 行为价值 = 删掉后质量分下降 ÷ token 数**：安全规则、输出格式、工具调用约束的价值密度最高（删了行为立刻漂移）；人设故事、领域介绍是"背景描写"，删 1500 token 质量分几乎不动。瘦身按价值密度从低到高删，遇质量底线即停。
- **实测方法**：token 计数用与供应商一致的 tokenizer（别用近似估）；质量回归用固定黄金集 + LLM-as-judge（Q7501）；新旧 prompt 用同一批请求做 win-rate 对比再全量。
- **caching 的字节级要求**：前缀按字节匹配，prompt 里改一个时间戳、一个随机 id 都会让整段缓存失效——system 模板要版本化、稳定化，把"当天日期"这类易变内容移到用户消息。
- **few-shot 的边际递减**：示例超过 2-3 个后质量增益趋平而 token 线性增长，且互相矛盾的示例比没有示例更糟——优先删第二个之后的示例。

```python
# 基线:Python 3.10+;纯标准库模拟 system prompt 瘦身的成本账与回归门禁
# 真实场景:段分类审计 -> 逐段删除+黄金集回归 -> 前缀缓存结构对齐
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Segment:
    name: str
    tokens: int
    kind: str                    # constraint(约束) / persona(描述) / fewshot(示例)
    behavior: float              # 该段对质量分的贡献(实测:删了掉多少分)
    essential: bool = False      # 不可删段(安全规则/工具 schema)


def daily_cost(tokens: int, qps: float, price_per_mtok: float,
               cache_discount: float = 1.0) -> float:
    """system prompt 每请求重复计费(缓存命中按折扣价)。"""
    return tokens * qps * 86400 / 1e6 * price_per_mtok * cache_discount


def prune(segments: list[Segment], budget_tokens: int,
          quality_floor: float) -> tuple[list[str], float]:
    """贪心瘦身:优先删'每 token 质量贡献'最低的段,质量分不过线即停。"""
    kept = list(segments)
    removed: list[str] = []
    quality = sum(s.behavior for s in kept)
    while sum(s.tokens for s in kept) > budget_tokens:
        # essential 段不参与;约束类给 5 倍保护权重
        ranked = sorted((s for s in kept if not s.essential),
                        key=lambda s: s.behavior / (s.tokens *
                                                    (5 if s.kind == "constraint" else 1)))
        if not ranked:
            break                                 # 只剩不可删段
        victim = ranked[0]
        if quality - victim.behavior < quality_floor:
            break                                 # 再删就破质量底线 -> 停手
        kept.remove(victim); removed.append(victim.name)
        quality -= victim.behavior
    return removed, quality


def demo() -> None:
    segs = [
        Segment("safety_rules", 600, "constraint", 30, essential=True),
        Segment("tool_schema", 1200, "constraint", 25, essential=True),
        Segment("output_format", 400, "constraint", 20),
        Segment("persona_story", 1500, "persona", 6),
        Segment("few_shot_1", 1800, "fewshot", 12),
        Segment("few_shot_2", 1800, "fewshot", 9),
        Segment("domain_intro", 1200, "persona", 4),
    ]                                            # 共 8500 token
    total = sum(s.tokens for s in segs)
    cost_raw = daily_cost(total, qps=10, price_per_mtok=3.0)
    print(f"瘦身前 {total} token:每天 system 计费 ${cost_raw:.0f}(10 QPS) ✅")

    removed, quality = prune(segs, budget_tokens=4000, quality_floor=60)
    kept_tokens = total - sum(s.tokens for s in segs if s.name in removed)
    cost_new = daily_cost(kept_tokens, qps=10, price_per_mtok=3.0)
    cost_cached = daily_cost(kept_tokens, qps=10, price_per_mtok=3.0, cache_discount=0.1)
    print(f"删除 {removed} -> {kept_tokens} token,质量 {quality:.0f} 分(线 60) ✅")
    print(f"成本 ${cost_raw:.0f} -> ${cost_new:.0f}/天,前缀缓存命中后 ${cost_cached:.0f}/天 ✅")
    assert cost_new < cost_raw * 0.55
    assert "safety_rules" not in removed and "tool_schema" not in removed
    print("essential 段(安全/工具 schema)全部保留 —— 每 token 行为价值最高 ✅")
    print("结构纪律:稳定前缀(system+工具 schema)启用 prefix caching,动态历史放后缀")


if __name__ == "__main__":
    demo()
```

**追问一**：为什么"约束类 token"比同样长度的描述性文字价值高得多？
答：token 的价值在于"改变输出行为的概率"——一条"输出必须是 JSON 且字段如下"的 50 token 约束，决定每次输出的结构合法性；1500 token 的人设描写可能只影响语气。删错一行的代价不对称：格式约束丢失 = 下游解析全线崩，人设丢失 = 语气略变。

**追问二**：prompt caching 命中率上不去，常见原因有哪些？
答：前缀不稳定（模板里嵌了日期/用户名/会话 id）、动态内容混进前缀（检索结果放 system）、多端点版本不一致（同一 system 存在两个微小差异版本分摊缓存）、TTL 过短流量稀疏——逐项排查：把前缀字节序列 hash 后看分布，两个 hash 就意味着两份缓存各占一半。

## 背诵要点
- System prompt 每请求重复计费，是最贵的常量；瘦身 = 段分类审计 + 删一段测一次（黄金集回归）+ 结构对齐前缀缓存。
- essential 不可删段：安全规则、工具 schema；价值密度排序：约束 > few-shot（2-3 个封顶）> 描述性文字。
- 缓存按字节匹配：模板版本化、易变内容（日期/id）移出前缀；命中价约 1/10，结构改对比删字更省钱。

## 复盘追问
- 瘦身后偶发"输出格式漂移"，怎么定位是删了哪段？（提示：黄金集分维度回归——格式类指标单独看，对齐被删段清单；格式约束可能需要补成 essential）
- 如何给业务方算清"这次瘦身的 ROI"？（提示：成本账（重复计费 × QPS）、延迟账（TTFT 与首包）、质量账（黄金集回归分）三张表，缺质量账的瘦身报告不予通过）

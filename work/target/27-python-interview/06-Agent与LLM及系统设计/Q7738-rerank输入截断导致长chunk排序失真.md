---
title: "[Q7738] rerank 只吃前 512 token：长 chunk 的后半段等于没参与排序"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7738 · rerank 只吃前 512 token：长 chunk 的后半段等于没参与排序

难度：P7 ｜ 标签：rerank、cross-encoder、截断策略、RAG 排序

基线：Python 3.12；cross-encoder `max_length=512`、tokenizer `truncation` 策略；纯 Python 模拟截断窗口。

**问**：rerank 模型（cross-encoder）输入上限 512 token，我们的 chunk 平均 800 token。压测发现"答案在 chunk 后半段"的 query 排序很差，把 chunk 截到 400 token 后 recall 反而上升。rerank 不是看全文吗？

**答**：
- **结论**：cross-encoder 的输入是 `[query, passage]` 拼接，超过 `max_length` 会被 **tokenizer 静默截断**（`truncation=True`，策略可能是 `longest_first` 按比例砍，也可能是只保一侧）。被截掉的部分对打分**没有任何贡献**，等于"不存在"。chunk 越长，被截比例越高，长文档系统性吃亏，而这批文档恰好是信息密度最高的。
- **取舍**：截断是硬约束（模型有上限），策略可选：`only_first` 保 query（本来就短，等于把 passage 砍得更狠）、`only_second` 保 passage、`longest_first` 按比例砍、或**提前把 chunk 切到 ≤ 上限**。chunk 小 → 粒度细、上下文碎片化；chunk 大 → rerank 丢尾部、生成噪声多。常见折中：chunk 256~512 token + overlap，rerank 不再截断。
- **实战**：① 统计 `len(tokenizer(chunk).input_ids)` 分布，P95 必须 ≤ `max_length`；② 显式指定 truncation 策略并记录被截比例；③ 超长 chunk 用"分段打分取 max / 加权池化"，而不是直接砍；④ 评测集必须包含"答案在尾部"的样本，否则发现不了；⑤ 截断比例进监控，超过 5% 报警。

```python
"""rerank 截断策略对比：答案在尾部时，头部截断会把相关文档判死。"""
MAX_LEN = 512
QUERY = ["退款"]


def score_window(kept: list[str], base: float) -> float:
    """玩具 cross-encoder：命中 query 词得满分，否则只有底分。"""
    hits = sum(1 for t in kept if t in QUERY)
    return base + (1.0 - base) * (hits / len(QUERY))


def truncate_head(tokens: list[str], n: int = MAX_LEN) -> list[str]:
    return tokens[:n]                       # 只保头部


def truncate_tail(tokens: list[str], n: int = MAX_LEN) -> list[str]:
    return tokens[-n:]                      # 只保尾部（only_second 的极端版）


def truncate_uniform(tokens: list[str], n: int = MAX_LEN) -> list[str]:
    """按比例抽样：保留全文覆盖，但会切断局部连续性、可能漏掉关键词。"""
    if len(tokens) <= n:
        return tokens
    step = len(tokens) / n
    return [tokens[min(len(tokens) - 1, int(i * step))] for i in range(n)]


def chunk(n_filler: int, answer_pos: int | None, tag: str) -> list[str]:
    tokens = [f"f{i}" for i in range(n_filler)]
    if answer_pos is not None:
        tokens[answer_pos] = "退款"          # 只有相关段落才埋 query 词
    tokens.insert(0, tag)
    return tokens


if __name__ == "__main__":
    docs = {
        "docA": chunk(800, 700, "退款政策说明"),     # 相关，但答案在 700/800 位置
        "docB": chunk(300, None, "配送时效"),
        "docC": chunk(260, None, "发票流程"),
        "docD": chunk(200, None, "会员权益"),
        "docE": chunk(180, None, "账户安全"),
    }
    base = {"docA": 0.25, "docB": 0.45, "docC": 0.40, "docD": 0.35, "docE": 0.30}

    for name, fn in {"head": truncate_head, "tail": truncate_tail,
                     "uniform": truncate_uniform}.items():
        scored = [(k, score_window(fn(v), base[k])) for k, v in docs.items()]
        scored.sort(key=lambda kv: -kv[1])
        top1 = scored[0][0]
        print(f"{name:<8} top1={top1} 命中={top1 == 'docA'} "
              f"分数={[round(s, 2) for _, s in scored]}")

    # 把 chunk 切到 rerank 上限以内：答案不会再被截掉
    short = chunk(400, 380, "退款政策说明")
    print("切成 400 token 后 head 截断仍保留答案:", "退款" in truncate_head(short))

    for key, tokens in docs.items():
        kept = truncate_head(tokens)
        print(f"  {key}: {len(tokens)} token, head 截掉 {1 - len(kept) / len(tokens):.0%}")

    print("结论：截断策略决定长文档生死；chunk 尺寸按 rerank 上限倒推，别让尾部白写")
```

**追问一**：为什么 `only_first` 可能更糟？
→ 解析：拼接顺序通常是 `[CLS] query [SEP] passage`，`only_first` 保的是 query（本来就几十 token），超长部分全从 passage 砍，等于把文档截得更短。要保证据就用 `only_second`，要均衡就用 `longest_first` 或先切 chunk。

**追问二**：cross-encoder 和 bi-encoder 的截断影响为什么不同？
→ 解析：bi-encoder 分别编码 query 和 doc，doc 超长只是丢尾部信息，向量仍能代表整体（池化后）；cross-encoder 是联合编码，截断直接改变 attention 可见范围，对"需要跨句推理"的样本影响大得多，也更难通过调阈值补救。

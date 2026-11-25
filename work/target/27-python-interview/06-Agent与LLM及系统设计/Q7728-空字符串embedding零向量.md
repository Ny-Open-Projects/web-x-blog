---
title: "[Q7728] 空字符串的 embedding：零向量让相似度变成 NaN"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7728 · 空字符串的 embedding：零向量让相似度变成 NaN

难度：P6 ｜ 标签：embedding、零向量、余弦相似度、RAG

基线：Python 3.12；OpenAI/text-embedding、BGE 等；纯 Python 实现余弦相似度。

**问**：知识库入库时没过滤空 chunk，某些 PDF 解析出来是空字符串/纯空白，embedding 接口返回了全零向量或直接报错。检索时这些空文档偶尔排在最前面，`score` 显示 `nan`；排序结果每次还不一样。零向量为什么会让余弦相似度失效？入库和查询两侧该怎么防？

**答**：
- **结论**：余弦相似度 = `dot(a,b) / (||a|| * ||b||)`，零向量的模长为 0，分母为 0 → 结果 `nan`（或除零异常）。`nan` 与任何数比较都返回 False，排序算法的行为取决于实现（可能排最前、最后或位置随机），于是"空文档霸榜"且不可复现。部分模型对空输入返回零向量，部分直接报 400，必须在**入库前**和**查询前**两侧都拦。
- **取舍**：过滤空文本最简单，但会丢掉"只有空白/标点/图片占位"的块，需要定义最小有效长度与语言相关规则；用 `eps` 平滑分母能避免 NaN，但零向量与任何向量的相似度都变成 0，仍会污染 top_k（只是不再 NaN）。更稳的是**不把零向量写进索引**，查询侧空输入直接返回空结果而不是硬算。
- **实战**：① 入库前 `text.strip()` 后判长度、去纯标点/纯空白，记录被丢弃数量；② 写入前校验向量模长 > 0，否则拒绝并告警；③ 查询空串直接短路返回空列表，不要调用 embedding；④ 对 `nan`/`inf` 分数做兜底过滤，并在评估里统计"零向量文档占比"。

```python
"""零向量导致余弦相似度 NaN，以及入库/查询两侧的防护。"""
import math


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return float("nan")          # 真实库可能直接抛 ZeroDivisionError
    return dot / (na * nb)


def is_valid_text(text: str, min_chars: int = 2) -> bool:
    stripped = text.strip()
    return len(stripped) >= min_chars and any(ch.isalnum() for ch in stripped)


def embed(text: str) -> list[float]:
    # 简化：空/纯空白 -> 零向量
    return [0.0, 0.0, 0.0] if not text.strip() else [1.0, float(len(text) % 3), 0.5]


if __name__ == "__main__":
    query = [1.0, 0.0, 0.5]
    docs = ["", "   ", "!!!", "python 面试", "rag 检索"]
    print("入库过滤:")
    kept = []
    for d in docs:
        vec = embed(d)
        norm = math.sqrt(sum(x * x for x in vec))
        ok = is_valid_text(d) and norm > 0
        print(f"  {d!r:<14} 有效={ok} 模长={norm:.1f}")
        if ok:
            kept.append((d, vec))

    print("检索分数:")
    for d, vec in kept:
        print(f"  {d}: {cosine(query, vec):.3f}")

    zero = embed("")
    score = cosine(query, zero)
    print("零向量分数:", score, "isnan:", math.isnan(score))
    print("排序含 nan:", sorted([0.9, score, 0.5], reverse=True),
          "-> 位置取决于实现，不可复现")
```

**追问一**：为什么有的 embedding 模型对空串返回零向量，有的直接报错？
→ 解析：取决于模型/tokenizer 与 API 实现：空串经过 tokenizer 可能变成 `[CLS] [SEP]` 两个特殊 token，仍能算出非零向量；也可能被判定为非法输入直接 400。零向量通常是"池化层没有有效 token"时的退化结果。不能假设某家 API 的行为，必须在适配层统一兜底。

**追问二**：用 `eps` 平滑分母后不再 NaN，问题就解决了吗？
→ 解析：没有。零向量与任何向量的余弦都变成 0，它仍会占据 top_k 的名额（尤其当所有真实分数也为负/接近 0 时），并且写进索引会浪费空间、干扰 ANN 图。正确做法是**不写入零向量**，而不是在打分时掩盖。

**追问三（可选）**：纯图片/表格页解析出的空文本块，除了过滤还能怎么处理？
→ 解析：可以对这类页做 OCR 或版面描述后再嵌入，或单独建"多模态索引"；至少要保留原文指针与页码，避免"文档存在但检索不到"的静默缺失。过滤要记录丢弃原因与数量，作为解析质量指标。

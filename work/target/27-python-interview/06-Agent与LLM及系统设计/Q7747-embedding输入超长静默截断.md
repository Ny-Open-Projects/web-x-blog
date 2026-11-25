---
title: "[Q7747] 1200 字的 chunk 只嵌入前 512 token，后半段等于没入库"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7747 · 1200 字的 chunk 只嵌入前 512 token，后半段等于没入库

难度：P7 ｜ 标签：RAG、embedding、输入截断、召回

基线：Python 3.12；字符级 token 化 + 哈希分桶向量，模拟 embedding 模型的 max tokens 截断。

**问**：文档切块按 1200 字切（overlap 100），embedding 模型上下文是 512 token。入库脚本直接 `embed(chunk)`，没报错。上线后发现：合同类文档前半段（甲乙方、金额）问得准，后半段（违约责任、退款条款）几乎问不到；把整篇文档换个顺序重切，又变成另一部分能查到。模型不是号称支持 512 token 吗，超了为什么不报错？

**答**：
- **结论**：多数 embedding 接口**超长静默截断**（取前 N 个 token），不报错也不提示。1200 字的中文大约 800~1200 token，后 300~700 token 根本没参与向量计算——它们对检索来说"不存在"。所以"能查到哪一段"取决于内容在 chunk 里的**位置**，而不是语义重要性；重切改变位置，可检索的部分就跟着变。
- **取舍**：① **按模型的 token 上限切块**，中文留安全余量（512 token 的模型，按"1 字≈1 token"保守估算建议 240~300 字/chunk），用模型自己的 tokenizer 计数而不是 `len(text)`；② 保留 overlap 但不要靠 overlap 掩盖截断——overlap 只解决边界语义，不解决"后半段没入库"；③ 长文档用"小块检索 + 父块生成"（小块保证嵌入完整，返回时取父块给 LLM），而不是把大块硬塞进 embedding；④ 入库前做**截断检测**：`token_count > limit` 直接拒绝或拆分，不要交给模型静默处理。
- **实战**：① 用真实 tokenizer 统计每个 chunk 的 token 数分布，P99 必须 < 上限；② 抽样验证：对 chunk 的**最后一句**构造查询，看能否召回该 chunk——这是最直接的自检；③ 评测集要覆盖"答案位于文档末尾"的样本，否则永远发现不了；④ 换 embedding 模型时（维度/上限都可能变）必须全量重嵌入并重跑评测。

```python
"""超长 chunk 被静默截断：尾部内容对检索不可见。"""
import math

MODEL_MAX_TOKENS = 256          # 假设模型上限 256 个"字符 token"
DIMS = 512


def tokenize(text: str) -> list[str]:
    return list(text)           # 简化：一个汉字 = 一个 token


def embed(text: str) -> list[float]:
    toks = tokenize(text)[:MODEL_MAX_TOKENS]      # 关键：静默截断
    vec = [0.0] * DIMS
    for t in toks:
        vec[ord(t) % DIMS] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


HEAD = ("本合同由甲方与乙方于 2026 年签订，配送时效为次日达，"
        "配送范围仅限一线城市，超区需另付运费。") * 26
TAIL = "退款条款：签收后 7 天内可申请退款，原路退回，3 个工作日到账。违约责任按日万分之五计。"
CHUNK = HEAD + TAIL

if __name__ == "__main__":
    query = "退款多久到账"
    qv = embed(query)

    full_chunk = CHUNK
    truncated_len = MODEL_MAX_TOKENS
    print("chunk 字符数:", len(CHUNK), "| 模型上限:", MODEL_MAX_TOKENS)
    print("被丢掉的比例: %.0f%%" % ((1 - truncated_len / len(CHUNK)) * 100))
    print("'退款条款' 起始位置:", CHUNK.index("退款条款"),
          "-> 远在截断点之后，没进向量")

    sim_truncated = cosine(qv, embed(CHUNK))
    sim_small = cosine(qv, embed(TAIL))     # 正确切块：含退款条款的小块
    print("\n余弦相似度:")
    print("  1293 字大块（截断后入库）:", round(sim_truncated, 4))
    print("  只含退款条款的小块      :", round(sim_small, 4))
    print("  阈值 0.30 下是否召回    :",
          sim_truncated >= 0.30, "/", sim_small >= 0.30)

    # 入库前自检：token 数必须 <= 上限
    def check(chunk: str) -> str:
        n = len(tokenize(chunk))
        return "ok" if n <= MODEL_MAX_TOKENS else f"超长 {n}>{MODEL_MAX_TOKENS}，必须拆块"

    print("\n入库检查:", check(CHUNK))
    print("按 240 字切块后:", [check(CHUNK[i:i + 240]) for i in range(0, len(CHUNK), 240)])
    print("结论：embedding 的截断是静默的；切块大小必须按 tokenizer 的真实上限来定")
```

**追问一**：加 overlap 能不能缓解"后半段没入库"？

→ 解析：只能缓解**边界**问题，缓解不了整体截断。overlap 的作用是让跨块的句子在相邻两块里都出现，避免"一句话被切断后语义不全"；但如果每块本身 1200 字、上限 512 token，overlap 100 字只是让被丢掉的 80% 换了个位置。要让尾部内容可检索，必须让**每一块都短于上限**，或者对长块做"摘要 + 多向量"（一个 chunk 存多个向量，分别覆盖不同段落）。

**追问二**：为什么不能用 `len(text)` 估 token 数？

→ 解析：tokenizer 不是按字符切：英文一个词可能 1~3 token，中文常见 1 字 1~2 token，emoji/代码/URL 的膨胀率完全不同。用字符数估算，中文可能低估（以为 500 字 = 500 token，实际 700），英文可能高估。可靠做法是直接调用模型的 tokenizer（`tiktoken`、`tokenizers` 库）或 API 返回的 usage；离线批量入库时对每个 chunk 计数并记录分布，超过上限的块直接拆，而不是让它静默截断。

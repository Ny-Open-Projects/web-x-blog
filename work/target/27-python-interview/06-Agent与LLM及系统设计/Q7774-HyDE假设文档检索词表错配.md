---
title: "[Q7774] 口语 query 搜不到书面文档：HyDE 假设文档检索的词表错配修复"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7774 · 口语 query 搜不到书面文档：HyDE 假设文档检索的词表错配修复

难度：P6 ｜ 标签：HyDE、假设文档、检索召回、词表错配、RAG

基线：Python 3.12；用词袋 + IDF 余弦模拟检索，复现口语 query 与文档词表零重叠导致的召回失败，以及 HyDE 扩展修复，全标准库实跑。

**问**：用户搜"服务怎么发版"，正确文档写的是"上线发布步骤"——零词重叠，向量检索照样漏召回。查询和文档的词表错配（vocabulary mismatch）为什么是召回第一杀手？HyDE（Hypothetical Document Embeddings）是怎么用"先编一份假答案"修复召回的？代价与适用边界是什么？

**答**：
- **结论**：词表错配的本质：**query 和文档是两种文体**——用户写口语（"弄上去""发版"），文档写书面语（"部署""上线发布"），表层词重叠趋近于零；密集向量模型能缓解但不能消灭错配（领域冷门词、新术语的 embedding 质量差），稀疏检索（BM25）更是完全依赖词重叠。HyDE 的做法：**让 LLM 先根据 query 生成一份"假设的完美答案"（hypothetical document），用这份假设文档的向量去检索**——假设答案天然使用文档的文体与词表（模型读过同领域的文档），与真实文档的向量距离大幅拉近，本卡用词袋模拟出同样的效果：零重叠的口语 query 经 HyDE 扩展后命中正确文档。它在数学上等价于一次"领域词表翻译"，把 query 搬进文档的语言体系。
- **取舍**：① 代价是每次查询多一次生成（延迟 +100~500ms、成本 +1 次调用）——高频头部 query 不值得（缓存与同义改写已覆盖），**冷门长尾 query 才是 HyDE 的主场**（长尾 query 的错配率最高且没有缓存兜底）；② 假设答案是模型"编"的，可能编错领域（把"部署"理解成 AI 模型部署而不是服务发布）——编错方向会带偏检索，需要 query 意图路由兜底（Q2855 分级路由）；③ 与多查询扩展（Q1191）的选择：多查询是"换几种问法"（同文体多次采样），HyDE 是"写一份答案"（跨文体翻译）——召回缺口在文体时用 HyDE，在表述歧义时用多查询，两者可组合；④ 索引侧的替代方案：入库时预先为每文档生成"潜在问题列表"一起索引（QHD，效果近似 HyDE 但查询时零生成成本）——**把翻译成本从查询时挪到入库时**，高 QPS 场景优先。
- **实战**：① 召回缺口诊断先行：badcase 按"检索不到 vs 检索到了没排上"分桶（Q1200 归因），只有"检索不到"桶里词重叠为零的才上 HyDE；② HyDE 的假设答案要限制篇幅（100~200 token）——太长会稀释 query 原有的强信号词；③ 评测：HyDE 开启前后跑同一检索评测集，盯"top-1 召回率"与 P99 延迟双指标；④ 假设答案生成失败（模型拒答/超时）的降级路径：直接用原 query 检索，不阻塞主链路。

```python
"""Q7774 HyDE 假设文档检索: 先让模型'编'一份假设答案再拿它去检索, 拉近词表差距。"""
from math import log

# 简化检索: 词袋向量 + 余弦
DOCS = {
    "d1": "部署服务到生产环境 需要先安装依赖 再配置环境变量 然后重启进程",
    "d2": "退货流程 用户在订单页申请 仓库收货后 退款原路返回",
    "d3": "上线发布步骤 构建镜像 推送仓库 滚动更新 灰度验证",
}
TOKENS = {d: set(doc.split()) for d, doc in DOCS.items()}
IDF = {t: log(len(DOCS) / (1 + sum(t in tk for tk in TOKENS.values())))
       for t in set().union(*TOKENS.values())}


def embed(text: str) -> dict[str, float]:
    return {t: (1 + log(text.split().count(t))) * IDF.get(t, 0)
            for t in set(text.split()) if t in IDF}


DOC_EMB = {d: embed(doc) for d, doc in DOCS.items()}


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    common = a.keys() & b.keys()
    dot = sum(a[t] * b[t] for t in common)
    na = sum(v * v for v in a.values()) ** 0.5
    nb = sum(v * v for v in b.values()) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def retrieve(query: str, topk: int = 1) -> list[str]:
    qv = embed(query)
    return sorted(DOCS, key=lambda d: -cosine(qv, DOC_EMB[d]))[:topk]


def hyde_expand(query: str) -> str:
    """模拟 LLM 生成的假设文档: 展开 query 缺的领域词表."""
    hypothesis = ("发版的完整流程是: 上线发布 构建镜像 推送仓库 滚动更新 灰度验证, "
                  "服务发布要保证回滚方案")
    return query + " " + hypothesis


if __name__ == "__main__":
    query = "服务怎么发版"                     # 口语 query: 只与 d1 重叠"服务", 正确目标其实是 d3
    naive = retrieve(query)
    expanded = retrieve(hyde_expand(query))
    overlap = set(query.split()) & set().union(*TOKENS.values())
    print(f"query 词表重叠: {sorted(overlap) or '无(零重叠)'} -> 零重叠时排序退化为字典序, naive 命中 d1 属于运气")
    print(f"naive 检索 top1 : {naive[0]} ({DOCS[naive[0]][:12]}...)")
    print(f"HyDE  检索 top1 : {expanded[0]} ({DOCS[expanded[0]][:12]}...)")
    ok = naive[0] == "d1" and expanded[0] == "d3"
    print(f"校验: HyDE 修复词表错配召回 -> {'通过' if ok else '异常'}")
    print("结论：口语 query 与书面文档词表错配是召回第一杀手;")
    print("      HyDE 用'假设答案'补词表, 代价是每次查询多一次生成, 适合冷门长尾 query")
```

**追问一**：HyDE 的假设答案"编错了领域"怎么办？这和查询改写（Q1191）的风险有什么不同？

→ 解析：假设答案错编的方向取决于模型对 query 的**意图判断**："部署"可以是服务部署、AI 模型部署、代码部署——模型选错分支，生成的假设文档就整体偏向错误领域，检索被系统性带偏（而且偏得很像"正常检索结果"，比空结果更难发现）。Q1191 多查询扩展的风险形态不同：它换几种问法，问法之间意图漂移但**单条 query 仍是 query 文体**，错误的影响是"混入噪声 query"，融合排序（RRF）里噪声被稀释；HyDE 的错误是"一份高权重的错误文体文档"，在余弦排序里就是主导信号。防御：① 意图分级前置（Q2855）：先小模型判意图分支，HyDE 提示里带上分支约束（"这是服务发版问题，假设文档要写部署流程"）；② 假设文档 + 原 query 双路检索融合（RRF 加权，原 query 保底）：HyDE 错编时原 query 的信号不被淹没；③ 抽检：HyDE 生成的假设文档抽样进评测，错编率 >10% 时降级为多查询扩展。核心认知：HyDE 是"用生成能力换检索召回"，生成不稳则检索跟着不稳——它的可靠性上限就是那次生成的可靠性。

**追问二**：为什么"入库时预生成潜在问题"（QHD）在高 QPS 场景下优于查询时 HyDE？两方案的索引膨胀账怎么算？

→ 解析：QHD（questions-documents）把 HyDE 的"文体翻译"从查询时挪到入库时：每篇文档入库时用 LLM 生成 N 个"用户可能会怎么问它"的问题，问题向量与文档一起入索引——查询时直接拿原 query 检索，零生成成本、零额外延迟。代价转移成**索引膨胀**：每文档多 N 条向量（N=3~5 时索引体积 ×4~6），embedding 计算成本在入库时一次性付出。两方案的决策面：① 查询分布：QPS 高且文档集合相对静态 → QHD（翻译成本被摊薄到每一次查询上收益最大）；文档天天变（新闻、工单流）→ 查询时 HyDE（入库预生成追不上更新频率）；② 成本结构：QHD 的成本 = 文档数 × N 次生成（入库期集中）；HyDE = QPS × 1 次生成（持续），月成本要按流量画像算——长尾 query 占比高、总量大的场景，QHD 的边际成本优势明显；③ 新鲜度：HyDE 天然适配新文档（无需预处理），QHD 需要入库管线配合（漏生成的新文档检索质量打折）。工程上常见的终态是混合：高频域预生成 QHD，长尾新文档查询时 HyDE 兜底——两套机制共享同一检索索引，只在 query 路由层分流。

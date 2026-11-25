---
title: "[Q7783] 小块召回大块喂模型：父子分块检索（small-to-big）"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7783 · 小块召回大块喂模型：父子分块检索（small-to-big）

难度：P6 ｜ 标签：父子分块、small-to-big、召回精度、上下文完整性、去重归并

基线：Python 3.12；实现"小块嵌入检索、父块喂模型"的两级索引与"小块命中的父块去重归并"逻辑，对比固定分块在"召回准但上下文残缺"上的失败案例，全标准库实跑。

**问**：RAG 里分块的两难——块小召回准但答案缺上下文，块大上下文全但向量稀释召回差（Q7503 分块策略矩阵的老矛盾）。父子分块（小块检索、父块回答）怎么解这个矛盾？父块去重与预算控制怎么做？什么场景父子分块反而是负优化？

**答**：
- **结论**：父子分块把"检索粒度"与"生成粒度"解耦：**子块**（100~300 字符，句子级）做嵌入与召回——粒度小，向量主题集中，命中精度高；**父块**（1000~2000 字符，章节/段落组）做上下文供给——召回命中的子块通过映射表换回它的父块喂给模型。本卡演示核心缺陷对比：固定大块检索时，一个含两主题的段落向量被稀释，查询只命中其中半相关内容，但整段喂入（噪音）；固定小块则召回准确但答案只有碎片（"工单怎么提"只召回了一句提交方式，缺前置条件）。父块层的关键工程是**去重归并**：top-k 子块命中常落在同一父块（同一章的三个句子），不去重就重复喂三遍挤爆预算（Q7712 overlap 冗余的同族账）——按父块聚合、按命中密度（命中子块数/父块总子块数）排序、预算内取 top 父块，跳过放不下的块而不是中断。适用判据：文档有**清晰的层级结构**（标题/章节）且答案常跨句子时收益最大；扁平短文档（FAQ、聊天记录）结构映射成本大于收益，直接小子块即可。
- **取舍**：① 两级索引的存储与维护成本：子块嵌入 + 父块原文双层存储，文档更新要重建子块索引并同步父块映射（Q7540 索引冷热的增量账）——映射表用稳定文档 ID + 章节路径锚定，别用行号偏移（文档一编辑就错位）；② 父块大小的甜点：父块 ≈ 模型单次回答所需上下文的 1~3 屏，太大稀释预算、太小又回到碎片问题——按"答案完整所需最小自足单元"定义父块边界（语义完整的一节），不是机械字数；③ 检索模式选择：纯子块检索（本卡）、子块检索+父块兜底（top-k 不满时补父块向量检索）、父子双路召回后融合（Q1190 RRF 的两级版）——复杂度递增，从第一种起步按 badcase 驱动升级；④ 与 rerank 的配合：父块喂模型前过一遍 rerank（Q7504）在预算内精选，父子分块解决"找得准"，rerank 解决"预算内放什么"，两段互补。
- **实战**：① 映射表是父块体系的心脏：`子块ID -> {文档ID, 父块ID, 章节路径, 偏移}`，任何映射错误都表现为"召回的内容驴唇不对马嘴"，映射表本身要有完整性断言（每个子块必须指向存在的父块）；② 评估三层指标分开：子块召回率（检索层）、父块覆盖答案度（人工标注答案所在父块是否进入）、端到端回答正确率（Q262 RAG 评估）——只看最后一层归因不了检索与生成的责任；③ 父块归并的预算公式：`预算 = top父块数 × 平均父块长度`，超预算时按密度分取舍——密度高说明整个父块都相关，优先保留；④ 多级父子（章→节→段）从两级起步，三级映射的维护成本爆炸，除非文档结构天然三级。

```python
"""Q7783 父子分块检索: 子块召回 -> 父块归并(去重+密度排序+预算)。"""


def build_index(doc: dict) -> tuple[dict, dict]:
    """doc: {doc_id: {parent_id: text}} -> 子块索引 + 子块->父块映射."""
    sub_index, mapping = {}, {}
    for doc_id, parents in doc.items():
        for pid, text in parents.items():
            sents = [s.strip() for s in text.split("。") if s.strip()]
            for sid, sent in enumerate(sents):
                key = f"{doc_id}:{pid}:{sid}"
                sub_index[key] = sent
                mapping[key] = (doc_id, pid)
    return sub_index, mapping


def retrieve(sub_index: dict, query_terms: set[str], top_k: int = 3) -> list[str]:
    """子块检索: 词命中打分取 top-k(真实实现为向量召回)."""
    scored = []
    for key, text in sub_index.items():
        score = sum(1 for t in query_terms if t in text)
        if score:
            scored.append((score, key))
    scored.sort(reverse=True)
    return [k for _, k in scored[:top_k]]


def merge_parents(hits: list[str], ptext: dict[str, str],
                  total_subs: dict[str, int], budget_chars: int) -> list[str]:
    """父块归并: 去重 -> 命中密度排序 -> 预算内取整父块."""
    hit_cnt: dict[str, int] = {}
    for h in hits:
        pid = h.split(":")[1]
        hit_cnt[pid] = hit_cnt.get(pid, 0) + 1
    density = {pid: hit_cnt[pid] / total_subs[pid] for pid in hit_cnt}
    picked, used = [], 0
    for pid, _ in sorted(density.items(), key=lambda kv: -kv[1]):
        t = ptext[pid]
        if used + len(t) > budget_chars:
            continue                    # 放不下跳过, 不中断(保留更密的小父块)
        picked.append(pid)
        used += len(t)
    return picked


if __name__ == "__main__":
    doc = {"d1": {
        "p1": "提交工单需先完成实名认证。认证入口在账户设置页。工单响应时长为2小时。",
        "p2": "退款流程需上传凭证。凭证支持图片与PDF格式。退款到账需3个工作日。"}}
    sub_index, mapping = build_index(doc)
    ptext = {"p1": doc["d1"]["p1"], "p2": doc["d1"]["p2"]}
    total_subs = {"p1": 3, "p2": 3}
    hits = retrieve(sub_index, {"工单", "实名", "提交"}, top_k=3)
    print(f"子块命中 {len(hits)} 条: {[sub_index[h][:14] for h in hits]}")
    hit_pids = {h.split(':')[1] for h in hits}
    picked = merge_parents(hits, ptext, total_subs, budget_chars=40)
    print(f"命中父块 {sorted(hit_pids)} -> 密度排序预算归并: 取 {picked}")
    uniq = len(picked) == len(set(picked))
    exact = picked == ["p1"] and hit_pids == {"p1"}
    # 大父块放不下时跳过而非中断: 预算 25 字, p1(36字)放不下但 p2(30字)也不行
    tight = merge_parents(hits, ptext, total_subs, budget_chars=20)
    print(f"紧预算 20 字: {tight} (放不下则全跳过, 不截断父块)")
    ok = (uniq and exact and tight == [])
    print(f"校验: 同父去重 + 密度排序 + 预算整块取舍 -> {'通过' if ok else '异常'}")
    print("结论：父子分块解耦'检索粒度'与'生成粒度': 子块准、父块全;")
    print("      归并三步: 去重 -> 命中密度排序 -> 预算内整块取舍, 映射表是心脏")
```

**追问一**：子块命中数很高但父块喂进去答案质量反而下降，可能的失败模式有哪些？

→ 解析：四个高频失败模式：① **父块粒度错配**：父块切得过大（把整章并成一个父块），密度排序后喂进来的是"命中 2 句 + 无关 800 字"，噪音稀释了答案——粒度校准方法是把父块边界对齐到"语义自足单元"（一节一议题），并用"父块信噪比"（命中子块字数/父块总字数）监控，低于阈值的父块改小块粒度；② **映射错位**：文档更新后子块索引重建了但映射表还指旧父块偏移，召回的子块与父块内容对不上——表现为"检索片段完全合理但喂给模型的上下文驴唇不对马嘴"，防线上靠映射完整性断言 + 文档版本号绑定（Q7056 schema 演进同族纪律）；③ **跨父块答案被割裂**：答案的关键推理跨两个父块（前提在 A 节、结论在 B 节），预算裁剪只留了密度高的 A——归并逻辑要支持"邻近父块联合保留"（父块间有引用/顺序关系时视为组），不能纯按密度贪心；④ **重复信息挤占**：多文档同主题（FAQ 与手册都讲同一功能），两个父块都命中且内容 80% 重复，归并后预算浪费一半——去重要做语义层（父块指纹/相似度合并，Q1510 近重复检测思想），不只是 ID 层。排查顺序：先看喂入的父块内容是否完整映射（防错位），再看信噪比（防粒度错），再看跨块结构（防割裂），最后查重复——badcase 驱动逐层收窄，比调参快。

**追问二**：父子分块与两阶段检索（召回+rerank）是什么关系？两者叠加的架构怎么演进？

→ 解析：两者解决不同维度的问题：父子分块解决**空间维度**（检索单元与生成单元的大小解耦），rerank 解决**预算维度**（候选池与最终喂入的精选），互相正交、可叠加。演进路线按 badcase 驱动分四步：① **基线**：固定子块 + top-k 直接喂（无父子无 rerank）——先量化基线的召回率与端到端正确率；② **父子分块介入**：badcase 显示"召回准但答案缺上下文"（答案需要的关键句不在喂入内容里）时上父子——归并层带去重与预算裁剪；③ **rerank 介入**：父块归并后候选仍超预算或顺序不佳（lost-in-the-middle Q7723 位置偏置开始咬人）时，加 rerank 精选与重排——父子与 rerank 的叠加形态是"子块召回 → 父块归并 → 父块 rerank → 预算装填"；④ **双路召回融合**：检索层再升级为"子块向量检索 + 父块 BM25 关键词检索"两路，RRF 融合（Q1190/Q2848），对付向量召回的词表盲区（Q7739 中文分词缺失的同族问题）。每步升级的验收标准都要三层指标齐动（子块召回率/父块覆盖度/端到端正确率），只看端到端会把检索层的收益与生成层的波动混在一起。成本账要同步记：两级索引 + rerank 每查询多一次模型调用（Q7653 rerank 吞吐账），QPS 上去后这笔钱不小——**架构升级永远跟着 badcase 与成本曲线走，不是跟论文走。**

# 137 ES 段（segment）机制（深挖）

> 分类：Elasticsearch 存储 | 难度：L4 | 题型：设计题 | 频率：中 | 关键词：**段生命周期**/**不可变取舍**/**merge 代价**/**运维边界**
> 原文锚点：第 1~98 段「ES 段不可变与段合并全貌」

## 思路与架构
ES 段的整个生命周期可串成一条链：
1. **写入**：doc 进 index buffer → refresh 到 OS cache 生成新段（不可变）。
2. **存储**：段内四类数据（倒排/stored field/doc_values/缓存）各司其职。
3. **清理**：更新/删除只标记，物理清除推迟到 merge。
4. **合并**：后台线程多阶段合并，减段数、清标记、提压缩，并有限流保护。
5. **运维**：force merge 是人工收尾，代价高需规划。

## 方案取舍
- **不可变 vs 可变的取舍**：不可变换来顺序写/免锁/缓存不失效/一致性，代价是更新删除必须标记+merge 延迟清理。
- **merge 收益 vs 代价**：merge 减段提压缩但耗 IO/CPU，故必须限流（max_thread_count、max_merge_count）。
- **自然 merge vs force merge**：自然只合小段、后台平滑；force merge 合大段、负载尖峰，仅适合只读/归档索引。
- **SSD vs HDD**：SSD 默认线程数即可，HDD 必须降 max_thread_count=1 避免 IO 打满。

## 答题技巧
- 答「段为什么不可变」用**五动机法**：顺序写/免锁/缓存/标记删除/一致性，逐条对应一个工程收益。
- 必点「删除是标记删除、物理删除在 merge 完成」——这是区分 P6/P7 的关键。
- 被追问性能调优时，直接抛 `max_thread_count` 默认值公式与 HDD 设 1 的结论。
- 收尾补一句「force merge 只用于不再写入的索引」，避免被追问时给出危险建议。

## ⚠️ 原文纠错
1. 事实核校： [经验] 段生命周期五环节、不可变五动机、merge 多阶段+限流、force merge 代价与差异——均正确，本卡为架构性归纳。
2. 崩坏词归一：源码将 segment 音译为 段/淡文件、Lucene 音译为 loosen/loser、merge 音译为 蛋合并/氮合并、force merge 音译为 firstmerge、Elasticsearch 音译为崩坏词（本卡统一为 Elasticsearch）。

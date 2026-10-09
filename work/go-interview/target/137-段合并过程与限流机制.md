# 137 段合并过程与限流机制

> 分类：Elasticsearch 存储 | 难度：L4 | 题型：机制题 | 频率：中 | 关键词：**merge 五阶段**/**max_merge_count**/**限流**/**max_thread_count**/**SSD/HDD**
> 原文锚点：第 38~65 段「段合并过程与合并调度限流」

## 一句话总述
段合并由独立线程执行，经「调度前检查 → mergeInit → mergeMiddle → commitMerge → mergeFinish → afterMerge」多阶段，落盘 FNM/.si 等文件；通过 `max_merge_count` 与 `index.merge.scheduler.max_thread_count` 做限流，防 merge 风暴拖累写入。

## 面试官视角
- 考察意图：是否了解 merge 不是「一键合并」，而是有调度、有阶段、有限流的复杂过程。
- 分档：P5 知 merge 在后台线程；P6 知多阶段与 FNM/.si 文件；P7 知限流参数与 SSD/HDD 调优。
- 红旗答案：以为 merge 无代价随意跑；或不知道 max_thread_count。
- 惊艳点：点出「默认 max_thread_count = max(1, min(4, floor(loadavg/2)))」，且 HDD 建议设为 1。

## 主问答
**Q（面试官原话）：** 段合并具体怎么执行？为什么要限流？
**A：**
1. **调度前**：检查单分片正在合并的段个数，超 `max_merge_count` 激活限流，进一步合并等待线程可用。
2. **mergeInit**：检查待合并段中文档是否都已被删除，是则直接跳过不合并。
3. **mergeMiddle**：对段内各类数据（总行存储/列存储/倒排表等）调不同合并方法；字段信息落 FNM 文件，段总体信息落 .si 文件。
4. **commitMerge**：合并完成后删除被合并段、释放内存、删物理文件。
5. **mergeFinish / afterMerge**：通知等待线程（force merge 等完成）；afterMerge 检查段数是否小于上限以决定是否继续限流。
6. **限流**：`index.merge.scheduler.max_thread_count` 控制单分片最大合并线程；默认 `max(1, min(4, floor(loadavg/2)))`（如 loadavg=10 → 10/2=5，min(5,4)=4，max(1,4)=4）。SSD 默认良好，HDD 建议设 1 降 IO 影响；可动态 API 改。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | merge 在哪跑？ | 基础 | 独立后台线程 | P5 |
| L2 | 落哪些文件？ | 细节 | FNM / .si | P6 |
| L3 | 为什么限流？ | 原理 | 防 merge 风暴拖慢写入 | P7 |
| L4 | 默认线程数？ | 调优 | max(1,min(4,loadavg/2)) | P7 |
| L5 | HDD 怎么配？ | 进阶 | max_thread_count=1 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 全版本 | 具体阶段名/默认随版本微调 | 阶段流程与限流意图稳定；低版本参数名略有差异需查官方文档 |

## 关键代码
```json
// 单分片合并最大线程数（HDD 场景）
PUT /idx/_settings
{ "index.merge.scheduler.max_thread_count": 1 }
```

## 总结与追问预判
merge 是「分阶段+限流」的后台工程，资源敏感。force merge 作为人工重操作还有额外注意事项——下一张讲。

## ⚠️ 原文纠错
1. 事实核校： [经验] 多阶段流程、FNM/.si 落盘、max_merge_count 限流阈值、max_thread_count 默认公式与 HDD 设 1、动态 API 改——均正确；源码对默认值的推导示例(loadavg=10→4)与公式自洽。
2. 崩坏词归一：源码将 merge 音译为 蛋合并/氮合并、Lucene 音译为 loser/ltserch、force merge 音译为 firstmerge/firstmergy、FNM 音译为 FNM(正确保留)、.si 音译为 点SI、Elasticsearch 音译为崩坏词（本卡统一为 Elasticsearch）。

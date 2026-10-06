# 138 ES match_phrase 查询

> 分类：Elasticsearch 查询 | 难度：L3 | 题型：概念题 | 频率：中 | 关键词：**match_phrase**/**短语匹配**/**位置**/**slop**
> 原文锚点：第 76~100 段「match_phrase 的顺序与相邻约束」

## 一句话总述
`match_phrase` 是 **短语匹配查询**：先分词，但要求分词后的 term 在文档中**以相同顺序、相邻位置**出现（默认 `slop=0`）；适合联系人搜索等高精度场景。

## 面试官视角
- 考察意图：match_phrase 比 match 多了"位置+顺序"约束。
- 分档：P5 知 match_phrase 是短语匹配；P6 知要求同序相邻；P7 知 slop 可调宽松度。
- 红旗答案：以为 match_phrase 只是 match 的别名。
- 惊艳点：点出 `slop` 参数——允许 term 间最大间隔，打破"必须严格相邻"。

## 主问答
**Q（面试官原话）：** match_phrase 和 match 有什么不一样？
**A：**
1. **同样分词**：和 match 一样先对关键词分词（"测试文本"→`测试`、`文本`）。
2. **加位置/顺序约束**：要求这些 term 在文档里**按查询的顺序、且相邻**出现——只有"测试…文本"顺序且紧邻的文档命中；"文本测试"顺序反了 → 不命中。
3. **单 term 退化为 match**：只查一个 term 时没有位置关系，两篇都命中。
4. **slop 调宽松**：`"slop": N` 允许 term 间最多间隔 N 个位置，打破严格相邻（如允许"测试 XX 文本"也命中），精度与召回的折中。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | match_phrase 分词吗？ | 基础 | 分词，但有位置约束 | P5 |
| L2 | 和 match 核心区别？ | 区分 | 要求同序+相邻 | P6 |
| L3 | 顺序反了能查到吗？ | 约束 | 不能（除非 slop） | P6 |
| L4 | 怎么放宽约束？ | 参数 | slop=N 允许间隔 | P7 |
| L5 | 何时用短语匹配？ | 选型 | 联系人/精确短语搜索 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 5.x~8.x | 无 | match_phrase 默认 slop=0（严格相邻）；slop>0 放宽 |

## 关键代码
```json
{ "match_phrase": { "content": { "query": "测试文本", "slop": 0 } } }
```

## 总结与追问预判
match_phrase = 短语匹配：分词 + 同序 + 相邻（slop=0）；slop 可调间隔。精度高于 match，适合短语/联系人搜索；与 term(不分词)、match(分词无位置) 形成三级精度。

## ⚠️ 原文纠错
1. 事实核校： [经验] match_phrase 分词+同序+相邻、单 term 退化为 match、slop 放宽间隔，均正确。
2. 崩坏词归一：mictphfreeze/machefreeze/matmatchfriase/matchfreezeze→match_phrase、micchifreeze→match_phrase。

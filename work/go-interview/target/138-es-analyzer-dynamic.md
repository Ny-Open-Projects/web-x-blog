# 138 IK 分词器与 dynamic mapping

> 分类：Elasticsearch 查询 | 难度：L3 | 题型：支撑知识 | 频率：中 | 关键词：**IK 分词器**/**ik_max_word**/**ik_smart**/**dynamic**
> 原文锚点：第 11~49 段「IK 分词器、HTML strip、dynamic 映射」

## 一句话总述
ES 查询效果**取决于分词器**：中文常用 IK 分词器（`ik_max_word` 细粒度建索引、`ik_smart` 粗粒度搜索）；`dynamic` 控制字段类型是否自动推断，生产建议 `strict`。

## 面试官视角
- 考察意图：term/match 行为差异的根因在 analyzer；顺带考 mapping 控制。
- 分档：P5 知 IK 是中文分词器；P6 知 ik_max_word(索引)/ik_smart(搜索)；P7 知 dynamic=strict 防脏字段。
- 红旗答案：以为索引和搜索用同一个分词器粒度最优。
- 惊艳点：点出"索引用细粒度(max_word)、搜索用粗粒度(smart)"的标准搭配。

## 主问答
**Q（面试官原话）：** 为什么同样的词 match 有时查得到有时查不到？
**A：**
1. **分词器决定 term**：写入用 `ik_max_word`（最细切分，如"测试文本"→`测试`/`文本`），搜索用 `ik_smart`（粗切分）；二者粒度不同影响召回。
2. **索引/搜索分词器分离**：mapping 里 `analyzer`(索引) 与 `search_analyzer`(搜索) 可不同；标准搭配是索引 `ik_max_word`、搜索 `ik_smart`，兼顾召回与精度。
3. **dynamic 映射**：`true`(默认) 自动推断类型并加字段；`strict` 拒绝未知字段写入；生产用 `strict` 防脏数据撑大 mapping。
4. **子字段 keyword**：字符串默认 `text` + 自动 `.keyword` 子字段；精确过滤走 `.keyword`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 中文用什么分词器？ | 基础 | IK 分词器 | P5 |
| L2 | 索引/搜索分词器怎么配？ | 配置 | max_word 建、smart 搜 | P6 |
| L3 | dynamic 有几种？ | 映射 | true/strict/false | P7 |
| L4 | 为什么生产用 strict？ | 治理 | 防未知字段撑大 mapping | P7 |
| L5 | HTML 怎么处理？ | 进阶 | char_filter HTML strip | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 7.x~8.x | IK 需装插件 | ik_max_word/ik_smart 为标准中文 analyzer；dynamic 默认 true |

## 关键代码
```json
{ "analyzer": "ik_max_word", "search_analyzer": "ik_smart", "dynamic": "strict" }
```

## 总结与追问预判
查询行为根因在 analyzer：索引 ik_max_word、搜索 ik_smart 是标准搭配；dynamic=strict 防脏字段，字符串默带 .keyword 子字段。理解这层才能解释 term/match 的差异。

## ⚠️ 原文纠错
1. 事实核校： [经验] IK 分词器 ik_max_word(索引)/ik_smart(搜索)、dynamic strict 拒未知字段、字符串默认 text+keyword 子字段，均正确。
2. 崩坏词归一：IKM/IKMmasword/IKpassword→IK / ik_max_word、xsmart/xmart/ICAMassword→ik_smart、ipad→IK 分词器、恰filter/HTMIstrip/HTMItrip→char_filter / HTML strip、ngrimanalyser/techniter→ngram analyzer/tokenizer、map→mapping、主分辨数/分辩数→主/副本分片数、refresh因ter→refresh_interval、OScatch→OS cache。

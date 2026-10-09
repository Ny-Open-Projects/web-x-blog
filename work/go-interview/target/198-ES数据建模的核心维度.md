# 198 ES 数据建模的核心维度

> 分类：Elasticsearch 索引建模 | 难度：L3 | 题型：设计题 | 频率：中 | 关键词：**数据建模**/**doc_values**/**index_options**/**预排序字段**/**keyword vs text**
> 原文锚点：第 1~14 段「ES 数据建模需要关注字段的更多属性」

## 一句话总述
ES 建模类似 MySQL 表结构，但字段有大量「开关属性」；把**排序、等值过滤、范围过滤、相关性打分、存储**这五个诉求映射到具体字段属性，是性能优化的核心。

## 面试官视角
- 考察意图：会不会把「业务查询模式」翻译成「ES 字段属性」，而不只是建个 text 字段了事。
- 分档：P5 知 keyword/text 区别；P6 知 doc_values/norms/index_options 取舍；P7 知预排序字段与 copy_to 的代价权衡。
- 红旗答案：所有字段一律 text + ik_max_word，或所有字段都开 doc_values。
- 惊艳点：点出「等值过滤字段关 doc_values 省磁盘/内存、text 关 norms 省存储」的精确取舍。

## 主问答
**Q（面试官原话）：** 企业网盘这种搜索场景，ES 的字段到底要怎么设计？
**A：**
1. **排序字段**：若存在固定排序字段（如 ctime），设 `index.sort.field` 预排序，数据按序落盘，检索免排序开销。
2. **等值过滤字段**：只参与 term 过滤、不排序不脚本 → `keyword` + `doc_values: false`，省列存与内存缓存。
3. **范围过滤字段**：数值类型走 BKD 树对 range 友好；若只有等值查询则直接用 `keyword`，不必用数值。
4. **大文本字段**：不需要展示原值就不存 `_source` 该字段（或 `store: false`），只留可被搜索的倒排。
5. **相关性无关字段**：text 字段不需要打分 → `index_options: DOCS` + `norms: false`，显著省存储。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | keyword 和 text 区别？ | 基础 | keyword 不分词精确、text 分词 | P5 |
| L2 | doc_values 干嘛的？ | 原理 | 列存，排序/聚合/脚本用，可关 | P6 |
| L3 | 什么时候关 doc_values？ | 取舍 | 只等值过滤、不排序聚合时关 | P6 |
| L4 | index_options 有哪几档？ | 深度 | DOCS/FREQS/POSITIONS/OFFSETS，越细越占空间 | P7 |
| L5 | 预排序字段的代价？ | 进阶 | 写入变慢、更新代价高，适合写少读多 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 6.0+ | `index.sort.field` 预排序为 6.0+ 稳定特性 | 按业务排序键设预排序；频繁更新的字段不适合 |

## 关键代码
```json
{
  "mappings": {
    "properties": {
      "uid":       { "type": "keyword", "doc_values": false },
      "file_size": { "type": "long" },
      "ctime":     { "type": "long" },
      "file_name": { "type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart" }
    }
  },
  "settings": {
    "index.sort.field": "ctime",
    "index.sort.order": "desc"
  }
}
```

## 总结与追问预判
建模第一性原理是「按查询模式反推字段属性」：排序→预排序、等值→keyword+关 doc_values、范围→数值、打分无关→关 norms/index_options。下一步常问分片数和 bulk 写入策略。

## ⚠️ 原文纠错
1. 事实核校： [经验] keyword 等值+关 doc_values、数值走 BKD 利于 range、text 关 norms/index_options 省存储、copy_to 合并查询字段——均正确。
2. 崩坏词归一：源码将 keyword 音译为 kword、text 音译为 test、doc_values 音译为 DOCvalues、index_options 音译为 indexoptions、copy_to 音译为 copytwo、norms 音译为 loms；源码将 Elasticsearch 音译为崩坏词，本卡统一为 Elasticsearch；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。

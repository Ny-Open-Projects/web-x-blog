## 思路与架构
```text
"已索引查不到"根因树：
- match(OR/AND)：查询 term 集 ⊆ 索引 term 集？
  - AND 要求 ⊆ 全包含；差一个 term 即不召回。
  - 差异来自 查询 analyzer ≠ 索引 analyzer。
- match_phrase：term 都在 + position 连续？
  - 不连续 ← 长词被再细分插入中间 term（IK max_word 高发）。
  - slop 放宽间隔，但过大损召回质量。
排查顺序：_analyze 对齐 term → 判 match/phrase 语义 → _termvectors 看 position → 统一 analyzer + 必要时 _reindex。
```

## 方案取舍
```text
- 召回率 vs 精度：ik_max_word 细粒度召回高但易插中间 term（phrase 坑多）；ik_smart 粗粒度少坑但召回低。按业务取舍。
- AND vs OR：确定性查询用 AND（全包含），模糊检索用 OR（至少命中）。
- slop：phrase 容忍间隔的应急阀，治标；治本是统一 analyzer / 换粗粒度。
- 一致性原则：search_analyzer 与索引 analyzer 必须一致，否则必现"查不到"。
```

## 答题技巧
```text
- 被问"查不到"：先抛根因"查询/索引分词不一致"，再分 match(term 集) 与 phrase(position) 两路。
- 必点工具：_analyze 看 term、_termvectors 看 position，别靠肉眼猜。
- 收尾落架构：建索引统一 analyzer、按需选 IK 粒度、analyzer 改动要 _reindex 才生效。
```

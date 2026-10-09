> 原文锚点：第 1~23 段综合「已索引match查不到…根因=查询/索引分词term不一致(AND全包含/phrase相邻)…用_analyze看分词…position间隔致phrase不召回…slop放宽」

## 一句话总述
"已索引却查不到"本质是**查询侧与索引侧 analyzer 产出的 term / position 不一致**。标准排查法是：① 用 `_analyze` 分别看查询串和索引字段的分词；② 对比 term 集合（`match`/AND 要求全包含）；③ 看 `_termvectors` 的 position 连续性（`match_phrase` 要求相邻，必要时 `slop`）；④ 从根上避免——建索引时统一查询/索引 analyzer、按需选 `ik_smart`/`ik_max_word`、加同义词/char filter。

## 面试官视角
面试官要的是"排查方法论"而非单点知识。能给出可落地的 4 步排查 + 架构级避免手段，即高分。

## 主问答
**Q（面试官原话）：** 线上 ES 已索引的数据 match 查不到，你怎么系统排查？

**A：**

1. **第一步·对齐分词**：用 `_analyze` 分别分析"查询串"和"索引字段（带 index analyzer）"，拿到两边 term 集合；差异就是查不到的直接原因。
2. **第二步·判 match 语义**：`match` 记默认 `OR`、显式 `AND` 要全包含——若差一个 term（如缺单字"中"），AND 必不召回，`OR` 可能召回，据此选 operator。
3. **第三步·判 phrase 相邻**：`match_phrase` 用 `_termvectors` 看每个 term 的 position，确认是否连续；不连续就用 `slop` 放宽，或确认是否有长词被再细分插入中间 term。
4. **第四步·架构避免**：建索引时**查询 analyzer 与索引 analyzer 保持一致**；按粒度选 `ik_smart`（粗，少中间 term）或 `ik_max_word`（细，召回高但易插 term）；必要时配同义词(synonym) / 字符过滤(char_filter) 补全 term。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | 首要排查动作 | 是否懂 _analyze | 先对齐两边分词 | 答不出即止 |
| L2 | match vs phrase 用哪步 | 是否懂分场景 | match 看 term 集、phrase 看 position | 答不出即止 |
| L3 | 怎么看 position | 是否懂 _termvectors | _termvectors 取各 term position | 答不出即止 |
| L4 | 根本避免手段 | 是否懂一致性 | 查询/索引 analyzer 统一 | 答不出即止 |
| L5 | ik_smart 还是 max_word | 是否懂粒度权衡 | 粗粒度少中间 term、细粒度召回高 | 答不出即止 |

## 版本与兼容性
- `_analyze` / `_termvectors` API 跨版本稳定；`ik_smart`/`ik_max_word` 为 IK 分词器两种粒度。
- 同义词/char_filter 在分析器配置中定义，机制跨版本一致。

## 关键代码
```go
// 排查四步的 go-elasticsearch 落地
// 1) 对齐：分别分析查询与索引字段
es.Indices.Analyze(strings.NewReader(`{"analyzer":"ik_max_word","text":"中华人"}`))               // 查询侧
es.Indices.Analyze(strings.NewReader(`{"index":"article","field":"content","text":"中华人"}`)) // 索引侧
// 2~3) 看 position
es.Termvectors(strings.NewReader(`{"fields":["content"]}`),
  es.Termvectors.WithIndex("article"), es.Termvectors.WithId("3"))
// 4) 建索引时统一 analyzer（mapping 里指定）
es.Indices.Create("article", es.Indices.Create.WithBody(strings.NewReader(`{
  "mappings": {"properties": {"content": {"type":"text","analyzer":"ik_max_word","search_analyzer":"ik_max_word"}}}
}`)))
```

## 总结与追问预判
- 口诀：**对齐分词(_analyze) → 判 match/AND(term 集) → 判 phrase(position) → 统一 analyzer 防复发**。
- 预判追问："统一 analyzer 后旧数据怎么办？"答：需 `_reindex` 或按新 mapping 重建索引，analyzer 改动不回溯已有文档。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 match、match_phrase、analyzer、term、position、_analyze、_termvectors、IK 分词器）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：match/match_phrase 语法见 138/`138-es-match-phrase-query`；analyzer 动态配置见 138；本卡只讲"查不到"的系统排查法与避免手段。

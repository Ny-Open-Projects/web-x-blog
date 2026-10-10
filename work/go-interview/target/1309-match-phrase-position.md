# 1309 match_phrase 的 term 顺序相邻与 slop

> 分类：Elasticsearch/查询 | 难度：L3 | 题型：八股题 | 频率：低 | 关键词：**match_phrase**/**position**/**相邻**/**slop**/**召回**

> 原文锚点：第 14~23 段「match_phrase查"中华共和国"匹配不到(要求term顺序相邻,查询分"中华"+"共和国"position 2和6不相邻)…slop参数(间隔term数,设3召回设2不召回)…match_phrase查"人民共和"查不到(原文相邻但"共和国"再细分出"国"使"人民"和"共和"position有间隔)」

## 一句话总述
`match_phrase` 比 `match` 更严：要求 term **按顺序且相邻**出现（靠 position 连续）。若查询分词后「中华」position=2、「共和国」position=6，中间隔了多个 term，就不召回；可用 `slop` 放宽"允许间隔多少个 term"。坑在于分词器会把长词再细分（"共和国"→"共和"+"国"），导致看似相邻的词在 position 上其实有间隔。

## 面试官视角
这是 match_phrase 的核心考点：position 相邻性 + slop。面试官想确认你懂"为什么肉眼相邻、ES 却说不相邻"——本质是 analyzer 把长词又切了一刀。

## 主问答
**Q（面试官原话）：** match_phrase 查"中华共和国"为什么召回不了？slop 是什么？

**A：**

1. **phrase 要求顺序 + 相邻**：`match_phrase` 不仅要 term 都存在，还要求它们在原文中的 **position 连续**（中间不能插其他 term）。
2. **position 不相邻就不召回**：查询"中华共和国"分词为 `中华`(position 2) + `共和国`(position 6)，两者中间隔了多个 term（position 不连续），所以召不回"中华人民共和国"。
3. **slop 放宽间隔**：`slop` = 允许两个 term 之间相隔多少个 term 仍算匹配。上例间隔 3 个 term，`slop=3` 可召回、`slop=2` 仍不行。
4. **长词再细分的坑**：查询"人民共和"看似原文相邻，但索引 analyzer 把"共和国"进一步切成 `共和`+`国`，使得"人民"和"共和"的 position 中间插了"国"这个 term，于是不相邻、召不回——**肉眼相邻 ≠ position 相邻**。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | phrase 和 match 区别 | 是否懂相邻约束 | phrase 要顺序+相邻，match 只含 term | 答不出即止 |
| L2 | slop 含义 | 是否懂间隔参数 | 允许间隔 term 数 | 答不出即止 |
| L3 | 为什么肉眼相邻却查不到 | 是否懂再分词 | 长词被切出中间 term | 答不出即止 |
| L4 | position 从哪看 | 是否懂 _termvectors | _termvectors 看每个 term 的 position | 答不出即止 |
| L5 | slop 过大后果 | 是否懂召回质量 | 过大召回不相关文档 | 答不出即止 |

## 版本与兼容性
- `match_phrase` / `slop` 跨 ES 版本稳定（5.x~8.x）。
- position 由 analyzer 决定；IK 的 `ik_max_word`（细粒度）比 `ik_smart` 更易产生中间 term，是该类坑的高发配置。

## 关键代码
```go
// match_phrase + slop 通过 go-elasticsearch 表达
es.Search(
  es.Search.WithIndex("article"),
  es.Search.WithBody(strings.NewReader(`{
    "query": {"match_phrase": {"content": {"query": "中华共和国", "slop": 3}}}
  }`)),
)
// slop=3 容忍"中华"与"共和国"之间隔 3 个 term，可召回"中华人民共和国"
// 排查用 _termvectors 看 position：
es.Termvectors(strings.NewReader(`{"fields":["content"],"_source":true}`),
  es.Termvectors.WithIndex("article"), es.Termvectors.WithId("3"))
```

## 总结与追问预判
- 口诀：**phrase=顺序+相邻(position连续)；slop 放宽间隔；长词再分词会插 term 导致"看似相邻实不相邻"**。
- 预判追问：怎么让"人民共和"也能召回？答：要么提高 slop、要么换 `ik_smart` 粗粒度 analyzer 减少中间 term、或业务上统一查询/索引 analyzer。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 match_phrase、slop、position、term、analyzer、IK 分词器）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：match_phrase 基础语法见 138；analyzer 动态配置见 138；本卡只讲 phrase 的 position 相邻性与 slop 调参，不重述基础语法。

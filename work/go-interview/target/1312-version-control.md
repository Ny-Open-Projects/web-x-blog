# 1312 ES 版本号乐观并发控制的三种类型

> 分类：Elasticsearch / 并发控制 | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**internal** / **external** / **external_GT** / **_version** / **版本冲突**
> 原文锚点：第 7~24 段「ES 每文档维护内部版本号存于 _version；提供 internal(默认)/external/external_GT 三种；internal 匹配才成功，external 提供>当前才成功，external_GT 提供>=才成功」

## 一句话总述
ES 乐观并发控制靠**版本号**实现，提供三种类型：**internal**（默认，ES 自管 `_version`，请求版本须与当前相等才成功）、**external**（客户端自管版本，提供值须 `>` 当前才成功并写回该值）、**external_GT**（提供值 `>=` 当前才成功）。版本不匹配则抛冲突异常。

## 面试官视角
- 意图：是否分得清三种版本类型的匹配规则，特别是 external 与 external_GT 的边界。
- P5 知 internal 匹配才更新；P6 知 external 用 `>`、external_GT 用 `>=`；P7 知 external 适用于外部系统同步、客户端须自管版本顺序。
- 红旗：把 external 说成"相等才成功"；混淆 external 与 external_GT 的等号处理。
- 惊艳点：点出 external 模式下"提供的版本会被写回文档"，因此外部系统必须保证版本单调递增 `[经验]`。

## 主问答
**Q（面试官原话）：** ES 的版本控制有哪几种，分别怎么判冲突？
**A：**
1. **internal（默认）**：ES 为文档自动维护 `_version`，每次索引/更新/删除递增；请求带 `version` 须**等于**当前值才成功，否则 409 冲突。适合纯 ES 内部场景。
2. **external（外部版本号）**：客户端自管版本，请求带 `version` 须**大于**当前值才成功，并把文档版本更新为提供值；`<=` 当前则拒绝。适用于与外部系统（如关系库）按版本同步。
3. **external_GT**：与 external 类似但放宽为**大于等于**当前值即成功（`>=`）；低于当前则失败。external 系列需客户端保证版本顺序正确，否则会丢失更新。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 默认类型 | 概念 | internal 匹配才成功 | 换题 |
| L2 | external 规则 | 机制 | 提供>当前才成功 | 判 P5 |
| L3 | external_GT | 边界 | 放宽为 >= | 判 P6 |
| L4 | 谁管版本 | 设计 | external 客户端自管 | 判 P6+ |
| L5 | 外部同步注意 | 进阶 | 版本须单调、防丢更新 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ES 全版本 | 6.6 起引入 _seq_no/primary_term | internal/external 仍可用；新版本默认推荐 seq_no 方式（见 1312-seqno-primaryterm） |

## 关键代码
```go
// 示意：internal / external 版本控制（elasticsearch-go），未做端到端验证
// internal：版本须等于当前
esapi.UpdateRequest{Index: "user", DocumentID: "1", Version: &v}.Do(ctx, es)

// external：版本须大于当前，且写回该值
ext := "external"
esapi.IndexRequest{
    Index: "user", DocumentID: "1",
    Version: &externalVer, VersionType: &ext, // VersionType="external"
}.Do(ctx, es)
// 返回 409 表示 version conflict，应用读取最新后重试
```

## 总结与追问预判
- 三种类型按"匹配规则"区分：internal 等、external 大于、external_GT 大于等于。
- 预判：_seq_no/primary_term 新机制 → 见 1312-seqno-primaryterm；实战重试模式 → 见 1312-es-concurrency。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（英文专有名词被错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：internal 匹配、external 用 `>`、external_GT 用 `>=`、版本不匹配抛冲突——均正确，未做更正。

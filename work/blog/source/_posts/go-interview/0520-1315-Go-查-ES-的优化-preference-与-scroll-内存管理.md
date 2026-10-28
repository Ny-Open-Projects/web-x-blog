---
disableNunjucks: true
title: "1315 Go 查 ES 的优化：preference 与 scroll 内存管理"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go · Elasticsearch 查询 | 难度：L3 | 题型：应用题 | 频率：中 | 关键词：**preference 本地分片** / **缓存命中** / **clearScroll** / **scrollID 变化才清** / **跨节点**
> 原文锚点：第 19~33 段「preference 参数让查询优先本地分片提缓存命中减跨节点；scroll 用完调 clearScroll 释放内存；scrollID 连续几次相同则变化后才清旧」

## 一句话总述
Go 查 ES 两个易漏的优化点：**preference**（指定查询优先打本地/某分片，命中分片级缓存、减少跨节点请求）与 **scroll 内存管理**（scroll 游标用完必须 `clearScroll` 释放 search context；若连续几次 scrollID 相同，要等 scrollID 变化后再清旧 ID，避免误清正在用的游标）。

## 面试官视角
- 意图：是否懂"查询侧缓存命中"和"scroll 资源必须主动释放"。
- P5 知 scroll 用完要清；P6 知 preference 提缓存命中、减跨节点；P7 知"scrollID 变化才清旧"的并发安全细节。
- 红旗：以为 scroll 自动释放；或不知道 preference 能提缓存命中。
- 惊艳点：点出"preference 的本质是让相同查询命中同一分片缓存，减少协调节点转发" `[边界]` 见 1314（Get/MGet/Query/Scroll）、1311-search-after（深翻页替代 scroll）。

## 主问答
**Q（面试官原话）：** 查询侧怎么优化、scroll 内存怎么管？
**A：**
1. **preference 提缓存**：副本分片也能答查询；不指定时请求随机打主/副分片。指定 `preference`（如连哪个节点就用其本地分片）可命中分片级缓存、减少跨节点转发、提查询效率。
2. **scroll 必清**：scroll 会占用 search context 内存，游标用完调 `clearScroll` 释放，否则内存泄漏。
3. **scrollID 变化才清旧**：若 `size` 很小，可能连续几次滚动 scrollID 相同；必须记录上一次 scrollID，**当它变化后**才安全清除旧 ID，避免误清正在使用的游标。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | scroll 要清吗 | 基础 | clearScroll 释放 | 换题 |
| L2 | preference 干嘛 | 优化 | 本地分片提缓存 | 判 P5 |
| L3 | 缓存命中 | 原理 | 减跨节点转发 | 判 P6 |
| L4 | 何时清旧 ID | 边界 | scrollID 变化才清 | 判 P6+ |
| L5 | scroll 替代 | 进阶 | PIT+search_after 新版 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ES 7.0+ | scroll 被 PIT+search_after 取代 | 新项目深翻页用 PIT+search_after；存量 scroll 仍须 clearScroll |

## 关键代码
```go
// 示意：preference 本地分片 + scroll 用完 clearScroll（未做端到端验证）
// 查询带 preference 命中本地分片缓存
res, _ := cli.Get().Index("user").Id("1").Routing("u123").Param("preference", "_local").Do(ctx)
// scroll 遍历
for {
    hits, scrollID := scrollOnce(ctx, dsl)
    process(hits)
    if len(hits) == 0 {
        break
    }
    if scrollID != lastScrollID { // 变化后才安全清旧
        clearScroll(ctx, lastScrollID)
        lastScrollID = scrollID
    }
}
clearScroll(ctx, lastScrollID) // 最后清
```

## 总结与追问预判
- 查询优化：preference 提缓存命中减跨节点；scroll 用完 clearScroll、scrollID 变化才清旧。
- 预判：查询 API 全集 → 见 1314；深翻页替代 → 见 1311；seq_no 并发 → 见 1312。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（英文专有名词被错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：preference 本地分片提缓存、scroll 用完 clearScroll、scrollID 变化才清旧——均正确，未做更正。

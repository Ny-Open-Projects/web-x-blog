---
disableNunjucks: true
title: "702 ServeMux 路由注册与匹配"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 网络 / net/http | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**ServeMux**/**HandleFunc**/**精确匹配优先**/**前缀/子树匹配**/**DefaultServeMux 全局**

> 原文锚点：第 10~14、50~54 段「HandleFunc 注册 / DefaultServeMux 全局注册」

## 一句话总述
`ServeMux` 是 net/http 的路由表，用 `HandleFunc(pattern, h)` 注册「模式 → 回调」。匹配规则：**精确路径优先**；以 `/` 结尾的 pattern 表示**子树（前缀）匹配**，命中最长前缀；不带 `/` 结尾的精确 pattern 仅精确相等才命中。包级 `http.HandleFunc` 注册到全局 **DefaultServeMux**，供 `ListenAndServe(nil)` 使用。

## 面试官视角
路由匹配是 ServeMux 的易错点，尤其「`/foo/` 是前缀子树、`/foo` 是精确」的区别。能讲清精确优先 + 最长前缀，并点出 DefaultServeMux 是全局单例（多包级注册会混在一起），就是合格。

## 主问答
**Q（面试官原话）：** ServeMux 怎么注册和匹配路由？

1. **注册**：`mux.HandleFunc("/api", h)` 把 `/api` 映射到回调 h；可注册多个不同 pattern。
2. **精确优先**：精确 pattern（不以 `/` 结尾）只在路径**完全相等**时命中，优先级最高。
3. **子树（前缀）匹配**：pattern 以 `/` 结尾（如 `/api/`）匹配该**前缀下的所有路径**，多个前缀取**最长匹配**。
4. **DefaultServeMux**：包级 `http.HandleFunc` 实际注册到全局 `http.DefaultServeMux`；用 `ListenAndServe(addr, nil)` 时 Serve 把它设为 handler——多个文件都调包级 HandleFunc 会**共享同一张全局表**，易冲突。
5. **404 与 Method**：无匹配 pattern 返回 404；同一 pattern 不同 method 需用 `Handle` + `Handler` 或框架（如 Gin）区分——原生 ServeMux 不按 method 分流。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 怎么注册路由？ | 说不清 HandleFunc |
| L2 | /foo 与 /foo/ 区别？ | 说不清精确 vs 子树 |
| L3 | 多个前缀怎么选？ | 说不清最长匹配 |
| L4 | DefaultServeMux 是啥？ | 说不清全局单例 |
| L5 | 按 method 分流？ | 说不清原生不支持 |

## 版本与兼容性
| pattern | 匹配 | 示例 |
|---------|------|------|
| `/api` | 精确 | 仅 `/api` |
| `/api/` | 子树前缀 | `/api/x`、`/api/y/z` |
| 无匹配 | 404 | — |

## 关键代码
```go
mux := http.NewServeMux()
mux.HandleFunc("/api", h1)    // 精确：仅 /api
mux.HandleFunc("/api/", h2)   // 子树：/api/x、/api/y 都走 h2（/api 本身走 h1）
// 包级全局注册（DefaultServeMux）：
http.HandleFunc("/global", h3)
log.Fatal(http.ListenAndServe(":8080", nil)) // handler=nil → 用 DefaultServeMux
```

## 总结与追问预判
核心：**精确优先、前缀取最长；包级 HandleFunc 进全局 DefaultServeMux**。追问拐向「启动与并发」——备好「ListenAndServe 每连接 goroutine、nil 兜底 DefaultServeMux」（见 702.md`）；中间件/Handler 链见 163.md` / `706-middleware-register.md`。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文「HandleFunc 注册路由、http.HandleFunc 用 DefaultServeMux」——准确；本卡补入「精确匹配优先于子树、以 / 结尾为前缀子树、多前缀取最长、原生不按 method 分流」的匹配细节（原文只演示根/ test 两路由未展开规则）。
2. 崩坏词归一：源码将 HTTP / 多路复用器 / 路由 / 携程 等音译为多组崩坏词，本卡统一为规范术语。

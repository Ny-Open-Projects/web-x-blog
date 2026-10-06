# 1114 pprof 离线分析

> 分类：性能与排障 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**go tool pprof** / **top -cum** / **火焰图**
> 原文锚点：第 71~115 段「top/flat/cum 列含义、list 看源码行、-http 图形界面」

## 一句话总述
`go tool pprof file.prof` 进入交互：top 看 flat 最高函数，`top -cum` 按累积(cum)排，`list 函数` 看逐行耗时；`go tool pprof -http=:8080` 出火焰图/图视图。

## 面试官视角
- 意图：是否会真刀真枪用 pprof 定位到行，读懂 flat/cum。
- P5 会用 top / P6 懂 flat vs cum、`list` 下钻 / P7 用 -http 火焰图、知道 profile 是静态快照。
- 红旗：把 flat 当 cum；不知道 `top -cum` 找"累积最重"的调用链。
- 惊艳点：flat 只算函数自身、cum 含其调用的总时长；定位热点先 `top -cum` 找重链再 `list` 下钻到行 —— 验证 `[经验]`。

## 主问答
**Q（面试官原话）：** 拿到 profile 文件怎么分析？flat 和 cum 什么区别？
**A：**
1. **结论**：`go tool pprof xxx.prof` 后 `top` 按自身耗时(flat)排，`top -cum` 按累积(cum)排，`list 函数` 看该函数逐行占比 `[源码]`。
2. **机制**：flat=函数自身代码耗时(不含被调)；cum=自身+等待被调返回的总时长，越底层 cum 越大；`go tool pprof -http=:8080` 启动 Web UI 含火焰图 `[源码]`。
3. **边界**：每次 `go tool pprof` 读的是**静态快照**，要新数据需重新采集再进工具；`-http` 依赖 graphviz 才能出图视图。
**加分层：** 先 `top -cum` 锁定最重调用链，再 `list` 逐层下钻到具体代码行，比盲目看 top 高效。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 用啥命令 | 概念 | go tool pprof | 换题 |
| L2 | flat/cum | 机制 | 自身/累积 | 判 P5 |
| L3 | 看哪行 | 边界 | list下钻 | 判 P6 |
| L4 | 火焰图 | 权衡 | -http | 判 P6+ |
| L5 | 快照陷阱 | 实战 | 重采才新 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | `-http`/火焰图长期可用 | top/-cum/list/-http 工作流不变 |

## 关键代码
```go
// 示意，未验证：分析已采集的 profile
// go tool pprof cpu.prof        // 交互模式
// (pprof) top -cum              // 按累积排序
// (pprof) list main.function1   // 看具体函数逐行耗时
// go tool pprof -http=:8080 cpu.prof  // 浏览器火焰图
```

## 总结与追问预判
- top 看 flat、top -cum 看累积链、list 下钻到行、-http 出火焰图；profile 是静态快照。
- 预判：CPU 原理 → 见 1114-cpu-profile；接入方式 → 见 1114-net-http-pprof。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 top/top -cum/list 命令、flat/cum 列含义与 -http 图形界面表述；仅做了机翻解码（如 gotoPPROF→go tool pprof、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。

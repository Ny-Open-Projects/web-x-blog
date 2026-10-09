# 1114 pprof 概览与采集方式

> 分类：性能与排障 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**pprof** / **runtime/pprof** / **net/http/pprof**
> 原文锚点：第 9~64 段「pprof 可采集 CPU/内存/锁/阻塞…三种采集方式」

## 一句话总述
pprof 内置在 Go 工具链，能采 CPU、堆(内存分配)、mutex 竞争、block 阻塞、goroutine 等 profile；三种接入：基准测试 flag、`runtime/pprof` 代码内、`net/http/pprof` HTTP。

## 面试官视角
- 意图：是否分得清各类 profile 与三种采集入口，知道生产用什么。
- P5 知三类 profile / P6 说清三种采集方式适用面 / P7 知生产首选 `net/http/pprof`、用完关路由。
- 红旗：把 CPU 与 heap 采样机制混为一谈；以为只能写代码采。
- 惊艳点：生产 HTTP 服务只需 `_ "net/http/pprof"` 空导入即用默认路由暴露 `/debug/pprof/`，零业务改动 —— 验证 `[源码]`。

## 主问答
**Q（面试官原话）：** pprof 都能采什么？一般怎么接入项目？
**A：**
1. **结论**：可采 CPU、堆内存分配、mutex 竞争、block 阻塞、goroutine、trace 等；接入有基准测试 flag、`runtime/pprof` 代码内、`net/http/pprof` HTTP 三种 `[源码]`。
2. **机制**：基准测试加 `-cpuprofile/-memprofile/-blockprofile/-mutexprofile` 落文件；`runtime/pprof.StartCPUProfile` 等手动采；`net/http/pprof` 空导入注册 `/debug/pprof/` 路由 `[源码]`。
3. **边界**：CPU/heap 长期开有开销，生产用 `net/http/pprof` 时应在定位完及时关掉路由，避免被外部触发采样。
**加分层：** 类型选型决定用哪个 profile：CPU 高用 cpu，内存涨用 heap，协程卡用 block/mutex。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 采哪些 | 概念 | cpu/heap等 | 换题 |
| L2 | 三种方式 | 机制 | 测试/代码/http | 判 P5 |
| L3 | 生产选啥 | 边界 | http/pprof | 判 P6 |
| L4 | 开销代价 | 权衡 | 采样有损 | 判 P6+ |
| L5 | 用完咋办 | 实战 | 关路由 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | `net/http/pprof` 长期存在 | 三类入口 + `/debug/pprof/` 不变 |

## 关键代码
```go
// 示意，未验证：三种接入之一 —— 基准测试
// go test -run=^$ -bench=. -cpuprofile=cpu.prof -memprofile=mem.prof ./...
// 之二是 runtime/pprof；其三是 _ "net/http/pprof" + http server
```

## 总结与追问预判
- 五类 profile + 三种接入；生产首选 http/pprof 且用完关。
- 预判：CPU 原理 → 见 1114；heap/mutex 区别 → 见 1114。

## ⚠️ 原文纠错
原文第 10 段将 pprof 第二类数据写作"非内存分配的数据"，结合后文对 memoryprofile/heap 的讨论，应为"内存分配数据"，"非"字疑为口误或机翻插入。其余各类 profile（CPU/锁/阻塞）与三种采集方式表述准确。核对范围：通读全文并重点核对 profile 分类与采集方式；仅做机翻解码（如 勾浪→Go、首时→守时 等），技术结论除该处还原外未改。

# 914 map 使用三注意：并发不安全 / float key / 无序

> 分类：Go/运行时 | 难度：L3 | 题型：陷阱题 | 频率：高 | 关键词：**并发不安全** / **float 作 key** / **无序遍历** / **写时 panic**
> 原文锚点：第 60~66 段「①map 并发不安全(写时查 hmap.flags 写状态→panic) ②float 作 key 精度问题取不到值 ③无序遍历(每次顺序可能不同)」

## 一句话总述
map 有三个高频注意事项：**① 并发不安全**——多个 goroutine 同时写会触发 `hmap.flags` 写状态检测并 **panic**（读也要配合 sync）；**② 避免用 `float` 作 key**——浮点精度问题可能导致同一逻辑值算出不同哈希、取不到对应 value；**③ 无序遍历**——`for range` 每次迭代顺序可能不同，不能依赖顺序。

## 面试官视角
- 意图：考察 map 的**实战坑**——并发/key 类型/遍历顺序，是面试必问三角。
- P6 能说出三个注意点；P7 能讲清"并发写为何 panic（flags 写标记检测，非简单竞态）"以及"float key 精度导致哈希不一致"。
- 红旗：以为 map 并发读安全（并发读写也不安全，必须全 sync）；以为 `float` 当 key 只是不推荐（实际可能永远取不到值）。
- 惊艳点：点出"并发安全用 `sync.Map` 或 `rwmutex` 包 map（见 107-rwmutex-safemap）"，连接到既有安全方案。

## 主问答
**Q（面试官原话）：** 用 map 有什么要注意的？
**A：**
1. **结论**：三注意——并发不安全、避免 float 作 key、无序遍历。
2. **机制① 并发不安全**：map 非并发安全。写操作会检查 `hmap.flags` 是否处于写状态，若检测到并发写（或并发读写），**直接 panic**（不是数据错乱，是主动崩溃）。多 goroutine 访问必须加锁或用 `sync.Map`。
3. **机制② float key**：浮点有精度误差，理论上相等的两个 float 可能因表示差异算出**不同哈希值**，落到不同桶，导致 `m[f]` 取不到预期 value。应改用整数/字符串等精确类型作 key。
4. **机制③ 无序**：`for range m` 的迭代顺序**不保证**、每次可能不同（Go 故意随机化起始桶防依赖顺序）。需要顺序时先收集 key 排序再取 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 并发安全吗 | 基础 | 不安全，并发写 panic | 判 P5 |
| L2 | 为何 panic | 机制 | flags 写状态检测 | 判 P6 |
| L3 | float key 坑 | 深度 | 精度→哈希不一致 | 判 P6+ |
| L4 | 遍历顺序 | 机制 | 无序随机化 | 判 P7 |
| L5 | 并发怎么解 | 体系 | sync.Map/rwmutex 见 107 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | 并发写 panic、float key 风险、无序遍历恒定 `[经验]` |
| 并发方案 | sync.Map | 高频并发用 `sync.Map` 或 `rwmutex`+map（见 107-rwmutex-safemap） |

## 关键代码
```go
package main

import "sync"

func main() {
    // ① 并发写会 panic：fatal error: concurrent map writes
    m := map[int]int{}
    var wg sync.WaitGroup
    for i := 0; i < 2; i++ {
        wg.Add(1)
        go func() { defer wg.Done(); m[1] = 1 }() // 并发写 → panic
    }
    wg.Wait()

    // ② 并发安全写法：sync.Map
    var safe sync.Map
    safe.Store(1, 1)
    _ = safe.Load(1)
}
```

## 总结与追责预判
- 三注意：并发写 panic(hmap.flags) / float key 精度取不到 / 无序遍历；并发用 sync.Map 或锁。
- 预判：底层结构 → 见 914-map-hmap-bmap；定位流程 → 见 914-map-key-locate；并发安全 map → 见 107-rwmutex-safemap；nil map → 见 414-slice-nil-vs-map。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"map 并发不安全(写时查 hmap.flags 写状态直接 panic)、避免 float 作 key(精度问题取不到 value)、无序遍历(每次顺序可能不同)"的描述，与 Go map 行为一致（runtime 对并发写做 flags 检测并 panic；float 作 key 因精度有风险；for range map 顺序随机化为 Go 既定行为）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。

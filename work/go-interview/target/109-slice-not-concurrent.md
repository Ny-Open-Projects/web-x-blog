# 109 切片 Slice 是并发安全的吗？

> 分类：Go/并发 | 难度：L2 | 题型：概念题 | 频率：高 | 关键词：**slice非并发安全**/**静默竞争**/**底层数组共享**/**并发append丢元素**/**引用类型**
> 原文锚点：第 1~19 段「slice 与 map 同为非并发安全容器、map 并发 panic 而 slice 静默覆盖、并发 append 一万只得九千多、底层同 array 竞争」

## 一句话总述
**Slice 不是并发安全的**。它与 map 同属容器类型、都无原生并发保护；但 map 并发冲突会强制校验直接 panic，slice 不会——并发 append 时不同 goroutine 读到相同索引、后者静默覆盖前者，导致数据丢失且难查。根因是 slice 是**引用类型**，底层指向同一底层数组，多 goroutine 操作同一数组相同索引即产生内存竞争。

## 面试官视角
- 考察意图：能否区分「slice 静默竞争」与「map 直接 panic」，并说清底层共享数组这一根因。
- 分档：P5 知 slice 非并发安全；P6 能解释并发 append 丢元素（len 不足）；P7 知引用类型共享底层数组、与 map 竞争表现差异。
- 红旗答案：认为 slice 并发会 panic（那是 map）；忽略底层数组共享只说「加锁就好」。
- 惊艳点：点出「slice 竞争是静默覆盖、无 panic，比 map 更隐蔽」，以及「竞争本质是对同一底层数组内存的并发访问」 [经验]。

## 主问答
**Q（面试官原话）：** slice 并发安全吗？为什么？
**A：**
1. **非并发安全**：slice 与 map 都无原生并发保护；但 map 冲突强制校验 panic，slice 不校验，并发写会**静默覆盖**丢数据 [经验]。
2. **并发 append 丢元素**：一万次并发 append 实际 len 只有九千多——不同 goroutine 拿到相同索引、后者覆盖前者 [经验]。
3. **根因=共享底层数组**：slice 是引用类型，底层引用同一 array；多协程操作同数组相同索引即内存竞争、共享元素被改 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 安全吗？ | 结论 | 非并发安全 | P5 |
| L2 | 咋丢的？ | 现象 | 并发 append 覆盖 | P6 |
| L3 | 为啥静默？ | 差异 | 不校验不 panic | P6 |
| L4 | 根因？ | 底层 | 共享底层数组 | P7 |
| L5 | 咋修？ | 解法 | 锁/channel/分片 | P7+ |

## 版本与兼容性
- 本卡只讲「slice 并发不安全本质」；两种修复见 `109-safeslice-rwlock`(RWMutex) 与 `109-safeslice-channel`(channel 串行化) [边界]。
- map 并发 panic 细节见 `914-map-concurrency-float`、race detector 见 `1018-goroutine-data-race-detector`/数据竞争见 `1019-data-race`——本卡只引不重述 [边界]。

## 总结与追问预判
slice 并发问题的本质是「多协程对同一底层数组的竞争」。解法沿「串行化访问」展开：加锁（RWMutex）或 channel actor；读多写少用 RWMutex，读少可用分片打散锁粒度。

## ⚠️ 原文纠错
1. 事实核校： [经验] slice 静默覆盖非 panic、并发 append 丢元素、引用类型共享底层数组——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（切片、并发安全、底层数组、索引、覆盖、协程等）。

```go
// slice 并发 append 静默丢元素（非 panic，比 map 更隐蔽）
func concurrentAppendLost() {
    s := make([]int, 0)
    var wg sync.WaitGroup
    for i := 0; i < 10000; i++ {
        wg.Add(1)
        go func(v int) { // 多 goroutine 操作同一底层数组
            s = append(s, v) // 竞态：读到相同 len 后写同索引，后者覆盖前者
            wg.Done()
        }(i)
    }
    wg.Wait()
    fmt.Println(len(s)) // 通常 < 10000，且无 panic
}
// 根因：slice 引用同一底层 array，并发读写同索引即内存竞争
```

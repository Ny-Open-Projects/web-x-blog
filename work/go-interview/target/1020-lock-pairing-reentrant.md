# 1020 加解锁配对与调用链重入死锁

> 分类：Go 并发/sync | 难度：L3 | 题型：陷阱题 | 频率：高 | 关键词：**defer Unlock 兜底** / **提前 return 漏解锁** / **调用链重入** / **fatal error**
> 原文锚点：第 25~37 段「加解锁要成对、提前 return 用 defer 兜底；同一锁跨函数加两次→重入 fatal error」

## 一句话总述
加锁必须**成对解锁**，最稳的做法是用 `defer mu.Unlock()` 兜底，防止中间 `return` 提前退出导致漏解锁；更要警惕**调用链重入**——同一 goroutine 经由 main→A→B 对同一把 Mutex 连续加两次（中间没解锁），Go 无重入锁，直接 fatal error 崩进程。机制细节见 925，本卡补"early-return 兜底"与"重死于调用链"两个实战视角。

## 面试官视角
- 考察意图：会不会用 defer 兜解锁、是否意识到重入死锁常藏在调用链而非明显自锁
- P5 知加解锁要配对；P6 能用 defer 兜 early-return、知重入 fatal；P7 能讲调用链重入的排查（栈帧/加锁路径）
- 红旗：手动在每分支解锁（易漏）；以为"不同函数里的锁不是同一把"
- 惊艳点：点出"重入死锁多发生在调用链（A 调 B 各加一次），不是手写的明显自锁" [源码]

## 主问答
**Q（面试官原话）：** 加锁解锁还有什么容易翻车的地方？
**A：**
1. **defer 兜 early-return**：加锁后若某条件满足就 `return`，手动解锁分支极易漏写；用 `defer mu.Unlock()` 保证任何路径都解锁，是最稳写法 [经验]。
2. **调用链重入致命**：同一把锁在 `main` 加一次、经 `test1`→`dosomething` 又被加一次（中间未解），Go 的 Mutex **不可重入**，单协程自锁直接 fatal error 终止进程——重入常藏在调用链而非显式自锁 [源码]。
3. **未加锁解锁也 panic**：对已解锁/未加锁的 Mutex 再 `Unlock` 会 panic（见 925-mutex-usage）；锁粒度要收住，避免长调用链里反复碰同一把锁 [边界]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 为何配对 | 常识 | 防死锁 | P5 |
| L2 | 怎么兜底 | 实战 | defer Unlock | P6 |
| L3 | 重入后果 | 机制 | fatal error | P6+ |
| L4 | 重入藏哪 | 边界 | 调用链 | P7 |
| L5 | 排查 | 实战 | 栈帧/加锁路径 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| go1.0+（sync） | 无 | 不可重入 fatal error、defer 兜解锁长期成立 |

## 关键代码
```go
var mu sync.Mutex

func test1()       { mu.Lock(); dosomething(); mu.Unlock() } // mu 已加
func dosomething() { mu.Lock(); /* 重入：main→test1→dosomething 同一把锁加两次 */
                     defer mu.Unlock() }

// ✅ 用 defer 兜 early-return，且避免调用链重复加锁
func safe(cond bool) {
    mu.Lock()
    defer mu.Unlock() // 任何 return 路径都解锁
    if cond { return } // 不会漏解锁
    // ...
}
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（SYNC→sync、勾浪→Go、态一/解一→test1、dosomething 保留、fadeerror→fatal error、china→channel 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 加解锁成对用 `defer` 兜底；调用链重入是隐蔽 fatal error 源。
- 不可重入机制/读锁再写锁见 925-lock-reentrancy、Mutex 三铁律见 925-mutex-usage（只引不重述）；误区(一)=闭包见 1017。

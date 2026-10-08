# 1013 Go 中的乐观锁实现

> 分类：Go/并发 | 难度：L3 | 题型：设计题 | 频率：中 | 关键词：**乐观锁** / **CAS** / **atomic.CompareAndSwap** / **版本号机制**
> 原文锚点：第 6~26 段「乐观锁两实现：CAS(atomic.CompareAndSwap自旋,冲突多CPU开销大,适合冲突少持锁短) + 版本号机制(加version字段,更新where version=旧值自增)」

## 一句话总述
Go 没有内置"乐观锁"类型，乐观锁靠两种模式实现：**CAS**（用 `sync/atomic` 的 `CompareAndSwap` 自旋重试，冲突多时 CPU 开销大，适合冲突少、持锁短）与**版本号机制**（给数据加 version 字段，更新时 `where version=旧值` 并自增，不一致则失败重试）。二者都是"先改、提交时校验"。

## 面试官视角
- 意图：考察乐观锁在 Go 里的落地能力，而非只会背概念。
- P5 知道 CAS 是乐观锁；P6 能写出 `atomic.CompareAndSwap` 自旋循环；P7 能讲清 CAS 的 CPU 开销缺陷与版本号机制适用场景。
- 红旗：以为乐观锁在 Go 里有现成类型；CAS 失败后不重试或无限自旋不退出。
- 惊艳点：点出"CAS 冲突多时一直重试→CPU 飙升"，所以适合冲突少；版本号机制天然适合 DB/有状态存储。

## 主问答
**Q（面试官原话）：** Go 里怎么实现乐观锁？
**A：**
1. **结论**：Go 乐观锁两种实现——① **CAS**：`atomic.CompareAndSwapXxx(addr, old, new)` 在 `for` 里自旋，期望值与当前一致才更新、否则重试；② **版本号**：数据带 `version` 字段，更新语句带 `where version=读取时的值` 并 `version+1`，被别人改过则 version 不匹配、更新失败可重试。
2. **机制（CAS 取舍）**：CAS 是"乐观"的——不先加锁，提交时校验。但**冲突概率大时 CAS 一直失败、不断重试**，空耗 CPU，所以只适合**冲突少、临界区极短**的场景（如计数器）；冲突多应退回悲观锁 Mutex。
3. **边界（版本号）**：版本号机制把"校验"下沉到数据行（DB 或带版本的结构体），适合有持久化/状态的场景；数据库里常 `update ... set status=?, version=version+1 where id=? and version=?` 实现 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 乐观锁实现 | 基础 | CAS / 版本号 | 判 P5 |
| L2 | CAS 怎么写 | 实现 | CompareAndSwap 自旋 | 判 P6 |
| L3 | CAS 缺陷 | 深度 | 冲突多 CPU 飙升 | 判 P6+ |
| L4 | 何时版本号 | 取舍 | 有状态/DB 场景 | 判 P7 |
| L5 | CAS vs Mutex | 联动 | 冲突少用 CAS | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | CAS 经 sync/atomic 提供（Go 1.19 起泛型 CompareAndSwap 更顺手）；版本号机制与语言版本无关 `[经验]` |

## 关键代码
```go
// 乐观锁实现一：CAS 自旋（冲突少、临界区短时合适）
func incr(addr *int64) {
    for {
        old := atomic.LoadInt64(addr)
        if atomic.CompareAndSwapInt64(addr, old, old+1) {
            return // 期望值未变才更新成功，否则重试
        }
        // 冲突多时这里会一直重试 → CPU 开销大
    }
}

// 乐观锁实现二：版本号机制（伪 SQL）
// UPDATE t SET status=?, version=version+1 WHERE id=? AND version=?
// 若期间被改，version 不匹配 → 影响行数 0 → 业务重试
```

## 总结与预判
- Go 乐观锁=CAS(atomic) + 版本号；CAS 适合冲突少，冲突多退回 Mutex。
- 预判：Mutex 悲观锁 → 见 1013-mutex-pessimistic；CAS vs Mutex 取舍 → 见 105-atomic-vs-lock；死锁 → 见 1013-deadlock-livelock。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"乐观锁两实现（CAS 自旋 / 版本号机制）、CAS 冲突多时 CPU 开销大、适合冲突少持锁短、版本号用于 DB/有状态场景"的描述，与并发编程一致。源码将术语音译为崩坏词，本卡统一为规范术语，技术结论未做更正。与 105-atomic-vs-lock（讲 CAS vs Mutex 何时用）互补——本卡聚焦"乐观锁模式本身"，不重复其取舍表 `[经验]`。

# 177 Go 如何用 map 实现不可重复集合（Set）

> 分类：Go 数据结构 / 集合 | 难度：L3 | 题型：实现题 | 频率：中 | 关键词：**set**/**map[T]struct{}**/**空结构体**/**RWMutex**/**部分删除内存不回收**

> 原文锚点：第 1~39 段「Go 无内置 set,借 map 键不重复实现...值用空结构体(零尺寸,地址相同/相等/size0验证)...map 非并发安全加 RWMutex...核心坑:删除部分键值内存不回收,删全部/nil才回收...低版本 Go1.11 清空也不回收→潜在泄漏」

## 一句话总述
Go 无内置 set，借 **map 键不可重复**实现集合；值用**空结构体 `struct{}`**（零尺寸，省内存）。map 非并发安全需包 `RWMutex`。**核心坑**：删除部分键值后内存**不回收**，仅删全部或 `map=nil` 才回收；低版本 Go（1.11）即使清空全部也不回收，与编译器/OS/CPU 架构相关，可能内存泄漏。

## 面试官视角
- 考察意图：是否真懂"空结构体做 value 省内存" + map 并发安全 + **部分删除不缩容**这一反直觉坑。
- 分档：P5 知 map[T]struct{} 实现 set；P6 能加 RWMutex 保证并发安全；P7 能讲"部分删除内存不回收 + 版本差异"。
- 红旗答案：用 `map[T]bool` 浪费内存；不知 map 删除不缩容；认为 delete 后内存立即释放。
- 惊艳点：点出「空结构体零尺寸」「部分删除 bucket 不回收，仅全删/nil 才回收」「低版本 Go 清空也不回收」 [经验]。

## 主问答
**Q（面试官原话）：** 怎么在 Go 里实现不可重复集合？
**A：**
1. **map[T]struct{}**：键存元素（键不可重复即集合语义），值用空结构体——零尺寸、多个空结构体地址相同且相等，不占内存 [经验]。
2. **空结构体验证**：两个 `struct{}{}` 变量地址相同、`==` 相等、`unsafe.Sizeof` 为 0，证其为零尺寸值 [经验]。
3. **并发安全**：map 非并发安全，用 `sync.RWMutex` 包 Add（加锁赋值）/Remove（`delete`）/Contains（查键 ok）/Size（`len`）/Clear（重新 `make`）[经验]。
4. **内存坑（关键）**：删除部分键值后内存**不回收**（bucket 不缩容）；删除全部或 `map=nil` 后才回落 [经验]。
5. **版本差异**：低版本 Go（如 1.11）即使清空全部键值也不回收，与编译器/OS/CPU 架构相关，易致内存泄漏 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么实现 set？ | 基础 | map[T]struct{} | P5 |
| L2 | 为何空结构体？ | 内存 | 零尺寸省内存 | P6 |
| L3 | 并发安全？ | 工程 | RWMutex 包 map | P6 |
| L4 | 删除内存回收？ | 关键坑 | 部分不回收/全删才回 | P7 |
| L5 | 版本差异？ | 深度 | 低版清空不回收 | P7+ |

## 版本与兼容性
- 空结构体零尺寸与末位对齐特例见 910 [边界]；本卡讲其作为 set value 的实战，不重述对齐原理。
- map 基础与 `RWMutex` 用法见 914*`/`925-mutex-usage` [边界]；本卡只带"包 map 做并发 set"。

## 关键代码

```go
// Go 无内置 set：用 map[T]struct{} 实现，空结构体零尺寸省内存
type Set[T comparable] struct {
    mu sync.RWMutex
    m  map[T]struct{}
}
func (s *Set[T]) Add(v T) {
    s.mu.Lock(); defer s.mu.Unlock()
    s.m[v] = struct{}{} // 值用空结构体，不占内存
}
func (s *Set[T]) Contains(v T) bool {
    s.mu.RLock(); defer s.mu.RUnlock()
    _, ok := s.m[v]; return ok
}
func (s *Set[T]) Remove(v T) {
    s.mu.Lock(); defer s.mu.Unlock()
    delete(s.m, v) // 注意：部分删除不回收 bucket 内存
}
```

## 总结与追问预判
set 实现 = map[T]struct{} + RWMutex。面试常追问「删元素后内存降吗」→ 答「部分删除 bucket 不缩容、不回收，只有全删或 nil 才回收，低版本甚至全删也不回收」；再追问规避则讲"定期重建 map 或换 sync.Map"。

## ⚠️ 原文纠错
1. 事实核校： [经验] 空结构体零尺寸、map 非并发安全需锁、部分删除内存不回收、低版 Go 清空不回收——均正确，符合 Go map 实现事实。
2. 崩坏词归一：源码将 Go 及相关概念音译为若干崩坏串（如将 Go、Go 版本、Go 环境、map、delete、nil、键值对等音译为非规范串），本卡统一为规范术语，无黑名单词。

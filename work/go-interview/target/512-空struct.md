# 512 空 struct{}：零尺寸值与 Set 的两种实现

> 分类：Go / 类型系统 | 难度：L2 | 题型：概念题 | 频率：中 | 关键词：**struct{}**/**零尺寸**/**map 集合**/**Set 封装**/**无值语义**
> 原文锚点：第 1~29 段「需要用到 map 类型且只判断 key 是否存在、不关心值的时候，通常会用空结构体做 map 的值…空的结构体不占空间…Go 没有集合类型，通常使用空结构体配合 map 实现集合…map 不支持并发操作，并发场景需要加锁」

## 一句话总述
`struct{}` 是**零尺寸类型**（`unsafe.Sizeof` = 0）——「只要存在性、不要载荷」时的零成本载体：**Go 没有原生 Set，惯用法是 `map[T]struct{}`**（value 占 0 字节，比 `map[T]bool` 省）；再封装一层 put/has/remove 就是完整 Set 类型。本质是**用类型系统表达「无值语义」**——读者一看 `map[string]struct{}` 便知这集合只关心 key。

## 面试官视角
- 考察意图：从「知道空结构体不占空间」到「知道它为什么适合做 Set、还能用在哪」——考察零尺寸类型在类型语义与内存两个层面的理解。
- 分档：P5 知道 struct{} 占 0 字节；P6 能写出 map + struct{} 的 Set 并说清与 bool 值的差异；P7 能延伸到信号 channel（`chan struct{}`）、接口比较语义与零尺寸的边界（末位字段对齐特例）。
- 红旗答案：说 `map[T]bool` 和 `map[T]struct{}` 完全等价没区别；不知道并发访问 map 要加锁。
- 惊艳点：「**value 类型本身就是文档**——`struct{}` 明确宣告『值域为空，别想从中读出东西』，而 bool 会诱导人读它」+ 实测 value 尺寸 0 vs 1 [实测]。

## 主问答
**Q（面试官原话）：** 空结构体有什么用？为什么常用它做 Set？
**A：**
1. **零尺寸是它的全部魔法**：实测 `unsafe.Sizeof(struct{}{}) = 0`——不占任何存储空间。Go 没有原生 Set 类型，惯用 `map[T]struct{}` 模拟：key 即元素，value 用空结构体表达「不存在值」 [实测]。
2. **与 `map[T]bool` 的实测对比**：同放一个元素，`map[int]struct{}` 的 value 尺寸 **0 字节**、`map[int]bool` 的 value 尺寸 **1 字节**——元素量大时累积差距可观（还要算上 bool 带来的额外桶内存布局影响） [实测]。
3. **两种实现姿势**：① **裸用**——`set1 := map[int]struct{}{}`，判断存在用 `_, ok := set1[k]`，添加 `set1[k] = struct{}{}`，删除 `delete(set1, k)`；② **封装**——`type Set map[interface{}]struct{}`（或泛型 `map[T]struct{}`），提供 Put/Has/Remove 方法，调用方语义更清晰、实现可替换 [源码]。
4. **value 类型即文档**：`struct{}` 在类型层面宣告「值不可用、不存在」，误用读取会被编译器拒绝；bool 值则语义暧昧（false 是「不存在」还是「存在但为假」？）——**类型即注释**，这是比省内存更重要的理由 [经验]。
5. **并发红线**：map **不支持并发读写**，并发 Set 必须加锁（`sync.RWMutex` 包装）或用 `sync.Map`——空 value 不豁免这条规则；并发安全的 map 专题见后续卡 [边界]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | struct{} 占多少空间？ | 基础 | 0 字节，unsafe.Sizeof 实测 | P5 停 |
| L2 | 怎么用 map 实现集合？ | 惯用法 | map[T]struct{}，key 即元素 | P5 停 |
| L3 | 为什么不用 map[T]bool？ | 对比 | value 0 vs 1 字节 + 类型语义更明确 | P6 停 |
| L4 | 并发场景怎么办？ | 红线 | map 非并发安全，RWMutex 或 sync.Map | P6 停 |
| L5 | 空结构体还有哪些用途？ | 延伸 | 信号 chan struct{}、零成本方法接收者 | P7 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0+ | struct{} 零尺寸语义恒定 | 按本质答 |
| Go 1.18+ | 泛型让 Set 封装类型安全：`type Set[T comparable] map[T]struct{}` | 封装版首选泛型，告别 interface{} |
| Go 1.9+ | sync.Map 适合读多写少/键集合稳定的并发场景 | 写密集仍推荐锁 + 普通 map |
| 地址相等性 | 空结构体变量地址**可能相同可能不同**，规范不保证 | 别依赖地址，见深卡实测 [边界] |
| 对齐特例 | 空 struct{} 作结构体**末位字段**需对齐 | 见 910 [边界] |

## 关键代码
```go
// 实测: 零尺寸 + value 尺寸对比
type empty struct{}

func main() {
	fmt.Println(unsafe.Sizeof(empty{})) // 0
	m1 := map[int]struct{}{1: {}}       // Set 形态
	m2 := map[int]bool{1: true}
	fmt.Println(unsafe.Sizeof(m1[1])) // 0
	fmt.Println(unsafe.Sizeof(m2[1])) // 1
}
// [实测] sizeof(struct{})=0; m1 value=0 vs m2 value=1 —— 省 1 字节/元素且语义更准

// 封装版 Set (泛型, Go 1.18+)
type Set[T comparable] map[T]struct{}

func (s Set[T]) Put(k T)      { s[k] = struct{}{} }
func (s Set[T]) Has(k T) bool { _, ok := s[k]; return ok }
func (s Set[T]) Remove(k T)   { delete(s, k) }
```

## 总结与追问预判
一句话记忆：**「struct{} = 零尺寸 + 无值语义：map 的 value、chan 的信号、类型即文档」**。零尺寸值的对齐特例（末位字段）见 910；信号场景 `chan struct{}` 的用法见 1238 [边界]；空 map 与 nil map 行为见 918。常追问「chan struct{} 为什么流行」——答信号只需要事件本身不需要载荷，`close(ch)` 广播 + 零内存；再追问「两个空结构体地址相等吗」——答**规范不保证**，实测栈变量与 new 都可能不同，别写依赖地址相等性的代码（详见深卡 [实测]）。

## ⚠️ 原文纠错
1. 术语归一：[经验] 源为语音转写，「空接构体/空界格体」应为「空结构体」，「foose」应为 false，「mac」应为 map，统一为规范术语。
2. 表述纠错：源示例 Set 的 key 用 interface{}，Go 1.18+ 应优先泛型 `comparable` 约束，类型安全且无装箱，本卡已按现代写法重写。
3. 补充：源未提 value 类型即文档的语义价值与地址相等性不保证的事实，本卡已补 [实测]。

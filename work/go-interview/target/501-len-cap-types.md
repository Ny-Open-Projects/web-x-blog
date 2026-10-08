# 501 哪些类型能用 len，哪些能用 cap

> 分类：Go 基础 / 类型系统 | 难度：L2 | 题型：辨析题 | 频率：高 | 关键词：**len、cap、数组、切片、chan、map、string、编译期常量**

> 原文锚点：第 1~34 段「数组长度与容量始终相等；map 容量无限制故不支持 cap；切片容量不小于长度；字符串 len 是字节数；数组长度在编译期求值可作常量；切片 len/cap 可用反射修改」

## 一句话总述
**len** 支持 5 类：**数组、切片、map、chan、string**（外加指针数组解引用等衍生形式）；**cap** 只支持 3 类：**数组、切片、chan**——**map 没有 cap**（容量无上限、无预分配语义），**string 没有 cap**（不可变、无容量概念）。语义上：`len` 是**当前元素个数**，`cap` 是**已分配空间的上限**；对 chan 而言 `len` 是**队列中待读元素数**、`cap` 是**缓冲区大小**。

## 面试官视角
P5 能背出「map 不能用 cap」；P6 要说出 chan 的 len/cap 语义差异（队列长度 vs 缓冲大小）以及**数组长度是编译期常量**这一条；P7 会追问「字符串的 len 是字节还是字符」——`len("Go语言") == 8` 而 `len([]rune("Go语言")) == 4`，这是 UTF-8 场景的固定考点。

## 主问答
**Q（面试官原话）：** Go 里哪些类型可以用 len？哪些可以用 cap？

1. **len 五类**：数组 `[N]T`、切片 `[]T`、map、chan、string `[源码]`。含义分别是固定长度、当前元素数、键值对数量、队列待读元素数、字节数。
2. **cap 三类**：数组、切片、chan `[源码]`。**map 不支持 cap**——map 会随写入自动扩容、没有"预分配容量"语义（`make(map[K]V, n)` 里的 n 只是 hint）；**string 也不支持**（不可变、无容量概念）。
3. **数组 len == cap 恒成立**，且**在编译期求值**：`const n = len([5]int{})` 合法，还能拿这个常量当另一个数组的维度 `[实测]`——本机实测 `const na = len([5]int{}) = 5` 可直接用于 `[na]int` 声明；而 `const nb = len(slice)` 会报 **`len(b) (variable of type []int) is not constant`**，因为切片长度是运行时值。
4. **chan 的 len/cap 最容易答错** `[实测]`：`make(chan int, 10)` 声明时给的是**容量**，此时 `len=0 cap=10`；只有往里发送后 `len` 才增长。**「chan 的长度是队列里已有的元素数，容量是缓冲区大小」**。
5. **string 的 len 是字节数不是字符数** `[实测]`：`"Go语言"` 的 `len = 8`（UTF-8 下一个汉字 3 字节），转 `[]rune` 后 `len = 4` 才是字符数。**统计中文字符个数必须转 rune**，这是固定陷阱。
6. **切片 len/cap 平时改不了，但反射和 unsafe 可以** `[实测]`：`make([]int, 1, 6)` 初始 `len=1 cap=6`，`reflect.Value.SetLen(2)` 后 `len=2 cap=6`、`SetCap(5)` 后 `len=2 cap=5`，`SetCap(8)` 越界会 panic `reflect: slice capacity out of range in SetCap`；Go 1.17+ 还能用 `unsafe.Slice(unsafe.SliceData(s), 6)` 直接把 `len` 重制成 6——**但两者都绕过了运行时保护，越界就是踩别人内存，生产禁用**。

## 追问链
| 层级 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 哪些类型能用 len？ | 基础 | 数组/切片/map/chan/string 五类 | 漏 string 或 chan，停在 L1 |
| L2 | 哪些能用 cap？ | 辨析 | 数组/切片/chan 三类，map 与 string 不行 | 以为 map 能 cap，停在 L2 |
| L3 | chan 的 len/cap 分别是什么？ | 语义精确 | len=队列待读元素数，cap=缓冲区大小 | 说反或说不清，停在 L3 |
| L4 | 数组长度是运行时值吗？ | 编译期常量 | 不是，编译期求值，可作 const 与数组维度 | 以为运行时求值，停在 L4 |
| L5 | `len("Go语言")` 是多少？ | UTF-8 陷阱 | 8（字节数），字符数需转 rune 得 4 | 答 4，停在 L5 |

## 版本与兼容性
| 版本 | 行为 | 现在该怎么答 |
|---|---|---|
| Go 全版本 | len 五类 / cap 三类 | 规则未变 |
| Go 1.17+ | `unsafe.Slice` / `unsafe.SliceData` | 可重制切片 len/cap，但生产禁用 |
| Go 1.20+ | `unsafe.SliceData` 取代 `&s[0]` 取址写法 | 避免 nil 切片的取址 panic |
| Go 1.21+ | `slices.Clip` / `slices.Grow` | 正规调 cap 的方式，替代反射 |

## 关键代码
```go
var a [5]int
b := make([]int, 3)
ch := make(chan int, 10)
m := map[string]int{"k1": 1}
s := "Go语言"

fmt.Println(len(a), cap(a)) // 5 5   数组恒等，且是编译期常量
fmt.Println(len(b), cap(b)) // 3 3   append 后变 4 6（容量翻倍）
fmt.Println(len(ch), cap(ch)) // 0 10  len 是队列元素数，cap 是缓冲大小
fmt.Println(len(m))           // 1     map 无 cap
fmt.Println(len(s), len([]rune(s))) // 8 4  字节数 vs 字符数

const na = len(a)      // 合法：数组长度编译期确定
// const nb = len(b)   // 编译错误：len(b) (variable of type []int) is not constant
```

## 总结与追问预判
答题骨架：**「len 五类、cap 三类、map 无 cap、string 字节数、数组是编译期常量、chan 是队列长度 vs 缓冲」**。面试官下一步常追问「`make(chan int, 10)` 之后 `len` 为什么是 0」「`make(map, 100)` 的 100 是什么意思」（只是预分配 hint，不是容量上限）、以及「切片扩容后 cap 怎么变」（见 `908-slice-grow.deep`）。

`[边界]` 本卡只讲 **len/cap 的适用类型与语义差异**，**不重述** nil 切片与空数组的对比（见 `415-nil-slice-vs-array`）、切片扩容的具体策略（见 `908-slice-grow.deep`）、`new` 与 `make` 的分工（见 `413-new-make-basics`）、nil 零值体系（见 `504-nil-zero-value-types`）。

## ⚠️ 原文纠错
1. 纠正：原文称「映射容量没有限制所以不支持 cap」——结论对但理由含糊，实质是 map 无预分配容量语义 `[经验]`。
2. 补充：原文未提 string 也**不能**用 cap，且 `len` 是字节数不是字符数 `[实测]`。
3. 补充：原文说「数组长度在编译期估值」正确，补实测：可作 const 与数组维度，切片则报 not constant `[实测]`。
4. 补充：原文用反射改 len/cap，实际 `SetCap` 越界会 panic，Go 1.17+ 的 `unsafe.Slice` 更危险 `[实测]`。
5. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语 `[经验]`。

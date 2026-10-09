> 原文锚点：第 1~13 段「通常我们在处理文本的时候呢，得到的是字节切片…直接转换呢，就会发生内存拷贝…string 转成 bat 强转过程中会发生内存的拷贝…bat 转成 string 强转过程中又会发生一次内存拷贝」（string→[]byte 与 []byte→string 的常规强转都会拷贝，底层指针变化）

## 一句话总述
`[]byte(s)` 和 `string(b)` 这种**常规强转都会发生一次内存拷贝**（分配新底层数组），大文本下浪费内存与 CPU；要实现「零拷贝」，必须绕过分配、让 string 与 []byte **共享同一块底层字节数组**——通过 `unsafe.Pointer` 在两者 header 间转换（或更推荐 Go 1.20+ 的 `unsafe.Slice`/`unsafe.StringData`）。

## 面试官视角
这是 Go 底层内存模型的经典题。考点：① 为什么强转会拷贝（header 结构不同 + 不可变语义）；② 零拷贝的原理（共享 Data 指针）；③ **Go 1.20+ 的官方零拷贝 API 是什么**——手写 `reflect.StringHeader` 是老写法且有 GC 风险。能说出「Data 是 uintptr、GC 不把它当指针根」这个坑，直接封神。

## 主问答
**Q（面试官原话）：** string 转 []byte 直接强转会发生拷贝吗？怎么做到零拷贝？

**A：**
1. **常规强转必拷贝**：`b := []byte(s)` 会**新分配**一块底层数组并把 s 的字节逐个复制过去——因为 string 不可变、[]byte 可变，Go 必须复制以保证 string 不被意外改写；`string(b)` 反向同理（再拷一次）。大文本下这是实打实的内存与 CPU 浪费。
2. **零拷贝本质 = 共享底层数组**：string 底层是 `StringHeader{Data uintptr, Len int}`，[]byte 底层是 `SliceHeader{Data uintptr, Len, Cap int}`。只要让 []byte 的 `Data` 指向 string 的 `Data`、Len/Cap 取 string 长度，两者就指向**同一块内存**，无需分配与复制。
3. **老写法（不推荐）**：用 `unsafe.Pointer` 把 `*string` 当 `*SliceHeader` 改写 Data/Len/Cap，共享底层数组实现零拷贝（见下代码）。但这种方式在 **Go 1.20+ 有 GC 风险**（SliceHeader.Data 是 `uintptr`，GC 不把它视为指针根，可能误回收）。
4. **官方写法（Go 1.20+ 推荐）**：`unsafe.Slice(unsafe.StringData(s), len(s))` 直接得到与原 string 共享底层数组的 []byte，类型安全、不必手搓 header，是现在的首选。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 强转会拷贝吗？ | header 差异/不可变 | 会，新分配+复制 | 说「不拷」算 L1 未过 |
| L2 | 零拷贝原理？ | 共享 Data 指针 | 让 []byte.Data 指向 string.Data | 说不清算 L2 未过 |
| L3 | 老写法怎么写？ | unsafe header | *string 当 *SliceHeader 改写 | 写不出算 L3 未过 |
| L4 | 老写法有坑吗？ | GC 风险 | Data 是 uintptr，GC 不扫为根 | 不知算 L4 未过 |
| L5 | 官方 API？ | Go1.20+ | unsafe.Slice/StringData | 只会老写法算 L5 未过 |

## 版本与兼容性
- `unsafe.Slice` / `unsafe.String` / `unsafe.StringData` / `unsafe.SliceData` 均为 **Go 1.20（2023-02）** 引入的官方零拷贝 API；`reflect.StringHeader`/`reflect.SliceHeader` 随之被**标注为不应用于构造**（直接构造不再保证 GC 正确）。
- string 不可变是语言保证；零拷贝得到的 []byte 一旦写入会破坏该保证，且若底层来自只读段（如字符串字面量在 `.rodata`）会触发 **SIGSEGV**（见 1113.md`）。
- 注意与「string 底层结构」基础（`903-string-storage.deep.md`、`903-string-data-pointer.md`）区分：本卡讲**转换是否拷贝**，那两张讲**存储结构本身**。

## 总结与追问预判
收口：**强转拷贝（新分配）、零拷贝共享 Data 指针；Go 1.20+ 用 `unsafe.Slice/unsafe.StringData` 官方 API，别再手写 header**。预判追问：① 反方向 []byte→string（见 1113.md`）；② 零拷贝的致命坑（不可变被破坏/GC/只读段 panic，见 1113.md`）。回答时把「Data 是 uintptr、GC 不扫为指针根」这句抛出来，是高阶分水岭。

## ⚠️ 原文纠错
源视频转写将 string / byte 切片 / unsafe.Pointer / string header / slice header 等音译为崩坏词（如「street」指代 string、「bat 切片」指代字节切片「byte slice」、「isavepoint」指代 unsafe.Pointer、「stringheader/sliceheader」保留但表述崩坏、「lidata」指代 Data 指针），本卡已还原为规范术语（string / []byte / unsafe.Pointer / StringHeader / SliceHeader / Data 指针）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 面试被问「零拷贝转换」，**先给 Go 1.20+ 官方 API 再提老写法**：`unsafe.Slice(unsafe.StringData(s), len(s))` 是正解。手写 `reflect.SliceHeader` 在 Go 1.20+ 是**反模式**（Data 为 uintptr、GC 不视为根、可能误回收底层数组），说出来比只背老写法更显你跟进了版本演进。

```go
package main

import (
	"reflect"
	"unsafe"
)

// 常规强转：发生拷贝（新分配底层数组）
func byCopy(s string) []byte { return []byte(s) }

// 老写法零拷贝（Go<1.20 常见，1.20+ 有 GC 风险，不推荐）
func StringToBytesLegacy(s string) []byte {
	sh := (*reflect.StringHeader)(unsafe.Pointer(&s))
	var b []byte
	bh := (*reflect.SliceHeader)(unsafe.Pointer(&b))
	bh.Data = sh.Data
	bh.Len = sh.Len
	bh.Cap = sh.Len
	return b
}

// 官方零拷贝（Go 1.20+ 推荐）：共享底层数组，类型安全
func StringToBytes(s string) []byte {
	return unsafe.Slice(unsafe.StringData(s), len(s))
}
```

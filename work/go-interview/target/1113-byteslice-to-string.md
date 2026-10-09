> 原文锚点：第 14~40 段「把一个字节切片呢零拷贝的方式转成一个字符串…把它转成反射的 sliceheader 类型…stringheader 的 data…我们最终转的呢是一个 string…指针类型的字节切片…星号表示的是对指针类型切片进行取值」（[]byte→string 零拷贝：构造 reflect string header，SliceHeader→StringHeader，注意 * 符号指针与取值含义）

## 一句话总述
`[]byte → string` 的零拷贝，是让新 string 的 `Data` 指针**直接指向**原 []byte 的底层数组、长度取原切片长度；老写法把 `*[]byte` 当 `*string` 解引用（两者 header 布局兼容），或更推荐 Go 1.20+ 的 `unsafe.String(&b[0], len(b))` 官方 API。

## 面试官视角
这是上一题的反方向，同样考 header 布局与 unsafe。考点：① 为什么 header 布局兼容就能直接 cast；② 老写法 `(*string)(unsafe.Pointer(&b))` 的原理与风险；③ **官方 `unsafe.String`**。能讲清「string 与 slice header 都是 Data+Len 开头，所以布局兼容可 reinterpret」这一底层事实，非常加分。

## 主问答
**Q（面试官原话）：** []byte 转 string 怎么零拷贝？为什么能直接把 *[]byte 当 *string 用？

**A：**
1. **header 布局兼容**：`string` 的 `StringHeader` 是 `{Data uintptr, Len int}`，`[]byte` 的 `SliceHeader` 开头也是 `{Data uintptr, Len int, Cap int}`——前两个字段完全一致。因此把 `*[]byte` 用 `unsafe.Pointer` 转成 `*string` 再解引用，Go 只会读前 16 字节（Data+Len），天然得到「指向同一底层数组、长度相同」的 string。
2. **老写法**：`s := *(*string)(unsafe.Pointer(&b))`——对 []byte 取地址、转成 `*string`、解引用。零分配、零拷贝，底层数组共享。
3. **官方写法（Go 1.20+ 推荐）**：`s := unsafe.String(&b[0], len(b))`，由标准库保证类型安全与 GC 正确，不必手动 reinterpret header。
4. **必须给 Cap/Len 一致**：零拷贝 string 的长度 = 原切片 Len；若越界读会导致读到切片 Capacity 之外的脏数据——长度必须严格取 `len(b)`，不能取 `cap(b)`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 为什么能直接 cast？ | header 布局兼容 | Data+Len 同布局可 reinterpret | 说不清算 L1 未过 |
| L2 | 老写法怎么写？ | unsafe reinterpret | *(*string)(unsafe.Pointer(&b)) | 写不出算 L2 未过 |
| L3 | 官方 API？ | Go1.20+ | unsafe.String(&b[0], len(b)) | 只会老写法算 L3 未过 |
| L4 | 长度取 len 还是 cap？ | 边界 | 取 len(b)，越界读脏数据 | 答 cap 算 L4 未过 |
| L5 | 共享底层有啥风险？ | 不可变破坏 | 改 []byte 会改 string（见 pitfalls） | 不知算 L5 未过 |

## 版本与兼容性
- `unsafe.String(ptr *byte, len int) string` 为 **Go 1.20+** 官方 API；对应 `unsafe.StringData(s)` 取 string 的 `*byte`、`unsafe.SliceData(slc)` 取切片 `*byte`。
- `reflect.StringHeader` 在 Go 1.20+ 文档明确「不应再用于构造新值」，仅适合**读取**已有 header；手写 `(*string)(unsafe.Pointer(&b))` 虽仍工作，但 GC 正确性不如官方 API 有保障。
- 注意 `&b[0]` 在 `len(b)==0` 时会 panic（空切片取首元素），需先判空或改用 `unsafe.SliceData`（Go 1.20+ 对空切片返回 nil 指针更安全）。

## 总结与追问预判
收口：**[]byte→string 零拷贝靠 header 布局兼容（Data+Len）+ 共享底层；Go 1.20+ 用 `unsafe.String(&b[0], len(b))`**。预判追问：① 正方向 string→[]byte（见 1113.md`）；② 共享底层的致命坑（不可变被破坏、只读段 panic、GC，见 1113.md`）。回答时把「string/slice header 前 16 字节同布局」这句抛出，最能体现底层功底。

## ⚠️ 原文纠错
源视频转写将 slice header / string header / 指针取值 / 字节切片 等音译为崩坏词（如「反射的 sliceheader 类型」保留但「hsisivepoint」「isavepoint」指代 unsafe.Pointer、「星号表示取值」语义保留但表述崩坏、「bat」指代 byte），本卡已还原为规范术语（SliceHeader / StringHeader / unsafe.Pointer / 指针解引用 / []byte）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 老写法 `*(*string)(unsafe.Pointer(&b))` 在 `len(b)==0` 时本身不 panic（只取地址不解引用元素），但 `unsafe.String(&b[0], len(b))` 的 `&b[0]` 会在空切片 panic。生产代码用 `unsafe.StringData`/`unsafe.SliceData`（Go 1.20+）对空切片返回 nil，更安全——这一细节是区分「写过」和「写对过」的关键。

```go
package main

import (
	"reflect"
	"unsafe"
)

// 老写法零拷贝：*[]byte 当 *string 解引用（header 前 16 字节布局兼容）
// ⚠ Go 1.20+ 不推荐手写，GC 正确性不如官方 API
func BytesToStringLegacy(b []byte) string {
	return *(*string)(unsafe.Pointer(&b))
}

// 官方零拷贝（Go 1.20+ 推荐）
func BytesToString(b []byte) string {
	if len(b) == 0 {
		return "" // 避免 &b[0] 对空切片 panic
	}
	return unsafe.String(&b[0], len(b))
}

// 反方向：string -> []byte 共享底层（Go 1.20+）
func StringToBytes(s string) []byte {
	return unsafe.Slice(unsafe.StringData(s), len(s))
}

var _ = reflect.StringHeader{}
```

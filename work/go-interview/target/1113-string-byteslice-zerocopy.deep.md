## 思路与架构
string 与 []byte 的零拷贝转换，本质是利用两者**底层 header 的内存布局兼容** + `unsafe.Pointer` 绕过「强转必分配」的语言规则，让两个类型**共享同一块字节数组**。

```text
底层结构（内存布局）
  string : | Data uintptr | Len int |            (16 字节)
  []byte : | Data uintptr | Len int | Cap int |  (24 字节)
  └─ 前 16 字节完全一致 → 可 reinterpret cast ─┘

转换路径
  string → []byte : 让 []byte.Data = string.Data, Len/Cap = string.Len
  []byte → string : 读 []byte 前 16 字节当 StringHeader（Data+Len）
  关键：都不分配新数组 = 零拷贝
```

**为何强转会拷贝**：`[]byte(s)`/`string(b)` 是**语义转换**——string 不可变、[]byte 可变，语言为保证不可变契约必须复制底层数组。零拷贝则**主动放弃该契约保护**（共享底层），因此需要 unsafe 且使用者自担风险。

## 方案取舍
| 方案 | 拷贝 | GC 安全 | 版本 | 适用 |
| --- | --- | --- | --- | --- |
| `[]byte(s)` / `string(b)` | 是（分配） | 安全 | 全版本 | 默认；需修改时用 |
| 手写 reflect header | 否 | ⚠ Go1.20+ 有风险 | 老代码 | 不推荐 |
| `unsafe.Slice`/`unsafe.String`（官方） | 否 | 安全 | Go 1.20+ | **首选零拷贝** |

**取舍结论**：绝大多数场景**不需要零拷贝**——一次分配的代价远小于 bug 风险。零拷贝只在「超大文本、转换极热路径、且结果只读」时收益明显，且应统一用 Go 1.20+ 官方 API，杜绝手写 `reflect` header。

**三大坑（必须记住）**：
1. 共享底层 → 改 []byte 破坏 string 不可变（连累其他持有者）。
2. 若 string 来自字面量（`.rodata` 只读段）→ 写入 SIGSEGV。
3. 手写 `SliceHeader.Data`(uintptr) → GC 不扫为指针根 → 可能误回收 → use-after-free（官方 API 用 `unsafe.Pointer` 规避）。

## 答题技巧
1. **先答语义再答底层**：开口先说「强转会拷贝是因为 string 不可变、[]byte 可变，语言必须复制保证契约」，再讲零拷贝如何绕过——显逻辑而非炫技。
2. **布局兼容一句话点破**：「string 与 slice header 前 16 字节都是 Data+Len，所以能 reinterpret」——这是所有零拷贝写法的根。
3. **版本演进是加分项**：明确「Go 1.20+ 用 `unsafe.String`/`unsafe.Bytes`/`unsafe.StringData`，手写 reflect header 是反模式（uintptr 非 GC 根）」。
4. **收尾落安全纪律**：「零拷贝结果当只读；需修改就老老实实拷贝」。这比只背写法更显工程成熟。
5. **避坑**：别说「零拷贝一定更快」（小字符串拷贝更便宜）；别把 `unsafe.String` 说成 Go 1.18 之前就有；别忽略空切片 `&b[0]` panic（用 `unsafe.SliceData`/`StringData` 规避）。

## 细节与核心 API

**强转必拷贝**（string 不可变契约保护，语言强制复制底层数组）：

```go
b := []byte(s) // 分配新数组
s2 := string(b)
```

**零拷贝首选：Go 1.20+ 官方 `unsafe` API**（用 `unsafe.Pointer` 作 GC 根，安全）：

```go
bs := unsafe.Slice(unsafe.StringData(s), len(s)) // string -> []byte，共享底层，只读
s3 := unsafe.String(&b[0], len(b))               // []byte -> string，共享底层，只读
// 写入 bs 会破坏 s 不可变契约，连累其他持有者；
// 若 s 来自字面量（.rodata 只读段），写入 -> SIGSEGV
```

**反模式（Go < 1.20 手写 reflect header）**：`SliceHeader.Data` 是 `uintptr`、非 GC 根，可能误回收导致 use-after-free；官方 API 用 `unsafe.Pointer` 规避，禁止手写 header。

**三大坑速记**：① 共享底层改 `[]byte` 破坏 string 不可变；② 字面量 string 写入 SIGSEGV；③ `uintptr` header 不被 GC 扫描 → use-after-free。

> 边界：string 内存泄漏完整链条见 905；逃逸分析见 1119。本卡只讲 string↔[]byte 零拷贝。

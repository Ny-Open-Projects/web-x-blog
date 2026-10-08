# 1112 Go 值尺寸（Size of Value）体系

> 分类：Go/性能 | 难度：L2 | 题型：基础题 | 频率：中 | 关键词：**值尺寸** / **直接值部** / **零尺寸值** / **unsafe.Sizeof**
> 原文锚点：第 1~31 段「赋值/传参/通道发送都复制直接值部；各类型值尺寸(bool1/int64 8/complex128 16/int1word/string2word/slice3word/map1word/interface2word)；struct=字段和+padding；array=元素×长度；零尺寸值(空结构体/[N]空结构体数组)」

## 一句话总述
Go 里赋值、传参、通道发送都复制**直接值部**（direct part），其大小叫**值尺寸**。基础类型尺寸固定（bool=1B、int64=8B、complex128=16B、string=2 机器字、slice=3 机器字、interface=2 机器字）；**struct=字段和+padding**，**array=元素尺寸×长度**；空结构体与元素为零尺寸的数组是**零尺寸值**（占 0 字节）。

## 面试官视角
- 意图：考察对"Go 传值到底复制多少"的底层认知，是性能优化的地基。
- P5 知道传值会复制；P6 能背出常用类型值尺寸（string/slice/interface 是 header）；P7 能讲清 struct padding、array 动态尺寸、零尺寸值的用途。
- 红旗：以为 slice 传参复制底层数据；以为大 struct 和 slice 复制代价一样。
- 惊艳点：点出零尺寸值（空结构体作 map 集合标记、channel 信号）的妙用；struct 尺寸含 padding。

## 主问答
**Q（面试官原话）：** Go 里传参复制的是什么？不同类型复制成本差多少？
**A：**
1. **结论**：复制的是**直接值部**——其尺寸因类型而异：bool/int8=1B、int32(rune)/float32=4B、int64/uint64/float64/complex64=8B、complex128=16B；int/uint/uintptr=1 机器字（64 位=8B）；string=2 机器字、slice=3 机器字、map/chan/func=1 机器字、interface(any)=2 机器字。
2. **机制**：**struct** 尺寸=所有字段尺寸之和 + 填充(padding)字节（对齐需要）；**array** 尺寸=元素尺寸×长度（动态，随长度变）。二者是仅有的"动态尺寸"类型——字段/元素越多，复制越贵。
3. **边界**：**零尺寸值**有两类——不含任何 >0 字段的空结构体、元素尺寸为零的数组（如 `[3]struct{}{}`），它们占 0 字节，常作 map 集合标记或 channel 信号，复制零成本 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 传值复制啥 | 基础 | 直接值部 | 判 P5 |
| L2 | 常用尺寸 | 数值 | string2word/slice3word | 判 P6 |
| L3 | struct/array | 动态 | 字段和+padding/元素×长 | 判 P6+ |
| L4 | 零尺寸值 | 进阶 | 空结构体/[N]空结构体 | 判 P7 |
| L5 | padding 影响 | 细节 | 对齐插入填充字节 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | 值尺寸规则恒定；64 位系统机器字=8B（源示例用 32 位故 slice=12B，现代 64 位应为 24B），答题时注明架构 `[经验]` |

## 关键代码
```go
// 用 unsafe.Sizeof 打印各类值的"直接值部"尺寸
func sizes() {
    var s struct{ a int64; b int32 } // 含 padding：8 + 4 + 4(pad) = 16
    fmt.Println(unsafe.Sizeof(bool(false)))      // 1
    fmt.Println(unsafe.Sizeof(int64(0)))         // 8
    fmt.Println(unsafe.Sizeof(complex128(0)))    // 16
    fmt.Println(unsafe.Sizeof(""))               // 16 (2×8, 64位)
    fmt.Println(unsafe.Sizeof([]int{}))          // 24 (3×8, 64位)
    fmt.Println(unsafe.Sizeof(map[int]int(nil))) // 8  (1×8)
    fmt.Println(unsafe.Sizeof(any(0)))           // 16 (2×8)
    fmt.Println(unsafe.Sizeof(s))                // 16 (含 padding)
    fmt.Println(unsafe.Sizeof(struct{}{}))       // 0  (零尺寸值)
}
```

## 总结与追问预判
- 复制=直接值部；基础类型固定、struct/array 动态（含 padding）；零尺寸值占 0。
- 预判：复制代价与指针取舍 → 见 1112-copy-cost-pointer；for-range 复制陷阱 → 见 1112-forrange-copy-trap。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"各类型值尺寸（bool1/int8 1/int32 4/int64 8/complex128 16/int1word/string2word/slice3word/map1word/interface2word）、struct=字段和+padding、array=元素×长度、零尺寸值（空结构体/[N]空结构体数组）"的描述，与 unsafe.Sizeof 实测一致。补充校正：源示例为 32 位系统（机器字=4B，故 slice=12B），已在版本栏注明现代 64 位系统机器字=8B（slice 头=24B）。仅做了 ASR 解码将多组术语崩坏词（直接直部→直接值部、间接值部→间接值部、值尺寸→值尺寸、速度→切片、速组→数组、root类型→rune、符合类型→复数类型、原生字→机器字、案例类型→any 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。

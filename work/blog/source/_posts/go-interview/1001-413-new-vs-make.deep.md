---
disableNunjucks: true
title: "413-new-vs-make.deep"
date: 2026-10-10 09:23:39
categories: [Go面试题集]
tags: [Go面试题集]
---

## 思路与架构
"new 和 make 的区别"是 Go 内存分配的第一题：把两个内置函数按「适用类型 / 返回值 / 是否初始化 / 参数 / nil 语义」五维拆开，再落到 slice 的实测差异与 new 的实战定位。它把 413- 三张主卡收敛成一张可现场背的速查表。

```text
new vs make 速查矩阵
  维度          new(T)              make(T,args)
  适用类型      任意类型            仅 slice/map/chan
  返回值        *T(指针)            T(本身)
  内存          清零零值            分配+初始化引用
  slice/map     指向 nil,需再make   非 nil,就绪可用
  参数          仅类型              类型+len[/cap]
  实战          数组 *[N]T 有用     引用类型首选
```

## 方案取舍
| 场景 | 用谁 | 理由 |
| --- | --- | --- |
| slice/map/chan 创建 | make | 初始化就绪、非 nil |
| 需显式 *T 且清零 | new | 返回 *T、内存清零 |
| 数组指针且清零 | new([N]T) | 等价于 &[N]T{} |
| 日常值/指针 | 字面量 | 最直观，少用 new |

**取舍结论**：引用类型一律 make；要指针且清零才考虑 new；数组是 new 少有的甜点。new 在 slice/map 上是"清零但不初始化引用"→ 指向 nil，这是它鸡肋的根因。

**分层边界**：数组声明的 new 写法细节在 414；本卡只做 new/make 五维对比与 slice 实测，不重述数组四种声明 [边界]。

## 答题技巧
1. **先抛三句**：make 仅三类型返回 T 并初始化；new 任意类型返回 *T 仅清零。
2. **slice 实测收尾**：make 非 nil 可直接用，new 是 nil 指针还要初始化——最直观。
3. **点 nil 判定**：看"引用有没有被初始化"，不看是否指针（s5 字面量也非 nil）。
4. **new 实战定位**：引用类型鸡肋、数组有用、工程偏好字面量。
5. **避坑**：不说"new 的 slice 能直接 append"；不把 new 和字面量说成完全等价；不忽略 map 同样适用上述规律。

## 细节与核心 API

```go
// new(T)：返回 *T，T 被零值初始化（只分配+清零），适用于任意类型
p := new(int)        // *int，指向 0
s := new(string)     // *string，指向 ""
// make：仅用于 slice/map/channel，返回“已初始化可用”的类型本身（非指针）
sl := make([]int, 0, 10)   // []int，已分配底层数组，cap=10
m  := make(map[string]int) // map，可直接写
ch := make(chan int, 3)    // chan，可立即收发
// 区别：
//  new 不初始化内部数据结构（如 map 用 new 只是 nil map，写入 panic）
//  make 针对三种引用类型做“运行所需”的初始化（哈希表/环形缓冲/通道结构）
// 经验：slice/map/chan 一律用 make；其它用 new 或直接字面量取地址 &T{}
// 不能 make(new(int)) 或 new(make(...))，二者不互套
```

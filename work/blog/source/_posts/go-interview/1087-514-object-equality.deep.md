---
disableNunjucks: true
title: "514 == 与 DeepEqual 分工深挖"
date: 2026-10-10 09:02:18
categories: [Go面试题集]
tags: [Go面试题集]
---

## 思路与架构
"判断两个对象是否完全相同"本质是**== 与 reflect.DeepEqual 的分工**：== 守类型系统（可比较类型才能比、比地址/值），DeepEqual 做结构深度遍历（递归+visit 防环）。它把 514- 三张主卡收敛成"何时用哪个"的选型表。

```text
对象相等判定选型树
  能否 == ? ──► 可比较类型(int/string/ptr/struct全可比字段…)
   │ 是                 └► 比类型+值/地址（快、编译期保证）
   │ 否(map/slice/func/含不可比字段)
   └─► 用 reflect.DeepEqual
         ├─ 比结构深度(递归)
         ├─ 指针比"指向的值"非地址
         ├─ 循环引用→true(visit 防环)
         └─ 代价:反射开销、容量不参与、NaN 特殊
```

## 方案取舍
| 场景 | 用谁 | 理由 |
| --- | --- | --- |
| 可比较类型比相等 | == | 快、编译保证 |
| map/slice/结构体比内容 | DeepEqual | == 不可比/只比地址 |
| 指针指向同值 | DeepEqual | 比"值"非"址" |
| 大结构/热路径 | 手写 Equal | 反射开销大 |

**取舍结论**：== 是类型系统的快路径，DeepEqual 是深度兜底；map/slice 只能 DeepEqual。命名类型 vs 匿名、指针同值、循环引用三处两者结果相反——记住这三点就够答题。

**分层边界**：可比较类型清单见 509；切片 == 规则见 415；指针 == 见 503（只引不重述）；本卡只做 == vs DeepEqual 分工 [边界]。

## 答题技巧
1. **先分工**：可比较类型用 ==，map/slice/含不可比字段用 DeepEqual。
2. **三反例**：命名类型名不同 / 指针同值不同址 / 循环引用——各给一例结果相反。
3. **点代价**：DeepEqual 反射开销、容量不参与、NaN 与自身 false。
4. **防坑**：绝不 `map == map`（编译不过）；热路径别 DeepEqual 大结构。
5. **避坑**：不说"DeepEqual 和 == 总一致"；不忽略 unexported 字段也参与比较。

## 细节与核心 API

```go
import "reflect"
a := []int{1, 2, 3}
b := []int{1, 2, 3}
fmt.Println(a == b)                 // 编译错误：slice 不能用 ==
fmt.Println(reflect.DeepEqual(a, b)) // true：递归比较元素
// == 对 comparable 类型比较（值/指针/数组/字段全 comparable 的结构体）
// DeepEqual 对 nil slice 与空 slice 视为不等，需注意
fmt.Println(reflect.DeepEqual([]int(nil), []int{})) // false
// 性能敏感场景改写为手动字段比较，避免反射开销
```

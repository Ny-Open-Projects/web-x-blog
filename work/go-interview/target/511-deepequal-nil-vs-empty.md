# 511 DeepEqual 与 bytes.Equal 比较 []byte：nil 语义分歧

> 分类：Go 类型系统 / 相等判断 | 难度：L2 | 题型：对比题 | 频率：中 | 关键词：**DeepEqual**/**bytes.Equal**/**nil 切片**/**IsNil**/**slices.Equal**

> 原文锚点：第 2~10 段「两个 nil 值切片 DeepEqual 为 false → IsNil 不对称 → bytes.Equal 为 true」

## 一句话总述
比较 `[]byte` 时两函数在 **nil 语义上分歧**：`reflect.DeepEqual([]byte(nil), []byte{})` 为 **false**——它先比 `IsNil()`，一个是 nil 一个不是，与内容无关；`bytes.Equal` 只比**内容**，把 nil 和空切片都当「空」处理，返回 **true**。非 nil 情形下两者一致。`==` 与 DeepEqual 的类型/指针/循环三大差异见 `514-deepequal-vs-equal.md`，本卡聚焦 nil 这一条。

## 面试官视角
这题是「nil 切片 vs 空切片」与「比较函数语义」的交叉考点。考官用一对最薄的反例（`var b []byte` vs `[]byte{}`）就能测出你是否真明白：**DeepEqual 的相等定义包含「nil 性」这一维度，bytes.Equal 的相等定义只有「内容」一个维度**。答不出 false/true 的分歧行为，说明对 nil 切片的两面性还没吃透。

## 主问答
**Q（面试官原话）：** DeepEqual() 与 bytes.Equal() 比较切片时有何区别？

1. **问题设定**：`var b1 []byte`（仅声明，nil）与 `b2 := []byte{}`（字面量，非 nil 空切片）——两者内容都是空，但 nil 性不同。
2. **DeepEqual 的回答：false**。反射进入 deepValueEqual 后，对 slice 分支先做 `v1.IsNil() != v2.IsNil()` 的短路判断——一个 IsNil 为 true 一个为 false，直接返回 false，**根本不比内容**。
3. **bytes.Equal 的回答：true**。语义是「两个字节切片内容是否相同」，实现上 nil 切片与空切片 len 都是 0，等长即等（`len(x)==len(y) && memequal`），nil 与空**无区别**。
4. **[实测] 全景对账**（go1.26.5）：DeepEqual(b1,b2)=false 而 bytes.Equal=true；两个都 nil（b1 vs b3）DeepEqual=**true**（IsNil 对称）；非空字面量（"go" vs "go"）两者都 true——**分歧只出现在「nil 性不对称」时**。
5. **泛型时代的选择**：1.21+ 的 `slices.Equal` 泛型版与 bytes.Equal 同语义（[实测] slices.Equal([]byte(nil), []byte{})=true、slices.Equal([]int(nil), []int(nil))=true），新代码比内容统一用 slices.Equal，`reflect.DeepEqual` 留给「含指针/结构体的深度比较」。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | nil 切片和空切片内容一样吗？ | 分不清 len 都为 0 但 IsNil 不同 |
| L2 | DeepEqual 对这对输入返回什么？ | 说不清 false 与 IsNil 短路 |
| L3 | bytes.Equal 为什么是 true？ | 说不清「只比内容/等长即等」 |
| L4 | 两个都 nil 时 DeepEqual 呢？ | 说不清 true（IsNil 对称） |
| L5 | 泛型切片怎么比？ | 说不清 slices.Equal 与语义归属 |

## 版本与兼容性
| 函数 | nil vs 空 | 双 nil | 非空同内容 | 说明 |
|------|-----------|--------|------------|------|
| reflect.DeepEqual | **false** | true | true | 相等含 nil 性维度 |
| bytes.Equal | true | true | true | 只比内容（len+memequal） |
| slices.Equal (1.21+) | true | true | true | 泛型版 bytes.Equal 语义 |

## 关键代码
```go
var b1 []byte  // nil
b2 := []byte{} // 非 nil 空切片

fmt.Println(reflect.DeepEqual(b1, b2)) // false: IsNil 不对称, 不比内容
fmt.Println(bytes.Equal(b1, b2))       // true:  内容都为空
fmt.Println(slices.Equal(b1, b2))      // true:  1.21+ 泛型, 同 bytes.Equal
```

[实测] 输出三行：false / true / true；`b1 == nil` 为 true、`b2 == nil` 为 false。

## 总结与追问预判
核心：**DeepEqual 的相等含 nil 性（IsNil 不对称即 false），bytes.Equal/slices.Equal 只比内容（nil 与空无区别）；分歧仅出现在 nil 性不对称时**。追问常拐向「== 能不能比切片」（不能，编译错）、DeepEqual 的机制细节与循环引用见 `514-deepequal-mechanism.md`/`514-deepequal-pitfalls.md`、`==` 三大语义差异见 `514-deepequal-vs-equal.md`、nil 语义族见 `504-nil-comparability.deep.md`，nil 性与深比较的交叉深挖见 `511-nil-semantics-equal.deep.md`。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文说「b2 用字面量声明相当于调用了 make 初始化」——不精确：字面量 `[]byte{}` 由编译器生成**长度 0 的非 nil 切片头**（data 指针可为 zerobase），并非显式调用 make；两者效果等价（len=0、非 nil），机制描述失准。
2. 术语归一：源文「bestequo/bestequal」=bytes.Equal、「deepequo」=DeepEqual、「你有/正变量/字变量」=nil/声明/字面量的音转，已统一为规范术语。

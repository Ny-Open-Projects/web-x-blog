# 514 reflect.DeepEqual 的实现机制

> 分类：Go 反射 / 相等判断 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**DeepEqual** / **nil 先判** / **类型校验** / **deepValueEqual 递归** / **visit 防环**
> 原文锚点：第 5~19 段「DeepEqual 先判都 nil→true；再 reflect 取类型不一致→false；再 deepValueEqual(switch 按类型+递归)；传 visit map 记录已比地址防死循环去重」

## 一句话总述
`reflect.DeepEqual` 判两个对象"深度相等"：先**都 nil→true**，再取类型**不一致→false**，最后 `deepValueEqual` 用 **switch 按类型逐一比 + 递归**下钻；并借助一个 **visit map 记录已比较的指针地址**，既去重又防止**循环引用导致无限递归**。源码把"代价小的判断前置提前返回"的写法值得借鉴。

## 面试官视角
- 考察意图：是否真读过 DeepEqual 源码、理解其短路与防环设计
- P5 知 DeepEqual 做深度比较；P6 能讲"nil/类型前置 + switch 递归"；P7 能讲清 visit map 的双重作用（去重 + 防环）
- 红旗：以为 DeepEqual 是简单逐字段比；不知道循环引用会爆栈
- 惊艳点：点出"visit map 记录已比地址——既是性能去重，也是循环引用的安全网（返回 true 终止递归）" [源码]

## 主问答
**Q（面试官原话）：** reflect.DeepEqual 内部是怎么实现的？
**A：**
1. **两道前置短路**：先判**双方都 nil→true**；再 `reflect.TypeOf` 取类型，**不一致直接 false**——小代价判断前置，提前返回提升效率 [源码]。
2. **switch + 递归**：核心 `deepValueEqual` 用 **switch 按具体类型**（基础/数组/切片/结构体/map/ptr/chan…）做判定，遇到复合类型**递归**下钻比内部元素 [源码]。
3. **visit map 防环去重**：递归过程把"已比较且为真的指针地址"记入 visit map；再遇到同一地址直接取上次结果——既减少重复比较，又**避免循环引用无限递归** [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | DeepEqual 干啥 | 概念 | 深度相等 | P5 |
| L2 | 前置判断 | 机制 | nil/类型短路 | P6 |
| L3 | 怎么递归 | 机制 | switch+递归 | P6+ |
| L4 | 循环引用 | 安全 | visit 防环 | P7 |
| L5 | 性能 | 实战 | 反射开销大 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 全版本 | DeepEqual 语义稳定 | nil/类型前置 + switch 递归 + visit 防环长期成立 |

## 关键代码
```go
// reflect.DeepEqual 的套路（示意，非源码）：小代价判断前置
func deepEqual(x, y any) bool {
    if x == nil && y == nil { return true }                   // 都 nil
    if reflect.TypeOf(x) != reflect.TypeOf(y) { return false } // 类型不同
    return deepValueEqual(reflect.ValueOf(x), reflect.ValueOf(y), make(map[visitKey]bool))
}
// deepValueEqual 内部按类型 switch + 递归；visit 记录已比地址防环
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（Go 语言、reflect、DeepEqual、切片/映射/函数、nil、双等号、deepValueEqual 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- DeepEqual = nil/类型前置 + switch 递归 + visit 防环；反射有开销，热路径慎用于大结构。
- == vs DeepEqual 区别见 514-deepequal-vs-equal；可比较类型清单见 509-comparable-types（只引不重述）。

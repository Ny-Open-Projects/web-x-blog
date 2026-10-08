# 514 DeepEqual 实战陷阱与边界

> 分类：Go 反射 / 相等判断 | 难度：L3 | 题型：用法题 | 频率：中 | 关键词：**map 不可 ==** / **容量不影响** / **反射开销** / **unexported 也比** / **NaN**
> 原文锚点：第 20~28,44~52 段「map 不可 == 但 DeepEqual 可(容量不同值同→true)；循环链表 DeepEqual true；反射有开销、不保证顺序无关」

## 一句话总述
实战里 `reflect.DeepEqual` 的几个要点：**map 不能用 ==（编译报错）但 DeepEqual 可**，且**容量不同不影响结果**（只比值）；**循环引用返回 true** 而非死循环；代价是**反射开销大**、**比较 unexported 字段**、且**不保证"顺序无关"语义**（map 本身无序但键值对逐一比）。理解边界才能用对。

## 面试官视角
- 考察意图：是否知道 DeepEqual 的能力边界与性能代价
- P5 知 map 用 DeepEqual 比；P6 能讲容量不影响、循环引用安全；P7 能讲反射开销 + unexported 也参与 + NaN 特殊处理
- 红旗：用 == 比 map（编译不过）；在热路径用 DeepEqual 比大结构（性能）
- 惊艳点：点出"两个 map 容量 10 vs 100、值相同，DeepEqual 仍 true——容量不是比较维度" [源码]

## 主问答
**Q（面试官原话）：** 用 DeepEqual 比 map/结构体有什么要注意的？
**A：**
1. **map 只能 DeepEqual**：`map` 不可用 `==`（编译报错），`DeepEqual` 可；且**只比键值、容量不参与**——容量 10 与 100 的两 map 值相同即 true [源码]。
2. **循环引用安全**：含环的结构（如循环链表 A→B→C→A）`DeepEqual` 返回 **true** 且不死循环（visit 防环），`==` 则 false [源码]。
3. **代价与边界**：基于**反射**，比大结构有开销；**unexported 字段也参与比较**；浮点 `NaN` 与自身 `DeepEqual` 为 false（符合 IEEE）——热路径应改用专用比较或手写 equal 方法 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | map 怎么比 | 用法 | DeepEqual | P5 |
| L2 | 容量影响? | 边界 | 不影响 | P6 |
| L3 | 循环引用 | 安全 | true 防环 | P6+ |
| L4 | 性能 | 实战 | 反射开销大 | P7 |
| L5 | NaN 呢 | 边界 | 与自身 false | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 全版本 | 语义稳定 | map 只能 DeepEqual、容量不参与、NaN 与自身不等 |

## 关键代码
```go
m1 := make(map[string]int, 10)
m2 := make(map[string]int, 100)
m1["a"], m2["a"] = 1, 1
fmt.Println(reflect.DeepEqual(m1, m2)) // true：容量不参与比较

type Link struct{ Next *Link }
a, b, c := &Link{}, &Link{}, &Link{}
a.Next, b.Next, c.Next = b, c, a // A→B→C→A 成环
fmt.Println(reflect.DeepEqual(a, a)) // true：visit 防环，不死循环
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（Go 语言、reflect、DeepEqual、切片/映射/函数、nil、双等号、循环引用 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- DeepEqual 比 map/结构/循环引用都安全，但反射有开销、容量不参与、NaN 特殊。
- 原理见 514-deepequal-mechanism；== 差异见 514-deepequal-vs-equal；可比较清单见 509（只引不重述）。

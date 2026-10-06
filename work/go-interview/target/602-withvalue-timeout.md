# 602 WithValue / WithTimeout / WithDeadline 三件套

> 分类：并发模型 | 难度：L1 | 题型：八股题 | 频率：高 | 关键词：**WithValue** / **WithTimeout** / **WithDeadline**
> 原文锚点：第 42~63 段「WithValue 传 requestID…WithTimeout 相对时间…WithDeadline 绝对时间点」

## 一句话总述
WithValue 在 context 上挂请求作用域键值对；WithTimeout(d) 等价于 WithDeadline(time.Now().Add(d))，前者给相对时长、后者给绝对时刻，二者都返回子 ctx 与 cancel。

## 面试官视角
- 考察意图：区分三个派生函数与相对/绝对时间，知道返回值是 (ctx, cancel)。
- P5 会调 WithXxx / P6 知 WithTimeout=WithDeadline 的语法糖 / P7 知 key 应用自定义类型防冲突。
- 红旗：以为 WithValue 能改已存值；把 WithTimeout 第二参当绝对时间。
- 惊艳点：WithTimeout 内部直接调 WithDeadline(now.Add(d))，二者共享同一截止逻辑 `[源码]`。

## 主问答
**Q（面试官原话）：** WithTimeout 和 WithDeadline 有什么区别，怎么用？
**A：**
1. **结论**：WithTimeout 接收相对时长，WithDeadline 接收绝对时间点，语义一致。
2. **机制**：WithTimeout(d) 即 WithDeadline(time.Now().Add(d))，到点关闭 Done 触发取消 `[源码]`。
3. **边界**：二者都返回 cancel，必须 defer/call cancel 释放定时器，否则资源不回收。
**加分层：** WithValue 的 key 推荐用自定义类型（非 string）避免不同包键名碰撞。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 三个函数 | 概念 | 说名字 | 换题 |
| L2 | timeout 区别 | 机制 | 相对 vs 绝对 | 判 P5 |
| L3 | cancel 干嘛 | 边界 | 释放定时器 | 判 P6 |
| L4 | Value key | 权衡 | 自定义类型 | 判 P6+ |
| L5 | 派生链层级 | 实战 | 多层包裹 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.7 起稳定 `[源码]` | 无 | 三函数自 1.7 不变；WithTimeout 始终是 WithDeadline 的封装 |

## 关键代码
```go
// 示意，未验证：链式派生 ctx
ctx := context.WithValue(r.Context(), "rid", rid) // 挂 requestID
ctx, cancel := context.WithTimeout(ctx, time.Second)
defer cancel() // 必须释放
```

## 总结与追问预判
- WithTimeout 是 WithDeadline 的语法糖；二者均返回 cancel 须调用。
- 预判：cancel 调用时机与泄漏 → 见 602-context-best-practices。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：核对 WithValue/WithTimeout/WithDeadline 的签名与相对/绝对时间关系；仅做机翻解码（withvalue→WithValue、withtimeout→WithTimeout、withthatline→WithDeadline、负极→父级、蛋→Done 等还原），技术结论未做更正。

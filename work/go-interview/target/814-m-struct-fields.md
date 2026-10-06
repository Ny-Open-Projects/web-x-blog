# 814 m 结构体字段与 P 的关联

> 分类：并发模型 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**curg** / **p** / **nextp** / **oldp** / **preemptoff**
> 原文锚点：第 127~181 段「m 结构体有 g0 字段…p 字段表示与当前 m 关联的 processor」

## 一句话总述
m 是内核工作线程的表示：curg 是当前 g，p/nextp/oldp 管理与之绑定的处理器，preemptoff 临时关抢占，g0/tls 支撑调度与线程本地存储。

## 面试官视角
- 考察意图：m 如何与 P 绑定、系统调用时如何解绑
- P5 知道 m 是线程、curg 是当前 g / P6 能讲 oldp 在 syscall 后恢复 / P7 能讲 preemptoff 的代价
- 红旗：认为 m 永远绑定同一个 p；答不出为何有 nextp/oldp
- 惊艳点：m 执行系统调用时把 p 存进 oldp，结束后据此重绑原 p `[源码]` runtime2.go

## 主问答
**Q：** m 结构体里和 P 调度最相关的字段有哪些？
**A：**
1. **curg / g0**：curg 是当前运行的 g，g0 是带调度栈的特殊 g（执行调度/GC）`[源码]`。
2. **p / nextp / oldp**：p 为当前绑定的 P，nextp 为下一个要绑的 P，oldp 暂存 syscall 前的 P `[源码]`。
3. **preemptoff / mallocing / id**：preemptoff 非空则禁抢占，mallocing 标记分配中，id 为 m 唯一标识 `[源码]`。
**加分层：** m 与 P 总数上一一绑定，但 m 总量（上限 1 万）通常多于 P。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | m 是什么 | 概念 | 内核工作线程 | 换题 |
| L2 | g0 干什么 | 机制 | 调度/GC 用特殊栈 | 判 P5 |
| L3 | oldp 何时用 | 边界 | 系统调用前后保存恢复 | 判 P6 |
| L4 | 为何禁抢占 | 权衡 | 关键区/调试，牺牲公平 | 判 P6+ |
| L5 | m 过多如何回收 | 实战 | 空闲 m 进休眠列表 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.20+ 稳定 | m 上限 MaxMCount=10000 长期未变 `[存疑]` | 照"curg/p/oldp + g0"答即可 |

## 关键代码
```go
// 示意，未验证：m 结构体与 P 关联字段（节选）
type m struct {
    g0    *g        // 调度用的特殊 g
    curg  *g        // 当前运行的 g
    p     puintptr  // 当前绑定的 P
    nextp puintptr  // 下一个要绑的 P
    oldp  puintptr  // syscall 前暂存的 P
    id    int64     // m 唯一标识
}
```

## ⚠️ 原文纠错
原文"preamactof/preamtof/pryelocof"等均严重崩坏，正确字段为 `preemptoff`（非空字符串时禁用抢占并保持当前 g 在本 m 执行）`[源码]`。其余 m 字段描述核对无误。

## 总结与追问预判
- m 经 curg/p/oldp 与 P 协作，g0 承载调度栈，preemptoff 临时关抢占；系统调用靠 oldp 解绑/重绑。
- 深入见 814-m-struct-fields.deep.md（m 内存布局与 g0 设计）。

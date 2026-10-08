# 173 用切片（数组）实现栈

> 分类：数据结构 / Go | 难度：L2 | 题型：实现题 | 频率：中 | 关键词：**栈**/**FILO**/**切片**/**push/pop/peek**/**切片截取内存泄漏**

> 原文锚点：第 10~28 段「数组（切片）实现栈」

## 一句话总述
栈是**先进后出（FILO）**结构，只在栈顶出入。用 Go 切片实现时，`push` 即 `append` 到末尾、`pop` 弹出末尾元素、`peek` 返回末尾元素不弹出；**注意切片截取 `[0:size-1]` 不会释放底层数组**，频繁 pop 易内存泄漏，应重建切片或显式置 nil 让旧元素被 GC。

## 面试官视角
切片实现栈是手撕题高频。考官不仅看能不能写对 push/pop，更看是否意识到「切片截取式 pop 的内存泄漏」并给出重建切片的写法——这是区分「写过」和「想过」的点。

## 主问答
**Q（面试官原话）：** 用数组怎么实现一个栈？

1. **结构定义**：用切片存元素，加一个 `size` 计数（也可直接 `len(slice)`）；并发场景再加 `sync.Mutex` / `sync.RWMutex`。
2. **push 追加末尾**：`append(data, x)` 并把 size+1，栈顶即 `data[size-1]`（下标从 0 起）。
3. **pop 弹末尾**：返回 `data[size-1]` 并 size-1；朴素写法 `data = data[0:size-1]` 只是缩了视图，**底层数组最后一个元素仍被引用、不被回收**。
4. **防内存泄漏**：pop 时应把弹出的槽位置 nil，或新建切片把前 size-1 个元素复制过去并赋给 `data`，使旧底层数组失去引用被 GC 释放。
5. **peek 不弹出**：直接返回 `data[size-1]`，size 不变；判空看 `size == 0`。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 栈的特征？ | 说不清 FILO |
| L2 | push/pop 怎么写？ | 说不清 append/末尾 |
| L3 | 截取 pop 有什么坑？ | 说不清内存泄漏 |
| L4 | 怎么避免泄漏？ | 说不清重建切片/置 nil |
| L5 | 并发怎么保安全？ | 说不清加锁 |

## 版本与兼容性
| 操作 | 时间复杂度 | 说明 |
|------|------------|------|
| push | O(1) 均摊 | 切片扩容时偶发 O(n) |
| pop | O(1) | 重建切片写法仍为 O(1) 复制 |
| peek | O(1) | 取末元素 |

## 关键代码
```go
type Stack struct {
    data []int
    size int
    mu   sync.RWMutex
}

func (s *Stack) Push(x int) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.data = append(s.data, x)
    s.size++
}

// Pop 置 nil + 缩视图，断开旧槽位引用，避免底层数组内存泄漏
func (s *Stack) Pop() (int, bool) {
    s.mu.Lock()
    defer s.mu.Unlock()
    if s.size == 0 {
        return 0, false
    }
    top := s.data[s.size-1]
    s.data[s.size-1] = 0        // 置 nil，断开引用
    s.data = s.data[:s.size-1]  // 缩视图
    s.size--
    return top, true
}

func (s *Stack) Peek() (int, bool) {
    s.mu.RLock()
    defer s.mu.RUnlock()
    if s.size == 0 {
        return 0, false
    }
    return s.data[s.size-1], true
}
```

## 总结与追问预判
核心：**切片栈 push=append、pop=弹末尾；截取 pop 不释放底层数组，要置 nil/重建切片防泄漏**。追问常拐向「和链表栈比优劣」——备好「数组栈随机访问快、增删慢；链表栈增删快、只顺序访问」（见 `173-stack-select.md`）。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文演示「用 `data = data[0:size-1]` 截取实现 pop」——指出该写法只是缩视图、底层数组最后一个元素不被回收，频繁 pop 会内存泄漏；本卡补入「置 nil + 缩视图」的修正写法。
2. 崩坏词归一：源码将切片 / 栈 / 入栈 / 出栈 / 栈顶 等音译为多组崩坏词，本卡统一为规范术语。

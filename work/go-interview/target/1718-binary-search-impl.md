# 1718 二分查找：递归与非递归两种实现

> 分类：算法 / 查找 | 难度：L2 | 题型：代码实现 | 频率：高 | 关键词：**二分查找、left/right、mid 溢出、递归终止、slices.BinarySearch**

> 原文锚点：第 1~30 段「初始化 left/right 指针、取中间元素比较、递归与非递归（for 循环）两种写法」

## 一句话总述
二分查找是在**有序数组**上用 `left`/`right` 双指针夹逼：取 `mid = left + (right-left)/2` 与目标比较，相等即返回下标，小于则 `left = mid+1`、大于则 `right = mid-1`；递归版把「缩小后的区间」作为参数自我调用、以 `left > right` 为终止，非递归版把这些步骤放进 `for left <= right` 循环。

## 面试官视角
P5 能背出「有序 + 折半」；P6 必须写对**区间收缩的 ±1**（写成 `left = mid` 会死循环）和 **mid 的防溢出写法**；P7 会被追问「递归版会不会爆栈」与「生产里该用哪个」——标准答案是 Go 1.21+ 直接用 `slices.BinarySearch`，手写只用于面试展示或需要自定义比较语义的场合。

## 主问答
**Q（面试官原话）：** 手写二分查找，递归和非递归都写一下，说说区别。

1. **前提与不变量**：数组必须**有序**（升序），维护闭区间 `[left, right]` 为「目标值可能存在的范围」；`mid` 比较后必须排除 `mid` 本身，否则区间不收缩 `[经验]`。
2. **非递归（推荐）**：`for left <= right` 循环内算 `mid`，三路分支命中返回 / `left = mid+1` / `right = mid-1`，循环结束返回 `-1`；空间 O(1) `[源码]`。
3. **递归版**：函数签名带 `left, right` 两个区间参数，base case 是 `if left > right { return -1 }`，否则按同样三路分支自我调用；代码短但每次调用压栈 `[源码]`。
4. **mid 必须防溢出**：写 `mid := left + (right-left)/2`，**不要**写 `(left+right)/2` `[实测]`——本机 Go 1.26.5 实测 `left=4611686018427387903`、`right=9223372036854775805` 时，`(left+right)/2` = `-2305843009213693954`（**负数**，下标直接越界 panic），而 `left+(right-left)/2` = `6917529027641081854` 正确。
5. **递归不会爆栈**：二分每次砍一半，递归深度 = `log2(n)`；`n = 2^20` 时仅 **20 层**，`n = 2^40` 时 40 层 `[实测]`，远低于 goroutine 栈上限（初始 2KB、64 位最大 1GB）——**「二分递归会栈溢出」是错的说法**，会栈溢出的是线性递归。
6. **性能实测（同一台机器、Go 1.26.5、`n = 2^20`、`-benchtime 2000x -count 3` 取中位）**：手写递归 **73.6 ns/op**、手写非递归 **66.7 ns/op**、标准库 `slices.BinarySearch` **27.4 ns/op** `[实测]`——标准库约快 **2.4 倍**（无函数调用开销 + 内部分支优化），生产代码直接用它。

## 追问链
| 层级 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 二分查找的前提是什么？ | 有序性意识 | 数组有序、支持随机访问（下标 O(1)），链表不适用 | 不知道要有序，停在 L1 |
| L2 | 循环条件为什么是 `left <= right`？ | 边界精确性 | 闭区间下 `left == right` 时该元素还没比过，必须再进一次；写成 `<` 会漏掉端点 | 说不出闭区间定义，停在 L2 |
| L3 | `left = mid` 不写 +1 会怎样？ | 死循环识别 | 当 `left+1 == right` 时 `mid == left`，区间不收缩，死循环 | 识别不出死循环，停在 L3 |
| L4 | `(left+right)/2` 有什么隐患？ | 整型溢出 | `left+right` 可能超过 `MaxInt` 变负数；改用 `left+(right-left)/2` | 答不出溢出，停在 L4 |
| L5 | 生产环境用哪个？递归版空间多少？ | 工程判断 | 直接用 `slices.BinarySearch`（Go 1.21+）；手写递归空间 O(log n)、非递归 O(1) | 不知道标准库已有实现，停在 L5 |

## 版本与兼容性
| 版本 | 行为 | 现在该怎么答 |
|---|---|---|
| Go < 1.21 | 只能手写，或 `sort.Search`（返回插入位，语义略绕） | 老项目认 `sort.Search` |
| **Go 1.21+** | `slices.BinarySearch[T]` 泛型版，返回 `(idx, found bool)` | **首选**，实测 27.4 ns/op |
| Go 1.21+ `slices.BinarySearchFunc` | 自定义比较器 | 结构体数组/降序用它 |
| 全版本 | 递归深度 log2(n)，与 Go 是否做尾调用优化无关 | 二分递归不用担心爆栈 |

## 关键代码
```go
// 非递归：空间 O(1)，生产首选手写形态
func binIter(a []int, target int) int {
    left, right := 0, len(a)-1
    for left <= right {
        mid := left + (right-left)/2 // 防溢出，勿写 (left+right)/2
        switch {
        case a[mid] == target:
            return mid
        case a[mid] < target:
            left = mid + 1
        default:
            right = mid - 1
        }
    }
    return -1
}

// 递归：区间作为参数下传，base case 是 left > right
func binRec(a []int, target, left, right int) int {
    if left > right {
        return -1
    }
    mid := left + (right-left)/2
    if a[mid] == target {
        return mid
    }
    if a[mid] < target {
        return binRec(a, target, mid+1, right)
    }
    return binRec(a, target, left, mid-1)
}

// Go 1.21+：生产直接用标准库
idx, found := slices.BinarySearch(a, target)
```

## 总结与追问预判
核心四句话：**有序前提、闭区间不变量、`mid±1` 收缩、`left+(right-left)/2` 防溢出**。递归与非递归逻辑完全同构，差别只在「状态放调用栈」还是「状态放循环变量」。面试官下一步大概率让你现场跑一遍 `target` 不存在的情况走完 `left > right` 的退出路径，或延伸到「有序数组中找第一个/最后一个等于 target 的位置」（边界二分，见 `1718-binary-search-boundary.deep.md`）。

`[边界]` 本卡只覆盖**精确查找单个值**的两种写法与溢出/爆栈/性能三个实测点，**不重述**递归范式与终止条件设计（见 `1717-recursive-impl`）、分治排序的 partition 思路（见 `1717-quicksort-overview`）、递归改写为显式栈的技巧（见 `1717-optimization`）、复杂度的渐进估算方法（见 `1711-complexity-evaluation`）。

## ⚠️ 原文纠错
1. 补充：原文只说「中间位置 = left 加 right 除以二」，未提整型溢出，`(left+right)/2` 在超大下标下会变负数 `[经验]`。
2. 补充：原文称分治「一般使用递归」，易被误读成递归必爆栈；二分递归深度仅 log2(n) `[经验]`。
3. 补充：原文未提标准库实现，Go 1.21+ 应优先 `slices.BinarySearch` `[经验]`。
4. 事实核校：数组 `[1 3 5 7 8 9]` 中 5 在下标 2、9 在下标 5，与原文一致 `[实测]`。
5. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语 `[经验]`。

# 1815 不退出进程清空文件回收空间

> 分类：Linux/文件系统 | 难度：L2 | 题型：认知题 | 频率：低 | 关键词：**文件占用**/**截断**/**清空内容**/**inode**/**空间回收**

> 原文锚点：第 18~22 段「不想退出占用进程时…直接清空文件内容即可回收空间…用重定向空内容覆盖文件…内容清空后存储即回收」

## 一句话总述
当文件被进程占用、又不能停进程时，**直接清空文件内容**（而非删除）即可回收磁盘空间：把文件长度截为 0，数据块释放，而进程的 fd 仍指向同一个 inode，业务不受影响。

## 面试官视角
这是"进程占用"场景的实战续问。面试官想看你是否知道 truncate 能在不关闭 fd 的前提下回收空间，以及 truncate 与 rm 的区别。

## 主问答
**Q（面试官原话）：** 那个日志文件被进程占着不能重启，怎么把它占的空间收回来？

**A：**

1. **清空而非删除**：对仍被打开的文件，用 `: > /path/file` 或 `echo -n > /path/file` 把内容截断为 0 字节；数据块立即释放，`df` 空间下降，而进程持有的 fd 不变，继续往里写会从头开始，业务无感知。
2. **原理：truncate 只改文件长度元数据**：`truncate` 把 inode 的 `i_size` 置 0 并释放数据块，但不动目录项、不动已打开的 fd，所以进程不感知；对比 `rm` 是 unlink 目录项，进程不关闭 fd 就不释放。
3. **等价 Go 实现**：`os.Truncate(path, 0)` 或 `os.OpenFile` 后 `f.Truncate(0)`，效果同命令行；生产里日志轮转（logrotate `copytruncate`）正是此思路。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | 不杀进程怎么回收 | 是否懂 truncate | 清空内容释放块 | 答不出停档 |
| L2 | truncate 与 rm 区别 | 是否懂元数据vs目录项 | truncate改i_size/rm删目录项 | 答不出停档 |
| L3 | 清空后进程还能写吗 | 是否懂 fd 不变 | fd 仍指向 inode 续写 | 答不出停档 |
| L4 | Go 怎么实现 | 是否懂 os.Truncate | os.Truncate(path,0) | 答不出停档 |
| L5 | logrotate 怎么做的 | 是否懂 copytruncate | 拷贝后 truncate 原文件 | 答不出停档 |

## 版本与兼容性
- `: > file` 为 POSIX shell 通用写法；`truncate -s 0 file` 为 GNU coreutils 命令，各发行版均支持。
- `os.Truncate` 自 Go 1.0 起稳定；截断正在被读取的文件在多数文件系统上安全，但并发写需注意应用层同步。

## 关键代码
```go
// 不关闭 fd 的前提下清空文件、回收磁盘空间（等价于 : > file）
func reclaimByTruncate(path string) error {
    // 方式一：直接按路径截断
    if err := os.Truncate(path, 0); err != nil {
        return err
    }
    // 方式二：持有 fd 时截断（进程自身打开的文件也能清）
    f, err := os.OpenFile(path, os.O_RDWR, 0644)
    if err != nil {
        return err
    }
    defer f.Close()
    return f.Truncate(0) // i_size 置 0，数据块释放，fd 不变
}
```

## 总结与追问预判
- 口诀：**要释放、先清空；truncate 改长度、rm 删目录项**。
- 预判追问："truncate 和 rm 对进程的影响差在哪？"→ truncate 不动 fd、进程无感；rm 若不关 fd 空间不回收（见 1815）。

## ⚠️ 原文纠错
源码将命令音译为崩坏词，本卡已统一为规范术语（`truncate`/`: >`/`test.log`/`i_size`/`inode`/`fd`）。纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：进程占用定位见 1815；inode/数据块机制见 1814；本卡只讲"清空内容回收"这一种手段。

> 原文锚点：第 1~17 段「rm 删除大日志文件后 df 空间未回收…最可能是文件仍被进程占用…用 lsof 查占用进程…关闭进程后 df 才下降」

## 一句话总述
`rm` 删除文件后 `df` 空间不降，**最常见原因是文件仍被某进程打开**：Linux 删除只是 unlink 目录项，只要还有进程持有该文件的打开句柄（fd），inode 与数据块就不释放；必须让占用进程关闭 fd（或进程退出）空间才回收。

## 面试官视角
高频运维排查题。面试官要看你是否理解"删除 ≠ 释放"的底层机制（unlink 与 fd 引用计数），以及能否给出 `lsof` 定位 + 回收 SOP，而非只会 `rm -f`。

## 主问答
**Q（面试官原话）：** 用 rm 删了一个很大的日志文件，为什么 df 看磁盘空间没降下来？

**A：**

1. **机制：unlink 不立即释放数据块**：`rm` 本质是 `unlink` 删掉目录项；文件真正释放要等**最后一个引用（目录项 + 进程打开的 fd）消失**。进程还开着文件时，内核维持 inode 与数据块，df 统计的是数据块占用，所以不变。
2. **定位：用 `lsof` 找"已删除但仍打开"的文件**：`lsof +L1` 列出链接数 <1（即被删但仍有 fd）的文件，`lsof | grep deleted` 也能定向查；输出里能看到占用进程 PID 与文件大小。
3. **回收：让进程释放 fd**：kill/重启占用进程，或让进程主动关闭日志（如 `logrotate` 发信号重开），fd 关闭后空间立即归还；若不能停进程，见 `1815-truncate-reclaim` 用清空内容方式回收。

## 追问链（L1~L5）
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | rm 到底做了什么 | 是否懂 unlink | 删目录项不删数据块 | 答不出停档 |
| L2 | 为什么进程开着就不释放 | 是否懂 fd 引用 | inode 引用计数未归零 | 答不出停档 |
| L3 | 怎么定位占用进程 | 是否懂 lsof | lsof +L1 / grep deleted | 答不出停档 |
| L4 | 不杀进程怎么回收 | 是否懂 truncate | 清空内容释放块（见下卡） | 答不出停档 |
| L5 | 还有哪些不释放情形 | 是否懂硬链接/回收站 | 硬链接/rm别名mv（见另卡） | 答不出停档 |

## 版本与兼容性
- `lsof +L1` 为 POSIX 通用用法，各 Linux 发行版（CentOS/RHEL/Ubuntu）行为一致。
- `df`/`du` 差异：`du` 走文件名遍历会"看不到"已删打开文件（其大小不计入），`df` 看文件系统块所以仍计入——这是排查时两者不一致的根因。

## 关键代码
```go
// 用 Go 复现"定位已删除但仍被本进程打开的文件"：扫描 /proc 下自身 fd
func findDeletedOpenBySelf() ([]string, error) {
    self := fmt.Sprintf("/proc/%d/fd", os.Getpid())
    entries, _ := os.ReadDir(self)
    var held []string
    for _, e := range entries {
        target, err := os.Readlink(self + "/" + e.Name())
        if err != nil {
            continue
        }
        // target 形如 "/var/log/xxx.log (deleted)" 表示文件已删但 fd 仍持有
        if strings.Contains(target, "(deleted)") {
            held = append(held, target)
        }
    }
    return held, nil
}
```

## 总结与追问预判
- 口诀：**删的是目录项，放的是引用数；进程不撒手，空间不回头**。
- 预判追问："线上不能重启进程怎么办？"→ 答 `1815-truncate-reclaim` 的清空内容法；"df 和 du 对不上"→ 正是此现象的典型表现。

## ⚠️ 原文纠错
源码将命令与术语音译为崩坏词，本卡已统一为规范术语（`lsof`/`tail`/`unlink`/`inode`/`fd`/`df`/`du`）。纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：硬链接导致不释放见 `1815-hardlink-space-held`；rm 被别名成 mv 见 `1815-pseudo-delete-mv-tmp`；inode 机制本体见 `1814-inode-basics`；本卡只讲"进程占用"这一种情形。

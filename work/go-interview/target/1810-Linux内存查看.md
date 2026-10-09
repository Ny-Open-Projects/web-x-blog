# 1810 Linux 内存查看：free 与 top 指标解读

> 分类：Linux/内存排查 | 难度：L2 | 题型：工具题 | 频率：中 | 关键词：**free -h** / **buffer vs cache** / **VIRT/RES/SHR** / **available**
> 原文锚点：第 1~31 段「free -h 六列(total/used/free/shared/buffers/cache/available)；buffer缓存磁盘块、cache缓存文件页；top 进程 VIRT/RES/SHR/%MEM；available含可回收缓存比free大」

## 一句话总述
系统级内存排查先看 `free -h`（系统整体）与 `top`（进程级）：`free` 的 `available` 才是新进程可用内存（含可回收缓存，通常比 `free` 大）；`top` 里 **VIRT** 是虚拟内存、**RES** 是常驻物理内存（不含 swap/SHR）、**SHR** 是共享内存（含共享库，不能直接相加）。`buffer` 缓存磁盘块、`cache` 缓存文件页。

## 面试官视角
- 意图：考察对"内存指标到底代表什么"的精确理解，常用来区分只背过命令的人和真排过问题的人。
- P5 知道 free/top 看内存；P6 能区分 VIRT/RES/SHR 与 buffer/cache；P7 能讲清 available 为何比 free 大、为何 SHR 不能直接相加。
- 红旗：以为 free 低就是内存不足（可能是 cache 占着）；以为 VIRT 就是真实占用；把多进程 SHR 直接相加。
- 惊艳点：点出 free 数据来自 /proc/meminfo，available 含可回收缓存因而比 free 大；buffer 缓存磁盘、cache 缓存文件。

## 主问答
**Q（面试官原话）：** 怎么看系统内存够不够？free 和 top 各看什么？
**A：**
1. **结论**：`free -h` 看系统整体——`available` 是新进程可用内存（含可回收缓存，通常 > `free`），`free` 是真正未使用；`top` 看进程级——**VIRT**=虚拟内存（申请过就算，含未分配物理）、**RES**=常驻物理内存（实际占用，不含 swap 与 SHR）、**SHR**=共享内存（共享库/代码，多进程不能直接相加）。
2. **机制**：`buffer` 是内核缓冲区（缓存磁盘块，约几十 MB，合并零散写）；`cache` 是页缓存+slab（缓存文件读页，下次免磁盘）。二者都可回收，所以 `available = free + 可回收缓存`，一般比 `free` 大 `[经验]`。
3. **边界**：仅 `free` 低不一定是问题（可能 cache 占着，可回收）；真内存不足要看 `available` 持续走低 + swap 被用。排进程用 `top` 按 RES 排序定位大户。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | free 看什么 | 基础 | available/free/buffer/cache | 判 P5 |
| L2 | VIRT/RES/SHR | 指标 | 虚/常驻/共享 | 判 P6 |
| L3 | buffer/cache | 区别 | 磁盘块/文件页 | 判 P6 |
| L4 | available 为何大 | 机制 | 含可回收缓存 | 判 P6+ |
| L5 | SHR 能相加吗 | 陷阱 | 不能，含共享库 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Linux 2.6+ 通用 | 无 | free/top/vmstat 指标语义跨发行版一致；available 列自 Linux 3.14 起在 /proc/meminfo 提供，老系统可能缺失 `[经验]` |

## 关键代码
```go
// Go 读取 /proc/meminfo —— free 命令的数据源
func readMemInfo() {
    b, _ := os.ReadFile("/proc/meminfo")
    want := []string{"MemTotal:", "MemFree:", "MemAvailable:", "Buffers:", "Cached:"}
    for _, line := range strings.Split(string(b), "\n") {
        for _, k := range want {
            if strings.HasPrefix(line, k) {
                fmt.Println(line) // 如 MemAvailable: 1234567 kB
            }
        }
    }
}
```

## 总结与追问预判
- free 看 available（非 free）；top 看 RES；buffer 磁盘块 / cache 文件页；SHR 不可相加。
- 预判：趋势与问题分类 → 见 1810；排查决策树 → 见 1810；Go 应用层 pprof 见 812/1114。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"free -h 六列含义、available 含可回收缓存比 free 大、buffer 缓存磁盘块/cache 缓存文件页、top 的 VIRT/RES/SHR/%MEM 定义、SHR 不能直接相加"的描述，与 Linux 内存模型一致。仅做了 ASR 解码将多组术语崩坏词（free杠h→free -h、幽heman→human、福瑞→free、shred→shared、avavailable→available、cathe/catch→cache、PROCmemoryinfo→/proc/meminfo、sreclambb/SNclaim→SReclaimable/SUnreclaim、拓扑命令→top 命令 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。

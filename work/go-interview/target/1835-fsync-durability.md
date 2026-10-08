# 1835 fsync / fdatasync：强制数据落盘

> 分类：内存与 OS / 文件系统 | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**fsync** / **fdatasync** / **强制写回** / **耐久性** / **性能代价**
> 原文锚点：第 12~23 段「FFINNC/FFdataSYNC强制将page cache写回磁盘…阻塞直到成功…极大降低IO性能」

## 一句话总述
`fsync`/`fdatasync` 强制把 page cache 中该文件的数据写回磁盘并**等待完成**，从而保证持久化；代价是每次调用都触发一次真实磁盘 IO，吞吐显著下降——耐久性与性能必须权衡，常用于 WAL、事务提交等"必须落盘"的关键路径。

## 面试官视角
- 意图：是否懂"延迟写回"的取舍，以及 fsync 是耐久性的最后一道闸门。
- P5 知 fsync 强制落盘；P6 说清它阻塞到完成、代价是磁盘 IO；P7 知 fdatasync 只同步数据不强制元数据、以及何时该用。
- 红旗：以为频繁 fsync 无代价；在不需要耐久的路径上也强制 fsync。
- 惊艳点：`fdatasync` 比 `fsync` 轻——它只把数据写回，不强制更新文件元数据（大小/时间），少一次元数据 IO；多数"只追加"场景够用 `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么保证写入的数据真正落盘？fsync 有什么代价？
**A：**
1. **fsync 强制**：调用后阻塞，直到该文件 page cache 数据写回磁盘并返回成功 `[源码]`。
2. **fdatasync 更轻**：只同步数据块，不强制刷新文件元数据（大小/修改时间），少一次元数据写，适合只追加写入。
3. **性能代价**：每次 fsync 是一次真实磁盘 IO，吞吐骤降——不能无脑每写都调。
4. **权衡**：仅关键路径（WAL 写、事务提交、账本）调 fsync；普通写依赖 page cache 延迟写回即可 `[边界]` 见 144-seqwrite-pagecache。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 怎么落盘 | 概念 | fsync | 换题 |
| L2 | 代价 | 权衡 | 磁盘IO↓ | 判 P5 |
| L3 | fdatasync | 差异 | 不同步元数据 | 判 P6 |
| L4 | 何时用 | 设计 | 关键路径 | 判 P6+ |
| L5 | 与崩溃 | 实战 | 消除丢失窗口 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| POSIX 长期稳定 | 现代 NVMe 下 fsync 仍比纯 cache 慢一个量级 | 耐久优先路径仍须 fsync，成本靠批量化摊薄 |

## 关键代码
```go
// 示意，未验证：关键数据写入后 fsync，保证崩溃也不丢
package main
import ("os"; "fmt")
func main() {
    f, _ := os.CreateTemp("", "durable")
    defer f.Close()
    f.Write([]byte("must-survive-crash"))
    if err := f.Sync(); err != nil { // 阻塞到数据真正写回磁盘
        fmt.Println("fsync 失败:", err)
    }
    // 此后即使系统崩溃，该数据已在磁盘上
}
```

## 总结与追问预判
- fsync 强制落盘、fdatasync 轻量、代价是磁盘 IO；仅关键路径使用。
- 预判：写路径 → 见 1835-write-path-pagecache；崩溃一致性 → 见 1835-crash-consistency；page cache 行为 → 见 144-seqwrite-pagecache。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语 `[经验]`。事实核校：fsync/fdatasync 强制写回并等待、代价是磁盘 IO 性能下降、fdatasync 不同步元数据更轻——均正确，未做更正。

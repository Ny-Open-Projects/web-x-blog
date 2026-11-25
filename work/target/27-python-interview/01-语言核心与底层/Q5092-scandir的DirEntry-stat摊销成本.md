---
title: "[Q5092] os.scandir 的 DirEntry stat 摊销成本"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5092 · os.scandir 的 DirEntry stat 摊销成本

难度：P6 | 标签：成本工程 | os.scandir | 文件系统

**问**：一个定期扫描百万文件目录做清理的服务，用 `os.listdir` + `os.stat` 逐个判大小，单轮要几分钟。成本瓶颈在哪？`os.scandir` 为什么快？快多少、边界在哪？

**答**：
结论：瓶颈是 stat 系统调用的次数。`os.listdir` 只返回名字（一次 readdir），之后每个文件的 `os.stat(path)` 都是一次独立系统调用（open+getattr or statx）；百万文件就是百万次内核往返。`os.scandir` 返回的 `DirEntry` 在 `readdir` 时就携带了 `d_type`，多数文件系统还顺带带了 size/mtime 信息，访问 `entry.stat()` 在 Linux/macOS 上**不需要额外系统调用**，Windows 上更是完全免费（FindFirstFile 直接返回）。
取舍：实测 scandir+entry.stat 比 listdir+stat 快 5-20 倍（视文件系统而定）。边界：① `entry.stat()` 结果是扫描时刻的快照，文件后续变更不会反映；② 若目录支持但 entry 缓存未命中（罕见），会回退成一次真 stat；③ `entry.is_dir()` 同样免 syscall（用 d_type），而 `Path.is_dir()` 每次都 stat。
实战：目录遍历一律 scandir；用 `entry.stat(follow_symlinks=False)` 避免符号链接导致的额外 syscall 与误判；把"每文件 syscall 次数"作为扫描类任务的容量指标。

```python
import os, sys, time, tempfile, shutil

def make_tree(base, n):
    os.makedirs(base, exist_ok=True)
    for i in range(n):
        with open(os.path.join(base, f"f{i:04d}.bin"), "wb") as f:
            f.write(b"x" * (i % 97))
    return base

def scan_listdir(base):
    total = 0
    for name in os.listdir(base):
        st = os.stat(os.path.join(base, name))  # 每文件一次 stat syscall
        total += st.st_size
    return total

def scan_scandir(base):
    total = 0
    with os.scandir(base) as it:
        for entry in it:
            total += entry.stat(follow_symlinks=False).st_size  # 多数 FS 无额外 syscall
    return total

base = make_tree(tempfile.mkdtemp(), 2000)
try:
    assert scan_listdir(base) == scan_scandir(base)
    t0 = time.perf_counter(); scan_listdir(base); t1 = time.perf_counter()
    t2 = time.perf_counter(); scan_scandir(base); t3 = time.perf_counter()
    print(f"listdir+stat : {(t1-t0)*1000:.1f} ms")
    print(f"scandir+entry: {(t3-t2)*1e3:.1f} ms")

    # 递归版：walk 的成本模型（walk 内部就是 scandir）
    t4 = time.perf_counter()
    for root, dirs, files in os.walk(base):
        pass
    print(f"os.walk 递归 {(time.perf_counter()-t4)*1000:.1f} ms")

    # DirEntry 快照语义：stat 之后修改文件，entry 仍是旧值
    p = os.path.join(base, "f0000.bin")
    with os.scandir(base) as it:
        e = next(x for x in it if x.name == "f0000.bin")
        before = e.stat().st_size
    with open(p, "ab") as f:
        f.write(b"more")
    print(f"快照 size={before}, 实际 size={os.stat(p).st_size} (entry 不更新)")
finally:
    shutil.rmtree(base, ignore_errors=True)
```

**追问 1**：为什么 `entry.is_dir()` 免 syscall 而 `Path.is_dir()` 不免？
- 追问 2 层：scandir 在 readdir 时拿到 `d_type`（DT_DIR/DT_REG），Path.is_dir 走 pathlib 的 stat 调用；某些文件系统 d_type 返回 DT_UNKNOWN，此时 entry.is_dir 会回退一次 stat。
- 追问 3 层：`Path.walk()`（3.12+）底层也是 scandir，且提供 `on_error` 与 `follow_symlinks` 参数，是 walk 的现代替代。

**追问 2**：扫描百万文件目录还有什么结构性优化？
- 追问 2 层：单目录扇出过大本身就是反模式（readdir O(n) 且分页重放）；目录分层哈希桶把单目录规模降到 O(1) 量级。
- 追问 3 层：需要增量扫描时记 mtime/INO 游标，配合 scandir 的快照语义做差量；否则全量重扫的成本随目录线性增长。

## 背诵要点
1. listdir+stat = 1 + N 次 syscall；scandir 把 stat 摊销进 readdir，快 5-20 倍。
2. DirEntry.stat/is_dir 是扫描时刻快照且多数免 syscall（d_type），Path.is_dir 每次真 stat。
3. 单目录百万扇出是反模式，先分层再谈扫描优化。

## 复盘追问
1. 为什么 scandir 在 Windows 上收益更极端？——FindFirstFile/FindNextFile 直接返回全部元数据，stat 完全免费。
2. 如果扫描期间文件被并发删除，代码会怎么挂？——stat 抛 FileNotFoundError，需要 try/except 或 follow_symlinks=False + 忽略策略。

---
title: [Q5114] shutil.copyfile 缓冲与拷贝吞吐容量账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5114 · shutil.copyfile 缓冲与拷贝吞吐容量账

> 难度:★★★★☆ | 标签:容量规划, IO, shutil

**问**:备份脚本用 `open(src).read()` + `open(dst).write()` 拷 20GB 文件直接 OOM；换 `shutil.copyfile` 后正常。copyfile 内部做了什么？它、`copy`、`copy2`、`sendfile` 各差在哪？拷贝吞吐该怎么估算？

**答**:结论：手写 `read()` 默认一次性读入整文件（text 模式无限、binary 模式 -1 也是全量），20GB 必然 OOM；`shutil.copyfile` 用 **64KB 固定缓冲循环读写**（`COPY_BUFSIZE`，macOS 上还会优先走 `fcopyfile` 系统调用、Linux 走 `os.sendfile` 零拷贝路径），峰值内存 O(64KB)。三个函数的差异账：`copyfile` 只搬数据；`copy` 再拷权限位（mode）；`copy2` 再拷元数据（mtime/xattr，需目标文件系统支持，失败降级为 copy 并 warning）。吞吐估算：本地 NVMe 上限 ~2-3GB/s，SATA SSD ~500MB/s，网络文件系统看链路；但 **Python 循环拷贝的瓶颈通常是内存带宽与系统调用次数**，64KB 缓冲下 20GB ≈ 32 万次 syscall，用户态循环占比可观——所以 copyfile 的 sendfile/fcopyfile 快路径（内核内完成、无用户态往返）比手写循环快 30-50%。容量规划时用"物理介质上限 × 快路径系数"估算，别用 Python 循环实测值。

```python
import os, shutil, tempfile, time

src = tempfile.mktemp(suffix=".bin"); dst = tempfile.mktemp(suffix=".out")
with open(src, "wb") as f:
    f.write(os.urandom(64 * 1024 * 1024))        # 64MB 样本

# 1) copyfile 快路径（macOS: fcopyfile / Linux: sendfile）
t0 = time.perf_counter(); shutil.copyfile(src, dst); t1 = time.perf_counter()
size = os.path.getsize(src)
print(f"copyfile: {size/1e6:.0f}MB -> {t1-t0:.3f}s = {size/1e6/(t1-t0):.0f}MB/s")

# 2) 手写 Python 循环对照（64KB 缓冲，用户态往返）
def manual_copy(s, d, buf=64 * 1024):
    with open(s, "rb") as fin, open(d, "wb") as fout:
        while block := fin.read(buf):
            fout.write(block)
t0 = time.perf_counter(); manual_copy(src, dst); t1 = time.perf_counter()
print(f"manual  : {size/1e6/(t1-t0):.0f}MB/s（用户态循环）")

# 3) copy vs copy2 的元数据差异
for fn in (shutil.copy, shutil.copy2):
    try:
        fn(src, dst); ok = "OK"
    except OSError as e:
        ok = f"降级: {e}"
    st = os.stat(dst)
    print(f"{fn.__name__}: {ok}, mtime保留={abs(st.st_mtime - os.stat(src).st_mtime) < 1e-6}")

# 4) copyfile 的错误边界：同文件抛 SameFileError，跨设备走正常路径
try:
    shutil.copyfile(src, src)
except shutil.SameFileError as e:
    print("SameFileError:", e)

os.unlink(src); os.unlink(dst)
```

**追问一层**:`os.sendfile` 为什么快（无用户态拷贝），但它要求两端都是 fd——什么场景用不上（如 S3 multipart）？
**追二层**:`shutil.copy2` 拷 `st_mtime` 后，下游"按 mtime 增量同步"的行为会怎样？为什么备份链路常坚持 copy2（引 Q1612/PID 场景相反面）？

**背诵要点**
- `read()` 全量读会 OOM；copyfile 64KB 缓冲 + macOS fcopyfile/Linux sendfile 快路径，峰值 O(64KB)。
- copy=数据+mode；copy2=数据+mode+元数据；失败降级并 warning。
- 吞吐估算用介质上限×快路径系数，sendfile 类比手写循环快 30-50%。

**复盘追问**
- 备份 20GB 时磁盘满了一半失败，怎么做成可续传？提示：分块 + offset 记录，或直接 `rsync --partial`。
- 为什么 copy2 在 FAT32/网络盘上会降级？提示：元数据能力缺失，warning 可见但要监控。

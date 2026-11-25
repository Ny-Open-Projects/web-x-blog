---
title: "[Q5091] mmap 文件映射的容量与随机访问成本账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5091 · mmap 文件映射的容量与随机访问成本账

难度：P6 | 标签：容量规划 | mmap | 零拷贝

**问**：一个索引服务需要随机读取 2GB 数据文件的任意偏移。同事把文件整个 `read()` 进 bytes（RSS+2GB），另一版用 `mmap` 只加了虚拟内存却很稳。mmap 的内存账到底怎么算？什么场景该用、什么场景是负收益？

**答**：
结论：`f.read()` 把 2GB 物理内存一次性占进 Python 进程堆（RSS 立刻 2GB，且再复制一份 bytes 峰值更高）；`mmap` 只占一段**虚拟地址空间**，物理内存按页（4KB）在真正访问时由缺页中断从 page cache 拉入——RSS 只反映"摸过的页"，且这些页本就在内核 page cache 里，不产生额外拷贝。容量账因此从"文件大小"变成"工作集大小"：随机读 10% 热点页，RSS 只有 ~200MB。
取舍：mmap 的收益在随机访问与共享（多进程映射同一文件共享物理页、fork 后零拷贝），代价是：① 缺页抖动不可控（磁盘慢时延迟尖刺比预读更疼）；② `bytes(mv)` 切片仍会复制数据，热循环里要避免；③ Windows 上写入映射涉及 flush 语义；④ 文件被并发截断后访问映射段直接 SIGBUS 崩进程——这是 mmap 最危险的事故面。
实战：随机索引读用 `mmap.PROT_READ` + `mv[start:end]` 按需切片，热页常驻由内核 page cache 管理；顺序全量解析大文件用流式 read（mmap 无收益）；写入端 resize 后必须先 `mmap.close()` 再 reopen。

```python
import mmap, os, tempfile, time

path = tempfile.mktemp(suffix=".bin")
size = 64 << 20  # 64MB 数据文件
with open(path, "wb") as f:
    for i in range(size // 4096):
        f.write(i.to_bytes(4, "little") + b"\0" * 4092)

# 方式1：全量读入 —— RSS 增加 64MB，且 bytes 复制一份
t0 = time.perf_counter()
with open(path, "rb") as f:
    blob = f.read()
t_read = time.perf_counter() - t0
print(f"全量 read: {t_read*1000:.1f} ms, 堆内常驻 {len(blob)/1e6:.0f} MB")
del blob

# 方式2：mmap —— 虚拟映射，按页缺入
t0 = time.perf_counter()
with open(path, "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # 随机摸 1% 页：RSS 增长只有工作集大小
    import random
    pages = random.sample(range(size // 4096), size // 4096 // 100)
    touched = sum(4 for p in pages if int.from_bytes(mm[p*4096:p*4096+4], "little") >= 0)
    t_map = time.perf_counter() - t0
print(f"mmap 随机访问 1% 页: {t_map*1000:.1f} ms, 触达 {touched} 次切片")

# mmap 的查找/切片语义像 bytes，但不复制整段
idx = mm.find(b"\1\0\0\0\0")
print("find 首个模式偏移:", idx)

# 事故面：resize 后旧映射可能 SIGBUS（演示只做安全部分）
with open(path, "r+b") as f:
    mm2 = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    f.truncate(10)              # 另一"进程"截断文件
    # 千万不要再访问越界页：越界页缺页时内核发现页不在文件内 → SIGBUS 直接杀进程
    # （SIGBUS 无法用 try/except 捕获，只能进程级防护）
    mm2.close()                 # resize 前必须关闭旧映射
with open(path, "r+b") as f:    # 重新按新长度建立映射
    mm3 = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print("resize 后重新映射长度:", len(mm3))
    mm3.close()
    f.truncate(size)            # 恢复文件，供后续演示

mm.close()
os.unlink(path)
```

**追问 1**：为什么说 mmap 读取"不产生额外拷贝"？
- 追问 2 层：read() 路径是 磁盘→page cache→用户缓冲区 两次拷贝；mmap 让用户虚拟地址直接映射 page cache 页，访问即数据。
- 追问 3 层：但 `mm[i:j]` 返回新 bytes 仍要复制该切片；避免热循环切片复制要用 `mv = memoryview(mm)` 再取子视图传给 struct/socket。

**追问 2**：多进程共享索引数据为什么首选 mmap？
- 追问 2 层：fork 前建立的映射随地址空间继承（MACOS 上 spawn 不继承，需各自 open 映射同一文件），物理页只有一份，是进程间零拷贝共享。
- 追问 3 层：需要进程间同步更新时用 `ACCESS_WRITE` + `msync()` 落盘，或退到 `multiprocessing.shared_memory`（本质也是 shm + mmap）。

## 背诵要点
1. read 全量=RSS 即文件大小；mmap RSS=工作集页数×4KB，容量账从文件大小变成访问模式。
2. mmap 零拷贝指的是内核页直达，切片仍复制；热路径用 memoryview。
3. 并发截断→SIGBUS 是 mmap 最大事故面，resize 必须关闭映射重开。

## 复盘追问
1. 索引文件启动预热要不要顺序摸一遍？——要：顺序缺页触发 readahead，把首查延迟摊到启动期。
2. 什么情况 mmap 反而更慢？——顺序扫描一次即弃（read 走预读更顺）或磁盘排队严重时缺页抖动放大 P99。

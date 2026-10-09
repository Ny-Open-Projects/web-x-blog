# 1827 mmap 适用边界与页错误语义深挖

> 覆盖源 18-27 的机制延伸：mmap 的页错误生命周期、malloc 的 arena/阈值策略（128KB 分界）、mmap 在数据库与 GC 里的实战用法、随机访问 mmap 的性能反例。主卡已给五局限，本附录做边界深挖。

## 思路与架构

```text
mmap 的页错误生命周期 (映射≠分配)
├─ mmap() 成功: 只登记 VMA (虚拟地址区间), 无物理页
├─ 首次访问某页: 缺页中断
│   ├─ 文件映射页: 从文件读入页缓存 -> 建立映射
│   └─ 匿名映射页: 分配物理页/零页 (写时复制)
├─ 写文件映射页: 脏页, 由内核回写线程刷盘 (不即时!)
│   └─ 崩溃语义: 未刷盘数据丢失 (见 1835-file-write-crash)
└─ malloc 的策略分界 (glibc ptmalloc)
    ├─ < 128KB: brk arena 内切块 (内存池, 零 syscall)
    ├─ >= 128KB: 直接 mmap (大块独立映射, free 即还)
    └─ 阈值可调 (M_MMAP_THRESHOLD), 有动态自适应
```

## 方案取舍
- **128KB 分界是 malloc 对 mmap 的精准运用**：ptmalloc 不是拒绝 mmap，而是**只在合适的地方用**——小块用 arena 池化（摊薄 syscall），大块直接 mmap（free 时立即归还内核，避免大块长期占住堆导致 arena 膨胀）。**「池化小块 + mmap 大块」**就是「不全用 mmap」的正面教材——两种技术按体量分工而非互相取代 [经验]。
- **mmap 随机访问的性能反例**：顺序扫大文件时 mmap 省拷贝很赚；但**随机访问稀疏分布**时，每个未命中页都触发一次缺页中断（+一次文件 IO），缺页风暴比 read 批量预读更慢。数据库内核（如 MySQL/PG 对数据文件的取舍）在 mmap vs 自管缓冲池上反复权衡后多选**自管缓冲池**——因为需要精细控制刷盘/预读/淘汰，mmap 的内核托管粒度太粗 [经验]。
- **mmap 共享内存的进程间语义**：MAP_SHARED 映射同一文件的多进程看到同一物理页——写立即可见（同一页），这是它做共享内存的根基；但要配合**同步原语**（文件锁/futex on mmap 区），映射本身不提供互斥。Go 的 sync.Pool 跨进程无关，进程间共享在 Go 里更常用 mmap+或 Unix socket 传递 fd 的方案 [经验]。
- **Go 运行时的活教材**：mcache（P 本地无锁小对象）→ mcentral（按 size class 全局回收）→ mheap（页级管理，向 OS mmap 申请_span）——**三级结构就是「池化摊薄 syscall + 大块 mmap」的完整落地**；答「不全用 mmap」收尾甩出这个例子，操作系统题立刻接到 Go 工程题 [经验]。

## 答题技巧
- 答局限时按「开销→碎片→复杂→资源→兼容」五点报全，每个点配一句具体机制（syscall/缺页/VMA 上限）——不空喊 [经验]。
- 被问「malloc 内部怎么做」→ 128KB 阈值 + arena 池化 + 大块 mmap——用 malloc 证明「不是不用 mmap 而是用在对的地方」[经验]。
- 被问「mmap 写文件会立刻落盘吗」→ 不会，脏页由内核回写，崩溃窗口语义见文件写崩溃专题——主动勾连版本边界 [经验]。
- 主动报 Go 例子：mcache/mcentral/mheap 三级 = mmap 取长补短的正解落地 [经验]。
- 主动边界到 `1827-mmap-limitations`（五局限主线）、`1835-file-write-crash`/`1835-file-write-crash.deep`（落盘语义）、`1836-zero-copy-evolution.deep`（mmap 变体在零拷贝谱系）、`915-map-growth-internals.deep`（Go 堆增长侧写），构成「内存管理」专题 [边界]。

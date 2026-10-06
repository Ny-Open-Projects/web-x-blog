# 812 Go 内存管理与泄漏排查深挖

## 思路与架构
Go 内存分配借鉴 tcmalloc 思想，核心是**三级缓存 + mspan 管理**，理解它才能讲清"泄漏"到底漏在哪一层。
- **三级结构**：`mcache`（每 P 一个本地缓存，无锁）→ `mcentral`（全局，按 sizeclass 管理 span 链表，被所有 P 共享）→ `mheap`（管理所有 mcentral 与堆区，大对象直接在此分配）。
- **mspan 与 sizeclass**：堆区按 8KB 页切分，多个页组成 **mspan**；按对象大小分 **67 种 sizeclass**（Go 1.5+）。微小对象（<16B）走 mcache 的 tiny 分配器；小对象（16B~32KB）按 sizeclass 选 mspan；大对象（>32KB）绕过 mcache/mcentral 直接从 mheap 拿。
- **堆区布局**：arena（实际堆内存）→ bitmap（标记对象是否含指针、GC 信息）→ spans（存 mspan 页指针与元信息）。虚拟地址从高（bitmap）到低（arena）增长。
- **泄漏的本质**：GC 只回收"不可达"对象。凡让对象**持续可达**的情形都漏——协程卡死、资源句柄敞着、C 堆逃出 GC 视野，都属此列。

## 方案取舍
- **三级缓存 vs 全局锁**：mcache 放本地消除大部分锁竞争，但代价是每个 P 都缓存各 sizeclass 的 mspan（有一定内存冗余）——用"少量空闲缓存"换"无锁快分配"，值。
- **tiny 分配器**：<16B 对象合并进同一块再切，省碎片；代价是 tiny 块内对象"一起活一起死"，可能拖慢小对象回收。
- **泄漏排查路径取舍**：先 `NumGoroutine()` 看协程是否涨（最便宜）→ 再 pprof heap 看 inuse_space 增量 → 协程/内存同涨基本锁定"协程泄漏"；若内存涨而协程不涨，查资源句柄/C 堆（C 堆 pprof 看不见，需 C 侧工具）。

## 答题技巧
1. **先讲分配器再讲泄漏**：开场用"三级结构 + 67 sizeclass + 三类对象"建立专业感，再落到"GC 只收不可达对象"这一统一逻辑。
2. **泄漏归类成四型**：① 协程未退出 ② 资源未关（for 内 defer）③ 锁/channel 阻塞 ④ cgo 未 free——四型各自对应一种"持续可达"机制，回答有结构。
3. **反直觉点**：① `defer` 是函数级不是块级，for 内 defer 会堆积；② **向 nil channel 收发永久阻塞**；③ cgo 的 C 堆泄漏在 Go pprof 不可见；④ 切片 append 扩容后底层数组换新地址，函数内修改不反映外层（见 9-23）。
4. **工具钩子**：定位必提"pprof 快照对比增量"与 `runtime.NumGoroutine()`，不要只说"看 pprof"。
5. **版本锚点**：sizeclass 67 种自 Go 1.5 起；大对象阈值 32KB 属经典划分，答时可说"约 32KB 以上走 mheap"。

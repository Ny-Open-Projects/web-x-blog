---
disableNunjucks: true
title: "915 map 扩容深挖：经典 hmap 与 Swiss Table 两代实现的对照"
date: 2026-10-10 09:02:18
categories: [Go面试题集]
tags: [Go面试题集]
---

> 深挖卡：把「扩容」从面试结论推进到源码级，覆盖两代实现的迁移算法、代价模型与线上排查手法。

## 思路与架构

**第一代（Go ≤ 1.23，hmap + bmap）**

```text
hmap{ count, B, buckets, oldbuckets, nevacuate, overflow, extra }
     桶数 = 2^B，每桶 8 对 + tophash[8]，桶满挂溢出桶链表

触发 → hashGrow(t, m, overLoadFactor ? 2^B<<1 : sameSize)
       sameSize=true 时桶数不变，只做整理（等量重建）
迁移 → growWork：每次写先 evacuate(nevacuate 桶) 再 evacuate(当前桶)
       evacuate 把旧桶 x 的元素按 hash 第 B 位分流到 x 与 x+2^B 两个新桶
       桶的溢出链一并搬走；nevacuate 递增，全搬完清 oldbuckets
```

关键点：**哈希值不需要重算**。桶数是 2 的幂，扩容后新桶下标只比旧桶多一位（第 B 位），判断这一位是 0 还是 1 就能决定元素落在低半区还是高半区，这正是「桶数恒为 2 的幂」的真正收益。

**第二代（Go 1.24+，Swiss Table）**

```text
Map{ used, seed, dirPtr, dirLen, globalDepth, globalShift, writing,
     tombstonePossible, clearSeq }
  ├─ 小 map（≤8 元素）：dirPtr 直接指向单个 group，dirLen=0，不建 table
  └─ 大 map：dirPtr 指向 table 指针数组（可扩展哈希），
             table{ used, capacity(2^N), growthLeft, localDepth, index, groups }

写路径 → growthLeft == 0 时：
         ① 先 pruneTombstones（墓碑 >10% 容量才做，原地整理 → 等价等量重建）
         ② 仍不够 → table.grow 翻倍 capacity 后 rehash
         ③ 表超大 → 目录分裂（extendible hashing），一次只拆一个 table，天然增量
删路径 → delete 置墓碑(tombstone)，used--，capacity 不变
```

架构差异带来的三个认知更新：

1. **增量粒度从「搬桶」变成「分裂表」**：经典实现用 `oldbuckets` + `nevacuate` 记账；Swiss 用可扩展哈希，目录里多个表可各自独立分裂，一个超大 map 的增长被切成许多个小步骤。
2. **触发判据从「元素数 vs 阈值」变成「剩余配额 growthLeft 归零」**：`maxGrowthLeft = capacity*7/8`（单 group 时为 `capacity-1`），每次写入递减，墓碑与已用槽位一起消耗配额——**所以"元素不多但增删频繁"同样会触发重建**，这正是原文提到的第二种情况。
3. **删除语义从「置 tophash 为 empty」变成「写墓碑控制字节」**：两者都不归还内存，但 Swiss 的墓碑会**占用探测序列**，数量多了会拖慢查询，因此需要 `pruneTombstones` 单独回收。

## 方案取舍

| 场景 | 做法 | 代价 | 建议 |
|---|---|---|---|
| 已知最终规模 | `make(map[K]V, n)` 预分配 | 一次性多占内存 | **强烈推荐**，省掉全部搬迁 |
| 规模未知且增长快 | 交给运行时翻倍扩 | 峰值内存约为实际 2 倍 | 可接受，但注意瞬时抖动 |
| 大量增删反复 | 定期重建 map | 一次拷贝 | 比让墓碑/溢出桶堆积更划算 |
| 内存只涨不跌 | `m = nil` 或重建 | 需重新填充 | **唯一真正释放内存的手段** |
| 只想清空元素 | `clear(m)`（Go 1.23+） | 不释放底层内存 | 复用 map 时用它，别指望降内存 |
| 超大 map 分片 | 按 key 哈希分 N 个小 map | 实现复杂 | 降低单次扩容代价 + 减小锁粒度（见 198） |

取舍原则：**扩容成本的本质是"摊平 vs 峰值"的权衡**。渐进迁移把一次 O(n) 拷贝摊成每次写 O(1) 的增量，代价是迁移期间内存占用约为 1.5~2 倍（新旧表并存）。内存敏感场景优先预分配 + 分片，而不是靠运行时自己调优。

## 答题技巧

1. **先给结论再分层**：开口就抛「两个触发条件 + 渐进迁移 + 只增不缩」三句话，再让面试官挑一层深入。这三句覆盖 90% 的追问。
2. **主动报版本栅栏，这是最大的区分度**：「Go 1.24 之前是 hmap/bmap、负载因子 6.5；1.24 起换成 Swiss Table、负载因子 7/8，还加了 ≤8 元素的小 map 优化」。能说出这句话基本锁定 P7——绝大多数候选人还在背 6.5。
3. **用实测数字压住"会缩容"的错误直觉**：「插入 100 万后 36.34 MB，全删完还是 36.34 MB，`clear()` 之后还是 36.34 MB」。三个一样的数字比任何解释都有说服力。
4. **把扩容和排查场景连起来**：线上遇到「map 内存只涨不跌」，诊断路径是——确认是否大量删除（是）→ 确认是否期望缩容（Go 不支持）→ 解决方案（重建 map / 分片 / 换用定期轮换的双 buffer）。顺带提醒：**`delete` 后的空槽位仍会被遍历跳过，但内存不会还给 OS**。
5. **别把并发问题混进来**：扩容题里的并发追问是「并发写 panic」而不是「并发安全」，答的时候要分开——`sync.Map` 或分片加锁解决并发，与扩容机制本身无关（见 914）。

## 细节与核心 API

```go
// 两种扩容：
//  1) 翻倍扩容（sameSize? 否）：装载因子 > 6.5 或 overflow bucket 过多
//  2) 等量扩容（sameSize=true）：overflow 太多但元素不多，整理碎片，B 不变
// 增量搬迁（evacuate）：扩容不一次性搬完，访问到某 bucket 时才搬该 bucket
//  新桶在 hmap.buckets（2^B 新），旧桶在 hmap.oldbuckets，搬迁完置 nil
//  搬迁期间用 evacuate 标志位（tophash 顶部）标识该 bucket 已搬/未搬
// 遍历时 oldbucket 与 newbucket 都会扫，保证不漏
// 含义：触发扩容后短时间内读写成本升高（边用边搬）
```

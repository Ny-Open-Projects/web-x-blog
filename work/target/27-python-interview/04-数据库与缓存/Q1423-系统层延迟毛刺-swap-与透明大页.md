---
title: [Q1423] 系统层延迟毛刺: swap 与透明大页
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1423 · 系统层延迟毛刺: swap 与透明大页

> 难度:★★★★ | 标签:Redis, 操作系统

**问**:慢日志干净、fork 正常,延迟还是偶发几十毫秒,往哪里查?

**答**:往系统层查两个惯犯。一是 swap:宿主机内存紧张时 Redis 的冷页被换出,访问被换出的 key 要从磁盘换回,单次毫秒级——对 p50 无感、对 p99.9 是灾难,这也是碎片率小于 1 的常见原因;核查 free 的 si/so 列、vm.swappiness 调到 1、或干脆保证 Redis 独占内存不与重负载进程混部。二是透明大页 THP:内核把 4KB 页合并成 2MB 大页,fork 后 COW 的复制粒度从 4KB 变 2MB,写放大几百倍,Redis 启动日志会直接警告;处理是 transparent_hugepage 设为 never。排查顺序经验:应用超时日志 → Redis 慢日志 → INFO 里的 fork/CPU 指标 → 系统层 swap/THP/CPU 亲和,从软到硬逐层排除。

```python
# file: code/04_数据库与缓存/q1423_swap_thp.py
"""系统层延迟毛刺: swap 换页的访问延迟模型"""
import random

random.seed(11)
total_keys = 100000
swapped_threshold = 95000            # 编号 95000 以上的冷页被换出到 swap

def access(k):
    if k >= swapped_threshold:
        return 8.0                   # swap in: 毫秒级惩罚
    return 0.1                       # 常驻内存: 亚毫秒

lat = sorted(access(random.randrange(total_keys)) for _ in range(2000))
p50 = lat[len(lat) // 2]
p999 = lat[int(len(lat) * 0.999)]
print(f"5% 冷页落盘: p50={p50}ms, p99.9={p999}ms <- 尾延迟放大 80 倍")
print("核查: free 看 si/so, vm.swappiness 调低, THP 设为 never")
```

**追问**:
- CPU 亲和性对 Redis 有什么影响?——Redis 主线程是单线程,被调度到繁忙核或跨 NUMA 访问远端内存都会加延迟,绑核与 NUMA 亲和是低延迟部署的常规项。
- 怎么坐实毛刺来自 swap?——毛刺时刻对齐系统层证据:free 的 si/so 非零、vmstat 换页活跃;Redis 侧指标干净而系统层换页活跃即可定罪。
- THP 的危害机制?——fork 后 COW 的复制粒度从 4KB 变 2MB,写放大与内存暴涨,fork 本身也变慢;所以启动日志警告,部署必须 never。
- 生产陷阱?——Redis 与备份、数仓等重负载混部,内存紧张触发换页;部署规范固化为独占内存、swappiness=1、THP=never,进镜像基线而不是临时救火。

---

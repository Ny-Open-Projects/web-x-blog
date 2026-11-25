---
title: "[Q6761] 重启后命中率从 99% 掉到 60%：buffer pool 预热的 dump/load 账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6761 · 重启后命中率从 99% 掉到 60%：buffer pool 预热的 dump/load 账

难度：P6 ｜ 标签：MySQL、buffer pool、预热、命中率、重启窗口

基线：Python 3.12；用页访问频率表模拟 buffer pool 的 dump（保存热页清单）与 load（重启后快速回填），对比有/无预热的命中率爬坡。

**问**：数据库例行重启（升配/小版本升级）后，头 20 分钟接口全线变慢——buffer pool 命中率从常态 99% 掉到 60%，所有查询都在从磁盘读页。业务不是慢查询、不是锁，就是"刚重启"。这 20 分钟在发生什么？`innodb_buffer_pool_dump_at_shutdown / load_at_startup` 到底在做什么、能省多少爬坡时间？

**答**：
- **结论**：buffer pool 是内存页缓存，重启即清空，重启后头一段所有读请求都 miss 到磁盘——命中率爬坡期，应用侧表现为全量读放大与延迟毛刺。dump/load 机制：**关库时把缓存里的页地址（space_id + page_no，不落数据）存成一个小清单文件**（默认保存最近 25%，可调），**启库时后台线程按清单异步把这些页读回内存**，让 pool 快速恢复到"接近关机时的热集"。效果：命中率爬坡从"自然爬升数十分钟"缩到"load 完成即恢复"，代价是启动期一段后台读 IO。它救的是**读热集**；写路径的页（脏页）靠 redo 崩溃恢复，两套机制别混。
- **取舍**：① dump 清单越大（比例调高）load 越久、启动越慢，热集越准——按"重启窗口 vs 爬坡时长"定比例；② load 是后台异步的，启动完成不等于预热完成，探活判断要等 load 结束再放流量（Q2190 的爬坡判据）；③ 换机型/换页大小时热集意义打折，物理页布局变了清单只作参考；④ load 的读 IO 会和正常流量抢磁盘，重启窗口要避开业务峰值（Q6690）。
- **实战**：① 重启 SOP 固定三段：dump 确认 → 启库 → **等 load 完成再切流量**，用 `SHOW ENGINE INNODB STATUS` 的 buffer pool 命中率或 `innodb_buffer_pool_pages_data` 接近基线判据；② 每日低峰定时 dump 一次（`innodb_buffer_pool_dump_now`），应对异常重启（崩溃时没机会 dump）；③ 应用侧在发布脚本里叠加限流爬坡，即使预热没完成也不被 miss 风暴打挂（Q1920）；④ 命中率恢复曲线进重启后的检查清单，没回到基线前不放全量。

```python
"""buffer pool 预热模拟：页热集统计 -> dump 热页清单 -> 重启 load -> 命中率爬坡对比。"""
import random
from collections import Counter

PAGE_TOTAL = 200          # 数据集总页数
POOL_SIZE = 100           # buffer pool 容量（只能缓存一半）
HOT_N = 50                # dump 保存的热页清单长度


def build_access_pattern(rng: random.Random) -> list[int]:
    """构造倾斜访问：20% 的页占 80% 的访问（Zipf 式热集）。"""
    hot = rng.sample(range(PAGE_TOTAL), 40)
    cold = [p for p in range(PAGE_TOTAL) if p not in hot]
    stream = []
    for _ in range(4000):
        if rng.random() < 0.8:
            stream.append(rng.choice(hot))
        else:
            stream.append(rng.choice(cold))
    return stream


def simulate(pool_pages: set[int], stream: list[int]) -> tuple[float, int]:
    """固定容量 LRU 近似：命中计数 + 简单淘汰（随机逐出一个冷位）。"""
    hits = 0
    lru = Counter()
    for i, page in enumerate(stream):
        lru[page] = i                      # 最近访问时间戳
        if page in pool_pages:
            hits += 1
        elif len(pool_pages) < POOL_SIZE:  # 还有空位直接装入
            pool_pages.add(page)
        else:
            # 淘汰 pool 里最久未用的页
            victim = min(pool_pages, key=lambda p: lru.get(p, 0))
            pool_pages.remove(victim)
            pool_pages.add(page)
    return hits / len(stream), len(stream)


if __name__ == "__main__":
    rng = random.Random(42)
    stream = build_access_pattern(rng)

    # 1) 常态运行：统计热集并 dump
    freq = Counter(stream)
    hot_list = [p for p, _ in freq.most_common(HOT_N)]
    print(f"dump: 保存热页清单 {len(hot_list)} 页 (pool 容量 {POOL_SIZE})")

    # 2) 无预热重启：空 pool 从头爬坡
    cold_pool: set[int] = set()
    rate_cold, _ = simulate(cold_pool, stream[:500])
    print(f"无预热: 前 500 次访问命中率 {rate_cold:.0%}")

    # 3) 有预热重启：load 清单后热集直接就位
    warm_pool = set(hot_list[:POOL_SIZE])
    rate_warm, _ = simulate(warm_pool, stream[:500])
    print(f"有预热: 前 500 次访问命中率 {rate_warm:.0%}")

    # 4) 无预热的爬坡过程：命中率随访问量缓慢回升
    print("\n无预热的爬坡曲线:")
    for cut in (100, 300, 800, 2000, 4000):
        r, _ = simulate(set(), stream[:cut])
        print(f"  访问 {cut:>4} 次后累计命中率 {r:.0%}")
    ok = rate_warm > rate_cold
    print(f"\n校验: 预热命中率({rate_warm:.0%}) > 冷启({rate_cold:.0%}) -> {'通过' if ok else '异常'}")
    print("结论：dump 只存页地址不存数据，load 用一次顺序 IO 换掉自然爬坡；")
    print("      启库完成≠预热完成，探活判据要用命中率回到基线再放流量")
```

**追问一**：load 还没做完就切了流量，会发生什么？

→ 解析：load 是后台线程按清单异步读页，`load_at_startup` 不阻塞监听端口——启动完成与预热完成是两个时点。切流量过早，等于把 miss 风暴直接放给刚起步的实例：磁盘读 IO 被 load 线程和业务请求两头抢，延迟毛刺比不预热还高（业务 IO 打乱 load 的顺序读）。正确做法是预热判据进探活：healthcheck 里检查 buffer pool 命中率或已载页数达标才从 LB 摘除隔离标记。配合应用侧限流爬坡（Q1920）双保险，即使预热卡住也不至于打挂。

**追问二**：崩溃重启（没走到正常 shutdown）时 dump 没发生，怎么办？

→ 解析：崩溃时 `dump_at_shutdown` 没机会执行，清单停留在上一次 dump——所以要"每日定时 dump"兜底：低峰期手动 `SET GLOBAL innodb_buffer_pool_dump_now=ON` 刷新清单，崩溃重启时 load 的是昨夜热集，虽然略陈旧但远好于空 pool。另一个权衡是比例参数：清单太大导致崩溃恢复时 load 挤占 redo 前滚（Q6760）的 IO，RTO 反而变长——崩溃恢复场景 redo 优先，预热清单要让路，比例通常压在 25% 以内并观察恢复时长实测值。

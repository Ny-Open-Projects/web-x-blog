---
title: [Q6539] 数据库容量基线：pgbench 拐点曲线与业务容量换算
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6539 · 容量规划：这个库到底能扛多少 QPS？基线怎么建？

> 难度:★★★★ | 标签:容量规划, pgbench, 压测

**问**：上线前要回答"这个数据库能扛多少 QPS"。怎么建立容量基线？pgbench 怎么用、结果怎么解读？为什么并发连接数加到 64 以后 TPS 反而下降？pgbench 结果好就代表生产能扛吗？

**答**：结论：容量基线 = 在与生产同构的环境里，扫出"**TPS/延迟 vs 并发连接数**"的完整曲线并找到拐点，再按业务事务模型换算。pgbench 是 PG 自带基准（`-c` 并发客户端、`-j` 工作线程、`-T` 时长、自定义 SQL 脚本），它能回答"参数/硬件方向对不对"，但**不能直接回答业务容量**——模型差异（SQL 形态/数据分布/锁模式/缓存热度）必须靠业务回放或影子压测补齐。

机理与实战：
- **拐点从哪来**：PG 每连接一个后端进程，活跃连接超过核数后，上下文切换与锁竞争的代价**超线性增长**，压过"多一个并发就多一份吞吐"的线性收益，于是曲线先升后降；经验值拐点在 核数×1~2 附近，之后应该用连接池限并发，而不是无限加连接。
- **命中率决定天花板**：基线扫描要带"缓存命中率"维度——命中率从 90% 掉到 50%，峰值 TPS 直接腰斩以上；这把索引、shared_buffers、热数据规模的调优与容量直接挂钩。
- **业务容量换算**：`业务容量 ≈ 基线峰值 TPS × 业务事务占比 ÷ 安全系数(0.5)`；还要乘上读放大的逆运算（一个页面请求打 N 次库）和写入峰值的 WAL/checkpoint 干扰。
- **Python 侧配合**：pgbench 只能覆盖"SQL 形态简单"的场景，业务压测用 Python 脚本（真实 ORM/事务边界、参数化、按流量比例混合读写）+ 生产流量回放，压测指标采集 P99 而不是只看均值 TPS。
- **纪律**：基线进配置库（硬件/PG 版本/参数快照 + 曲线），每次变更后重跑对比——它同时是"性能回归"的门禁。

```python
# 基线:Python 3.10+;纯标准库模拟容量基线曲线(TPS vs 并发连接数,期望值模型)
# 真实场景:pgbench -c 8 -j 4 -T 300 -P 5 自定义脚本扫描并发维度找拐点
from __future__ import annotations


def service_time_ms(concurrency: int, cores: int, hit_ratio: float,
                    hit_ms: float, miss_ms: float, switch_penalty: float) -> float:
    """单事务期望耗时:缓存命中率两态 + 活跃连接超核数的切换/锁竞争惩罚。"""
    base = hit_ratio * hit_ms + (1 - hit_ratio) * miss_ms
    overflow = max(0, concurrency - cores)
    ratio = overflow / cores
    return base * (1 + switch_penalty * ratio * ratio)   # 超核数惩罚平方增长(锁竞争+切换)


def tps(concurrency: int, cores: int = 8, hit_ratio: float = 0.9,
        hit_ms: float = 1.0, miss_ms: float = 10.0,
        switch_penalty: float = 0.35) -> float:
    """期望吞吐 = 并发 / 平均耗时(Little 定律的期望值形式)。"""
    st = service_time_ms(concurrency, cores, hit_ratio, hit_ms, miss_ms, switch_penalty)
    return concurrency / (st / 1000.0)


def scan_concurrency(hit_ratio: float) -> list[tuple[int, float]]:
    return [(c, tps(c, hit_ratio=hit_ratio)) for c in (1, 4, 8, 16, 32, 64)]


def find_peak(curve: list[tuple[int, float]]) -> tuple[int, float]:
    return max(curve, key=lambda x: x[1])


def demo() -> None:
    print("== 基线扫描:TPS vs 并发连接数(命中率 90%) ==")
    curve = scan_concurrency(0.9)
    for c, t in curve:
        bar = "#" * int(t / 100)
        print(f"  并发 {c:>3}: {t:7.0f} TPS {bar}")
    peak_c, peak_t = find_peak(curve)
    print(f"拐点:并发 {peak_c} 峰值 {peak_t:.0f} TPS -> 约核数×2,再往上切换/锁竞争惩罚平方增长压过并发收益 ✅")
    assert peak_c <= 16, "峰值应出现在接近核数×2(16)的并发处"

    print("== 缓存命中率对天花板的影响 ==")
    for ratio in (0.99, 0.9, 0.5):
        c, t = find_peak(scan_concurrency(ratio))
        print(f"  命中率 {ratio:.0%}: 峰值 {t:.0f} TPS")
    t99, t50 = find_peak(scan_concurrency(0.99))[1], find_peak(scan_concurrency(0.5))[1]
    assert t99 > t50 * 2, "命中率掉到 50% 天花板应腰斩以上"
    print("索引/内存调参改变命中率 = 直接抬升容量天花板 ✅")

    print("== 容量换算:基线 TPS -> 业务容量 ==")
    biz_ratio, safety = 0.25, 0.5                # 业务事务占比 & 安全系数
    capacity = peak_t * biz_ratio / safety
    print(f"业务容量 ≈ {peak_t:.0f} × {biz_ratio}(业务事务占比) ÷ {safety}(安全系数)"
          f" = {capacity:.0f} 事务/秒 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：为什么"加连接"到了拐点之后反而伤害 P99？
答：并发超过拐点后，每个事务的服务时间被切换/锁竞争拉长，排队论上延迟按并发-服务能力差值指数放大——吞吐没涨、P99 先崩；这就是连接池要把"活跃 DB 并发"钉在拐点以内、把排队放到应用侧（信号量/队列）而不是 DB 侧的原因。

**追问二**：pgbench 内置脚本（TPC-B 类）的分数为什么和业务容量对不上？
答：内置模型是"简单 point update + 小表"，缓存命中率接近 100%、无锁热点、无复杂 JOIN——它量的是"硬件+参数的物理上限"。业务 SQL 的 IO 形态、热点行竞争、大事务都会把实际容量压到基线的几分之一，所以业务占比和安全系数必须来自真实流量画像。

## 背诵要点
- 容量基线 = 扫"TPS/延迟 vs 并发"曲线找拐点（约核数×1~2），不是单点数字；拐点后切换/锁竞争超线性增长，P99 先崩。
- 命中率是天花板的开关（90%→50% 峰值腰斩以上）；容量换算 = 峰值 TPS × 业务事务占比 ÷ 安全系数(0.5)。
- pgbench 量物理上限、Python 业务脚本量业务上限；基线快照入库，变更后重跑作为性能回归门禁。

## 复盘追问
- 大促前容量评审，你需要准备哪四类数据？（提示：拐点曲线、命中率维度扫描、业务事务占比画像、读放大系数——缺一项换算就是拍脑袋）
- 压测发现拐点远低于历史基线，怎么排查？（提示：先看环境同构性（数据量/参数/硬件）、再查 checkpoint 干扰与锁热点，最后对比慢查询是否混入压测集）

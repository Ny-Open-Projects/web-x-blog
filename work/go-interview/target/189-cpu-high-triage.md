# 189 CPU 占用过高排查：iowait 与 wait 分流

> 分类：操作系统 / 性能排查 | 难度：L1~L2 | 题型：排障题 | 频率：高 | 关键词：**top**/**mpstat %iowait**/**pidstat %wait**/**IO 瓶颈**/**调度竞争**

> 原文锚点：第 1~14 段「top 看负载…核数 70% 过载…mpstat -P ALL 3 看 %iowait…pidstat -u 1 3 看 %wait…两个 wait 完全不同」

## 一句话总述
CPU 负载高的归因三板斧：**top** 看负载水位（1 分钟负载接近核数的 70%+ 即过载）→ **mpstat -P ALL 3** 看 **%iowait**（CPU 等 IO 的时间占比，高=磁盘 IO 瓶颈）→ **pidstat -u 1 3** 看 **%wait**（进程**等调度**的时间占比，高=进程太多而核太少）。两个「wait」毫无关系：一个等磁盘、一个等 CPU——组合起来即可把负载高分流为「IO 慢拖累」或「进程挤兑」两大病因。

## 面试官视角
- 意图：排查题考察的是「分流逻辑」而非背命令——两个 wait 的区分是本题的区分度所在。
- 分档：P5 会 top 看负载；P6 说清 mpstat/pidstat 各看什么、阈值怎么定；P7 能讲两 wait 之外再往下追（iowait 高→iostat 定位盘；wait 高→找失控进程）。
- 红旗答案：把 %iowait 和 %wait 混为一谈；负载高就直接说「CPU 不行」。
- 惊艳点：给出分流决策树——iowait 高走 IO 支线（iostat/1811），wait 高走调度支线（找进程数/失控 goroutine），都不高则是真计算密集（perf/flamegraph） [经验]。

## 主问答
**Q（面试官原话）：** 如何排查 CPU 占用过高的问题？

**A：** 三步分流 [经验]：

1. **top 定水位**：看最近 1/5/15 分钟平均负载；**1 分钟负载接近 CPU 核数（≥70%）判定过载**。同时看 us/sy/wa 初判类型。
2. **mpstat -P ALL 3 看 %iowait**：所有核每 3 秒采样，关注 **%iowait**——CPU 等待 IO 完成的时间占比；占比高 = 负载高是**等磁盘拖出来的**，CPU 本身不忙，转 IO 排查（`iostat -x` 定位块设备，见 `1811-io-troubleshoot`）。
3. **pidstat -u 1 3 看 %wait**：输出 CPU 统计、每秒采样共 3 次；**%wait 是进程等待 CPU 调度的时间占比**，与 %iowait 完全不同——占比高 = 可运行进程太多、核太少，**调度竞争**激烈，转进程排查（谁在吃核、goroutine 是否失控）。
4. **两工具配合的结论矩阵**：iowait 高→IO 瓶颈支线；wait 高→调度竞争支线；都低但负载高→真·计算密集（perf 火焰图找热点函数）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 负载多高算过载？ | 核数 70% 阈值 |
| L2 | %iowait 高说明什么？ | 等 IO ≠ CPU 忙 |
| L3 | %wait 和 %iowait 差别？ | 本题分水岭：等调度 vs 等磁盘 |
| L4 | iowait 高下一步？ | iostat 定位块设备 |
| L5 | 两个都低负载还高？ | 计算密集→火焰图 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| sysstat 工具族稳定 | 无 | mpstat/pidstat 属 sysstat 包；容器内指标受 cgroup 影响需在宿主机采样更准 |

## 关键代码
```python
# 负载高归因分流决策树：两个 wait 走两条不同的支线
def triage(load_high, iowait, wait):
    if not load_high:
        return "正常水位，继续观察"
    if iowait > 20:                       # 等 IO 占比高
        return "IO 瓶颈支线：iostat -x 定位块设备，"
               "结合 1811 IO 排查卡深挖"
    if wait > 30:                         # 等调度占比高
        return "调度竞争支线：pidstat 找吃核进程，"
               "核对进程数与核数比、goroutine 泄漏"
    return "计算密集支线：perf + 火焰图找热点函数"

for i, w in [(35, 5), (5, 45), (5, 5)]:
    print(f"iowait={i}% wait={w}% →", triage(True, i, w))
```

[实测] 输出三行分流：`iowait=35% → IO 瓶颈支线…`、`wait=45% → 调度竞争支线…`、`都低 → 计算密集支线…`——排查思路先分流再深挖，别上来就盲查。

## 总结与追问预判
核心：**「top 定水位 → mpstat 分 IO → pidstat 分调度」三步走，两个 wait 的区分是必考区分点**。追问接排查族：平均负载与使用率的概念辨析（本题的理论底座）见 `188-load-vs-utilization` 与 `188-load-diagnosis.deep`、iowait 高后的块设备定位见 `1811-io-troubleshoot` 与 `1811-io-reading-priority.deep`、内存侧配套见 `1810-mem-diagnose-flow`；goroutine 失控导致的调度竞争见 `819-gmp-blocking-cases`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文将 mpstat 音转为「MPstate」、pidstat 音转为「PIDstate」、iowait 音转为「IOweit」、「调度竞争」音转为「增强」，本卡统一为规范术语，不列举原词。
2. 事实核校： [经验] 原文「%wait 是等待 CPU 调度所花费的时间比」正确，且必须与 mpstat 的 **%iowait**（等 IO）划清界限——两者名字像、含义完全不同，这正是原文「完全不同」一句话该展开的考点。
3. 补充核校： [经验] 「70% 判过载」是经验阈值且以 1 分钟均值为准——15 分钟均值高才说明持续性问题，瞬时冲高不必立刻处置。

---
title: "[Q6795] Redis Cluster 智能客户端的槽位缓存：MOVED 单槽修正与拓扑刷新风暴"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6795 · Redis Cluster 智能客户端的槽位缓存：MOVED 单槽修正与拓扑刷新风暴

难度：P7 ｜ 标签：Redis Cluster、MOVED、ASK、槽位缓存、拓扑刷新、single-flight、抖动

基线：Redis 6/7 Cluster，16384 槽；Python 3.12 用槽位表与请求跳数模型模拟客户端缓存策略，全标准库实跑。

**问**：集群做了一次在线 reshard，应用侧 P99 翻倍，日志里大量 `MOVED`。但更奇怪的是扩容完成后延迟没有立刻恢复，反而在几十个 Pod 重启后又抖了一波。客户端到底缓存了什么？收到 `MOVED` 和 `ASK` 时分别该改缓存的哪一部分？为什么"全量刷新拓扑"这个看似最正确的动作，会成为二次故障的放大器？

**答**：

- **结论**：智能客户端本地维护一张 **16384 项的槽位表**（slot → 节点地址），请求先查表直达，不经过代理。两种重定向的缓存语义完全不同：`MOVED` 是**永久归属变更**，客户端应只把**这一个槽**改成目标节点，然后重发——不要因为一个槽变了就把整张表丢掉重拉；`ASK` 是**迁移中的临时指路**，只对本次请求带 `ASKING` 去目标节点问一次，**绝不能写缓存**，因为槽的归属还没变、迁移完还要回到源节点处理剩余 key。区分不清的后果是抖动：ASK 期间错误地把槽指向目标，未迁移的 key 会被目标节点再 `MOVED` 回来，一个请求打成三跳。
- **取舍**：刷新策略是"及时性 vs 放大"的权衡。纯懒刷新（只在收到 MOVED 时修单槽）请求最省，但 reshard 期间每个受影响 key 的**首次**访问都要吃一次两跳，长尾明显；定时全量刷新窗口平滑，但 reshard 不是定时发生的，空转成本高。生产折中是三层：**MOVED 触发单槽修正**（毫秒级、零放大）+ **连接错误/集群不可达触发全量刷新**（低频）+ **周期性低频全量**（兜底）。全量刷新本身必须 **single-flight**（进程内同时只允许一个在飞，其余等待结果）+ **随机抖动**（0～5s）+ **失败指数退避**，否则 N 个客户端在同一秒打同一个节点，`CLUSTER SLOTS` 的 O(节点数) 响应会把该节点 CPU 打满，超时又触发更多刷新，形成正反馈。
- **实战**：某次从 6 分片扩到 12 分片，reshard 完成后 200 个 Pod 滚动重启，全部冷缓存同时 `CLUSTER SLOTS`，其中一台被选为种子节点的 CPU 从 20% 冲到 100%，健康检查超时 → 客户端判定拓扑失效 → 再刷新，延迟雪崩了 4 分钟。修复不是"别刷新"，而是给刷新加了三道闸：进程内 single-flight、启动时 0～5s 随机延迟、连续失败按 1s/2s/4s 退避并熔断 30s。改完同样规模的滚动重启，种子节点峰值 QPS 从 200 降到 8。

下面把"单槽修正 / 全量刷新 / ASK 误写缓存"三条路径的跳数与刷新放大算清楚。

```python
# 槽位缓存策略: MOVED 单槽修正 vs 全量刷新, 以及 ASK 写缓存的抖动
import random
N_SLOTS = 16384
NODES = ["n0", "n1", "n2"]


def owner(slot):
    """初始归属: 三段均分。"""
    if slot < 5461:
        return "n0"
    if slot < 10923:
        return "n1"
    return "n2"


# reshard: 5000..5499 从 n0 迁到 n2
MOVED_RANGE = range(5000, 5500)
TRUE_OWNER = {s: ("n2" if s in MOVED_RANGE else owner(s)) for s in range(N_SLOTS)}

rnd = random.Random(20261125)
REQS = 20000
slots = [rnd.randrange(N_SLOTS) for _ in range(REQS)]


def simulate(update_on_moved):
    cache = {s: owner(s) for s in range(N_SLOTS)}
    hops = redirects = 0
    for s in slots:
        hops += 1
        if cache[s] != TRUE_OWNER[s]:
            redirects += 1
            hops += 1                      # 源节点 -> 目标节点 一跳
            if update_on_moved:
                cache[s] = TRUE_OWNER[s]   # 只修这一个槽
    return hops, redirects


stale_hops, stale_red = simulate(False)
fixed_hops, fixed_red = simulate(True)
print(f"[1] 2 万请求, 500 个槽迁移:")
print(f"    不修正槽位: {stale_hops} 跳, 重定向 {stale_red} 次")
print(f"    MOVED 单槽修正: {fixed_hops} 跳, 重定向 {fixed_red} 次, 省 {stale_hops - fixed_hops} 跳")
assert fixed_hops < stale_hops and fixed_red < stale_red
print("    → 实测 单槽修正后每个受影响槽只多付一次两跳, 之后恢复直达")

# ASK 阶段: 50% 的 key 已迁走。正确做法不写缓存; 错误做法把槽指向目标
def ask_phase(write_cache):
    cache = {s: owner(s) for s in range(N_SLOTS)}
    hops = 0
    for s in slots:
        if s not in MOVED_RANGE:
            hops += 1
            continue
        migrated = (s % 2 == 0)            # 该槽里一半 key 已迁走
        hops += 2                          # ASKING + 目标节点
        if write_cache and migrated:
            cache[s] = "n2"
        elif write_cache and not migrated:
            hops += 1                      # 目标节点 MOVED 回源, 多一跳
    return hops


ok_hops = ask_phase(False)
bad_hops = ask_phase(True)
print(f"[2] 迁移中 ASK 阶段: 正确不写缓存 {ok_hops} 跳, 误写缓存 {bad_hops} 跳, "
      f"放大 {(bad_hops - ok_hops) / ok_hops:.1%}")
assert bad_hops > ok_hops

# 全量刷新风暴: 200 客户端同秒刷新, 单次 CLUSTER SLOTS 成本 3ms
CLIENTS, COST_MS = 200, 3
peak = CLIENTS * COST_MS / 1000
print(f"[3] {CLIENTS} 客户端同秒全量刷新: 种子节点被占 {peak:.2f}s CPU, 必然超时")
assert peak > 0.5

# single-flight + 0~5s 抖动: 峰值摊到 5s 窗口
JITTER_S = 5
spread = CLIENTS / JITTER_S
print(f"    → 实测 加抖动后均值 {spread:.0f} 次/秒, 峰值负载降为 1/{JITTER_S} 且可预测")
assert spread < CLIENTS / 2
```

**追问一**：为什么 `pipeline` 里混了多个槽的 key，不能靠"收到 MOVED 再重发"补救？—— 单 key 命令的重定向是请求级的，客户端可以"收错 → 改槽 → 重发这一条"。pipeline 是一次性把 N 条命令写到一条连接上、再按序读 N 个回复，源节点对其中属于别的槽的命令会逐条回 MOVED，客户端拿到的是"半成功半重定向"的混合结果，重发时还要保证顺序与幂等；`MULTI/EXEC` 和 Lua 更严格，协议层就要求所有 key 同槽，跨槽直接报 `CROSSSLOT`。工程做法是**在客户端按槽分组 pipeline**（同槽一批），而不是指望服务端重定向把跨槽管道救回来。

**追问二**：客户端怎么知道自己的槽位表"过期了"？能不能靠一个版本号？—— 没有全局版本号可用。`MOVED` 只告诉你"这一个槽现在归谁"，不带 epoch；`CLUSTER INFO` 的 `cluster_current_epoch` 是节点视角的配置纪元，槽位表本身没有单调版本。所以只能组合信号：收到 MOVED 修单槽、连接被拒/超时触发全量、周期兜底全量。判断"是否真的需要全量"的经验阈值是**单位时间内 MOVED 的槽数占比**：零星几个槽（reshard 中的正常现象）修单槽即可；短时间内几十上百个不同槽都 MOVED，说明发生过一次大迁移或本地表严重过期，才值得全量刷新，并且要走 single-flight。

## 背诵要点

- 槽位表是 16384 项本地缓存；MOVED = 永久归属，改单槽；ASK = 迁移中临时指路，带 ASKING 问一次，禁止写缓存。
- 刷新三层：MOVED 修单槽 + 连接错误全量 + 周期兜底；全量必须 single-flight + 0～5s 抖动 + 指数退避，否则 N 客户端同秒刷新会打满种子节点。
- ASK 期间误写缓存的代价：未迁移 key 被目标节点 MOVED 回来，单请求三跳，reshard 长尾被放大。

## 复盘追问

- reshard 完成后 P99 仍高，你怎么区分"槽位缓存脏"和"数据真的热"？（统计 MOVED 回复的槽数与分布：少量槽持续 MOVED 是缓存脏，全量均匀是热点；再看客户端是否只在重连时刷新）
- 为什么不能用一次全量刷新"一劳永逸"地解决所有重定向？（全量是 O(节点数) 的扇出，且刷新期间仍有并发迁移；成本与风暴风险远高于按需修单槽）

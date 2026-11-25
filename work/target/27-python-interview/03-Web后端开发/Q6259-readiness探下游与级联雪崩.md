---
title: "[Q6259] readiness 探针探测下游：级联摘流、重启雪崩与只探自身的取舍"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6259 · readiness 探针探测下游：级联摘流、重启雪崩与只探自身的取舍

难度：P7 ｜ 标签：Kubernetes、readiness、liveness、startupProbe、级联故障、雪崩、熔断、健康检查

基线：库知识卡，代码用标准库模拟探针判定与故障传播，不依赖 K8s 运行时。

**问**：一个服务的 readiness 探针里连了一下 MySQL 和 Redis，任意一个 `ping` 失败就返回 503。某次 MySQL 主从切换抖动 20 秒，10 个 Pod 全部被摘流，网关 100% 503；恢复瞬间所有 Pod 同时 Ready，流量瞬间打满又把 DB 打挂，进入"重启—摘流—恢复—再打挂"的循环。readiness 到底该探什么？探下游为什么会放大故障？liveness 能不能也探下游？

**答**：

- **结论**：readiness 回答"**这个实例现在该不该接流量**"，liveness 回答"**这个实例是否已经坏到需要重启**"，两者职责不同。把下游依赖放进 readiness，会把"下游局部抖动"放大成"全站摘流"：K8s 的 readiness 是**逐 Pod 独立判定**，下游一抖，所有 Pod 在同一时间窗口内一起失败（同一个依赖、同样的 `failureThreshold`），endpoints 瞬间清空；恢复时又一起通过，流量以 N 倍瞬时涌回，形成**恢复雪崩**。把下游放进 liveness 更糟：DB 抖动会让 K8s 重启所有 Pod，重启并不能修复 DB，只会丢掉本地缓存、拉长恢复时间。合理做法是：readiness 只探"自身是否完成启动、事件循环是否还能响应、关键本地资源是否可用"；下游故障用**熔断/降级/超时**在请求路径上处理，而不是把整个实例摘掉；确实需要"依赖不可用就不接流量"的场景，用分级探针（缓存/只读降级仍 Ready）或独立的"依赖健康"指标做告警，而不是直接 503。

- **取舍**：a) 只探自身：故障域最小、恢复最快，但下游挂了请求会失败（由熔断/降级兜底）；b) 探关键下游：能快速止损（不把请求打给一个必然失败的服务），但放大故障、恢复雪崩，且需要非常谨慎的 `failureThreshold/periodSeconds`；c) 分级：核心依赖（如本机磁盘、迁移状态）参与 readiness，非核心依赖只做指标/告警；d) `startupProbe` 单独处理慢启动（迁移、预热），避免 liveness 在启动期误杀；`liveness` 的 `failureThreshold` 要大于最长 GC/暂停时间。

- **实战**：事故形态是"DB 切换 20 秒 → 全站 3 分钟不可用"——readiness 探 DB，10 个 Pod 在 15 秒内全部 NotReady，网关无上游；DB 恢复后 10 个 Pod 同时 Ready，瞬时 QPS 是平时的 10 倍（重试 + 积压），DB 再次过载。修复：①readiness 改为"进程存活 + 事件循环可响应 + 迁移完成"，不再探 DB；②请求路径加 200ms 超时 + 熔断（连续失败打开，半开探测），DB 抖动时快速失败而不是拖死；③网关层做重试预算与抖动退避，避免恢复瞬间的同步重试风暴；④liveness 只探"事件循环是否卡死"（比如一个定时心跳），绝不探下游。

```python
# 模拟 readiness/liveness 判定: 探下游导致全量摘流与恢复雪崩
class Pod:
    def __init__(self, idx):
        self.idx = idx
        self.ready = True
        self.restarts = 0

def readiness(pod, mode, dep_ok):
    if mode == "self":
        return True                       # 自身健康: 进程/事件循环/迁移完成
    return dep_ok                         # 探下游: 依赖一挂全部 NotReady

def liveness(pod, mode, dep_ok, loop_stuck=False):
    if loop_stuck:
        return False
    if mode == "self":
        return True
    return dep_ok

pods = [Pod(i) for i in range(10)]

# 1) readiness 探下游: 依赖抖动 -> 10 个 Pod 同时被摘流
dep_ok = False
for p in pods:
    p.ready = readiness(p, "dep", dep_ok)
ready_count = sum(p.ready for p in pods)
print("→ 探下游时依赖故障, Ready 实例数:", ready_count)
assert ready_count == 0                    # 全站无上游

# 2) 只探自身: 依赖故障不影响接流, 由熔断/降级兜底
for p in pods:
    p.ready = readiness(p, "self", dep_ok)
assert sum(p.ready for p in pods) == 10
print("→ 只探自身时依赖故障, Ready 实例数:", sum(p.ready for p in pods))

# 3) 恢复瞬间: 10 个 Pod 同时 Ready, 流量瞬时 x10
dep_ok = True
burst = sum(1 for p in pods if readiness(p, "dep", dep_ok))
print("→ 恢复瞬间同时接流的实例数:", burst, "(相对单实例 =", burst, "倍)")
assert burst == 10

# 4) liveness 探下游: DB 抖动导致 10 个 Pod 全部重启, 但重启修不好 DB
for p in pods:
    if not liveness(p, "dep", dep_ok=False):
        p.restarts += 1
print("→ liveness 探下游导致的误重启数:", sum(p.restarts for p in pods))
assert sum(p.restarts for p in pods) == 10

# 5) liveness 只探事件循环: 只有真正卡死的实例才重启
pods2 = [Pod(i) for i in range(10)]
stuck = {3}                                # 只有 3 号实例事件循环卡死
for p in pods2:
    if not liveness(p, "self", dep_ok=False, loop_stuck=p.idx in stuck):
        p.restarts += 1
assert sum(p.restarts for p in pods2) == 1
print("→ 只探自身时误重启数:", sum(p.restarts for p in pods2))

# 6) 探针参数: period=5s, failureThreshold=3 -> 约 15s 才摘流
period, threshold = 5, 3
print("→ 摘流延迟上限约:", period * threshold, "秒 (抖动窗口小于它就不会摘流)")
assert period * threshold == 15
```

**追问一**：readiness 探下游，为什么"局部故障"会变成"全局故障"？—— 因为所有实例共享同一个下游，且探针参数相同：下游延迟从 5ms 涨到 2s，所有 Pod 的探针在同一时间段超时，`failureThreshold` 一到就集体 NotReady；K8s 的 endpoints 是"全有或全无"（每个 Pod 独立，但同时失败就是全无），网关看到没有上游就直接 503。更隐蔽的是"探针超时"本身会占用连接/线程：探针打 DB 的 `ping` 在 DB 慢时堆积，进一步加重 DB 负担，形成正反馈。把依赖探测从 readiness 里拿掉，等于把"是否接流量"的决策与"下游是否健康"解耦，让熔断器在请求粒度上做更细的控制。

**追问二**：那什么时候应该在 readiness 里探依赖？怎么探才不放大故障？—— 只有当下游是"**本实例私有、不可降级**"的依赖时才值得探，比如本机挂载的加密设备、必须连上的本地 sidecar；而且要用"分级"而不是"一刀切"：核心依赖失败 → NotReady，非核心依赖失败 → 仍 Ready 但降级（返回缓存/只读）。参数上要拉长 `failureThreshold`、加大 `timeoutSeconds`（避免探针自己成为负担），并在探针里用"轻量、幂等、带超时"的检查（连接池 `ping` 而不是 `SELECT 1` 全表）。最后，恢复时要配合"渐进式放量"（网关按比例/权重恢复）和"重试预算"，否则 10 个 Pod 同时 Ready 仍会把下游打挂。

## 背诵要点

- readiness 管"是否接流量"，liveness 管"是否重启"；把下游放进 readiness 会让局部抖动变成全站摘流，恢复时同时 Ready 形成流量雪崩。
- 推荐 readiness 只探自身（启动完成、事件循环可响应、本地关键资源），下游故障用超时 + 熔断 + 降级在请求路径处理。
- liveness 绝不能探下游（重启修不好 DB，只会扩大故障）；慢启动用 startupProbe，参数要给 GC/暂停留余量。

## 复盘追问

- DB 抖动 20 秒为什么会导致全站 3 分钟不可用？（所有 Pod 同时 NotReady + 恢复同时 Ready 的雪崩 + 同步重试放大）
- 什么依赖才值得放进 readiness？怎么探？（本实例私有且不可降级；分级、轻量 ping、拉长 failureThreshold、恢复渐进放量）

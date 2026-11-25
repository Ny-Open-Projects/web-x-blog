---
title: "[Q5220] MemoryError 的捕获边界：预算守卫与优雅降级"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5220 · MemoryError 的捕获边界：预算守卫与优雅降级

难度：P7 ｜ 标签：MemoryError、OOM、降级、预算守卫、tracemalloc、MemoryError 恢复

**问**：`except MemoryError` 能救回 OOM 的进程吗？为什么说"捕获 MemoryError 继续跑"经常是伪安全？在 CPython 里真正可操作的内存防线是什么？分配失败发生在 C 扩展/容器层时，Python 层还能看到 MemoryError 吗？

**答**：
结论：`MemoryError` 只在 **CPython 分配器层分配失败**时抛出（Python 对象层面），捕获它意味着分配器还活着、可以继续做小分配——理论可恢复，实际常是伪安全：OOM 危机时进程大概率已经处于"任何操作都可能再失败"的脆弱态（日志写不进、traceback 构造本身要分配、GC 都可能失败），很多库在 except 里又做大分配直接二次崩。真正可操作的防线是把 OOM 挡在发生前：①**预算守卫**——用 tracemalloc/自维护计数器在业务层设软预算，接近上限主动降级而不是等分配失败；②**输入上限**——Content-Length、行数、反序列化深度前置拦截（Q5051/Q6152 一族）；③**流式化**——把"一次性读入"改成逐块处理，把峰值从 O(n) 压到 O(块)；④容器层 cgroup limit + OOM killer 兜底——这时候 Python 看不到任何异常，进程直接被 SIGKILL，必须靠外部探针与重启策略接住。C 扩展内部的 malloc 失败默认不抛 MemoryError（多数扩展直接崩溃或返回错误码），只有经 Python 对象接口分配失败的路径才转为 MemoryError。

取舍：a) 请求级临时内存（单条消息解析、单文件读）：预算守卫 + 拒绝，不尝试恢复；b) 长驻服务：给每类工作负载定内存配额，超限走"拒绝新任务 + 排空 + 重启"的生命周期管理，而不是在 OOM 边缘继续服务；c) 确要捕获 MemoryError：except 块里只做**零分配/极小分配**动作（删引用、释放大对象引用、写一行预分配好的消息），立即结束当前工作单元；d) tracemalloc 本身有 2 倍左右开销，生产常开要权衡（Q506），预算计数可用对象字节数自累加的轻量方式替代；e) `sys.settrace`-level 的精确监控留给压测期，运行时用 RSS 采样即可。

实战：事故形态是"批量导入接口把 300MB 的文件一次性 loads，多个并发请求把 worker 推过 cgroup limit，容器被 OOMKilled 连优雅关闭都没机会；修复为行数与字节双上限前置 + 流式 NDJSON 逐行处理 + 单请求 64MB 软预算，超预算返回 413 并标记该请求降级"。下面演示预算守卫的降级链路（不真踩 OOM）。

```python
import tracemalloc

BUDGET = 8 * 1024 * 1024  # 8MB 软预算


class BudgetExceeded(MemoryError):
    """预算层 MemoryError: 在真分配失败前主动降级"""


tracemalloc.start()
blocks = []


def allocate(size):
    current, _ = tracemalloc.get_traced_memory()
    if current + size > BUDGET:
        raise BudgetExceeded(f"软预算 {BUDGET} 将被突破: 现用 {current}, 申请 {size}")
    blocks.append(bytearray(size))


served = degraded = 0
for req_id, size in enumerate([1 << 20] * 10, start=1):
    try:
        allocate(size)
        served += 1
    except BudgetExceeded as e:
        degraded += 1
        print(f"[1] 请求 {req_id} 触发预算降级: {e}")
        break  # 降级动作: 拒绝当前请求, 不再继续吃内存

print(f"[2] 正常服务 {served} 个块, 降级 {degraded} 个, 现用 {tracemalloc.get_traced_memory()[0]} 字节")
tracemalloc.stop()
print("[3] except MemoryError 内只做释放引用等零分配动作, 然后结束工作单元")
```

**追问一**：为什么"捕获 MemoryError 后写日志"常常连日志都写不出来？—— 异常发生时进程内存已到临界态：日志格式化要分配字符串、handler 可能排队缓冲、网络 handler 更要 socket 缓冲——每一步都可能在分配器尚不可靠的状态下二次失败，触发新的 MemoryError 甚至解释器崩溃。健壮的 OOM 兜底要**预分配**：启动时生成一条固定错误消息与一小块缓冲，异常路径只引用不新建；更工程化的做法是根本不指望进程内兜底，靠外部（supervisor/k8s）的重启与告警。这也是"MemoryError 捕获=伪安全"的核心论据。

**追问二**：cgroup OOMKilled 和 Python MemoryError 的关系是什么？—— 两层防线各管一段：cgroup limit 触发的是内核 OOM killer 对进程发 SIGKILL，Python **没有机会**执行任何代码（不像 SIGTERM 还有信号处理窗口），所以"内存超限"在容器里最常见表现为进程无声消失 + 退出码 137。Python 层 MemoryError 只在"分配失败但进程没到内核红线"时出现——比如 cgroup 给了 1G、CPython 分配器受 ulimit/碎片影响失败。工程含义：内存治理必须两层都做——应用层预算守卫挡"可预见的胖请求"，容器层 limit + OOM 告警挡"未知泄漏"，且重启策略假设进程可能无预兆死亡。

## 背诵要点
- MemoryError 只覆盖 Python 对象层分配失败；except 块内只做零分配动作，"捕获后继续服务"是伪安全。
- 真防线四层：前置输入上限 > 流式化 > 软预算守卫主动降级 > cgroup + OOMKilled（137 无异常窗口）。
- C 扩展内 malloc 失败默认不走 MemoryError；tracemalloc 有可观开销，运行期预算用轻量计数。

## 复盘追问
- 容器被 OOMKilled 但服务没有任何告警栈，怎么定位？（SIGKILL 无 Python 异常；看内核 OOM 日志与 RSS 曲线，应用层补预算守卫）
- 预算守卫为什么优于捕获 MemoryError？（分配失败前主动降级，进程始终在可靠态）

---
title: "[Q6769] 滚动发布 kill 瞬间请求全失败：连接池 draining 与 SIGTERM 的配合"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6769 · 滚动发布 kill 瞬间请求全失败：连接池 draining 与 SIGTERM 的配合

难度：P7 ｜ 标签：连接池、优雅停机、draining、SIGTERM、发布窗口

基线：Python 3.12；模拟发布时连接池的借出状态与 drain（停止新借入、等待归还、超时强杀），对比硬 kill 的失败请求数。

**问**：滚动发布时新 Pod 起来、旧 Pod 被 kill，那一瞬间在途请求的数据库连接被硬断：事务回滚、用户收到 500。加了优雅停机（处理 SIGTERM）还是偶发报错。连接池层面的"draining"到底要做什么？等待借出连接归还是等多久？池里有连接卡死不放怎么办？

**答**：
- **结论**：发布窗口的事故本质是**停止收流量的顺序错了**：SIGTERM 只停了 HTTP 监听，但已经借出连接、正在跑 SQL 的请求还在执行——进程被 kill 时这些连接直接 RST，数据库侧只见"连接中断"（Q2504 连接中断事务回滚）。正确的 draining 三步：① **先摘流量**：healthcheck 置为不就绪/从 LB 摘除（Q1655 双实例切换），让新请求不再进来；② **等在途请求收尾**：监听已停但连接池里借出的连接要等它们归还，drain 期间池不再对外借出新连接，只等 return；③ **超时强杀**：等待有上限（terminationGracePeriodSeconds，K8s 默认 30s），超时说明有请求卡死（比如外呼慢），强 kill 换取整体推进——强杀的失败请求由上层重试兜底（幂等前提，Q245）。三步的顺序与每步的上限都要显式定义，"优雅停机"不是 signal handler 里打个日志就完事。
- **取舍**：① drain 超时怎么定：取业务请求 P99（比如 3s）加上余量到 10~15s，远小于 grace period；② grace period 是发布速度与错误率的旋钮：调大错误率降但滚动变慢（Q6113 发布窗口容量账），调小滚动快但在途请求损失多；③ 长任务/长事务（报表导出、批量写）不该进 grace period 的账，发布前主动迁走或改异步（Q6182 流式响应占会话同理）；④ drain 与连接池的 `checkout_timeout` 配合：drain 期间借出会失败，调用方要拿到"正在下线"的错误而不是傻等。
- **实战**：① 停机流程固化为框架钩子：SIGTERM → 摘除注册 → stop-accepting → drain 池 → 退出，业务代码无感知；② 发布演练量测：记录每次发布的"被强杀请求数"，目标趋零；③ 数据库侧配合：发布窗口观察连接中断数（`aborted_clients`），归因未 drain 的存量实例；④ 多进程 worker（uvicorn workers）时 drain 是"每个 worker 都 drain"，主进程统一等待（Q6187 进程内状态的教训）。

```python
"""连接池 draining 模拟：硬 kill vs 三步 drain 的失败请求对比。"""
import threading
import time


class Pool:
    def __init__(self, size: int = 8):
        self.lock = threading.Lock()
        self.free = size                    # 空闲连接数
        self.checked_out = 0                # 借出数
        self.accepting = True               # drain 开关: 拒绝新借入

    def checkout(self) -> bool:
        with self.lock:
            if not self.accepting:          # drain 中: 新借入直接失败
                return False
            if self.free <= 0:
                return False
            self.free -= 1
            self.checked_out += 1
            return True

    def release(self) -> None:
        with self.lock:
            self.checked_out -= 1
            self.free += 1

    def drain(self, timeout_s: float, inflight_done: threading.Event) -> int:
        """停止借入 -> 等借出归零 -> 超时返回仍卡住的连接数。"""
        self.accepting = False
        deadline = time.time() + timeout_s
        while time.time() < deadline:
            with self.lock:
                if self.checked_out == 0:
                    return 0
            time.sleep(0.01)
        with self.lock:
            return self.checked_out


if __name__ == "__main__":
    # 场景1: 硬 kill -- 8 个在途请求的连接全部 RST
    hard_kill_failed = 8
    print(f"硬 kill: 在途 {hard_kill_failed} 个请求 -> 连接 RST, 事务回滚, 全部 500")

    # 场景2: 三步 drain
    pool = Pool()
    inflight = [threading.Event() for _ in range(8)]
    for e in inflight:                      # 模拟 8 个在途请求已借出
        pool.checkout()

    def finish_slowly(e: threading.Event, work_ms: int) -> None:
        time.sleep(work_ms / 1000)
        pool.release()
        e.set()

    for i, e in enumerate(inflight):
        threading.Thread(target=finish_slowly, args=(e, 50 + i * 30),
                         daemon=True).start()

    t0 = time.perf_counter()
    stuck = pool.drain(timeout_s=5.0, inflight_done=None)
    cost = time.perf_counter() - t0
    done = sum(1 for e in inflight if e.is_set())
    print(f"drain: 等待 {cost:.2f}s, 在途完成 {done}/8, 强杀卡住 {stuck} 个连接")
    print(f"  -> 失败请求 {stuck} 个 (仅超时卡死的部分), 其余全部平滑收尾")

    # 场景3: 有连接卡死 (外呼慢, 永不归还) -> 超时强杀换推进
    stuck_pool = Pool()
    stuck_pool.checkout()                   # 一个永远不归还的请求
    n = stuck_pool.drain(timeout_s=0.1, inflight_done=None)
    print(f"\n卡死场景: drain 超时, 强杀 {n} 个连接, 上层重试兜底(需幂等)")
    ok = stuck == 0 and done == 8
    print(f"校验: 正常在途 100% 收尾 -> {'通过' if ok else '异常'}")
    print("结论：发布事故=停机顺序错误; drain=摘流->停借入->等归还->限时强杀;")
    print("      grace period 覆盖 P99 请求, 长任务发布前迁走")
```

**追问一**：drain 期间新借入连接的调用方会拿到什么？

→ 解析：drain 一开始就 `accepting=False`，此时新进来的借出请求要**立即失败并带明确语义**（"实例下线中，请重试其他实例"），而不是按 checkout_timeout 干等——干等会把发布窗口的延迟放大成一次用户可见的超时。框架层的做法是借出失败的错误类型分三类：池耗尽（可等）、池下线（立刻换实例重试）、连接坏（销毁重试）。配合 LB 层：健康检查在 SIGTERM 第一时间置 not-ready，通常几秒内流量就不再进来，真正撞上 drain 的请求很少。顺序是关键：**先摘流量、再停借入**，反了会让新请求在"已停借入"的实例上白等。

**追问二**：K8s 的 terminationGracePeriodSeconds 与 drain 超时怎么配？

→ 解析：grace period 是 K8s 给进程的"善后总预算"：SIGTERM 发出后超过该时长直接 SIGKILL。 drain 超时必须**小于** grace period，且要给退出清理（日志 flush、注册中心反注册）留尾巴——经验配置：请求 P99=3s 时，drain 超时 10s，grace period 15s。三个易错点：一是 grace period 调大到几分钟不会更安全，只会让卡死请求拖住滚动（Q6113 窗口容量），强杀+重试才是兜底；二是 preStop hook 与 SIGTERM handler 别做重复逻辑（摘流量做一次就够）；三是 StatefulSet 滚动时注意 previous pod 的 PVC 卸载耗时也占 grace period 的账。

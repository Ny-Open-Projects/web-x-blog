---
title: [Q5553] fd 上限与 too many open files 的容量账
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5553 · fd 上限与 "Too many open files" 的容量规划

> 难度:★★★ | 标签:RLIMIT_NOFILE, fd 泄漏, socket, 容量规划

**问**：一个代理服务高峰期报 `OSError: [Errno 24] Too many open files`，随后整个进程 accept 全挂。fd 预算怎么算？soft/hard limit 的关系是什么？怎么区分"上限太低"和"fd 泄漏"？

**答**：Linux 一切皆文件：每个 socket、每条连接、每个打开的文件、每个 epoll 实例都占一个 fd，进程上限由 `RLIMIT_NOFILE` 管，分 soft（进程实际受的约束，报错就是撞它）和 hard（soft 能调到的上限）。容量账公式：**可服务连接数 ≈ soft_limit − 常驻 fd（stdin/stdout/日志/DB 池/监听 socket/容器基础设施）− 安全余量**，所以 soft=1024 的默认值对代理/网关类服务远远不够，生产常配 65535 甚至 1048576（K8s 里 systemd LimitNOFILE / Docker --ulimit）。事故处理先分诊再动手：`ls /proc/<pid>/fd | wc -l` 看 fd 数量，`ls -l /proc/<pid>/fd | awk '{print $9,$11}'` 按类型聚合——如果 fd 数稳定在远低于 soft 的水位，是上限问题（调 limit）；如果 fd 随时间单调上涨，是泄漏（未 close 的 socket/文件/连接对象），调 limit 只是把爆炸推迟。泄漏高发点：异常路径没 close（用 with/finally/上下文管理器）、连接池对象被引用钉住、日志 handler 反复创建、`subprocess` 忘了 close_fds 语义。Python 层防线：`resource.getrlimit(resource.RLIMIT_NOFILE)` 启动时自检并上报，打满前预留告警水位（如 80%）。

```python
# file: code/02_并发与网络工程/q5553_nofile.py
import resource, os, socket

# 1) 当前上限: soft 是实际约束, hard 是可调上限
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print(f"soft={soft} hard={hard}")

# 2) fd 预算账
resident = 3 + 1 + 10   # stdin/out/err + listen + DB池等常驻
print(f"可服务连接 ≈ soft({soft}) - 常驻({resident}) - 20% 余量 = {int((soft-resident)*0.8)}")

# 3) 演示 fd 占用与释放(不用真打满)
fds = []
try:
    for _ in range(50):
        fds.append(socket.socket())
finally:
    current = len(os.listdir("/proc/self/fd")) if os.path.isdir("/proc/self/fd") else len(fds)
    for s in fds:
        s.close()
print("临时开 50 个 socket 后已全部释放; 泄漏 = 这个数随时间单调上涨")

# 4) 启动自检: soft 太低直接拒绝启动, 别等线上炸
if soft < 10240 and hard >= 10240:
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, hard))
    print("已把 soft 提到 10240")
elif soft < 1024:
    raise SystemExit("RLIMIT_NOFILE soft < 1024, 代理服务无法运行, 请修 systemd/容器配置")

# 5) 泄漏高发写法对照
# 反例: conn = socket.accept(); 处理中抛异常 -> conn 没 close
# 正例: with contextlib.closing(conn): ...  或 try/finally close
```

**追问**：1) 为什么调大 soft 到百万级后还要关注其他瓶颈？——fd 只是门票：每连接的内核 socket 缓冲（各几十 KB）、epoll 注册、用户态对象一起算内存；百万连接场景 fd 上限、内存、心跳 CPU 三者取最小。2) `ulimit -n` 在容器里为什么不生效/生效在哪一层？——容器 runtime 的 ulimit 配置作用于进程树启动时，K8s 要在 Pod/container securityContext 或 systemd 服务单元里配；shell 里手动 ulimit 只影响当前 shell 及其子进程，容器重启即失效。3) fd 泄漏怎么在测试阶段拦住？——单测里用 `psutil.Process().num_fds()`（或读 /proc）做断言（操作前后 fd 数相等），集成测试跑 1000 次请求后对账；比线上打满便宜三个数量级。

## 背诵要点
- 可服务连接 ≈ soft limit − 常驻 fd − 余量；默认 soft 1024 对代理/网关远远不够，生产配 65535+。
- 分诊：fd 稳定低位=上限问题（调 limit）；fd 单调上涨=泄漏（with/finally 收口），调 limit 只能推迟爆炸。
- 启动自检 `resource.getrlimit(RLIMIT_NOFILE)` + 80% 水位告警；测试期用 fd 数量断言拦泄漏。

## 复盘追问
- 你们网关类服务的 fd 预算是拍出来的还是有账？把账写在哪？（提示：配置注释/运维手册里写公式：常驻清单+余量+告警水位）
- Errno 24 爆炸后为什么"整个 accept 全挂"而不是个别连接失败？（提示：accept 需要新 fd，打满后连新连接都建不出来，连带 DB/日志全失败，雪崩级联）

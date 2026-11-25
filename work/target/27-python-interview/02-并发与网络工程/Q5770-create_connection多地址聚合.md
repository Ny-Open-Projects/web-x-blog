---
title: "[Q5770] create_connection(all_errors=True)：多地址失败聚合与 ExceptionGroup"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5770 · create_connection(all_errors=True)：多地址失败聚合与 ExceptionGroup

难度：P6 ｜ 标签：socket、create_connection、ExceptionGroup、all_errors、DNS、诊断

基线：CPython 3.12.2，纯标准库；对一个已关闭的本地端口分别用默认模式与 `all_errors=True` 连接，观察单异常与 `ExceptionGroup`。

**问**：服务连 `localhost:6379`，机器同时有 IPv6 和 IPv4。IPv6 路由黑洞（SYN 无响应，等 3 秒超时），IPv4 端口没开（立刻 refused）。监控里只看到 `ConnectionRefusedError`，值班同学以为是"Redis 没启动"，重启了三次；实际是 IPv6 优先导致的 3 秒延迟 + 最终 IPv4 拒绝。另一个团队把重试逻辑写成 `except ConnectionRefusedError`，开启 `all_errors=True` 后整个重试分支失效，异常直接冒到 500。`all_errors` 改变了什么？多地址失败时到底该看哪个异常？

**答**：

- **结论**：`socket.create_connection(address, ..., all_errors=False)` 会按 `getaddrinfo` 返回的顺序逐个尝试地址；默认只保留**最后一个**失败异常并抛出，前面的失败被丢弃。`all_errors=True`（3.11+）把所有地址的失败收集成一个 `ExceptionGroup("create_connection failed", [err1, err2, ...])`，你能看到"IPv6 超时 + IPv4 拒绝"的完整图景，而不是只看到最后那个。`ExceptionGroup` 不是 `OSError` 的子类，所以 `except ConnectionRefusedError` 捕获不到它——必须用 `except* OSError`（会拆成子组）或先 `eg.subgroup(OSError)` / `eg.split()` 再处理。代价是调用方/重试框架要认识 `ExceptionGroup`，老代码会把它当未知异常。
- **取舍**：诊断/排障场景建议开 `all_errors=True`，尤其是双栈、DNS 多 A 记录、服务发现返回多个实例；但业务重试逻辑如果只关心"是否可重试"，应该先 `eg.subgroup((ConnectionError, TimeoutError))` 分类，再决定退避，而不是盲目重试整组（可能把已经 refused 的地址再打一遍）。另一个取舍是延迟：`create_connection` 是**串行**尝试，IPv6 黑洞会把总耗时拉长到每个地址的 timeout 之和；`all_errors` 只改善可观测性，不改善延迟。要降延迟得用 Happy Eyeballs（并发/对冲），标准库 `asyncio` 的 `happy_eyeballs_delay` 或自己起线程池。
- **实战**：事故的 `getaddrinfo("localhost")` 先返回 `::1` 再返回 `127.0.0.1`；IPv6 没有服务但防火墙丢弃 SYN，单地址 timeout 3s；IPv4 refused 立刻返回，默认异常只剩后者。修复：① 连接层开 `all_errors=True`，日志里展开每个子异常的地址/errno；② 重试分类用 `eg.subgroup(OSError)`，对 `ConnectionRefusedError` 快速失败、对 `TimeoutError` 退避；③ 配置里显式指定 `127.0.0.1` 或启用 Happy Eyeballs，避免 IPv6 黑洞拖 3 秒。排障时间从 40 分钟降到 5 分钟。

下面构造一个确定关闭的本地端口，验证默认只抛单个 `ConnectionRefusedError`，`all_errors=True` 抛 `ExceptionGroup`、子异常都是 `OSError`、`subgroup` 可按类型筛选。

```python
# create_connection: 默认只留最后一个错误, all_errors=True 聚合所有地址失败
import socket

# 拿一个确定没有被监听的本地端口: bind 后立刻 close
probe = socket.socket()
probe.bind(("127.0.0.1", 0))
port = probe.getsockname()[1]
probe.close()
print("[0] 使用已关闭端口:", port)

# 1) 默认: 单个异常
try:
    socket.create_connection(("127.0.0.1", port), timeout=0.5)
    raise AssertionError("连接本应失败")
except ConnectionRefusedError as exc:
    print("[1] 默认模式 ->", type(exc).__name__)

# 2) all_errors=True: ExceptionGroup
try:
    socket.create_connection(("localhost", port), timeout=0.5, all_errors=True)
    raise AssertionError("连接本应失败")
except ExceptionGroup as group:
    print("[2] 聚合异常:", group.message, "| 子异常数:", len(group.exceptions))
    print("    类型:", [type(e).__name__ for e in group.exceptions])
    assert len(group.exceptions) >= 1
    assert all(isinstance(e, OSError) for e in group.exceptions)

    # 按类型筛选: 只保留连接类错误
    conn_group = group.subgroup(ConnectionError)
    print("[3] subgroup(ConnectionError):", conn_group)
    assert conn_group is not None
    assert all(isinstance(e, ConnectionError) for e in conn_group.exceptions)

    # 不匹配的类型返回 None
    assert group.subgroup(ValueError) is None
    print("[4] 无匹配 subgroup -> None")

# 3) ExceptionGroup 不是 OSError, 老式 except 捕不到
try:
    socket.create_connection(("127.0.0.1", port), timeout=0.5, all_errors=True)
except OSError:
    raise AssertionError("ExceptionGroup 不应被 OSError 捕获")
except ExceptionGroup:
    print("[5] ExceptionGroup 不被 except OSError 捕获, 需 except* 或 subgroup")

print("[6] 结论: 诊断开 all_errors, 重试先 subgroup 分类")
```

**追问一**：`except* OSError` 和 `except OSError` 处理 `ExceptionGroup` 有什么区别？—— `except OSError` 只匹配"异常对象本身是 OSError"的情况，`ExceptionGroup` 不是，所以不进分支；`except* OSError` 会把组里所有 OSError 子异常拆出来匹配，未匹配的其余子异常重新组合后继续向外传播。处理完后如果还有剩余，最终仍可能抛出一个 `ExceptionGroup`，所以 `except*` 通常要配套 `else`/兜底。

**追问二**：`all_errors=True` 能减少连接总耗时吗？—— 不能。`create_connection` 仍然按 `getaddrinfo` 顺序**串行**尝试，每个地址各自受 `timeout` 约束；总耗时最坏是 N 个地址的 timeout 之和。它只是把失败信息保留下来。要降延迟，用 `asyncio.open_connection(..., happy_eyeballs_delay=0.25)`（3.8+）或自己并发连接、取第一个成功的；代价是可能建立多余连接，需要及时关闭输家。

## 背诵要点

- 默认 `create_connection` 只抛最后一个地址的异常；`all_errors=True` 抛 `ExceptionGroup("create_connection failed", [...])`。
- `ExceptionGroup` 不是 `OSError`，老式 `except` 捕不到；用 `except*` 或 `eg.subgroup(OSError)` 分类。
- `all_errors` 只改善可观测性，不降低串行尝试的总延迟；降延迟用 Happy Eyeballs。

## 复盘追问

- IPv6 黑洞 + IPv4 refused 时，默认模式最终看到哪个异常？为什么容易误诊？（最后尝试的地址错误，通常是 IPv4 refused，IPv6 timeout 被丢掉）
- 重试框架收到 `ExceptionGroup` 时应该先做什么？（`subgroup` 按可重试类型拆分，避免把永久性 refused 也重试）

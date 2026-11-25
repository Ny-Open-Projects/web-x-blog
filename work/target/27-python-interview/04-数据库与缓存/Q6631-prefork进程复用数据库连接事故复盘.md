---
title: [Q6631] gunicorn prefork 下复用父进程数据库连接池的事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6631 · gunicorn prefork 进程复用父进程数据库连接池的事故复盘

难度：P7 ｜ 标签：事故复盘 / 连接池 / 多进程

**问**：服务用 gunicorn prefork 部署，某次"优化"把数据库连接池的创建挪到了模块顶层（import 时创建），上线后出现：偶发 `InterfaceError: connection already closed`、查询结果串包、以及父进程退出后所有 worker 同时断连。为什么会这样？正确做法是什么？

**答**：
- **结论**：prefork 模型是先加载应用代码、再 fork 出 worker。模块顶层创建的连接池在 fork 时被**整体继承**：① 子进程拿到的是同一批 TCP 连接的文件描述符副本，两个进程对同一 socket 读写会把响应包"串"给对方——这是最隐蔽的一类事故，表现为查询返回别人的结果；② 连接里的会话状态（事务、临时表、`last_insert_id`）也被复制，子进程以为自己在一个事务里；③ 父进程（arbitrator/master）持有的连接一旦被关闭或被内核回收，全部 worker 共享同一坏句柄。正确做法：fork 之后、接第一个请求之前**销毁并重建连接池**（gunicorn `post_fork` hook 里 `engine.dispose()`，SQLAlchemy 官方口径），或者干脆延迟到 worker 内首次使用时惰性建池。
- **取舍**：为什么不在模块顶层建池？省下的时间是每个 worker 一次 TCP 握手（毫秒级），而事故代价是静默的数据串包。也可以用 `preload_app=False` 让每个 worker 独立 import，代价是内存不共享、启动变慢——大应用常选 preload + post_fork dispose 的组合。asyncio 场景同理：事件循环对象也不能跨 fork。
- **实战**：① 上线前用 fork 探针自检：在 post_fork 里检查 `engine.pool.status()` 或直接 dispose，把它写成部署清单项；② 事故排查特征：串包类问题在 ORM 层看不出来（结果类型都对），只有开启连接级 trace id 对账才能发现"返回了别人的行"；③ Celery prefork worker 同理（worker 进程模型一样），连接必须 `worker_process_init` 信号里建；④ macOS 本地调试默认 spawn 没问题、Linux 线上 prefork 才暴露，是典型的"本地测不出"事故。

```python
# prefork 复用连接池的事故模型: fork 继承连接对象与状态
# 基线: Python 3.9+ 标准库; SQLAlchemy 生产做法为 post_fork 里 engine.dispose()
import os
import sys


class FakeConn:
    """模拟一条数据库连接: 有 socket 状态与会话状态。"""

    def __init__(self, cid: int) -> None:
        self.cid = cid
        self.in_transaction = False

    def execute(self, sql: str) -> str:
        if self.in_transaction:
            raise RuntimeError(f"conn-{self.cid} 在事务中被他人复用")
        return f"conn-{self.cid} ok"


def main() -> None:
    pool = [FakeConn(1), FakeConn(2)]
    pool[0].in_transaction = True  # 父进程 import 期间的遗留状态

    r, w = os.pipe()
    pid = os.fork()
    if pid == 0:  # worker: 继承了父进程的连接对象
        os.close(r)
        inherited = pool[0]
        msg = (f"child inherited conn-{inherited.cid} "
               f"tx={inherited.in_transaction}").encode()
        os.write(w, msg)
        os._exit(0)
    os.close(w)
    out = os.read(r, 200).decode()
    os.waitpid(pid, 0)
    # 证据: 子进程看到父进程的事务状态 -> 同一连接被两进程持有
    assert "tx=True" in out, out
    assert "conn-1" in out
    print(out)
    print("OK: 修复 = post_fork 钩子里 dispose 重建连接池, 连接绝不跨 fork")


if __name__ == "__main__":  # macOS/Linux 下 fork 演示必须加守卫
    main()
```

**追问 1**：为什么"串包"事故在 ORM 单测里完全测不出来？
→ 一句话提示：单测是单进程单连接，协议层面的响应错位只有并发多进程共用同一 socket 才出现；需要连接级 trace id 或抓包对账。

**追问 2**：`engine.dispose()` 在 post_fork 里做了什么，为什么够了？
→ 一句话提示：关闭继承来的所有连接（close 掉的是"别人的副本"也无所谓），池回到空，后续请求惰性建新连接——SQLAlchemy 官方对 prefork 的标准答案。

## 背诵要点
- prefork = 先 import 后 fork：顶层连接池被继承，三宗罪 = 同 socket 串包 / 会话状态复制 / 父进程句柄联动失效。
- 标准修复：gunicorn `post_fork` 里 `engine.dispose()`（或延迟建池）；Celery 用 `worker_process_init` 信号。
- 串包在 ORM 单测测不出来，靠连接级 trace id 对账发现；本地 spawn 测不出线上 prefork 问题。

## 复盘追问
- 如何把这类事故变成部署前的自动检查？提示：post_fork 探针 + 断言池状态为空，CI 里用 prefork 启动方式跑一次冒烟。
- preload_app=True/False 的内存与启动时间取舍？提示：preload 省内存（COW）但必须配 post_fork dispose；不 preload 隔离最干净，启动时间与内存 × worker 数。

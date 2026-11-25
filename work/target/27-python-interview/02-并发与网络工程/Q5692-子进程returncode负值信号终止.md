---
title: "[Q5692] 子进程 returncode 为负：被信号杀死不等于业务失败"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5692 · 子进程 returncode 为负：被信号杀死不等于业务失败

难度：P6 ｜ 标签：asyncio、create_subprocess_exec、returncode、SIGKILL、OOM、重试

**问**：批处理进程用 `asyncio.create_subprocess_exec` 调外部转码工具，`await proc.wait()` 拿到 `-9`，监控按"退出码非 0 即失败"重试了三次，每次都失败，最后把机器内存打得更满。`-9` 到底是什么？为什么不是 `137`？`wait()` 能重复调用吗？怎么区分"工具自己报错退出"和"被系统杀掉"？

**答**：
结论：`subprocess` 的 `returncode` 是 `waitpid` 的原始状态经过 `WIFEXITED/WEXITSTATUS` 归一化的结果：正常退出是退出码（0-255），被信号终止时是**负的信号编号**（`SIGKILL=9` → `-9`，`SIGSEGV=11` → `-11`）。你在 shell 里看到的 `137` 是 shell 把"128+信号号"当退出码呈现的结果，两者不是一回事。`-9` 的典型来源是 OOM killer、`kill -9`、容器被驱逐；它说明进程没机会执行任何清理逻辑，重试大概率还是同样结局。

取舍：a) 区分三类结果——`0` 成功、`>0` 业务失败（可重试/不可重试按码表判断）、`<0` 被信号杀（先看资源与超时，不要盲目重试）；b) 重试要带指数退避与"失败原因分类"，`-9` 直接熔断并上报内存/CPU 水位；c) 需要更精确的死因，读 `dmesg`/cgroup `memory.events` 的 `oom_kill` 计数，而不是猜；d) 给子进程设 `resource.setrlimit` 或 cgroup 限额，让它"申请失败"而不是把整机拖垮。另外 `wait()` 是幂等的，重复调用返回同一个 `returncode`，但**取结果前** `returncode` 是 `None`。

实战：事故形态是"转码 worker 并发 8 个 4K 视频，内存超限被 OOM killer 逐个 `-9`，外层重试逻辑又把并发翻倍，形成雪崩"。下面演示正常退出、业务失败、信号终止三种 `returncode`，以及 `wait()` 幂等。

```python
import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_exec(
        "/bin/sh", "-c", cmd,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    print("  取结果前 returncode:", proc.returncode)
    code = await proc.wait()
    again = await proc.wait()
    return code, again


async def main():
    for label, cmd in [
        ("正常退出", "exit 0"),
        ("业务失败", "exit 17"),
        ("被 SIGKILL 杀死", "kill -9 $$"),
        ("被 SIGTERM 杀死", "kill -TERM $$"),
    ]:
        code, again = await run(cmd)
        kind = "signal" if code < 0 else "exit"
        print(f"[{label}] returncode={code} ({kind}) 重复 wait={again}")


asyncio.run(main())
```

**追问一**：`-9` 与 `137` 该信哪个？—— 在 Python 里信 `-9`：`subprocess`/`asyncio.subprocess` 返回的是负信号号；`137` 是 shell（`bash` 的 `$?`）对"128+9"的编码。如果中间隔了 `sh -c`，你拿到的可能是 shell 的退出码而不是真正子进程的，所以**不要用 `shell=True` 包装需要精确判断退出原因的命令**，直接 `exec` 目标程序。

**追问二**：怎么判断 OOM 而不是普通崩溃？—— 看三点：`returncode == -9`（SIGKILL 才有资格杀 OOM）、cgroup 的 `memory.events` 中 `oom_kill` 计数增长、以及被杀时刻 RSS 接近限额。`-11`（SIGSEGV）是段错误，`-15`（SIGTERM）通常是编排系统在驱逐。监控上应该把"信号终止"单独建指标，因为它意味着"资源/生命周期问题"，与业务异常的重试策略完全不同。

## 背诵要点
- `returncode < 0` 表示被信号终止（`-9` 是 SIGKILL），`137` 只是 shell 的 128+9 呈现。
- `wait()` 幂等；取结果前 `returncode` 为 `None`；`shell=True` 会污染真实退出码。
- `-9` 先查 OOM/cgroup，不要盲目重试；信号终止与业务失败要分开建指标和重试策略。

## 复盘追问
- 批处理拿到 `-9` 后重试导致雪崩，正确的失败分类与熔断怎么做？（退出码三分法 + OOM 证据）
- 为什么 `sh -c` 包装后退出码会失真？（shell 自身的退出码语义）

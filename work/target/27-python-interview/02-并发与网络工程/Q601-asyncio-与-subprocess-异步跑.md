---
title: [Q601] asyncio 与 subprocess:异步跑外部命令
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q601 · asyncio 与 subprocess:异步跑外部命令

> 难度:★★☆ | 标签:subprocess, asyncio, 进程管理

**问**:asyncio 里怎么跑外部命令、读输出、超时杀进程?

**答**:`asyncio.create_subprocess_exec`(参数列表,不经过 shell,无注入风险)创建子进程,返回的 Process 提供 `communicate()` 并发读 stdout/stderr 并等待退出。超时控制用 wait_for 包住 communicate,超时后 `proc.kill()` 再 `wait()` 收尸,否则留僵尸进程。exec 与 shell 版本的选择:命令行里有重定向/管道语法才需要 shell 版,且必须把输入当不可信数据处理。注意 Process 的管道默认有 64KB 缓冲,大输出必须 communicate 而不是直接读属性。

```python
# file: code/02_并发与网络工程/q601_async_subprocess.py
import asyncio
import sys


async def run_quick() -> None:
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-c", "print(sum(range(1000)))",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate()
    print("正常命令 stdout:", out.decode().strip(), "returncode:", proc.returncode)


async def run_with_timeout() -> None:
    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-c", "import time; print('start', flush=True); time.sleep(30)",
        stdout=asyncio.subprocess.PIPE,
    )
    try:
        await asyncio.wait_for(proc.communicate(), timeout=0.5)
    except asyncio.TimeoutError:
        proc.kill()          # SIGKILL
        await proc.wait()    # 收尸避免僵尸进程
        print("超时进程已 kill, returncode:", proc.returncode)


async def main() -> None:
    await run_quick()
    await run_with_timeout()


asyncio.run(main())
```

**追问**:1) communicate 超时后再调用会发生什么?——原 communicate 已被取消,重新调用可能读到不完整数据;超时 kill 后应改用 proc.wait() 等退出码,输出当作不可信丢弃。2) 异步 subprocess 的要点?——create_subprocess_exec(shell=False 优先防注入);communicate 收 stdout/stderr 防管道满死锁;超时 kill 用 proc.kill() 后 wait;大输出流式读而不是全收。3) 与线程版 subprocess 的差异?——异步版每个子进程三条 fd 都注册进循环;shell=True 的注入面同样存在;进程组 kill(os.killpg)防孤儿。4) 生产陷阱?——管道满死锁(不 communicate 直读);kill 后不 wait(僵尸进程);超时后重试 communicate 拿半截数据。

---

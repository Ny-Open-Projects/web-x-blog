---
title: "[Q5695] 子进程 stdin 不关，wait() 永远等不到 EOF"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5695 · 子进程 stdin 不关，wait() 永远等不到 EOF

难度：P6 ｜ 标签：asyncio.subprocess、stdin、EOF、drain、死锁

**问**：用 `create_subprocess_exec("cat", stdin=PIPE, stdout=PIPE)` 喂了一段数据，`drain()` 也返回了，接着 `await proc.wait()` 却一直不返回，最后被外层超时杀掉。为什么 `cat` 收到了数据还不退出？`drain()` 是不是"数据已送达"的保证？什么时候必须 `stdin.close()`？

**答**：
结论：`cat` 的终止条件是 **stdin 上的 EOF**，不是"收到一行数据"。父进程不 `close()` 写端，管道就一直是打开的，`cat` 永远阻塞在 `read()` 上，`wait()` 自然等不到。`drain()` 只保证"写缓冲低于高水位"，即数据已被交给内核/传输层，**不表示对端已读完，更不表示对端会退出**。EOF 只能由写端关闭（或进程退出）产生。

取舍：a) 一次性投喂：`write` → `drain` → `stdin.close()` → `await proc.wait()`，顺序不能反；b) 交互式协议（需要边写边读）：先并发读 stdout/stderr，再按协议写，最后关 stdin，避免"父进程等子进程退出、子进程等父进程读缓冲腾空"的双向死锁；c) 大输出场景用 `proc.communicate(input=...)`，它内部同时处理读写与关闭，是标准库给出的安全封装。注意 `stdin.close()` 之后 `await stdin.wait_closed()` 才能确保 flush 完成，`drain()` 不能替代。

实战：事故形态是"批量调 `gzip -d` 解压流，父进程写完压缩数据就 `wait()`，子进程等 EOF，父进程等退出，worker 全部挂死，监控只看到 P99 飙到超时"。下面演示不关 stdin 时 `wait()` 挂住、关闭后立即返回，以及 `communicate()` 的一体化写法。

```python
import asyncio


async def main():
    proc = await asyncio.create_subprocess_exec(
        "cat",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
    )
    proc.stdin.write(b"hello\n")
    await proc.stdin.drain()
    print("[1] drain 返回，但 cat 仍在等 EOF")

    try:
        await asyncio.wait_for(proc.wait(), 0.3)
        print("[2] 不该到这里")
    except TimeoutError:
        print("[2] 不关 stdin -> wait() 挂住")

    proc.stdin.close()                 # 触发 EOF
    out = await proc.stdout.read()
    code = await proc.wait()
    print("[3] 关闭 stdin 后:", code, out)

    # 一体化写法：communicate 负责写入、关闭、并发读取
    proc2 = await asyncio.create_subprocess_exec(
        "cat",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
    )
    out2, _ = await proc2.communicate(b"batch\n")
    print("[4] communicate:", proc2.returncode, out2)


asyncio.run(main())
```

**追问一**：`stdin.close()` 之后还要 `await stdin.wait_closed()` 吗？—— 建议加。`close()` 触发 flush 与关闭，`wait_closed()` 等底层管道真正关闭；在 asyncio 里 `StreamWriter.close()` 是"请求关闭"，`wait_closed()` 才是"关闭完成"。如果不 `await`，紧接着的 `proc.wait()` 通常也能工作（顺序由事件循环保证），但在"关完立刻复用 fd/删除临时文件"的场景里，没等关闭完成会踩到 `ResourceWarning` 或 `EBADF`。

**追问二**：只关 stdin、不读 stdout，会不会也死锁？—— 会。子进程输出超过管道缓冲（Linux 默认 64KiB）后写阻塞，父进程在 `wait()` 等退出，双方互等。这就是经典的三管道死锁。解法是并发消费 stdout/stderr（`communicate`、或 `asyncio.gather(proc.stdout.read(), proc.stderr.read(), proc.wait())`），而不是"先写后等"。

## 背诵要点
- 子进程退出靠 stdin EOF，`drain()` 只保证写缓冲下降，不产生 EOF。
- 一次性投喂顺序：`write` → `drain` → `stdin.close()` → 读输出 → `wait()`。
- 不读 stdout/stderr 且输出超管道缓冲会死锁；`communicate()` 是安全封装。

## 复盘追问
- `cat` 收到数据却永不退出，如何从 EOF 语义解释？（写端未关）
- 子进程 + 三管道在什么条件下互相等待？（写满 stdin、读满 stdout、wait 退出）

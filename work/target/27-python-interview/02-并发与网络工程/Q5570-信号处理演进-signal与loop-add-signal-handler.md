---
title: [Q5570] 信号处理演进：signal.signal 与 loop.add_signal_handler
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5570 · 信号处理演进：signal.signal 与 loop.add_signal_handler

> 难度:★★★★ | 标签:版本演进, 信号, 优雅停机, asyncio

**问**：SIGTERM 到达时服务的"优雅停机"逻辑只跑了一半就断了。为什么 `signal.signal` 注册的处理函数在 asyncio 里跑在"主线程的任意字节码边界"？`loop.add_signal_handler` 的实现差异是什么？SIGTERM/SIGINT/SIGUSR1 的生产矩阵怎么配？

**答**：机制差异是根源：`signal.signal` 注册的处理函数由 **C 层信号中断触发**——信号到达时主线程在**任意两条字节码之间**被打断、跳去执行 Python handler，执行完再回来。三个坑：a) handler 与主线程代码并发执行（同一栈交错），共享状态在 handler 里看是"半更新"状态；b) handler 里做复杂操作（await、锁、日志重配置）会重入死锁或抛错被吞；c) **阻塞调用期间信号不投递**——GIL 持有的 C 调用（大计算、某些系统调用）会延迟处理直到返回，停机超时就是这么来的。`loop.add_signal_handler`（Unix only）走的是 **self-pipe/socketpair 模式**：signal handler 只写一个字节唤醒 epoll，真正的回调作为普通事件回调在**下一次事件循环迭代**里执行——与协程并发模型一致，可以安全操作 loop 资源、cancel 任务、清理连接。版本演进：signal.signal 是 POSIX 老机制，add_signal_handler 是 3.3 起 asyncio 标配（Windows ProactorEventLoop 不支持，见既有 Q5521），3.13+ 仍无跨平台方案——Windows 降级用 signal.signal + 只做"置标志位"最小动作。生产矩阵：**SIGTERM** = 优雅停机入口（stop accepting → drain → cleanup，超时上限 < K8s gracePeriod）；**SIGINT** = Ctrl-C 同 SIGTERM 但保留 traceback；**SIGUSR1** = 排障开关（dump 线程栈，faulthandler.register）；SIGKILL 不可捕获所以停机要在 gracePeriod 内完成。铁律：无论哪种注册方式，handler 里只做"置事件/取消任务"，重活放任务里。

```python
# file: code/02_并发与网络工程/q5570_signal_handler.py
import asyncio, signal, sys, os

async def graceful(stop_event):
    server = await asyncio.start_server(lambda r, w: None, "127.0.0.1", 0)
    print("服务启动:", server.sockets[0].getsockname())

    # loop.add_signal_handler: 回调在事件循环迭代里执行, 可安全操作 loop
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, lambda: stop_event.set())

    print("等待信号 (演示 0.1s 后自投 SIGTERM)")
    async def self_sigterm():
        await asyncio.sleep(0.1)
        os.kill(os.getpid(), signal.SIGTERM)
    asyncio.create_task(self_sigterm())

    await stop_event.wait()                 # 收到信号
    server.close()
    await server.wait_closed()              # 停止 accept -> drain 连接
    print("优雅停机: 连接排空 + 资源释放完成 (在事件循环里跑, 不是中断栈)")

asyncio.run(graceful(asyncio.Event()))

# 1) 降级: Windows / ProactorEventLoop 不支持 add_signal_handler
def fallback_signal():
    got = {"n": 0}
    def handler(signum, frame):     # 中断任意字节码边界, 只做最小动作
        got["n"] += 1               # 置标志位, 重活留给主循环轮询
    try:
        signal.signal(signal.SIGTERM, handler)
        os.kill(os.getpid(), signal.SIGTERM)
        import time; time.sleep(0.05)   # 等中断返回
        print("signal.signal 降级路径: handler 只置标志, n =", got["n"])
    finally:
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
fallback_signal()

# 2) 排障开关: SIGUSR1 dump 栈 (faulthandler)
import faulthandler
faulthandler.register(signal.SIGUSR1, file=sys.stderr) if sys.platform != "win32" else None
print("SIGUSR1 -> faulthandler dump 全部线程栈 (排障矩阵)")

# 3) 演示 handler 中断点的"半更新"视角 (示意, 不重复执行)
print("矩阵: SIGTERM=优雅停机(<gracePeriod) / SIGINT=同停机留traceback / SIGUSR1=dump栈 / SIGKILL=不可捕获")
```

**追问**：1) 为什么 handler 里的日志可能死锁？——logging 持有模块级锁，若主线程正持锁写日志时信号打断它，handler 再写日志就重入同一把非重入锁（threading.Lock）死锁；所以 handler 里用 `os.write(2, b'...')` 直写 fd 或干脆只置标志。2) 停机超时（gracePeriod 到了还没 drain 完）怎么办？——K8s 直接 SIGKILL，所以 drain 要有硬上限（gracePeriod-1s）后主动 `os._exit(0)`；在途请求的"未完成承诺"靠幂等键让客户端重试（跨到 03 类 Q6060）；停机指标要记录"drain 用时/被杀请求数"。3) self-pipe 模式自己能实现吗？——可以：`os.pipe()` 非阻塞写端放 handler、读端用 `loop.add_reader` 监听，asyncio 内部就是这么做的；理解它有助于在 select/kqueue 级自研循环里复刻同样语义。

## 背诵要点
- signal.signal 的 handler 在主线程任意字节码边界被中断执行：与主代码交错、易重入死锁、阻塞调用期间不投递；handler 只置标志。
- loop.add_signal_handler（Unix）走 self-pipe + epoll：回调在事件循环迭代里跑，可安全 cancel 任务/关 server；Windows 降级 signal.signal。
- 矩阵：SIGTERM 优雅停机（drain 上限=gracePeriod-1s 后 _exit）、SIGINT 留 traceback、SIGUSR1 faulthandler dump、SIGKILL 不可捕获。

## 复盘追问
- 你们的停机 handler 里跑了多少重活？有没有在 handler 里 await/加锁/写日志？（提示：对照"handler 只置标志"铁律审计；演练 drain 超时路径）
- SIGUSR1 这类排障开关上线了吗？K8s gracePeriod 与 drain 上限的差值是多少？（提示：补 faulthandler.register 与停机指标：drain 时长/被杀请求数）

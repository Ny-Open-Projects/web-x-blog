---
title: [Q849] 优雅停机与 SIGTERM 的应用侧行为
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q849 · 优雅停机与 SIGTERM 的应用侧行为

> 难度:★★★☆ | 标签:停机, 信号

**问**:容器收到 SIGTERM 后,uvicorn/Gunicorn 分别做什么?应用代码要配合什么?

**答**:uvicorn 收 SIGTERM:停止接受新连接 → 等待在途请求完成 → 执行 lifespan 关闭(释放连接池)→ 退出;SIGINT 行为更激进(中断在途)。Gunicorn master 把信号转发给 worker 并等排空(graceful_timeout 兜底)。应用代码配合三点:**lifespan/atexit 里释放资源**(连接池、消费线程)、后台任务要有退出检查点(shutting_down 标志)、不能假设进程永生——半完成的写操作要靠幂等与客户端重试兜底。

```python
# file: code/03_Web后端开发/q849_sigterm.py
import signal

def shutdown_plan(sig: int) -> str:
    if sig == signal.SIGTERM:
        return "停止 accept, 排空在途请求, 关闭 lifespan 资源"
    if sig == signal.SIGINT:
        return "快速退出, 中断在途请求"
    if sig == signal.SIGHUP:
        return "gunicorn 平滑重载 worker"
    return "未知信号"

print("SIGTERM:", shutdown_plan(signal.SIGTERM))
print("SIGINT:", shutdown_plan(signal.SIGINT))
```

**追问**:
- SIGKILL 之后还来得及清理吗?——来不及,这是不可捕获的兜底,所以 grace period 要足够长,KILL 只是最后手段。
- WebSocket 长连接怎么优雅停机?——先广播 close 帧给客户端触发主动迁移,再排空,超出宽限才硬断。

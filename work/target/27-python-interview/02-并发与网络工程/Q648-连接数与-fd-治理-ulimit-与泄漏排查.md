---
title: [Q648] 连接数与 fd 治理:ulimit 与泄漏排查
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q648 · 连接数与 fd 治理:ulimit 与泄漏排查

> 难度:★★★☆ | 标签:fd 泄漏, ulimit, 容量

**问**:服务跑久了报 Too many open files,怎么系统性地治理?

**答**:三层:1) 认知——每个 socket/文件/管道都占一个 fd,RLIMIT_NOFILE 限制进程上限(软限可自调至硬限,硬限需 root),ulimit -n 只影响当前 shell;2) 治本——fd 泄漏的常见来源:异常路径没 close、连接池没有最大上限、日志/临时文件句柄忘收、subprocess 管道没回收;用 lsof -p <pid> 统计 fd 类型分布,增长曲线定位泄漏点;3) 治标——调高软限到硬限、systemd LimitNOFILE、容器环境注意 dockerd 的默认限制。代码上用 contextmanager/with 管理一切可关闭资源,让异常路径也必然释放。

```python
# file: code/02_并发与网络工程/q648_fd_governance.py
import os
import resource
import socket


def count_fds() -> int:
    if os.path.isdir("/proc/self/fd"):
        return len(os.listdir("/proc/self/fd"))
    return len(os.listdir("/dev/fd"))  # macOS


def show_rlimit() -> tuple:
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print(f"RLIMIT_NOFILE: soft={soft} hard={hard}")
    return soft, hard


if __name__ == "__main__":
    soft, hard = show_rlimit()
    # 尝试把软限提到硬限 (无需 root)
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        print(f"软限已提升至硬限: {resource.getrlimit(resource.RLIMIT_NOFILE)[0]}")
        resource.setrlimit(resource.RLIMIT_NOFILE, (soft, hard))  # 恢复
    except (ValueError, PermissionError) as e:
        print(f"提升受限: {e!r}")

    base = count_fds()
    print(f"当前 fd 数: {base}")

    # 泄漏演示: 200 个 socket 不关闭
    leaked = [socket.socket() for _ in range(200)]
    after_leak = count_fds()
    print(f"打开 200 个 socket 后: {after_leak} (+{after_leak - base})")

    # 正确姿势: 上下文管理器保证释放
    with socket.socket() as auto_closed:
        during = count_fds()
    after_close = count_fds()
    print(f"with 语句期间 {during}, 退出后 {after_close} (自动回收)")

    for s in leaked:
        s.close()
    print(f"手动关闭泄漏 socket 后: {count_fds()}")
    assert count_fds() <= base + 2
```

**追问**:1) 线上怎么快速确认是 fd 泄漏还是容量不足?——观察 fd 数随时间是否单调增长(泄漏)还是稳定在高位波动(容量不足);lsof 分类统计里某类 fd(如 socket 到同一远端)持续增长即泄漏源。2) fd 泄漏的高频代码模式有哪些?——异常路径没 close(不用 with/contextmanager)、连接池无上限、每请求新建 SSLContext/socket 对象、subprocess 管道读完没收、FileHandler 反复创建、TLS wrap 失败没关底层 socket(Q630)。3) 排查工具链怎么组合?——ls /proc/<pid>/fd | wc -l 看增长曲线(单调增长=泄漏,高位波动=容量不足);lsof -p 按 symlink target 分类统计,某类(如到同一远端的 socket)持续增长即泄漏源;配合 py-spy/rpdb 找到创建点。4) 生产陷阱?——容器环境的 ulimit 继承 dockerd 语义,调了 systemd 不生效;调高 RLIMIT_NOFILE 只是延后崩溃,泄漏必须修代码;改了 ulimit 没重启进程(只影响设置之后的新进程)。

---

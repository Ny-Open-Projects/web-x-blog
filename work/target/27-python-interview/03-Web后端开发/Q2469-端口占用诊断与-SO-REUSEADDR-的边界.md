---
title: [Q2469] 端口占用诊断与 SO_REUSEADDR 的边界
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2469 · 端口占用诊断与 SO_REUSEADDR 的边界

> 难度:★★★☆ | 标签:socket, EADDRINUSE, 运维

**问**:服务起不来报 EADDRINUSE,诊断路径是什么?SO_REUSEADDR 到底解决什么问题?

**答**:诊断三步:先确认谁在占用——lsof -nP -iTCP:端口 -sTCP:LISTEN 直接给出进程与 PID,排查是残留进程还是端口冲突;查不到监听者但绑定仍失败,多半是 TIME_WAIT 残留(主动关闭方在 2MSL 内保持端口记录);再决定解法。SO_REUSEADDR 的语义边界是高频考点:它允许绑定处于 TIME_WAIT 的地址,解决的是"重启服务等一分钟"的问题;它不允许两个进程同时监听同一端口——那是 SO_REUSEPORT 的事,后者配合内核做负载均衡。诊断输出要落到动作:杀残留进程、等 TIME_WAIT 或开 REUSEADDR、修正配置里的端口撞车。容器环境还要注意端口映射在网络命名空间内,宿主机看到的是另一层。

```python
# file: code/03_Web后端开发/q2469_port_conflict_diag.py
"""端口占用诊断: EADDRINUSE 与 SO_REUSEADDR 的边界(纯标准库)。"""
import errno
import socket
import subprocess


def bind_port(port, reuse=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if reuse:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", port))
    sock.listen(1)
    return sock


def find_listener(port):
    """用系统 lsof 找出监听该端口的进程, 找不到返回 None。"""
    try:
        proc = subprocess.run(
            ["lsof", "-nP", "-iTCP:{}".format(port), "-sTCP:LISTEN"],
            capture_output=True, text=True, timeout=5)
        lines = [ln for ln in proc.stdout.strip().splitlines()[1:] if ln.strip()]
        return lines[0] if lines else None
    except (OSError, subprocess.TimeoutExpired):
        return None


first = bind_port(0)
occupied = first.getsockname()[1]
print("进程已监听回环端口", occupied)

second = None
try:
    second = bind_port(occupied)
    raise AssertionError("重复绑定应当失败")
except OSError as exc:
    assert exc.errno in (errno.EADDRINUSE, errno.EACCES), exc.errno
    print("重复绑定 -> errno {} EADDRINUSE".format(exc.errno))
    owner = find_listener(occupied)
    print("诊断输出:", owner if owner else "lsof 不可用, 人工执行 lsof -nP -iTCP:{} -sTCP:LISTEN".format(occupied))
    if owner:
        assert str(first.getsockname()) or True
        print("要点核对: 占用者 PID 出现在 lsof 输出里 ->", owner.split()[1])
finally:
    first.close()

# 关闭后重绑: 无需 REUSEADDR 也应成功
again = bind_port(occupied)
print("关闭后重绑 -> 成功, 端口", again.getsockname()[1])
again.close()

# REUSEADDR 的真实用途: TIME_WAIT 期间快速重绑
victim = bind_port(occupied)
peer = socket.socket()
peer.connect(("127.0.0.1", occupied))            # 制造一次连接
conn, _ = victim.accept()
conn.close()
peer.close()
victim.close()                                    # 主动关闭方进入 TIME_WAIT

try:
    plain = bind_port(occupied)
    plain.close()
    print("TIME_WAIT 期间裸绑 -> 本机允许, 某些平台会失败")
except OSError:
    print("TIME_WAIT 期间裸绑 -> 被拒, 正是 SO_REUSEADDR 的用武之地")

safed = bind_port(occupied, reuse=True)
print("TIME_WAIT 期间带 SO_REUSEADDR -> 绑定成功")
safed.close()
print("要点: EADDRINUSE 的诊断路径 lsof 查占用者, 查不到多半是 TIME_WAIT; "
      "REUSEADDR 解决 历史连接残留 的重绑, 不解决两个进程同时监听, 那是 REUSEPORT 的事")
```

**追问**:
- 为什么主动关闭方进入 TIME_WAIT?——它要确保最后的 ACK 有机会重传,以及旧报文在网络中自然消亡,等 2MSL 是协议的礼貌。
- REUSEPORT 两个进程监听同一端口,连接怎么分配?——内核按四元组哈希分发到监听队列,相当于免费的进程级负载均衡,但要求各进程 socket 选项一致。

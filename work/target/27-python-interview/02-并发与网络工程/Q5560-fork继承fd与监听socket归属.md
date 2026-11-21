---
title: [Q5560] fork 继承 fd 与监听 socket 的归属规则
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5560 · fork 继承 fd 与监听 socket 的归属规则

> 难度:★★★★ | 标签:fork, fd 继承, close_fds, pass_fds, 原理机制

**问**：一个服务 fork 子进程跑外部工具后，偶发"父进程 accept 收不到连接"。fd 在 fork 时的继承规则是什么？`subprocess` 的 close_fds/pass_fds 在管什么？"监听 socket 归谁"的协议应该怎么定？

**答**：fork 复制整个进程时**fd 表也被复制**——子进程拿到所有 fd 的副本，指向同一批内核打开文件描述。两个后果：a) 每多一个持有者，对端的连接/管道就多一份"还开着"的证据，`read` 到 EOF 的语义被拖延（谁没关，谁就在拖）；b) 监听 socket 被多个进程同时 accept 时，内核会**抢占式分配**连接（预 accept 模型），某进程只 close 了部分 fd 或处理慢，就出现"连接被错误的进程吃掉"——本案例的根因。规则层：Python 3.4 起 fd 默认**不可继承**（PEP 446，`O_CLOEXEC`），`subprocess.run` 默认 `close_fds=True` 只留 0/1/2，需要传给子进程的 fd 必须显式 `pass_fds`；`socket`/`file` 对象的 `inheritable`/`cloexec` 属性控制 fork/exec 行为。监听 socket 归属协议只有两种正确形态：**单 accept 方**（父进程或专职进程 accept 后把已建立连接发给 worker，或 worker 显式 close 监听 fd），或**有意共享 + SO_REUSEPORT**（每 worker 独立 bind，内核分桶，见 Q5507）——"fork 时顺手继承"这种偶然共享必须消灭：fork 前列 `os.listdir("/proc/self/fd")` 审计，fork 后子进程立即关闭所有非职责 fd。

```python
# file: code/02_并发与网络工程/q5560_fd_inherit.py
import os, sys, subprocess

r, w = os.pipe()
print("父进程 fd 可继承性:", os.get_inheritable(r), os.get_inheritable(w))  # PEP 446 默认 False

# 1) subprocess 默认 close_fds=True: 子进程只留 0/1/2
# 子进程用 F_GETFD 自查: 无 pass_fds 时 fd 不可用(CLOEXEC/fd 不存在)
code = (
    "import os, fcntl, sys\n"
    f"try:\n"
    f"    fcntl.fcntl({w}, fcntl.F_GETFD)\n"
    "    sys.exit(0)\n"
    "except OSError:\n"
    "    sys.exit(3)"
)
p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True)
print("默认(不传)子进程拿不到 pipe fd:", p.returncode == 3)

# 2) pass_fds 显式放行: 子进程拿到 fd 副本并可用
code2 = f"import os; os.write({w}, b'child-ok')"
p2 = subprocess.run([sys.executable, "-I", "-c", code2], pass_fds=(w,), capture_output=True)
os.close(w)
print("pass_fds 后父进程读到:", os.read(r, 16))
os.close(r)

# 3) 归属协议审计: fork 前列出职责外的 fd, 子进程立即关闭
print("fork 前审计: os.listdir('/proc/self/fd') 对比职责清单, 多余的在子进程入口统一 close")
print("规则: 监听 socket 只允许两种形态 -> 单 accept 方, 或 SO_REUSEPORT 每 worker 独立 bind")
```

**追问**：1) `O_CLOEXEC` 只管 exec，不管 fork——那 fork 出的子进程（不 exec）还是持有全部 fd，怎么办？——对，multiprocessing fork 模式下子进程继承一切，靠 `multiprocessing` 内部清理 + 自己在 worker 入口显式 close；这就是 forkserver/forkserver 模式更干净的原因之一（子进程从干净快照启动）。2) "父进程 accept 收不到连接"怎么用工具实锤？——`ss -tlnp` 看监听 fd 被几个进程持有；`/proc/<pid>/fd` 对比各进程 fd 表；strace 看 accept 分布在被哪个 pid 抢走。3) 子进程持有监听 fd 但从不 accept，有什么隐性伤害？——它会拖住 listen 队列的引用（不影响 accept 本身），但它崩溃/退出时可能触发连接状态异常；更重要的是这个 fd 在子进程里是完全未审计的攻击面。

## 背诵要点
- fork 复制 fd 表：共享内核打开文件描述，未关闭的持有者拖延 EOF；多进程抢 accept 会"连接被错误进程吃掉"。
- PEP 446：Python 3.4+ fd 默认不可继承（O_CLOEXEC 管 exec 不管 fork）；subprocess 默认 `close_fds=True`，要传就显式 `pass_fds`。
- 监听 socket 只许两种形态：单 accept 方，或 SO_REUSEPORT 每 worker 独立 bind；fork 前审计 `/proc/self/fd`，fork 后子进程立即关职责外 fd。

## 复盘追问
- 你们 fork/multiprocessing 的子进程入口，有没有统一的"fd 职责清单关闭"步骤？（提示：抽一个 initializer/入口函数，按职责白名单关 fd 并打日志）
- "accept 被抢"这类事故在压测里怎么提前暴露？（提示：多进程 accept 分布监控——按 pid 统计 accept 次数，偏差大即形态不对）

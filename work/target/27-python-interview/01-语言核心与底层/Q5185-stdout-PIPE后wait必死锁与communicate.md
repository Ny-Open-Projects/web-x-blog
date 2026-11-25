---
title: "[Q5185] stdout=PIPE 后 wait() 必死锁：管道背压与 communicate"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5185 · stdout=PIPE 后 wait() 必死锁：管道背压与 communicate

难度：P6 ｜ 标签：subprocess、PIPE、死锁、communicate、僵尸进程

**问**：`p = subprocess.Popen(cmd, stdout=subprocess.PIPE)` 之后调 `p.wait()`，为什么输出一多就 100% 卡死？管道缓冲区到底多大？`communicate()` 凭什么不会死锁？子进程超时后 `kill()` 一下就算收尾了吗？

**答**：
结论：管道是有容量上限的内核缓冲区（本机实测 64KiB），子进程写满之后 write 阻塞；父进程在 `wait()` 里只等"进程退出"、并不读管道，双方互等，谁也不会前进。这正是典型的管道背压死锁。`communicate()` 用 selector/线程同时读 stdout 和 stderr、读完再 wait，所以能把背压消化掉。`kill()` 只发 SIGKILL，既不回收僵尸、也不排空管道——必须再 `communicate()`（或 `wait()` + 手动读完），否则 fd 泄漏、僵尸残留。

取舍：抓输出最省心的写法就是 `subprocess.run(..., capture_output=True, timeout=...)`，超时抛 `TimeoutExpired` 后内部已经 kill + 收尸。明确不需要输出时，干脆不设 PIPE（继承父进程 stdout，或重定向到文件），既不会死锁也省内存。要边跑边处理（流式日志）就得自己起线程读，不能用 wait。

实战：事故形态是"部署脚本里 `Popen(kubectl logs ...)` 再 `wait()`，本地几十行日志没事，线上几千行直接挂到 job 超时"。下面同时演示三件事：只 wait 不读必然超时、kill 后 communicate 能拿到已写入的 64KiB、communicate 一次跑完 4MB；最后一行说明 `returncode` 在 wait 之前是 None（不能拿它判断完成）。

```python
import subprocess
import sys
import time

BIG = "import sys; sys.stdout.buffer.write(b'x' * 4_000_000); sys.stdout.flush()"

p = subprocess.Popen([sys.executable, "-c", BIG], stdout=subprocess.PIPE)
t0 = time.perf_counter()
try:
    p.wait(timeout=2)  # 只等不读：子进程写满管道后阻塞，父进程永远等不到退出
    print("没有死锁？")
except subprocess.TimeoutExpired:
    print(f"wait() 2 秒超时（子进程卡在写管道）pid={p.pid}")

p.kill()
out, _ = p.communicate()  # kill 后仍然要收尸 + 排空管道
print("kill+communicate 收尾:", len(out), "字节")

t0 = time.perf_counter()
r = subprocess.run([sys.executable, "-c", BIG], capture_output=True)
print("communicate 一次搞定:", len(r.stdout), "字节,", round(time.perf_counter() - t0, 2), "秒")

z = subprocess.Popen([sys.executable, "-c", "import sys; sys.exit(3)"])
print("未 wait 的 returncode:", z.returncode)
z.wait()
print("wait 之后:", z.returncode, "| 已回收:", z.poll() is not None)
```

**追问一**：为什么 kill 之后还要 communicate？—— 两件事没做：a) 子进程变成僵尸，要 `wait()` 才回收；b) 管道里还有已写入但未读的字节（本例 65536），不排空就丢数据、fd 也不释放。`communicate()` 一次把读 + wait 都做了，所以"kill 之后统一 communicate"是最省心的收尾模板。

**追问二**：只把 stderr 重定向到 PIPE 也会死锁吗？—— 会。任何被 PIPE 的流都受同一个容量限制，而 stderr 往往是日志大户（traceback、progress bar），比 stdout 更容易写满。一个常见误区是"我只抓 stderr 不抓 stdout 就不会死锁"——恰恰相反，未 capture 的那一路直接继承父进程 fd，反而安全。

## 背诵要点
- `wait()` 不读管道；子进程写满 64KiB 管道即阻塞，父子互等 → 死锁。
- `communicate(timeout=...)` 同时排空 stdout/stderr 并 wait，是唯一安全模板；超时后 kill 也必须再 communicate 收尸。
- kill 只发信号：僵尸要 wait、管道要排空；`returncode` 在 wait 前是 None。

## 复盘追问
- `Popen(stdout=PIPE).wait()` 在大输出下必挂，画出两端的阻塞点并给出两种修法。（管道容量、父不读、communicate/不 capture）
- kill 之后还漏了什么，为什么必须 communicate？（僵尸回收、管道残留、fd 释放）

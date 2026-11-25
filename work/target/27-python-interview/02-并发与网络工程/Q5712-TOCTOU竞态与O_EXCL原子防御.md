---
title: "[Q5712] TOCTOU：exists 后 open 的竞态窗口与 O_EXCL 原子防御"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5712 · TOCTOU：exists 后 open 的竞态窗口与 O_EXCL 原子防御

难度：P6 ｜ 标签：TOCTOU、竞态、O_EXCL、os.open、符号链接、原子性

**问**：`if not os.path.exists(p): open(p, 'w')` 为什么是竞态？两个进程同时走这段代码会发生什么？`O_CREAT|O_EXCL` 为什么能根治"只该建一次"的场景？符号链接让 TOCTOU 危害升级到什么程度，防御姿势是什么？

**答**：
结论：TOCTOU（Time-Of-Check To-Time-Of-Use）= "检查"与"使用"之间存在**窗口**，窗口内另一个执行体可以改变文件系统状态：两个进程都看到"不存在"，都进入创建分支，后者覆盖前者；或者更糟——检查时的普通文件在打开瞬间被替换成指向 /etc/passwd 的符号链接，你以高权限进程的身份写了别人的文件。根治原则：**检查与使用合并成一个原子操作**——创建用 `os.open(path, O_CREAT|O_EXCL|O_WRONLY)`（存在即 FileExistsError，不存在才创建，内核单步完成）；独占锁用 `flock`（打开即锁）；替换用 `os.replace`（原子 rename）；"打开自己刚校验过的文件"用 `os.open` 拿 fd 再 `os.fdopen`，全程对着**同一个 fd**操作，而不是对路径二次解析。凡是"先 lstat 看一眼再 open"的写法，都在把内核当单线程用。

取舍：a) 幂等创建（锁文件、临时目录占位）：O_EXCL + 捕获 FileExistsError，重试或退出；b) 需要覆盖写（配置文件）：直接 open('w') 无所谓竞态（语义就是覆盖）或写临时文件 + os.replace 原子发布（Q380/Q5190）；c) 高权限服务处理外部可控路径：禁用"路径→校验→open"两段式，改为 open fd → fstat 校验类型/属主 → 对 fd 操作，彻底绕开路径被换的可能性；d) `os.path.exists` 的返回值仅供"乐观快速路径"，任何**安全决策**不能建立在其结果上；e) 多进程写同一日志不是 O_EXCL 场景，是 O_APPEND 场景（Q5717），先分清"创建互斥"与"追加互斥"两类竞态。

实战：事故形态是"定时任务用 exists 判断单实例锁文件，两台机器 NFS 共享目录时钟偏移，双实例同时通过检查、同时写库造成幂等键冲突告警；修复为 O_EXCL 创建 + 陈旧锁按 pid 存活判定接管（Q1612 的单实例方案）"。下面验证窗口竞态与原子防御。

```python
import os
import tempfile
import threading
import time

d = tempfile.mkdtemp()
p = os.path.join(d, "lock")


def racy_create(tag, result):
    if not os.path.exists(p):
        time.sleep(0.002)  # 人为放大检查-使用之间的窗口
        try:
            fd = os.open(p, os.O_CREAT | os.O_WRONLY)  # 没有 O_EXCL: 覆盖创建
            os.write(fd, tag.encode())
            os.close(fd)
            result.append(f"{tag}:created(覆盖)")
        except OSError as e:
            result.append(f"{tag}:{e.errno}")
    else:
        result.append(f"{tag}:existed")


def atomic_create(tag, result):
    try:
        fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, tag.encode())
        os.close(fd)
        result.append(f"{tag}:created")
    except FileExistsError:
        result.append(f"{tag}:exists(原子拒绝)")


r1, r2 = [], []
t1 = threading.Thread(target=racy_create, args=("A", r1))
t2 = threading.Thread(target=racy_create, args=("B", r2))
t1.start(); t2.start(); t1.join(); t2.join()
print("[1] 无 O_EXCL 竞态结果:", r1 + r2, "——双方都可能'创建成功'且后者覆盖")

os.unlink(p)
a1, a2 = [], []
t1 = threading.Thread(target=atomic_create, args=("A", a1))
t2 = threading.Thread(target=atomic_create, args=("B", a2))
t1.start(); t2.start(); t1.join(); t2.join()
print("[2] O_EXCL 原子创建:", a1 + a2, "——只有一方 created")

# 符号链接: lstat 校验与打开之间被换链的防御 = 对 fd 校验
real = os.path.join(d, "real.txt")
with open(real, "w") as f:
    f.write("safe")
fd = os.open(real, os.O_RDONLY)
st = os.fstat(fd)
print("[3] 对 fd 做 fstat 校验(非路径):", os.path.basename(real), st.st_size, "字节——路径可被换, fd 不会")
os.close(fd)
```

**追问一**：为什么 `os.path.exists` 返回 True 之后就 open 还是可能 FileNotFoundError？—— 检查与打开之间文件被删（另一进程的临时文件清理、GC 型清理任务），这正是 TOCTOU 的另一种方向："有变无"。防御不是"再查一次"，而是把异常当正常路径：open 直接裸调，`FileNotFoundError`/`FileExistsError` 作为**预期分支**处理（EAFP），检查类操作只用于优化用户体验（提前给出友好提示），不承担正确性。

**追问二**：符号链接攻击的完整链路是什么样？—— 高权限服务以 root 身份处理 `/tmp/work/result`：先 lstat 确认是普通文件、属主正确，然后 open 写入。攻击者在 lstat 与 open 的窗口里把 `result` 替换成指向 `/etc/shadow` 的符号链接——lstat 看到的是旧文件（校验通过），open 跟随新链接写入了系统文件。防御三选一：①对**不可信目录**（/tmp）根本不做路径操作，工作文件放私有目录（0700）；②`os.open` 打开后 `os.fstat` 校验（对 fd 校验，链接无从作祟），Linux 还可加 `O_NOFOLLOW` 让 open 遇符号链接直接失败；③整个目录用受控的 mkdtemp（0700，Q2101）。原则：权限敏感的文件操作，校验对象必须是 fd，永远不能是可被第三方替换的路径。

## 背诵要点
- TOCTOU = 检查与使用之间的窗口；exists 只能做乐观快速路径，不承担安全/正确性决策。
- 原子化合并：O_CREAT|O_EXCL 管创建互斥、flock 管互斥锁、os.replace 管原子替换；错误当正常分支（EAFP）。
- 不可信路径的安全操作对 fd 做 fstat 校验（O_NOFOLLOW），绝不对"刚看过的路径"二次解析。

## 复盘追问
- 双实例同时通过 exists 检查，为什么？怎么根治？（窗口竞态；O_EXCL 原子创建）
- 高权限服务写 /tmp 下文件为什么危险？（符号链接替换窗口；open fd + fstat/O_NOFOLLOW）

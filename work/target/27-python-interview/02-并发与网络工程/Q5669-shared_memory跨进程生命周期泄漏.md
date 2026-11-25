---
title: "[Q5669] shared_memory 跨进程生命周期泄漏"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5669 · shared_memory 跨进程生命周期泄漏

难度：P7 ｜ 标签：shared_memory、/dev/shm、resource_tracker、生命周期、零拷贝

**问**：`multiprocessing.shared_memory.SharedMemory` 的 `close()` 和 `unlink()` 到底分别释放什么？为什么"子进程 close 了、父进程还用着"是安全的，而"某个进程只 close 不 unlink"会让 `/dev/shm` 里的段残留？`resource_tracker` 在什么时候会打印 `leaked shared_memory` 警告、为什么它经常是误报？进程被 SIGKILL 后共享内存段谁来回收？

**答**：
结论：`close()` 只断开**当前进程**对该段的 `mmap` 映射（释放本进程的地址空间与 fd），不删除内核里的共享内存对象；`unlink()` 才删除**名字**（在 POSIX 上是 `/dev/shm/psm_xxx` 文件），使新进程无法再 attach，已有映射仍可用直到各自 `close()`。因此正确协议是"**所有使用者各自 close，由唯一的所有者负责 unlink**"——通常创建者或父进程当所有者。泄漏有两种：① **名字泄漏**——最后一个使用者没调 `unlink()`，段留在 `/dev/shm` 直到重启（占内存、占文件名）；② **映射泄漏**——进程反复 attach 却忘记 close，fd 与虚拟地址耗尽。`resource_tracker` 是 `multiprocessing` 的辅助进程，注册每个 SharedMemory 名字，父进程退出时检查"还有谁注册着"并打印 `leaked shared_memory objects` 警告——但它在**子进程被 SIGKILL、来不及向 tracker 注销**时会误报（段其实已被内核回收或仍被父进程合法持有），所以警告要结合 `ls /dev/shm` 看名字是否真残留，不能见警告就删。SIGKILL 后若段还有其它映射，内核保留对象直到最后一个映射关闭；若名字还在但无映射，则成为孤儿段，需手动 `SharedMemory(name=...).unlink()` 清理。

取舍：跨进程共享大对象时要明确"所有权模型"——谁创建、谁持有、谁在何时 unlink，最好用上下文管理器把"attach → 用 → close"包起来，并由父进程在 `finally` 里统一 unlink；不要依赖 GC 自动回收（CPython 的 `SharedMemory.__del__` 只 close 不 unlink，正是为了避免误删别人的段）。对" worker 可能被强杀"的场景，要在父进程维护名字清单，启动时扫描 `/dev/shm` 清理上次崩溃的残留（按命名前缀区分自己的段）。

实战：事故形态是"批处理跑完后 /dev/shm 被撑满、后续任务创建 SharedMemory 失败"，或"日志里刷 leaked shared_memory 警告但 /dev/shm 看似正常"——前者查 unlink 归属，后者查是否 SIGKILL 误报。下面跑出完整生命周期：创建 → attach 读取 → close 后仍可重开 → unlink 后 attach 失败。

```python
from multiprocessing import shared_memory
import os

# 1) 创建并写入
shm = shared_memory.SharedMemory(create=True, size=1024)
name = shm.name
shm.buf[:12] = b"hello-shared"
print("created:", name, "size:", shm.size)

# 2) 另一进程（此处同进程示意）attach 读取
peer = shared_memory.SharedMemory(name=name)
print("peer read:", bytes(peer.buf[:12]))
peer.close()                       # 使用者：只 close

# 3) 创建者 close 后，名字仍在 -> 可重新 attach
shm.close()
reopened = shared_memory.SharedMemory(name=name)
print("after close, reopen OK:", bytes(reopened.buf[:12]))
reopened.close()

# 4) unlink 删除名字 -> 之后 attach 失败（孤儿段清理的正确做法）
shm.unlink()
try:
    shared_memory.SharedMemory(name=name)
except FileNotFoundError:
    print("after unlink: FileNotFoundError (名字已删除)")

# 5) 容量视角：/dev/shm 上的残留文件
print("shm path prefix: /dev/shm/" + name, "exists after unlink:",
      os.path.exists("/dev/shm/" + name))
```

**追问一**：为什么 `SharedMemory.__del__` 只 close 不 unlink？——因为一个对象被 GC 时，无法知道"是否还有别的进程正 attach 在这个名字上"，贸然 unlink 会让正在使用的进程后续 attach 失败、破坏共享契约；名字的删除权必须交给明确的所有者。代价是"忘记 unlink"会成为孤儿段——这用显式所有权协议与启动清理来补，而不是靠 GC。

**追问二**：`resource_tracker` 警告什么情况下是真泄漏、什么情况下是误报？——真泄漏：段确实由本应负责的进程创建且没人 unlink，`ls /dev/shm/<name>` 能看到文件且无进程在用；误报：worker 被 SIGKILL 没来得及从 tracker 注销，或段被 fork 继承导致 tracker 状态与实际持有者不一致，此时名字可能已被父进程合法持有或内核已回收。判断依据是"名字是否真实残留在 /dev/shm 且无人使用"，而不是警告本身——先确认再清理，避免误删在用的段。

## 背诵要点
- `close()` 断本进程映射、`unlink()` 删名字（/dev/shm 对象）；协议是"各自 close，唯一所有者 unlink"。
- 泄漏两类：名字残留（没人 unlink）/ 映射与 fd 泄漏（attach 不 close）；`__del__` 只 close 不 unlink。
- resource_tracker 警告可能是 SIGKILL 误报，先 `ls /dev/shm` 确认再清理；强杀场景父进程维护名字清单做启动清理。

## 复盘追问
- 批处理跑完 /dev/shm 被撑满导致后续任务创建失败，如何用所有权模型定位并修复？（明确 unlink 所有者、上下文管理器、启动清理残留，讨论 __del__ 为何不 unlink）
- 日志刷 `leaked shared_memory` 但 /dev/shm 看似正常，如何判断真泄漏还是 SIGKILL 误报？（查名字实际残留与持有进程，讨论误删在用段的风险）

---
title: [Q5509] shared_memory 生命周期陷阱与孤儿块泄漏排查
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5509 · shared_memory 生命周期陷阱与孤儿块泄漏排查

> 难度:★★★ | 标签:shared_memory, 泄漏排查, multiprocessing

**问**：`multiprocessing.shared_memory` 在什么情况下会变成「孤儿块」泄漏到重启？`close`/`unlink`/resource_tracker 三者的关系怎么理清？子进程崩溃后怎么找出并清理孤儿块？3.13 的 track 参数改变了什么默认行为？

**答**：结论：生命周期铁律是「**所有使用者 close，最后一个使用者 unlink**」——但真实事故都出在违反它的路径上：1) **进程崩溃没走 finally**：unlink 永远没人调，块挂在 `/dev/shm` 直到重启或手动清；2) **谁先 unlink 的竞态**：使用者 A unlink 后 B 还在访问，B 读到已释放段（SIGBUS/段错误式崩溃）；3) **resource_tracker 的误报与真报**：CPython 给每个 SharedMemory 注册跟踪，子进程退出时对「自己 attach 过但没 close」的块报 `leaked shared_memory objects` 警告——注意 tracker 只在**自己进程视角**工作，创建者进程崩了 tracker 也死了，没人管孤儿。排查路径：`ls /dev/shm` 看名字（默认前缀 `psm_`/`wnsm_`），`/proc/<pid>/maps` 找谁还映射着；清理用 `ipcrm` 或直接 unlink 文件（确认无进程映射后）。3.13 的变化：`SharedMemory(track=False)` 允许跳过 tracker 注册——配合「创建者主动管理、worker 只用不 track」的模式消除误报警告；同时 `resource_tracker` 对共享内存从「警告即泄漏」改为更精确的所有权模型（创建者 track、使用者不 track）。取舍：track=False 是双刃剑——少了 tracker 兜底，漏 unlink 无人提醒，必须自己有创建侧的注册表（记录块名与 TTL）。实战规范：块名带业务前缀与时间戳，启动时扫描清理超龄孤儿块（自愈脚本），比依赖 tracker 可靠。

```python
# 基线:Python 3.9+(3.13 起支持 track=False)。Linux/macOS 运行;/dev/shm 查看孤儿。
import multiprocessing.shared_memory as shm
import os, sys

def create_with_owner_pattern() -> str:
    # 创建者:track=True(3.13 默认),登记块名,负责最终 unlink
    block = shm.SharedMemory(create=True, size=1024, name=None)
    block.buf[:4] = b"DEMO"
    return block.name, block            # 返回供清理;真实代码注册进本地注册表

name, owner_block = create_with_owner_pattern()
print("created:", name, "-> /dev/shm/", name)

# 使用者(模拟另一进程视角):只 attach + close,不 unlink
user = shm.SharedMemory(name=name)      # attach 已存在的块
print("user sees:", bytes(user.buf[:4]))
user.close()                            # 使用者只 close

owner_block.close()
owner_block.unlink()                    # 创建者确认无人使用后释放
print("unlinked; ls /dev/shm 应已无该块")

# 3.13+:track=False 演示(仅 3.13 可用)
if sys.version_info >= (3, 13):
    anon = shm.SharedMemory(create=True, size=64, track=False)
    print("3.13 track=False: tracker 不再注册,泄漏需创建侧自管")
    anon.close(); anon.unlink()

if os.name == "posix":
    print("排查孤儿: ls /dev/shm | grep psm_ ;清理前确认无进程映射(/proc/*/maps)")
```

**追问**：
1) 子进程访问已 unlink 的块会怎样？——unlink 删的是名字，只要还有进程映射着，内存还在（引用语义类似文件）；但新 attach 会失败。危险的是「close 后 buf 的 memoryview 还活着」——访问已 close 的段是未定义行为（读零或段错误），所以要保证 memoryview 生命周期 < SharedMemory 生命周期。
2) 为什么 multiprocessing.Queue 传 SharedMemory 对象会出泄漏误报？——通过 Queue pickle 传递时，接收端进程 attach 后若忘记 close，退出时 tracker 报泄漏；3.13 的 track=False + 显式管理就是为此。规范是「传块名（str），接收方自己 attach/close」而不是传对象。
3) 服务长跑怎么防孤儿？——三件套：块名带 TTL 时间戳、启动与定时任务扫描 `/dev/shm` 超龄块、创建侧用 try/finally + 崩溃兜底（atexit 不保证执行，所以靠扫描自愈）；监控上把 /dev/shm 使用率当容量指标告警。

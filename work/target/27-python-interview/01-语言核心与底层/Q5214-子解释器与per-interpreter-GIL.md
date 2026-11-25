---
title: "[Q5214] 子解释器与 per-interpreter GIL：隔离了什么，共享了什么"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5214 · 子解释器与 per-interpreter GIL：隔离了什么，共享了什么

难度：P7 ｜ 标签：子解释器、PEP684、PEP554、GIL、隔离模型、mod_wsgi

**问**：同一进程里可以跑多个 Python 解释器吗？子解释器和多进程隔离的差异是什么？PEP 684 给每个子解释器独立 GIL 后，能像线程一样共享对象吗？mod_wsgi/嵌入式场景里的子解释器踩过什么坑？

**答**：
结论：同一进程可以创建多个子解释器（`_interpreters` 模块 3.13 才有稳定公开 API，3.12 及之前只能经 C-API `Py_NewInterpreter` 或等实验模块使用；`InterpreterPoolExecutor` 同为 3.13+）。隔离模型是**同一进程 + 各自独立的模块字典、内建表、GIL（3.12+ 经 PEP 684 按解释器分配）**；但**底层内存分配器、进程级资源（fd、信号处置、文件系统、环境变量）共享**。与多进程比：省了 fork/spawn 的启动与序列化成本、可传 cross-interpreter 数据通道（buffer 协议字节），但隔离强度低一档——C 扩展的全局状态、非线程安全库在解释器间照样互踩。与多线程比：对象默认不共享（各自模块表），跨解释器传对象要显式走通道或 pickle，绕开了"GIL 下共享 dict 竞态"那一层。

取舍：a) CPU 密集并行要真收益：3.12 子解释器可用但生态不成（扩展未适配 per-interpreter GIL 的都隐式共享全局 GIL 锁），生产上仍优先多进程；b) 嵌入式宿主（mod_wsgi 多应用隔离、插件沙箱）子解释器是标准手段——省内存、启动快，代价是要求所有 C 扩展声明 `Py_mod_multiple_interpreters` 兼容；c) 全局不可变资源（字符驻留表、 immortal 对象、某些缓存）跨解释器共享，这是性能红利也是状态泄漏点；d) fd/信号/chdir 是进程级：一个解释器里改 cwd、装信号 handler，另一个解释器看得见——"隔离"的边界要背下来；e) 等生态：业务代码用子解释器并行的时机看 3.13/3.14 的 `InterpreterPoolExecutor` + 常用扩展的兼容声明，写法上先用进程池占位。

实战：事故形态是"嵌入宿主用两个子解释器跑两套插件，插件 A 的 C 扩展（内部静态全局缓冲区）与插件 B 并发调用时数据互串；排查发现该扩展未声明解释器兼容，宿主降级为 A/B 分进程承载"。下面用进程对照演示隔离模型的两条边界（模块状态不共享 / 进程资源共享），不依赖 3.13 API。

```python
import subprocess
import sys
import threading

child = (
    "import sys; "
    "st = getattr(sys, '_demo', 0) + 1; "
    "sys._demo = st; "
    "print(st)"
)
r1 = subprocess.run([sys.executable, "-c", child], capture_output=True, text=True)
r2 = subprocess.run([sys.executable, "-c", child], capture_output=True, text=True)
print("[1] 两个独立解释器进程各自看到:", r1.stdout.strip(), r2.stdout.strip(), "——模块状态不共享")

# 对照: 同一解释器内的线程共享同一套模块状态
state = {"n": 0}
lock = threading.Lock()


def bump():
    for _ in range(1000):
        with lock:
            state["n"] += 1


ts = [threading.Thread(target=bump) for _ in range(4)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print("[2] 同解释器线程共享模块状态:", state["n"], "——线程模型, 需要锁")

# 子解释器的定位: 介于两者之间——
# 模块级状态各自一份(像进程), 内存与 fd 同进程共享(像线程)
print("[3] 进程级资源(如 stdout fd)在同进程任何解释器中都是同一个")
```

**追问一**：PEP 684 的 per-interpreter GIL 为什么要求 C 扩展做适配？—— 扩展若在内部用 C 级静态全局（缓存表、单例句柄），两个解释器同时执行它的代码就变成**真并发**访问同一份内存——以前有全局 GIL 兜底，现在每个解释器各自的 GIL 管不到别人。所以扩展必须声明 `Py_mod_multiple_interpreters`（支持）或用 `PyType_FromSpec`/ immortal 化等手段把全局态改造为解释器局部；未适配的扩展在子解释器里 import 直接被拒。这就是"子解释器并行不是免费的线程池"的根本原因。

**追问二**：mod_wsgi 的 WSGIDaemonProcess 与子解释器方案怎么权衡？—— mod_wsgi 的 application group `%{GLOBAL}` 是全进程单解释器（所有应用同模块表，一个应用的猴子补丁污染所有人），`(application)` 是每应用一个子解释器（隔离模块表，但 C 扩展全局态与进程资源仍共享），daemon process 是真进程隔离（最强，成本是内存与启动）。选择取决于隔离需求层级：Python 层状态隔离用子解释器够，任何 C 扩展或系统资源层面的互不信任必须上多进程。

## 背诵要点
- 子解释器 = 同进程内各自模块表 + 各自 GIL（PEP 684，3.12 起按解释器分配）；fd/信号/cwd/分配器仍进程级共享。
- 隔离强度排序：多进程 > 子解释器 > 多线程；C 扩展未声明兼容时子解释器并行不成立。
- 生产并行今天仍选进程池；子解释器的收益是嵌入式宿主的隔离与省内存，不是 3.12 业务并行。

## 复盘追问
- 两个子解释器里的 C 扩展为什么还会互踩？（扩展静态全局不被 per-interpreter GIL 保护）
- 子解释器和多进程的隔离边界差在哪？（进程级资源与底层分配器共享）

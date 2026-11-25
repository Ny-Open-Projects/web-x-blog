---
title: [Q5615] 进程池异常回传的 pickle 成本与信息丢失账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5615 · 进程池异常回传的 pickle 成本与信息丢失账

> 难度:★★★★☆ | 标签:成本工程, pickle, 进程池

**问**:进程池 worker 里抛的异常到父进程 `future.result()` 时还能 `raise`，但日志里 `__cause__`、局部变量、自定义属性全丢了，有时甚至直接收到一句 `PicklingError`。异常跨进程回传到底经历了什么？成本和信息各损失在哪？

**答**:结论：进程池的异常回传路径是 **worker 内异常 → 在 `_process_worker` 里捕获 → `pickle.dumps(exception实例)` → 结果队列 → 父进程 `pickle.loads` → `future.set_exception` → `result()` 时重抛**。两笔账：a) **成本**：异常对象的 pickle 包含它引用的一切——`args`、`__cause__`/`__context__` 链、自定义属性。如果异常里塞了 DataFrame、request 对象等大引用，每条失败任务都会序列化一次大对象，错误风暴时回传带宽远超正常任务（对照 Q5543 的 IPC pickle 税）；b) **信息丢失**：pickle 只保状态不保行为——`traceback` 对象**不进 pickle**（3.12 前），父进程拿到的 traceback 是"重抛时新建的栈"（只有 `_process_worker` 往上这一段），原始 worker 栈要靠异常消息/自定义属性携带；不可 pickle 的属性（socket、生成器、lambda）静默丢或抛 `PicklingError`，含 `__cause__` 链时失败得更隐蔽。工程规范：① worker 异常**收敛为可序列化的业务异常**，原始 traceback 以字符串属性 `orig_tb` 带回；② 异常对象保持轻（只带 message、code、紧凑上下文）；③ 捕获 `concurrent.futures.process.BrokenProcessPool` 区分"worker 崩溃"与"任务失败"（对照 Q2664 毒化全池）。

```python
import multiprocessing as mp
import traceback as tb_mod
from concurrent.futures import ProcessPoolExecutor

class Heavy:
    """模拟异常对象上挂的大引用"""
    def __init__(self):
        self.payload = bytearray(4 * 1024 * 1024)    # 4MB

class BizError(Exception):
    """默认的 Exception pickle 只保留 args；想带回自定义字段必须重写 __reduce__"""
    def __init__(self, code, msg, extra=None, orig_tb=None):
        super().__init__(code, msg)
        self.code = code
        self.extra = extra               # 事故源头：挂大对象
        self.orig_tb = orig_tb           # 修复：以文本携带原始栈

    def __reduce__(self):
        return (BizError, (self.code, self.args[1], self.extra, self.orig_tb))

def bad_task(i):
    if i == 2:
        raise BizError("E1", "下游超时", extra=Heavy())   # 大引用挂在异常上
    return i * 2

def good_task(i):
    if i == 2:
        try:
            raise RuntimeError("socket timeout")         # 模拟底层异常
        except RuntimeError:
            raw = tb_mod.format_exc()                    # 在 except 里拿到真实栈
        raise BizError("E1", "下游超时", orig_tb=raw)    # 只带轻量文本
    return i * 2

if __name__ == "__main__":           # macOS spawn 守卫
    mp.set_start_method("spawn", force=True)

    # 事故形态：异常带大对象 → 回传 pickle 成本高；若带不可序列化对象则直接 PicklingError
    with ProcessPoolExecutor(max_workers=2) as ex:
        futs = [ex.submit(bad_task, i) for i in range(3)]
        for f in futs:
            try:
                f.result()
            except Exception as e:
                info = f"{type(e).__name__}: {e}"
                extra = getattr(e, "extra", None)
                print(info, "| extra 大小:",
                      len(extra.payload) if extra else None,
                      "| __cause__:", e.__cause__)

    # 修复形态：轻异常 + 原始栈文本回传
    with ProcessPoolExecutor(max_workers=2) as ex:
        for f in [ex.submit(good_task, i) for i in range(3)]:
            try:
                f.result()
            except BizError as e:
                print("拿到完整信息: code=", e.code,
                      "| 原栈首行:", e.orig_tb.splitlines()[0])
```

**追问一层**:为什么 traceback 对象不进 pickle——它引用了哪些不可序列化的东西？3.11 的 `traceback.TracebackException` 如何在"只传文本"与"结构化"之间折中？
**追二层**:`BrokenProcessPool` 与业务异常在 `future.result()` 上怎么区分？OOM 被 cgroup 杀掉的 worker 在父进程表现为哪种异常（对照 Q2664、Q6042）？

**背诵要点**
- 回传链路：worker 捕获 → pickle 异常实例 → 结果队列 → 父进程重抛；traceback 对象不进 pickle，原栈只靠文本/属性携带。
- 异常上的大引用或不可序列化对象（socket/lambda/生成器）会让回传变贵或抛 PicklingError；含 __cause__ 链失败更隐蔽。
- 规范：worker 收敛轻量业务异常 + orig_tb 文本；区分 BrokenProcessPool（进程崩溃）与任务异常。

**复盘追问**
- 错误风暴时结果队列积压拖慢正常任务，怎么在队列侧限流？提示：异常聚合上报而非逐条回传，或按 code 采样带回 extra。
- orig_tb 文本里若含敏感信息（SQL、token）随异常进日志，治理动作是什么？提示：worker 侧脱敏后再 format_exc（引 Q2644）。

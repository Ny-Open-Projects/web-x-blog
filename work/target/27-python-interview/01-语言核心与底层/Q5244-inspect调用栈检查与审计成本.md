---
title: "[Q5244] inspect 调用栈检查：currentframe、getouterframes 与审计成本"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5244 · inspect 调用栈检查：currentframe、getouterframes 与审计成本

难度：P6 ｜ 标签：inspect、currentframe、getouterframes、调用栈、审计日志、帧引用泄漏、性能成本、sys._getframe

**问**：运行时怎么拿到"是谁在调用我"——`inspect.currentframe()`、`sys._getframe()`、`inspect.getouterframes()` 三者的成本与能力差异？审计日志/权限校验用调用栈检查有什么坑？帧引用为什么会造成内存泄漏？热路径为什么禁用栈检查？

**答**：
结论：三个 API 是同一件事的三档成本：①**`sys._getframe(depth)`**——直接跳进 C 层拿帧对象，几乎零成本，但是"实现细节"（CPython 私有语义，PyPy 等实现慢或缺省）；②**`inspect.currentframe()`**——内部就是 `sys._getframe(1)` 但对不支持的解释器返回 None，是兼容层首选；③**`inspect.getouterframes(frame, context=n)`**——每层帧构造 `FrameInfo`（帧+文件名+行号+函数名+**context 代码行文本**，要从源文件读 n 行！），成本随深度线性放大且含磁盘 IO，最贵但产出人可读的栈。用法骨架：审计/权限场景在入口处 `caller = frame.f_back`（跳过自己这层），取 `caller.f_code` 的 `co_name`/`co_filename`/`f_lineno` 即可归因——**只用 code 对象属性就不触发源码读取**，成本可控。坑面：a)**帧引用是强引用**——拿到 frame 不释放，会连带把整条 f_back 链上所有帧的局部变量钉在内存里（traceback 泄漏同族，Q5052），循环里反复 currentframe 必须 `del frame`；b)**优化器无关**——CPython 3.11+ 特化与 C 扩展帧的处理不同：C 扩展调用不产生 Python 帧（栈检查看不到它），断言会低估真实调用链；c)**热路径禁用**——每次调用都遍历 f_back 链与构造对象，百万 QPS 下是纯开销；权限校验的正确形态是显式传上下文（参数/ContextVar，Q1281），栈检查只做兜底或离线审计；d)**跨帧改局部变量**（frame.f_locals 写入）在 3.13 前不可靠——审计只读不写。

取舍：a) 取"直接调用者"：`sys._getframe(1).f_code` 足够（注意 depth 语义，0 是自己）；b) 取"完整可读栈"：`inspect.getouterframes` 只在错误路径/低频审计用，且 context=0 或 1 控制源码读取量；c) 全线程栈：`sys._current_frames()` 拿所有线程此刻的帧根，配合 getouterframes 可做线程转储（Q2688 的手写实现），用于卡死诊断；d) 装饰器场景：want 层数要按"装饰器 wrapper 加了几层"动态偏移，漏算会把 wrapper 当调用者；e) 生产开关：栈检查逻辑用环境变量降级（关闭时只记 `sys._getframe(1).f_code.co_name`），把成本藏在配置后面。

实战：事故形态是"权限中间件用 getouterframes(context=2) 做调用审计，压测 QPS 从 8000 掉到 2100——profile 显示大头在 getouterframes 的 linecache 源码读取；修复为热路径只取 f_back.f_code 三元组（不再读源码行），完整栈审计改为异步旁路采样（1% 请求 + 错误路径 100%），且审计函数 finally 里 del frame 防帧链泄漏"。下面实测三档 API 的成本与归因能力。

```python
# inspect 调用栈检查: currentframe、getouterframes 与成本分档
import inspect
import sys
import time

def audit_direct(action: str) -> None:
    """档位1: 只取直接调用者的 code 三元组, 不读源码, 成本最低"""
    caller = sys._getframe(1).f_back if False else sys._getframe(1)
    code = caller.f_code
    print(f"[direct] {action} <- {code.co_filename.rsplit('/', 1)[-1]}:{caller.f_lineno} in {code.co_name}")

def caller_a() -> None:
    audit_direct("read-config")

def caller_b() -> None:
    caller_a()

def audit_full(action: str) -> None:
    """档位2: 完整可读栈, 每层含源码行, 只适合低频/错误路径"""
    frame = inspect.currentframe()
    try:
        infos = inspect.getouterframes(frame, context=1)   # 每层读 1 行源码
        for info in infos[1:4]:
            print(f"[full  ] {info.function}@{info.lineno}: {info.code_context[0].strip() if info.code_context else '?'}")
    finally:
        del frame                                          # 切断帧强引用链

def caller_c() -> None:
    audit_full("delete-user")

caller_a()
caller_b()
caller_c()

print("--- 帧引用泄漏: 拿到 frame 不释放会钉住整条 f_back 链 ---")
def leaky() -> list:
    frames = []
    for _ in range(3):
        frames.append(sys._getframe())     # 每个都是同一条链的入口
    return frames

import gc
before = len(gc.get_objects())
hold = leaky()
gc.collect()
after = len(gc.get_objects())
print("    持有帧引用期间对象数变化:", after - before, "(真实泄漏需配合大对象演示, 这里展示引用形态)")
print("    帧的 f_back 链:", hold[0].f_back is not None, "-> 释放须 del/置 None")
del hold

print("--- 成本实测: 热路径为什么禁用 ---")
def cost(fn, n: int = 50000) -> float:
    t0 = time.perf_counter()
    for _ in range(n):
        fn()
    return (time.perf_counter() - t0) / n * 1e6

def bare() -> None:
    pass

def with_getframe() -> None:
    f = sys._getframe(1)
    f.f_code.co_name
    del f

def with_outer() -> None:
    inspect.getouterframes(sys._getframe(1), 1)

print(f"    baseline 裸调用      : {cost(bare):8.3f} us/次")
print(f"    sys._getframe        : {cost(with_getframe):8.3f} us/次")
print(f"    getouterframes(ctx=1): {cost(with_outer):8.3f} us/次  <- 差两个数量级, 热路径禁用")
print("[rule ] 热路径只取 f_code 三元组; 完整栈留错误路径; 拿帧必 del; 归因优先显式上下文")
```

**追问一**：`sys._getframe(depth)` 的 depth 语义是什么？装饰器堆叠后审计函数怎么拿到"真正的业务调用者"而不是 wrapper？—— depth 是"从当前帧往上跳几层"：`_getframe(0)` 是当前函数自己的帧，`_getframe(1)` 是直接调用者。装饰器堆叠时每层 wrapper 都是一帧，审计函数若被三层装饰器包住，真实业务调用者要用 `while frame.f_back and frame.f_back.f_code.co_filename == __file__:` 这类**按条件上溯**（跳过本模块内所有 wrapper 帧）而不是硬编码 depth——硬编码在装饰器数量变化时静默错位。更稳的形态：装饰器自己负责把业务调用点记录进闭包（def 时拿不到，但 wrapper 里 `sys._getframe(1)` 拿到的就是真实调用者），审计逻辑下沉到各 wrapper 而不是集中在最内层。另一个边界：C 扩展/内置函数调用**不产生 Python 帧**，f_back 链里会出现"跳跃"——审计报告要容忍这种断层并标注"native boundary"。

**追问二**：`inspect.getouterframes` 为什么慢？linecache 缓存在这里扮演什么角色，什么情况下反而失效？—— 慢在三处：①每层帧构造 FrameInfo 对象（元组 unpack + 若干字符串拼接）；②**读源码行**——`context=n` 要用 linecache 从磁盘读函数所在文件的相关行做上下文展示；③属性访问触发 f_lineno 的"指令偏移→行号"反查。linecache 把整文件按行缓存在内存（`linecache.cache`），同一文件反复审计时第二次起免磁盘——所以基准测试里它看起来比真实生产快；失效场景：文件被轮转/重建（日志代码热替换、容器内挂载变化）导致缓存 key 的 mtime/size 校验失败，linecache 会重新读盘，且 **checkcache 不被自动调用时可能给出陈旧行文**；还有超大源文件被长期驻留在 linecache.cache 里构成内存占用。工程结论：getouterframes 是"人看的调试工具"，机器消费的审计/监控一律走 code 三元组或显式上下文传递——把读源码、拼可读栈这种贵动作留给异常路径。

## 背诵要点
- 三档成本：sys._getframe(depth) 最快（CPython 私有）、inspect.currentframe 兼容层、getouterframes 每层构造 FrameInfo 且读源码行（linecache）最贵。
- 帧是强引用：拿 frame 不释放会钉住整条 f_back 链的局部变量，循环里必须 del；C 扩展调用不产生 Python 帧，栈检查有断层。
- 热路径禁栈检查：归因用 f_back.f_code 三元组或显式上下文（ContextVar）；装饰器堆叠按条件上溯而非硬编码 depth。

## 复盘追问
- 审计日志想记录调用者，热路径怎么做才不拖垮 QPS？（sys._getframe(1).f_code 三元组不读源码；完整 getouterframes 只留错误路径并 del frame；根本解是显式上下文传参）
- 为什么栈检查在 3.11+ 的 C 扩展边界会漏帧？（C 函数不产生 Python 帧，f_back 链跳跃；审计需容忍断层并标注 native boundary）

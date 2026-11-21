---
title: [Q5052] 异常对象长期持有 traceback 内存泄漏事故
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5052 · 异常对象长期持有 traceback 引起的内存泄漏事故复盘

> 难度:★★★★ | 标签:traceback, frame, 异常, 内存泄漏, 事故复盘

**问**：一个错误上报模块把捕获的异常对象放进全局列表 `recent_errors` 供诊断页展示，灰度后 RSS 缓慢上涨不回落。异常对象为什么会"拖住"一大片内存？`except X as e` 的作用域规则是什么？正确的错误上报姿势是什么？

**答**：异常对象身上挂着 `__traceback__`，traceback 是一条**帧对象链**——每一帧都持有该层当时所有局部变量的引用。所以你"只存了一个异常"，实际锁住了异常路径上整条调用栈的局部对象（大 buffer、连接、请求体）。三个根因依次排查：a) **全局/长生命周期容器存了异常对象本身**（本案例）；b) `except X as e` 虽然在块结束时自动 `del e`（PEP 3110 防止变量泄漏），但如果 except 块里把 `e` 存进了列表/闭包/self 属性，泄漏照样发生；c) `sys.exc_info()`/traceback 对象被第三方 APM 钩子持有。修复姿势：上报时**立即提取标量信息**（`type(e).__name__`、`str(e)`、`traceback.format_exc()` 格式化后的字符串、`e.__traceback__.tb_frame` 里的少量白名单字段），然后丢弃异常对象；若确实要留 traceback 用于离线分析，序列化成字符串或用 `traceback.extract_tb()` 拿 StackSummary（纯字符串栈），不要留对象引用。另外 `raise ... from err` 会形成 `__cause__` 链，链上每个异常都拖一份帧栈，长链异常比想象中重得多。

```python
# file: code/01_语言核心与底层/q5052_tb_leak.py
import gc, weakref, traceback

class Big:
    def __init__(self):
        self.payload = bytearray(1024 * 1024)  # 1MB

refs = []
def make_error():
    b = Big()
    refs.append(weakref.ref(b))   # 先注册弱引用再抛错, 便于观察存活
    raise ValueError("boom")

# 事故复现: 全局列表持有异常对象 -> tb -> frame -> Big 无法回收
recent_errors = []
try:
    make_error()
except ValueError as e:
    recent_errors.append(e)       # 反例: 存了异常对象
err = recent_errors[0]
gc.collect()
print("异常被持有, tb 存活:", err.__traceback__ is not None)
print("tb 帧里的 1MB Big 仍存活(泄漏中):", refs[0]() is not None)

# 修复: 只上报提取出来的标量信息
recent_errors.clear()
try:
    make_error()
except ValueError as e:
    recent_errors.append({
        "type": type(e).__name__,
        "msg": str(e),
        "stack": traceback.extract_tb(e.__traceback__),  # StackSummary 纯字符串栈
    })
    # except 块结束时 e 自动被 del (PEP 3110), 无需手动
gc.collect()
print("改为存摘要后 Big 已释放:", refs[0]() is None)
print("提取的栈:", recent_errors[0]["stack"].format()[0].strip())
```

**追问**：1) 为什么 `except X as e` 块结束后访问 `e` 会 NameError？——PEP 3110：块结束自动执行 `del e`，防止异常对象被裸名字钉住泄漏；要延长生命周期只能显式赋值给别的名字。2) `raise new_err from err` 之后 err 的帧栈还在吗？——在，挂在 `new_err.__cause__`（或 `__context__` 隐式链）上，整条链每层各持一份帧栈；日志里打印的就是这条链，链长会放大内存与日志体积。3) 重试框架里"保存上次异常再重试"怎么不泄漏？——只保留 `(type, str, extract_tb)` 三元组；重试成功后立刻清引用，避免跨请求持有旧帧。

## 背诵要点
- 异常对象 → `__traceback__` → 帧链 → 各层局部变量，存异常=锁住整条调用栈的内存。
- `except X as e` 块结束自动 `del e`（PEP 3110）；存进全局容器才是真正泄漏源。
- 上报只存标量+`traceback.extract_tb()` 字符串栈；`raise from` 的 `__cause__` 链每层都拖帧栈。

## 复盘追问
- 你们的全局错误收集/APM 上报里，谁还持有异常对象？怎么证明？（提示：灰度前后 tracemalloc 快照对比 + 按 traceback 类型聚合分配点）
- 日志系统里整段 `traceback.format_exc()` 存盘和只存摘要，成本差多少？（提示：帧数×每帧行数，热门异常路径的 QPS 相乘）

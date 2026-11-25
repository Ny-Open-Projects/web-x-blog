---
title: "[Q5224] raise 的三种形式与裸 raise 重抛语义"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5224 · raise 的三种形式与裸 raise 重抛语义

难度：P6 ｜ 标签：raise、裸重抛、__context__、__cause__、异常链、traceback 保真

**问**：`raise` 有哪三种合法形式？`except` 里裸 `raise` 与 `raise SameException`、`raise NewError from exc` 各有什么区别？`__context__` 与 `__cause__` 分别记录什么？为什么说"裸 raise 是唯一保真重抛"？

**答**：
结论：三种形式——①`raise`（裸重抛当前活跃异常）；②`raise SomeException`（抛类=零参实例化，或抛实例）；③`raise SomeException from cause`（显式成链）。核心区别在**身份与链路**：裸 `raise` 重抛的是**同一个异常对象**，类型、消息、traceback 全部原样保真，语义是"处理了一半，继续往上抛"；`raise NewError from exc` 抛出新异常，`__cause__` 指向 `exc`（用户显式指定的因果），同时 `__context__` 也指向 exc（隐式上下文）；不带 `from` 的 `raise NewError` 会让 `__context__` 指向正在处理的旧异常（隐式链，Q5088 排障时看到的 "During handling of the above exception..."），只有 `from None` 才把链彻底压掉。traceback 保真度的差异最实际：裸 raise 的栈帧完整（从最初 raise 点到当前点），包装重抛则多一截新栈——排障读栈时"哪个才是真正出错的行"取决于用的是哪种写法。

取舍：a) 通用兜底日志层：捕获→记录→裸 raise，类型不变让上层按既有 except 分支继续工作；b) 抽象边界/防腐层：底层异常翻成业务异常，用 `from exc` 保链（排障双栈都看得到）；c) 面向用户的 API 错误：`from None` 压掉实现细节链，避免内部栈泄漏给响应体（Q2644 的信息泄漏面）；d) 绝不用 `raise SameException("新消息")` 重抛同类异常——那是一个新实例，原 traceback 被替换，现场丢失；e) 裸 raise 必须在当前 `except` 作用域内，出了作用域活跃异常已清空，会 RuntimeError "No active exception to re-raise"；f) `finally` 里裸 raise 会覆盖原异常（Q526/Q1814 的 return/异常覆盖规则），重抛链路要避开 finally。

实战：事故形态是"重试装饰器在 except 里 `raise RetryExhausted('failed')`，上层 except TimeoutError 再也接不住，原本可恢复的超时被当成未知异常打进 500；修复为裸 raise 透传，或显式 `from exc` 定义重试异常的父类让捕获矩阵成立"。下面演示三种形式下的链路字段。

```python
# raise 的三种形式与裸 raise 重抛
class Transient(Exception):
    pass


def attempt(tag: str) -> None:
    try:
        if tag == "bare":
            try:
                raise Transient("原始故障")
            except Transient:
                raise                      # 形式一: 裸 raise, 原样重抛, traceback 保真
        elif tag == "wrap":
            try:
                raise Transient("原始故障")
            except Transient as exc:
                raise RuntimeError("包装后重抛") from exc   # 形式二: 显式链, __cause__
        else:  # mute
            try:
                raise Transient("原始故障")
            except Transient:
                raise RuntimeError("包装后重抛") from None  # 形式三: from None 压链
    except BaseException as top:
        ctx = top.__context__
        cause = top.__cause__
        print(f"[{tag}] 异常={type(top).__name__} | __context__={type(ctx).__name__ if ctx else None}"
              f" | __cause__={type(cause).__name__ if cause else None}")


attempt("bare")
attempt("wrap")
attempt("mute")
print("[4] 裸 raise 是唯一保真重抛: 语义不变、traceback 原样、不制造新异常类型")
print("[5] raise 新异常会隐式成链 (__context__); from exc 显式成链; from None 明确压链")
print("[6] except 块里裸 raise 必须在当前 except 作用域内, 出了作用域会 RuntimeError")
```

**追问一**：`__context__` 和 `__cause__` 在排障时怎么用？—— 两者都可能指向"之前的异常"，语义不同：`__cause__` 只在 `from exc` 显式设置时非空，代表"我确信是它导致的"；`__context__` 是解释器自动记录的"处理 A 时又发生了 B"的现场。排障优先级：先看最外层异常的最终消息，再沿 `__cause__`（若非 None）找根因，`__context__` 作为兜底线索——`from None` 的代码等于主动销毁了这条线索，只在"确定要隐藏内部细节"时用。打印层面 `traceback.format_exception` 会把两条链都展开，日志里 "The above exception was the direct cause..." 与 "During handling..." 前缀就是这两类链的标记（Q5088）。

**追问二**：重试装饰器为什么必须区分"裸透传"与"包装重抛"？—— 捕获矩阵是按**类型**匹配的：上层写的 `except TimeoutError` 只认 TimeoutError。装饰器把 TimeoutError 包成 RetryExhausted 后，上层既有的分支全部失效，异常从"可重试的超时"变成"未分类的 500"——这是装饰器改写异常类型时最隐蔽的破坏。工程规则：装饰器若不改异常语义就裸 raise；若必须包装，定义新异常继承原类型（`class RetryExhausted(TimeoutError)`），或在上层文档里写明类型迁移。本质：异常类型是 API 契约的一部分，重抛方式即契约变更方式。

## 背诵要点
- raise 三形式：裸 raise（同一对象保真重抛）、raise 类/实例（新异常）、raise X from cause（显式链）。
- __cause__ 只由 from 设置；__context__ 是隐式现场链；from None 压链用于面向用户错误防泄漏。
- 重抛铁律：不改语义就裸 raise；包装需继承原类型或重写捕获矩阵；裸 raise 不可离开 except 作用域。

## 复盘追问
- 重试装饰器为什么让上层的 except TimeoutError 失效？（包装重抛换了类型；裸透传或继承原类型修契约）
- __context__ 与 __cause__ 排障时先看哪个？（cause 是显式根因，context 是隐式现场；from None 会销毁线索）

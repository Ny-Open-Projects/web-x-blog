---
title: [Q526] try/finally 与 return:finally 的覆盖行为
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q526 · try/finally 与 return:finally 的覆盖行为

> 难度:★★★★ | 标签:异常, finally

**问**:try 里 return 了,finally 里的 return 会怎样?finally 里 return 为什么会「吃掉」异常?

**答**:finally 无条件执行,且其中的 return/break 会覆盖 try/except 里已经产生的返回值——try 的 return 表达式先求值、结果暂存,finally 若自己也 return,栈上留下的是 finally 的值,原来那份被丢弃。更危险的是:异常传播路径上 finally 的 return 会直接终止传播,异常凭空消失(相当于 __exit__ 返回 True 的语句级版本)。规范:finally 只放清理代码(关文件、解锁),绝不放 return/break/continue;需要「无论成败都返回」的语义用显式变量在 try 外返回。

```python
# file: code/01_语言核心与底层/q526_finally_return.py
def trap():
    try:
        return "from try"
    finally:
        return "from finally"         # 覆盖 try 的返回值

def swallow():
    try:
        raise ValueError("boom")
    finally:
        return "exception eaten"      # 异常被 return 静默终结

def rethrow_with_finally():
    try:
        raise ValueError("real")
    finally:
        print("finally runs during unwind")   # 清理:finally 的正职

if __name__ == "__main__":
    print(trap())
    print(swallow())
    try:
        rethrow_with_finally()
    except ValueError as e:
        print("propagated:", e)
```

**追问**:1) finally 里抛新异常会怎样?——新异常取代原异常并向外传播,原异常挂在新异常的 __context__ 上;所以 finally 里的清理代码自身要用 try 包住,避免顶掉真正的错误。2) 为什么 finally 里的 return 能终结异常传播?——异常传播是沿调用栈逐帧展开,finally 是展开路径上必经代码;它的 return/break 把「继续展开」改成「带值正常返回」,等于语句级吞异常(3.8+ 编译器会给 SyntaxWarning)。3) 底层怎么实现?——try/finally 在 3.10+ 编译为异常表(exception table 条目),return 的值先暂存,展开到 finally 再决定用哪个值、是否继续传播。4) 生产陷阱?——finally 里做可能抛错的 close(如网络 flush)顶掉业务异常;finally 里 return 让 bug 凭空消失;规范是 finally 只清理,清理自身 try/except 记日志。

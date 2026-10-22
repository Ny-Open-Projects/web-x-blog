# 31. try/except/else/finally 各段什么时候执行

> 分类：语言基础/异常 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**else** / **finally** / **return 覆盖**
> 原文锚点：第 26~29 段「try 块包含可能抛出异常的代码…else 里是没有异常时执行，finally 无论是否发生都会执行」

## 一句话总述
`try` 包风险代码，`except` 处理异常，`else` **只在没异常时**跑，`finally` **无论如何都跑**——但 `finally` 里写 `return` 会**吞掉异常并覆盖返回值**。

## 面试官视角
- **考察意图**：else 常被人忽略，finally 的坑常被踩，两处最能区分真用过还是背过。
- **P5** 知道 finally 释放资源 / **P6** 能说清 else 的真实价值 / **P7** 知道优先用 `with` 替代手写 try/finally。
- **红旗**：① 把 `else` 说成"其他异常"；② 在 `finally` 里 return/break；③ 以为进程被 kill 时 finally 也会执行。
- **惊艳点**：`finally` 中有 `return` 时，**正在传播的异常会被静默丢弃**。验证：运行下方 `g()` 观察输出 `[实测]`

## 主问答
**Q：try/except/else/finally 分别什么时候执行？else 有什么用？**
**A：**
1. **先给结论**：`else` **无异常才执行**，`finally` **必然执行**（用于关闭文件、连接、锁）。
2. **再给机制**：把"只可能抛异常的几行"放进 try、把"成功后才做的逻辑"放进 else，`except` 就**不会误捕后续代码的同类异常**——这才是 else 存在的价值，不是语法糖。
3. **最后给边界**：`finally` 里的 `return`/`break`/`continue` 会**吞掉**正在传播的异常；进程收到 SIGKILL、机器断电等场景下 finally **不会**执行。
**加分层**：资源释放优先用 `with`（上下文管理器），比手写 try/finally 更难漏，语义也更明确。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | finally 一定会执行吗 | 术语 | 正常路径必执行 | 换题 → 不及格 |
| L2 | else 和 finally 有何区别 | 机制 | 无异常 vs 无条件 | 判 P5 |
| L3 | finally 里 return 会怎样 | 边界/反例 | 吞异常、覆盖返回值 | 判 P6 |
| L4 | 为什么要用 else 而不是都塞进 try | 设计动机 | 防误捕 | 判 P6+ |
| L5 | 资源释放你更倾向怎么写 | 工程判断 | with 上下文管理器 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| CPython 3.x 全系 | 3.11（PEP 654）新增 `except*` 处理异常组，本卡结论不受影响 | 按四段语义答；异常组另说 |

## 关键代码
```python
def f(path):
    try:
        fh = open(path)
    except FileNotFoundError:
        return "missing"
    else:
        return fh.read()          # 这里的异常不会被上面的 except 误捕
    finally:
        print("finally 必跑")
        # return "x"              # 若打开：吞掉异常并覆盖返回值

def g():
    try:
        raise ValueError("boom")
    finally:
        return "swallowed"        # ValueError 被静默丢弃
print(g())                       # swallowed
```

## ⚠️ 原文纠错
原文对 else/finally 的描述正确；原文未提"`finally` 中 return 会吞掉异常、覆盖返回值"这一高频陷阱，此处补充 `[经验]`。

## 总结与追问预判
- else 防误捕、finally 保释放；finally 里别写 return，资源优先用 with。
- 下一题：见 30（异常继承体系）、32（自定义异常）。

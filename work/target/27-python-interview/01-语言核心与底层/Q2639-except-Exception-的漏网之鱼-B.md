---
title: [Q2639] except Exception 的漏网之鱼:BaseException 直系亲属
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2639 · except Exception 的漏网之鱼:BaseException 直系亲属

> 难度:★☆☆☆☆ | 标签:异常, BaseException, 异常层次

**问**:为什么「包住一切」的 `except Exception` 还是会漏?漏掉的是谁,该不该接?

**答**:继承树顶端是 `BaseException`,它的直系子类里 `KeyboardInterrupt`(Ctrl+C)、`SystemExit`(sys.exit)与 `GeneratorExit`(生成器关闭)刻意**不是** Exception 的子类——设计意图就是让 `except Exception` 不拦截用户主动退出与控制流信号,否则 CLI 无法退出、生成器无法清理。所以 `except Exception` 是「业务异常兜底」而非「绝对兜底」;真要在最外层收口一切(守护进程主循环、提交崩溃报告)才用 `except BaseException`,而且必须重新抛出(`raise`)而非吞掉。写兜底时先想清楚:这个 handler 的存在是为了处理、翻译还是记录——只有翻译层有权不重新抛。

```python
# file: code/01_语言核心与底层/q2639_except_exception.py
"""except Exception 拦不住 BaseException 直系子类。"""


def risky():
    raise KeyboardInterrupt          # 模拟 Ctrl+C


if __name__ == "__main__":
    # except Exception 放行 KeyboardInterrupt
    try:
        try:
            risky()
        except Exception:
            print("不会打印:Exception 接不住")
    except KeyboardInterrupt:
        print("KeyboardInterrupt 穿透了 except Exception")

    # 最外层收口:必须重新抛出
    try:
        risky()
    except BaseException as exc:
        print("BaseException 收口:", type(exc).__name__, "-> 应该 raise")
        # 正确姿势是 raise,演示进程不退出这里选择不重抛
```

**追问**:1) GeneratorExit 为什么也绕开 Exception?——生成器被 close 时从挂起的 yield 点抛入,若被普通 except 吞掉,生成器无法正常结束,协议要求它继续向外传。2) 漏网名单的完整机制?——KeyboardInterrupt/SystemExit/GeneratorExit 继承 BaseException;CancelledError(3.8+)同样——它们是控制流信号,不是程序错误;except Exception 兜不住,裸 except 才兜(那是更大的错误)。3) 与 except* 的关系?——except* 不允许整组捕 BaseException(Q469);ExceptionGroup(含普通异常)会被 except Exception 捕获但语义要拆包。4) 生产陷阱?——裸 except 吞 KeyboardInterrupt;async 任务里 except Exception 误吞 CancelledError 破坏取消传播;try/finally 收尾不重抛。

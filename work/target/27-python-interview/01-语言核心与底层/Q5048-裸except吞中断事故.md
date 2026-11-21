---
title: [Q5048] 裸 except 吞 KeyboardInterrupt 事故复盘
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5048 · 裸 except 吞 KeyboardInterrupt 的事故复盘

> 难度:★★★ | 标签:异常, BaseException, 事故复盘, except

**问**：一次发版回滚时服务"杀不掉"：SIGTERM 无效、Ctrl-C 也停不下来，最终靠 kill -9。排查发现热循环里有一处 `except:`。裸 except 为什么能吞掉 KeyboardInterrupt 和 SystemExit？异常层次到底怎么设计？catch 的正确姿势是什么？

**答**：Python 异常树根是 `BaseException`，下面四个"控制流异常"不该被业务捕获：`KeyboardInterrupt`（SIGINT/键盘中断）、`SystemExit`（sys.exit）、`GeneratorExit`（生成器关闭，Q019）、3.8+ 的 asyncio.CancelledError（3.8 起继承 BaseException，Q5516）。`except:` **裸写等价于 `except BaseException:`**——全部吞掉：主循环里裸 except 捕获 KeyboardInterrupt 后记日志继续跑，进程就对 Ctrl-C/SIGTERM 免疫了，这就是"杀不掉"事故的机制。事故里往往还有第二层伤害：裸 except 连 `SystemExit` 都吞，优雅关闭逻辑（发 flush、退注册）被跳过。正确姿势三条：1) **业务层永远 `except Exception`**（不含 BaseException 分支），让控制流异常自然穿透；2) 需要"清理但继续传播"时用 `try/finally` 或 `contextlib.suppress`（只 suppress 指定类型）而不是吞；3) 捕获范围**最小化**——只捕预期类型（`except KeyError`），宽 except Exception 兜底也要 `logger.exception` 留痕再决定 re-raise。工程防线：lint 规则（ruff E722 裸 except、BLE001 盲捕 Exception）+ code review 清单 + 对"必须吞一切"的顶层入口（worker 主循环）显式分开处理 BaseException：记录后按退出协议退出而不是继续跑。

```python
# file: code/01_语言核心与底层/q5048_bare_except.py
import sys

def worker_bare():
    """事故版: 裸 except 吞掉 KeyboardInterrupt, 进程杀不掉"""
    for _ in range(5):
        try:
            raise KeyboardInterrupt            # 模拟 SIGINT 到达
        except:                                # == except BaseException
            pass                               # 记个日志继续跑 -> 免疫中断
    return "bare: 跑完了(事故)"

def worker_correct():
    """修复版: except Exception 放行控制流异常"""
    for _ in range(5):
        try:
            raise KeyboardInterrupt
        except Exception:                      # KeyboardInterrupt 不属于 Exception
            pass
    return "correct: 跑完了(但这不该发生)"
    # 实际上 KeyboardInterrupt 直接抛出循环 -> 上层优雅关闭

def worker_suppress():
    """只抑制预期类型: contextlib.suppress"""
    from contextlib import suppress
    with suppress(KeyError, ValueError):       # 显式清单
        {}["k"]
    return "suppress: 只吞白名单"

print(worker_bare())
try:
    worker_correct()
except KeyboardInterrupt:
    print("correct: KeyboardInterrupt 正常穿透 -> 进程可被优雅终止")

print(worker_suppress())

# 顶层入口的正确 BaseException 处理: 记录后按协议退出, 不复活
def main_loop():
    try:
        raise KeyboardInterrupt
    except Exception as e:                     # 业务异常: 兜底留痕
        print("业务异常兜底:", type(e).__name__)
    except BaseException as e:                 # 控制流异常: 记录 + 传播, 不吞
        print(f"控制流 {type(e).__name__} -> 走优雅关闭, 退出码 130")
        return 130
    return 0

code = main_loop()
print("退出码协议: 130 = SIGINT 终止 | python:", sys.version_info[:2])
```

**追问**：1) 为什么 3.8 把 `asyncio.CancelledError` 从 Exception 挪到 BaseException？——旧继承下 `except Exception` 会吞取消信号，Task 的取消传播（Q5516/Q5503）失效，协程"取消不掉"与本次事故同构；挪到 BaseException 让取消不可被普通兜底吞掉。2) `finally` 里抛新异常会怎样？——覆盖原异常（旧异常进入 `__context__` 链）；清理代码自己也要 try/except Exception 保护，避免清理失败掩盖真实故障。3) SIGTERM 默认行为为什么不受裸 except 影响？——SIGTERM 默认终止进程（不产生 Python 异常），事故里"SIGTERM 也停不掉"是因为服务注册了 SIGTERM handler 抛 KeyboardInterrupt/走自定义关闭路径，同样被裸 except 吞掉；没注册 handler 时 kill -TERM 本来就能杀。

## 背诵要点
- 裸 except == except BaseException，吞 KeyboardInterrupt/SystemExit/GeneratorExit/CancelledError。
- 业务层只捕 Exception；清理用 finally/suppress 白名单；顶层 BaseException 记录后按退出协议退出。
- 3.8 起 CancelledError 归 BaseException，取消信号不可被 except Exception 吞掉。

## 复盘追问
- "杀不掉"事故的完整排查路径是什么？（提示：先 ps 看进程状态与信号注册，strace/dtruss 看是否阻塞在 syscall，再 grep 裸 except）
- 你的服务需要在"任何情况下都不留下半写数据"与"必须能被杀掉"之间权衡，退出协议应怎么设计？（提示：信号 → 置停止标志 → 有界排空超时 → 强制退出码）

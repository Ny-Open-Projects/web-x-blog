# 30. 为什么自定义异常继承 Exception 而不是 BaseException

> 分类：语言基础/异常 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**BaseException** / **KeyboardInterrupt** / **SystemExit**
> 原文锚点：第 7~14 段、第 31~46 段「所有 Python 异常都继承 BaseException…为什么不是继承 BaseException 呢」

## 一句话总述
异常根类是 `BaseException`，`SystemExit` / `KeyboardInterrupt` / `GeneratorExit` 与 `Exception` **并列**挂在它下面；业务异常必须继承 `Exception`，否则 `except BaseException` 会把 **Ctrl-C 与 sys.exit() 一起吞掉**。

## 面试官视角
- **考察意图**：是否真的理解"业务错误"与"进程生命周期事件"的分界。
- **P5** 知道继承 Exception / **P6** 能画出层级并说出那三个系统级异常 / **P7** 能补上"except 子类必须写在前"和"`except Exception` 漏掉系统异常正是设计意图"。
- **红旗**：① 说"所有异常都继承 Exception"；② 图省事写 `except BaseException: pass`；③ 不知道 Ctrl-C 的本质是抛 `KeyboardInterrupt`。
- **惊艳点**：写了 `except BaseException: pass` 之后 **Ctrl-C 会失效**，进程只能靠 `kill -9` 结束。验证：脚本里包一层后按 Ctrl-C 观察 `[实测]`

## 主问答
**Q：Python 异常的继承关系是怎样的？为什么自定义异常要继承 Exception？**
**A：**
1. **先给结论**：`BaseException` 是根；`SystemExit`、`KeyboardInterrupt`、`GeneratorExit` 与 `Exception` **平级**；其余常见异常（`SyntaxError`、`AssertionError`、`MemoryError`、`IndexError`、`KeyError` 等）都继承 `Exception`。
2. **再给机制**：Ctrl-C 被解释器转成 `KeyboardInterrupt` 抛出，`sys.exit()` 抛 `SystemExit`，生成器被 close 时抛 `GeneratorExit`——它们表示**生命周期事件**，不是业务错误。
3. **最后给边界**：`except Exception` 抓不到这三个，而这**正是想要的**：否则业务兜底逻辑会把退出流程一起吃掉。
**加分层**：多个 `except` 分支必须**子类写在前、父类写在后**，否则子分支永远不可达。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 异常的基类叫什么 | 术语 | BaseException | 换题 → 不及格 |
| L2 | Exception 下有哪些常见异常 | 机制 | ValueError/KeyError/IndexError… | 判 P5 |
| L3 | Ctrl-C 抛出的是什么 | 边界 | KeyboardInterrupt | 判 P6 |
| L4 | 捕获 BaseException 会怎样 | 反例 | 吞掉退出信号 | 判 P6+ |
| L5 | 你怎么做异常兜底分层 | 架构判断 | 边界层统一捕获 Exception | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| CPython 3.x 全系 | 该层级未变 | 业务异常一律继承 Exception |

## 关键代码
```python
class BizError(Exception):
    pass
print(BizError.__mro__)   # (BizError, Exception, BaseException, object)
for name in ("SystemExit", "KeyboardInterrupt", "GeneratorExit"):
    cls = eval(name)
    print(name, "是 Exception 子类吗:", issubclass(cls, Exception))   # 全为 False
try:
    raise BizError("订单已关闭")
except Exception as e:
    print("caught:", e)
```

## ⚠️ 原文纠错
原文把 BaseException、KeyboardInterrupt 写成音译形式，已还原为标准类名。原文"捕获父类异常时所有子类都在捕获范围内"正确；原文未提"except 分支子类必须在前"，此处补充 `[经验]`。

## 总结与追问预判
- 系统级三兄弟与 Exception 平级；业务异常挂 Exception，退出信号才不会被吞。
- 下一题：见 29（异常 vs 错误码）、32（自定义业务异常）。

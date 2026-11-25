---
title: "[Q5157] 常量折叠 peephole 与重复求值成本账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5157 · 常量折叠 peephole 与重复求值成本账

难度：P6 ｜ 标签：peephole、常量折叠、字节码、成本工程

**问**：CPython 编译期会折叠哪些表达式、规则边界在哪？为什么 `2**32` 折叠而 `min(1, 2)` 不折叠？把常量提到模块级、写字面量、用"看起来聪明"的表达式，各自的运行时成本差多少？

**答**：
结论：peephole 优化在编译期做**纯函数且无异常路径的常量运算折叠**：字面量间的 `+ - * / ** << >> %`、字符串拼接（`"a" + "b"`）、常量元组/列表→tuple（如 `in (1, 2)` 转成常量 tuple）、`not` 常量、以及布尔/比较常量短路折叠。边界：**函数调用永不折叠**（`min(1,2)`、`abs(-1)` 留在运行时，因为不知道函数是否被重定义）、**跨语句不折叠**（变量赋值后的运算）、**可能抛异常的折叠会保守回退**（如大整数幂导致超限）。成本账：热循环里每次折叠失败的常量表达式都是一次字节码求值（BINARY_OP + 对象分配），模块级预计算把 N 次求值摊成 0 次——但注意模块级变量是全局查找，热循环内再局部化（`local = MODULE_CONST`）省 LOAD_GLOBAL。

取舍：不要为折叠做极端的"字面量化"（`0.2625` 这种魔法数字伤害可维护性，折叠收益纳秒级）；值得做的是**编译期可判的结构**：`if x in ("a", "b", "c")` 折叠成常量 tuple 比 `in ["a","b","c"]` 旧版本省一次列表构建（3.12+ 列表也会优化），而 `frozenset` 常量在 3.x 大多不折叠成 LOAD_CONST（构造留在运行时），高频路径应放模块级。

实战：用 `dis.dis` 验证折叠结果再决定优化；热路径常量三步走——模块级定义、函数入口局部化、循环外再提升；折叠器是版本相关的实现细节（3.11/3.12 均有调整），不要把行为当契约写进正确性逻辑。

```python
import dis, timeit

def folded():
    return 2 ** 32                      # 编译期折叠

def not_folded_call():
    return min(1, 2)                    # 函数调用，运行时求值

def not_folded_var():
    n = 10
    return n ** 32                      # 跨语句不折叠

def in_tuple():
    return "b" in ("a", "b", "c")       # 常量元组 -> LOAD_CONST

def in_frozenset():
    return "b" in frozenset(("a", "b")) # 构造留在运行时

for fn in (folded, not_folded_call, not_folded_var, in_tuple, in_frozenset):
    consts = [c for c in fn.__code__.co_consts if not hasattr(c, "co_code")]
    print(f"{fn.__name__:18} consts={consts}")

print("\n-- dis of folded --")
dis.dis(folded)

# 成本账：折叠 vs 运行时求值 vs 局部变量
t1 = timeit.timeit("2**32", number=10_000_000)                  # 字面量：解释器仍每次执行 BINARY_OP（交互态无编译折叠）
t2 = timeit.timeit("f()", number=10_000_000, globals={"f": folded})   # 折叠后：LOAD_CONST
t3 = timeit.timeit("min(1, 2)", number=10_000_000)
print("literal 2**32 : %.3fs   folded LOAD_CONST: %.3fs   min(1,2): %.3fs" % (t1, t2, t3))
```

**追问一**：折叠会不会改变语义？举一个被禁止的例子。——会的话就不折叠。例如 `1 << 10000` 会产生巨型整数，peephole 早期版本可能折叠出内存放大（CVE 级别问题），后续版本对"结果过大"加了上限保护并回退到运行时；同样 `0.1 + 0.2` 折叠与否必须与运行时逐位一致，否则同一表达式两个写法结果不同。

**追问二**：为什么 `in ("a","b","c")` 能折叠而 `in {"a","b","c"}`（set）大多不能？——tuple/list 是不可变字面量结构，可整体作为 co_consts 常量加载；set 构造涉及哈希计算与对象语义（元素可为可变上下文），编译器不保证求值等价，因此留在运行时。3.12 后对集合字面量有专门的成员测试优化指令，但机制不是折叠而是新 opcode。

## 背诵要点
- peephole 折叠"纯字面量、无异常路径"的算术/比较/字符串拼接与常量元组；函数调用与跨语句一律不折叠。
- 热路径常量：模块级定义 + 函数入口局部化（省 LOAD_GLOBAL）+ dis.dis 验证。
- 折叠是版本相关实现细节，可作为性能参考不可作为正确性依赖。

## 复盘追问
- 一个每秒百万次调用的校验函数里写着 `if x in ("A","B") and 1<<20 > x > 0`，如何评估并落地优化？（dis 看折叠、局部化、预计算掩码，讨论可读性折衷）
- 为什么不能把"peephole 是否折叠"写进代码评审 checklist？（版本升级会变，正确性应依赖语义而非编译产物）

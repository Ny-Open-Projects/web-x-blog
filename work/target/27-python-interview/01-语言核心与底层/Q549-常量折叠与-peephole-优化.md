---
title: [Q549] 常量折叠与 peephole 优化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q549 · 常量折叠与 peephole 优化

> 难度:★★★★ | 标签:字节码, 编译器

**问**:2**10 在字节码里是运行时算的还是常量?CPython 编译期做了哪些优化?

**答**:编译器的窥孔优化器在生成字节码后扫描:常量折叠(字面量间的算术/位运算,2**10 → 1024 进 co_consts;有保护,超长结果与除零不折叠)、相邻字符串字面量拼接、跳转调整、死代码删除(if False 分支)、unary not/not in 重写(如 x not in y 直接生成 CONTAINS_OP 反转标志,省一次 not)。能折叠的前提是「纯编译期可见的常量表达式」;变量参与就没有折叠,哪怕语义上可预计算。理解它可解释「为什么 sometimes id 相同」「为什么空 if 分支消失」这类现象。

```python
# file: code/01_语言核心与底层/q549_constant_folding.py
import dis
import types

def compute():
    x = 2 ** 10                 # 折叠为 1024
    y = 1 + 2 * 3               # 折叠为 7
    z = "ab" "cd"               # 相邻字面量拼接
    return x, y, z

if __name__ == "__main__":
    print(compute())
    consts = [c for c in compute.__code__.co_consts
              if not isinstance(c, types.CodeType)]
    print("folded consts:", consts)
    for ins in dis.get_instructions(compute):
        print(f"  {ins.opname:14s} {ins.argrepr}")
```

**追问**:1) 为什么字符串比较常量不折叠而算术折叠?——优化器只折叠「便宜且无副作用」的运算;字符串等值比较涉及任意长度与哈希策略,折叠收益不稳定,故保守跳过。2) 折叠的边界?——编译期只动常量子表达式(2*3、True and x 不折叠因为短路语义);过长的结果(如万位数字幂)有保护跳过,防编译期 DoS。3) 优化层级?——peephole 在字节码层做窥孔改写,3.10+ 部分优化上移到 AST/编译器两级;确认实际行为用 dis.dis 而不是猜。4) 生产陷阱?——在常量表达式里放副作用(3.7 前的折叠曾改变过副作用次数)——新版已防;以为断点会命中常量表达式;性能优化写「聪明的常量式」不如直接字面量,编译器早做了。

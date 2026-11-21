---
title: [Q474] f-string 与格式化迷你语言
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q474 · f-string 与格式化迷你语言

> 难度:★★☆☆ | 标签:字符串, 格式化

**问**:f"{x:>10.2f}" 里的格式规范是谁解析的?f-string 相比 format 快在哪?

**答**:冒号后的部分遵循「格式规范迷你语言」(PEP 3101 定义):[[填充]对齐][正负号][#][0][宽度][,][.精度][类型],由各类型的 __format__ 解析——数字支持进制与精度,datetime 支持strftime指令,自定义类实现 __format__ 可接入同一套语法。性能上 f-string 在编译期生成字节码直接取值拼接,省掉 format 方法的模板解析与分发;str.format 与 % 慢在运行时解析模板。f"{expr=}" 调试语法(3.8+)把表达式文本与求值结果一起输出。

```python
# file: code/01_语言核心与底层/q474_fstring_mini_language.py
import math
from datetime import datetime

value = 1234567.891
now = datetime(2026, 11, 1, 9, 30)

if __name__ == "__main__":
    print(f"{math.pi:.3f}")                    # 精度
    print(f"{value:,.2f}")                     # 千分位
    print(f"{value:+012.1f}")                  # 宽度 正号 补零
    print(f"{255:x} {255:#06x} {255:b}")       # 进制
    print(f"{now:%Y-%m-%d %H:%M}")             # datetime 指令
    print(f"{'left':<10}|{'right':>10}|{'center':^10}")
    print(f"{value:.2e}")                      # 科学计数
    print(f"{value=:.2f}")                     # 3.8 调试语法
```

**追问**:1) 自定义类如何参与这套迷你语言?——实现 __format__(self, spec) 并按 spec 分支;不想自定义就继承 int/float 的语义或直接委托 __format__ 给内部数值。2) f-string 快在哪一层?——编译期把插值表达式编成字节码,运行时零模板解析;str.format 每次解析模板串、% 走协议分发。3.12 的 PEP 701 重写 tokenizer,支持嵌套同类引号与多行表达式。3) __format__ 与 __str__ 的关系?——format(v, spec) 调 type(v).__format__;spec 为空默认委托 __str__,非空按类型解析。datetime 对 strftime 指令的支持就是 __format__ 接入迷你语言的范例。4) 生产陷阱?——f-string 直接嵌入用户可控表达式,任意属性访问有开销也有信息泄露面;日志热路径上复杂 f-string 即使级别关闭也白算,要用 lazy % 形式;拼 SQL 是注入源头,参数化查询不可替代。

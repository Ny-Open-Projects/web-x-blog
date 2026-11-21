---
title: [Q557] int 任意精度:大整数运算
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q557 · int 任意精度:大整数运算

> 难度:★★★☆ | 标签:int, 数值

**问**:Python 的 int 怎么做到无限大?大数运算的性能代价在哪?

**答**:int 是「数字数组」结构:小整数(单 digit,30 位)走快速路径,大整数是 digit 数组动态扩容,位数即数组长度,理论无上限(受内存与 3.11+ 的 str 转换 4300 位限制防 DoS)。性能:加减 O(位数)、乘法学校算法 O(位数²)、幂运算按需;sys.getsizeof 随位数增长(2**100 比 2**30 大)。3.11 引入 int↔str 转换的默认位数限制(4300),因为转换是平方级——处理超大数(密码学、竞赛)需要 sys.set_int_max_str_digits 调整或用 gmpy2;get/set_int_max_str_digits 这两个 API 也是 3.11+ 才有,低版本运行演示时该行打印说明跳过。哈希上大 int 取模质数,所以 hash(2**100) 仍是普通小数。

```python
# file: code/01_语言核心与底层/q557_big_int.py
import sys

if __name__ == "__main__":
    print("platform word:", sys.maxsize)
    big = 2 ** 200
    print("bits:", big.bit_length())
    print("sizeof 2**30 :", sys.getsizeof(2 ** 30))
    print("sizeof 2**200:", sys.getsizeof(big), "(digit array grows)")

    print("to bytes:", (2 ** 64).to_bytes(9, "big").hex())
    print("hash is small:", hash(big))
    if sys.version_info >= (3, 11):
        print("int max str digits limit:", sys.get_int_max_str_digits())
    else:
        print(f"该特性需要 Python 3.11+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")
```

**追问**:1) 为什么 int→str 转换要设限制?——转换是 O(n²) 的除法循环,攻击者构造数亿位的 int 转 str 可把单个请求打满 CPU(等于哈希 DoS 的算术版);限制是 3.11 的安全补丁,需要时显式放宽。2) 任意精度的底层实现?——PyLong 是 30-bit digit 数组加符号位,加减线性、乘除超阈值走 Karatsuba;运算全在 C 层,Python 层无溢出概念。3) 安全限制的形态?——3.11+ 默认 str/int 互转上限 4300 位,超出 ValueError;sys.set_int_max_str_digits 可调或置 0 关闭;只影响十进制转换,不影响算术。4) 生产陷阱?——解析外部大 ID/证书大数突然 ValueError,要显式放宽;JS 端 JSON 大整数被 float 化的跨语言问题;用 int 存 hash 后转 hex 的位宽假设错误。

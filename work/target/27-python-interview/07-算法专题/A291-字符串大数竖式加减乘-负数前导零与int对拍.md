---
title: "[A291] 字符串大数竖式加减乘：负数、前导零与 Python int 对拍，以及何时算作弊"
date: 2026-11-25
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A291 · 字符串大数竖式加减乘：负数、前导零与 Python int 对拍，以及何时算作弊

> 难度:★★★☆ | 标签:字符串, 大数运算, 竖式乘法, 边界处理, 对拍

**问**（笔试·编程题）：给定两个十进制字符串（可能带 `+`/`-`、前导零、长度到 200 位），实现 `add_str` 与 `mul_str`，不许用 `int()` 做大数运算：① 符号与绝对值分离：加法四种符号组合如何归约成「同号相加 / 异号相减」，减法如何复用加法；② 竖式加法/减法的进位与借位，为什么从低位往高位扫；③ 竖式乘法：`res[i+j+1] += a[i]*b[j]` 的下标映射，为什么最后统一处理进位，复杂度 O(n·m)；④ 归一化：`-0`、`+0`、`000123`、空串怎么统一成规范形式；⑤ 与 `str(int(a) + int(b))` / `str(int(a) * int(b))` 做 40 组随机 + 极值对拍，并说清为什么「先转 int 再算」在笔试里算作弊、在生产里却是正确答案。

**答**：① 分工与总体策略：本卡只讲「字符串上的竖式四则」，不涉及除法/取模（A206 正则、A244 文本 diff 都不相关）。先写 `_cmp_abs`、`_add_abs`、`_sub_abs` 三个纯绝对值原语，`add_str` 只做符号分派：同号 → 绝对值相加、符号沿用；异号 → 绝对值相减、符号跟绝对值大的一方；相等则返回 `"0"`。减法 `a - b` 直接转成 `add_str(a, _negate(b))`，**不单独写减法**，这样符号逻辑只有一处。② 竖式加法从末位往前扫，`carry` 初始 0，逐位 `s = da + db + carry`，当前位 `s % 10`、`carry = s // 10`，循环结束后 carry 还可能为 1，必须再补一位；减法（保证 `|a| ≥ |b|`）逐位 `d = da - db - borrow`，若 `d < 0` 则 `d += 10, borrow = 1`，否则 `borrow = 0`，最后 `lstrip('0')`。低位先算是因为进位/借位方向天然从低到高，反向扫需要预判高位，写不出来。③ 乘法不需要在双层循环里逐位进位：先 `res = [0]*(n+m)`，对每对 `(i,j)` 做 `res[i+j+1] += int(a[i]) * int(b[j])`，累加完再从 `res` 末尾向前统一 `res[k-1] += res[k] // 10; res[k] %= 10`——单次乘积累加不会超过 81×200，Python int 完全无溢出；下标 `i+j+1` 的来源是「`a[i]` 权重 `10^(n-1-i)`、`b[j]` 权重 `10^(m-1-j)`，乘积落在 `10^(n+m-2-i-j)`，对应 `res` 下标 `i+j+1`」。复杂度 O(n·m) 时间、O(n+m) 空间，200 位只有 4 万次内层循环。④ 归一化是本题最大的坑：解析时先记符号再 `lstrip('0')`，空串归一成 `"0"`；结果为 0 时统一返回 `"0"`（不能返回 `"-0"` 或 `"+0"`）；乘法任一因子为 0 直接短路返回 `"0"`，避免 `"000"×"123"` 产生一堆零再 strip。⑤ 对拍：`int()` 在 Python 3 里是任意精度，`str(int(a)*int(b))` 就是权威参考，40 组随机长度 1~60、随机符号与随机前导零，再加 200 位极值；**但笔试时不能用**——题面考的就是竖式与进位，直接 `int` 等于把题删了；生产里反而应该用 `int`，因为 CPython 的 `long` 用 30 位 limb 做 Karatsuba，比手写竖式快几个数量级且经过 decades 的测试，手写只应该出现在教学、嵌入式无大数库、或需要固定内存/无堆分配的场景。

```python
# 全部标准库；字符串大数加减乘（含符号/前导零），与 Python int 权威结果对拍
import random

def _cmp_abs(a, b):
    """比较两个已去符号、去前导零的数字串的绝对值。"""
    if len(a) != len(b):
        return -1 if len(a) < len(b) else 1
    return (a > b) - (a < b)

def _add_abs(a, b):
    i, j, carry, out = len(a) - 1, len(b) - 1, 0, []
    while i >= 0 or j >= 0 or carry:
        s = carry
        if i >= 0:
            s += int(a[i]); i -= 1
        if j >= 0:
            s += int(b[j]); j -= 1
        out.append(str(s % 10))
        carry = s // 10
    return "".join(reversed(out))

def _sub_abs(a, b):
    """要求 a >= b（绝对值），返回 a-b 的规范串。"""
    i, j, borrow, out = len(a) - 1, len(b) - 1, 0, []
    while i >= 0:
        d = int(a[i]) - borrow - (int(b[j]) if j >= 0 else 0)
        if d < 0:
            d += 10
            borrow = 1
        else:
            borrow = 0
        out.append(str(d))
        i -= 1
        j -= 1
    return "".join(reversed(out)).lstrip("0") or "0"

def _norm(sign, digits):
    digits = digits.lstrip("0") or "0"
    if digits == "0":
        return "0"
    return sign + digits

def add_str(a, b):
    a, b = a.strip(), b.strip()
    na, nb = a.startswith("-"), b.startswith("-")
    aa = a.lstrip("+-").lstrip("0") or "0"
    bb = b.lstrip("+-").lstrip("0") or "0"
    if na == nb:
        return _norm("-" if na else "", _add_abs(aa, bb))
    c = _cmp_abs(aa, bb)
    if c == 0:
        return "0"
    if c > 0:
        return _norm("-" if na else "", _sub_abs(aa, bb))
    return _norm("-" if nb else "", _sub_abs(bb, aa))

def mul_str(a, b):
    a, b = a.strip(), b.strip()
    na, nb = a.startswith("-"), b.startswith("-")
    aa = a.lstrip("+-").lstrip("0") or "0"
    bb = b.lstrip("+-").lstrip("0") or "0"
    if aa == "0" or bb == "0":
        return "0"
    res = [0] * (len(aa) + len(bb))
    for i in range(len(aa) - 1, -1, -1):
        for j in range(len(bb) - 1, -1, -1):
            res[i + j + 1] += int(aa[i]) * int(bb[j])
    for k in range(len(res) - 1, 0, -1):
        res[k - 1] += res[k] // 10
        res[k] %= 10
    out = "".join(map(str, res)).lstrip("0") or "0"
    return ("-" if na != nb else "") + out

if __name__ == "__main__":
    rng = random.Random(2911)

    def rand_num():
        n = rng.randint(1, 60)
        s = "".join(rng.choice("0123456789") for _ in range(n))
        if rng.random() < 0.3:
            s = "0" * rng.randint(1, 3) + s
        if rng.random() < 0.4:
            s = "-" + s
        elif rng.random() < 0.2:
            s = "+" + s
        return s

    # 1) 40 组随机加法 + 40 组随机乘法，与 int 权威结果对拍
    for _ in range(40):
        a, b = rand_num(), rand_num()
        assert add_str(a, b) == str(int(a) + int(b)), ("add", a, b)
        assert mul_str(a, b) == str(int(a) * int(b)), ("mul", a, b)
    print("大数对拍: 40 组随机加法 + 40 组随机乘法 vs Python int，全等 ✅")

    # 2) 符号矩阵：四种组合的加法 + 乘法符号规则逐条断言
    assert add_str("5", "3") == "8" and add_str("-5", "-3") == "-8"
    assert add_str("5", "-3") == "2" and add_str("-5", "3") == "-2"
    assert add_str("3", "-5") == "-2" and mul_str("-5", "3") == "-15"
    assert mul_str("-5", "-3") == "15"
    print("符号矩阵: 同号/异号/大减小/乘法符号 全过 ✅")

    # 3) 前导零与零的规范形：-0/+0/000 一律归成 "0"
    for z in ("0", "-0", "+0", "000", "-0000", ""):
        assert add_str(z, "0") == "0", z
        assert mul_str(z, "123") == "0", z
    assert add_str("000123", "-00023") == "100"
    assert mul_str("00012", "0003") == "36"
    print("归一化: 前导零/±0/空串 全部规范为 0 或去零结果 ✅")

    # 4) 极值：200 位全 9 相加/相乘、长度差悬殊、大数减小数
    big = "9" * 200
    assert add_str(big, big) == str(int(big) * 2)
    assert mul_str(big, big) == str(int(big) ** 2)
    assert add_str("1" + "0" * 199, "1") == "1" + "0" * 198 + "1"
    assert add_str("-" + big, "1") == str(-int(big) + 1)
    assert mul_str(big, "-1") == "-" + big
    print("极值: 200 位全 9 的加法/平方/悬殊长度/大减小 全过 ✅")

    print("对拍通过：字符串大数 80 组随机 + 符号矩阵 + 归一化 + 极值全绿")
```

**追问**：1) 为什么笔试题禁止 `int()`，这不是「有轮子不用」吗？—— 因为题目考的是**过程能力**：进位、借位、下标映射、符号归约、前导零，这些是「能否把一件事拆到机器层」的信号，用 `int` 只是调用了一个黑盒，信号为零。判断标准不是「有没有库」，而是**题面是否把该库定义成被考察对象**：如果题目是「实现一个计算器服务」，用 `int` 完全正确；如果题目是「实现大数乘法」，用 `int` 等于交白卷。面试里正确姿势是先问一句「允许用语言内置大数吗」，不允许再写竖式。2) 生产代码真的永远用 `int` 吗？—— 绝大多数是，但有三类例外：① 语言没有原生大数（C/Go 需引库），且场景只做加减（如金额字符串对账），手写竖式可避免引依赖；② 需要**固定内存/无动态分配**的嵌入式或内核态，竖式可按位流式处理；③ 需要**可审计的逐位中间结果**（如金融计息的每一步、教学演示）。除此之外手写没有性能优势：CPython 的 `int` 乘法对大数会用 Karatsuba，200 位就已比纯 Python 双层循环快，位数越大差距越大。3) 如果要求支持小数或科学计数法怎么办？—— 不要在原函数上打补丁，先把输入**规范化成「符号 + 整数串 + 小数点位置」三元组**（定点表示），加减乘都转成整数竖式，最后按小数点位置插回；除法则要单独定精度与舍入规则（这是另一道题）。核心原则是**符号、小数点、前导零三类「表示层」问题必须在进入竖式前剥离干净**，否则每个运算都要重复处理，必然漏分支——这也是本卡先写 `_norm` 与符号分派、再写三个绝对值原语的原因。

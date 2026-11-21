---
title: [Q329] numpy 广播机制
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q329 · numpy 广播机制

> 难度:★★★ | 标签:numpy, broadcasting

**问**:解释 numpy 的广播规则,并说明什么情况下会报错。

**答**:广播让不同形状的数组做运算:从末尾维度向前对齐,两维度相等或其中一方为 1 时可兼容,为 1 的一方沿该轴复制扩展;维度数不齐时短的在前面补 1。若从末尾对齐后某轴既不相等也都不是 1,则抛 ValueError。广播是零拷贝的"虚拟扩展",性能好但要小心它是逻辑复制,不会真的占内存,配合 reshape 与 np.newaxis 可以写出非常简洁的距离矩阵、归一化代码。

```python
# file: code/05_数据分析与工程化/q329_numpy_broadcast.py
try:
    import numpy as np
except ImportError:
    print("该题演示需要第三方库 numpy:pip install numpy,原理见正文")
    raise SystemExit(0)

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])          # shape (2, 3)
    b = np.array([10, 20, 30])         # shape (3,) -> (1, 3) 广播
    print(a + b)
    col = np.array([[100], [200]])     # shape (2, 1) 广播成 (2, 3)
    print(a + col)
    # 归一化:每列减去均值,广播经典用法
    print((a - a.mean(axis=0)) / a.std(axis=0))
    # 形状 (2, 3) 与 (2,) 不兼容 -> ValueError
    try:
        a + np.array([1, 2])
    except ValueError as e:
        print("expected error:", e)

if __name__ == "__main__":
    main()
```

**追问**:
- np.newaxis 有什么用?它在指定位置插入长度为 1 的轴,把一维数组变成行向量或列向量,是手动控制广播方向的工具。
- 广播失败的典型报错?——`ValueError: operands could not be broadcast together`,两轴既不相等也都不是 1;reshape/newaxis 补齐维度即可。
- 广播是复制数据吗?——不是,虚拟扩展零拷贝;但它会让某些「看似省内存」的运算物化大结果,如 (n,1)-(1,n) 产生 n×n 矩阵。
- broadcasting 的经典应用?——`a[:, None] - b[None, :]` 距离矩阵、按行归一化 `x / x.sum(axis=1, keepdims=True)`。

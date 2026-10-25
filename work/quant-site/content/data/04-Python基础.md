---
title: Python 基础
track: data
order: 4
summary: 变量与类型、list/dict、条件循环、函数、异常，用 Python 做数据分析的最小语法集。
---

# Python 基础

> 掌握 Excel/SQL/Tableau 已能应对入门分析；要更高效、可复用、自动化，就上 Python。

## 变量与基本类型

```python
name = "BTC"        # str
price = 100         # int
ratio = 0.618       # float
flag = True         # bool
print(price * ratio)   # 61.8
```

## 数据结构

```python
prices = [100, 90, 120]              # list：有顺序
prices.append(150); prices[0]         # 追加 / 索引

coin = {"symbol": "BTC", "price": 100}   # dict：key-value
coin["price"]                            # 100
```

## 条件与循环

```python
if price > 100: action = "sell"
elif price < 90: action = "buy"
else: action = "hold"

total = sum(p for p in prices)      # 循环/推导式求和
```

## 函数与异常

```python
def avg(xs):
    return sum(xs) / len(xs)

try:
    data = fetch(url)          # 网络/IO 可能失败
except Exception as e:
    print("失败：", e); data = None
```

> 数据分析常用的第三方库，`pandas`（处理表格）、`numpy`（数值计算）、`matplotlib`（绘图）、`requests`+`BeautifulSoup`（爬虫），都会在后续课程用到。

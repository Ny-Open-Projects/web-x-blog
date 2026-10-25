---
title: 第3课 · Python 编程基础
track: quant
order: 3
summary: 环境安装、基本类型、list/dict/字符串、条件与循环、函数、异常处理——量化编码的最小必备集。
---

# 第3课 · Python 编程基础

> 量化用 Python 实现。本课覆盖写策略前必须掌握的语法最小集，配合 PyCharm 边写边运行。

## 3.1 环境安装

- **Python**：官网下载（macOS 也可自带）；安装后配好 `python` 命令。
- **PyCharm**：写 Python 的 IDE（类似写 Word，不必有畏难情绪）。
- **第三方库**：量化核心是 `pandas`（数据分析）、`numpy`、`matplotlib`，用 `pip install pandas numpy matplotlib` 安装。

```bash
pip install pandas numpy matplotlib
```

## 3.2 基本类型与计算

```python
# 注释：程序不执行，用于说明用意（非常重要！）
price = 100          # int
ratio = 0.618        # float
name = "BTC"         # str
flag = True          # bool
print(price * ratio, name, flag)   # 61.8 BTC True
```

## 3.3 list / dict / 字符串

```python
# list：有顺序的一组对象，元素可不同类型
prices = [100, 90, 80, 120]
prices.append(150)           # 追加
print(prices[0], prices[-1]) # 100 150（索引/切片）

# dict：成对的 key-value
coin = {"symbol": "BTC", "price": 100, "vol": 12.5}
print(coin["symbol"], coin.get("price"))  # BTC 100

# 字符串：转义用反斜杠
s = 'what\'s wrong'
print(s.upper(), len(s))     # WHAT'S WRONG 13
```

## 3.4 条件语句与循环语句

```python
# 条件：不同条件执行不同代码（如根据行情决定买/卖）
price = 105
if price > 100:
    action = "sell"
elif price < 90:
    action = "buy"
else:
    action = "hold"
print(action)   # sell

# for 循环：重复的事交给循环
total = 0
for p in [100, 90, 120]:
    total += p
print(total)    # 310
```

## 3.5 函数

把一段完整功能封装起来反复调用：

```python
def sma(prices, n=5):
    """简单移动平均：最近 n 个收盘价的均值"""
    return sum(prices[-n:]) / n

print(sma([1, 2, 3, 4, 5, 6]))   # (2+3+4+5+6)/5 = 4.0
```

## 3.6 异常处理

实盘 7×24 运行时，网络抖动、交易所超时会偶发报错，**不能让程序因此崩溃**：

```python
try:
    data = fetch_from_exchange("BTC")   # 可能因网络失败
except Exception as e:
    print("取数失败，稍后重试：", e)
    data = None
finally:
    log("本轮取数结束")
```

> 小结：变量/类型 → list/dict/字符串 → 条件/循环 → 函数 → 异常处理，是写量化策略的最小语法集。重点体会**异常处理**——它是程序能长期稳定运行的关键。下一课用 pandas 玩转数据。

# 10. 字符串编码：bytes 与 str 的分工

> 分类：版本差异/编码 | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**str** / **bytes** / **encode** / **decode**
> 原文锚点：第 30~42 段「在 Python 2 里面默认的是字节…字节串是给计算机看的，unicode 是给人看的」

## 一句话总述
Python 3 彻底分离 **`str`（文本，给人看）** 与 **`bytes`（字节，给机器传）**；边界上只做两件事：**进来 decode、出去 encode**。

## 面试官视角
- **考察意图**：有没有被中文乱码折磨过——没踩过坑的人只能背结论。
- **P5** 知道 3 里 str 是 Unicode / **P6** 能说清"传输用字节、操作用文本" / **P7** 能定位 `UnicodeDecodeError` 的真实成因。
- **红旗**：① 说"Python 3 没有编码问题"；② 混用 `str` 与 `bytes` 拼接；③ 不知道 `encode`/`decode` 默认编码。
- **惊艳点**：Python 3 里 `str` 与 `bytes` **不能直接拼接**，会直接抛 `TypeError`——这道硬边界正是乱码问题的防火墙 `[经验]`。

## 主问答
**Q：Python 3 里字符串和字节串怎么区分？实际开发怎么处理编码？**
**A：**
1. **先给结论**：`str` 是 Unicode 文本、`bytes` 是字节序列；**读入即 decode，写出即 encode**，中间一律用 `str` 操作。
2. **再给机制**：`str.encode()` 默认按 UTF-8 编码成 `bytes`，`bytes.decode()` 逆向还原；Python 2 的 `str` 默认就是字节、需要 `u""` 才是 Unicode，这正是 2 时代编码噩梦的根源 `[经验]`。
3. **最后给边界**：3 里两者不可隐式转换，拼接会直接报错；只有**显式** `encode`/`decode` 才能跨过这条边界，乱码几乎都源于在边界上用错了编码。
**加分层**：文件与网络 IO 都要**显式指定 encoding**，依赖系统默认（`locale.getpreferredencoding`）在跨机器部署时会忽然翻车。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | str 和 bytes 是什么 | 概念 | 文本 vs 字节 | 换题 |
| L2 | 怎么互相转换 | 机制 | encode / decode | 判 P5 |
| L3 | 默认编码是什么 | 细节 | UTF-8 | 判 P6 |
| L4 | 混用会怎样 | 边界 | TypeError | 判 P6+ |
| L5 | 线上乱码怎么定位 | 实战 | 查边界处的编码 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x 全系 | Python 2 的 `str` 即字节，`unicode` 需 `u""` 前缀 | 按"文本/字节二分 + 边界显式转换"答，并点出 2 的历史包袱 |

## 关键代码
```python
s = "中文"
b = s.encode("utf-8")      # str -> bytes，网络传输/落盘前
print(type(b), b)          # <class 'bytes'> b'\xe4\xb8\xad\xe6\x96\x87'
print(b.decode("utf-8"))   # bytes -> str，读入后
```

## ⚠️ 原文纠错
未发现技术错误。原文「字节串给计算机看、Unicode 给人看、传输时 encode、操作时 decode」的总结正确；机翻中的术语拼写错误已还原为 `unicode` / `encode` / `decode`。

## 总结与追问预判
- 文本与字节二分，边界必须显式转换。
- 下一题：见 9（print 差异）、11（除法差异）。

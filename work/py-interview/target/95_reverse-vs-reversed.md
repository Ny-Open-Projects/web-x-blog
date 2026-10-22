# 95. list.reverse() 与 reversed()：一个原地、一个返回新序列

> 分类：Python 语言/内置方法 | 难度：L1 | 题型：八股题 | 频率：中 | 关键词：**原地** / **返回值** / **迭代器** / **None**
> 原文锚点：第 21~24 段「使用 reversed 我们得到的是一个新序列，s 本身并没有被修改；而 s.reverse() 就把 s 改成了倒序」

## 一句话总述
`list.reverse()` 是**原地反转、返回 `None`**；`reversed(s)` 是**内置函数、返回一个反向迭代器、不改原对象**；想要新列表就写 `list(reversed(s))` 或切片 `s[::-1]`。

## 面试官视角
- **考察意图**：考**可变/不可变与返回约定**的基本功，这是 Python 高频送分题，也是常见踩坑点。
- **P5** 分不清两者 / **P6** 说清"一个原地一个新建" / **P7** 还能解释为什么内置方法普遍返回 `None`（**命令-查询分离**，提醒你发生了原地修改）`[经验]`。
- **红旗**：① 写 `s = s.reverse()` 结果拿到 `None`；② 以为 `reversed()` 返回列表直接 `len()`；③ 对字符串调 `.reverse()`（`str` 没有这个方法）。
- **惊艳点**：`reversed()` 是**惰性迭代器**，只在遍历时才产出，对超大序列更省内存；切片 `s[::-1]` 则立即生成**新列表**。验证：`reversed([1,2,3])` 打印出来是 `list_reverseiterator` 对象 `[实测]`。

## 主问答
**Q：`list.reverse()` 和 `reversed()` 有什么区别？**
**A：**
1. **归属与返回**：`reverse()` 是 **list 的方法**，原地修改列表并**返回 `None`**；`reversed()` 是**内置函数**，接受任意序列，返回一个**反向迭代器**，原对象不变。
2. **用法**：要新列表就 `list(reversed(s))` 或 `s[::-1]`；要原地就 `s.reverse()`，且**不要写 `s = s.reverse()`**（会得到 None）。
3. **注意**：字符串是**不可变**类型，没有 `reverse()` 方法；`reversed("abc")` 返回迭代器，需 `''.join(...)` 拼回字符串。
**加分层**：Python 的可变对象原地方法（`sort`/`reverse`/`append`）普遍返回 `None`，这是刻意设计——**用返回值提醒调用者这是原地操作** `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 两者区别 | 概念 | 原地 vs 新序列 | 换题 → 不及格 |
| L2 | reverse() 返回什么 | API | None | 判 P5 |
| L3 | reversed() 返回什么 | API | 迭代器 | 判 P6 |
| L4 | 字符串能用吗 | 类型 | str 无 reverse() | 判 P6+ |
| L5 | 为什么返回 None | 设计 | 命令-查询分离 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x | `list.reverse()` 返回 None | 别赋值给原变量 `[实测]` |
| Python 3.x | `reversed()` 返回迭代器 | 需 list() 或 join() 物化 |
| Python 3.x | 支持 `__reversed__` 协议的自定义类 | 可被 reversed() 消费 |

## 关键代码
```python
s = list("abc")
print(s.reverse())              # None —— 原地方法不返回列表
print(s)                        # ['c', 'b', 'a'] —— 原对象已改

t = list("abc")
r = reversed(t)
print(r, t)                     # <list_reverseiterator object> ['a','b','c']
print(list(r))                  # ['c', 'b', 'a'] —— 迭代器需物化
print(t[::-1], t)               # ['c','b','a'] ['a','b','c'] —— 切片不改原对象

word = "abc"
print("".join(reversed(word)))  # cba —— str 不可变，只能拼回新字符串
```

## ⚠️ 原文纠错
原文"`reversed(s)` 返回新序列且原 `s` 不变、`s.reverse()` 原地修改 s"的观察正确，予以保留；需补充一点：原文演示中写成 `list(reversed(s))` 强转才得到列表，`reversed()` 本身返回的是**迭代器**而非列表，卡面已按实际行为表述。转写中的音译词已还原为标准术语。

## 总结与追问预判
- `reverse()` 原地返回 None；`reversed()` 返回迭代器不改原对象。
- 下一题：见 94（原地反转字符串）、96（回文数）。

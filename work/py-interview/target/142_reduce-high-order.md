# 142. 高阶函数 reduce：把序列规约为单一值，位于 functools

> 分类：编程范式/函数式 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**reduce** / **规约** / **functools** / **累积**
> 原文锚点：第 17~22 段「reduce 接收 function、序列、初始值，把前次结果不断应用到后面（规约）；Python3 移到 functools」

## 一句话总述
**`reduce(fn, seq, init)`** 用二元函数 `fn` 把序列**从左往右规约**成单一值（`fn(前次结果, 当前元素)`）；**Python 3 中它从内置移到了 `functools.reduce`**。

## 面试官视角
- **考察意图**：考你是否知道 `reduce` 的**位置变化**（Py2 内置 → Py3 functools）以及它的"累积"语义，而不是把它当普通循环。
- **P5** 能写出 `reduce(lambda a,b: a+b, range(1,6))` 求 1~5 和 = 15 / **P6** 能说明**累积顺序**（先 `1+2`，结果再 `+3`…）与 **init 初始值**的作用，并指出 Py3 需 `from functools import reduce` / **P7** 能指出**多数求和/累积应直接用 `sum`/`for`**，reduce 可读性差，仅在特定归并（如把 list 摊平成结构）才划算 `[经验]`。
- **红旗**：① 以为 `reduce` 仍是内置（Py3 在 functools）；② 不知道初始值的意义；③ 用 reduce 做本可 `sum()` 的求和（过度使用）。
- **惊艳点**：`reduce` 的累积本质是**左折叠**——`reduce(f, [a,b,c]) == f(f(a,b), c)`。验证：求和例子结果与 `sum(range(1,6))` 一致 `[实测]`。

## 主问答
**Q：reduce 是干嘛的？为什么它在 functools 里？**
**A：**
1. **结论**：`reduce` 把二元函数**反复作用**于序列，把多值"折叠"成一个值；Py3 因不常用把它从内置挪到 `functools`。
2. **机制**：每次拿"上一次结果"和"下一个元素"喂给 `fn`（`fn(acc, x)`），可选 `init` 作为初始累加器；如 `reduce(add, 1..5)` = `((1+2)+3)+4)+5` = 15。
3. **边界**：简单求和用 `sum()` 更快更清晰；reduce 适合真正需要**自定义归并**的场景，别为用而用。
**加分层**：`init` 还能决定"空序列时返回什么"，避免 `TypeError`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | reduce 干嘛 | 概念 | 规约成单值 | 换题 → 不及格 |
| L2 | 在哪导入 | 版本 | functools | 判 P5 |
| L3 | 累积顺序 | 机制 | 左折叠 | 判 P6 |
| L4 | init 作用 | 深入 | 初始值/空序列 | 判 P6+ |
| L5 | 何时不用 | 判断 | sum/for 替代 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 2 | reduce 为内置 | 旧代码无需导入 |
| Python 3 | 移至 functools | from functools import reduce |
| 求和 | sum 优先 | 非自定义归并别用 reduce |

## 关键代码
```python
from functools import reduce
s = reduce(lambda a, b: a + b, range(1, 6))   # 1+2+3+4+5
print(s)                            # 15 —— 等价于 sum(range(1,6))
```

## ⚠️ 原文纠错
原文"reduce 在 Python3 里转移到 functools；接收 function、序列、初始值，把前次结果每次应用到后面（规约），求和例子 1+2+3+4+5=15"——准确（机翻"functiontooth"=**functools**，"lambrange"=**lambda range**）。原文"它返回的结果"未明说返回迭代器（reduce 返回单值，不适用惰性），正确。原文未强调"Py3 需从 functools 导入"这一版本翻转点（仅说"转移"），已在版本节明确；也未提"简单求和应优先 sum()"，已在加分层与 P7 补充 `[经验]`。无事实错误，仅部分机翻音译需还原。

## 总结与追问预判
- `reduce` 左折叠归约，Py3 在 functools；简单求和用 `sum`。
- 下一题：**闭包本质**（143）、**map/filter**（140/141）。

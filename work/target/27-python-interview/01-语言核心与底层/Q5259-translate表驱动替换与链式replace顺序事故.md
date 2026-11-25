---
title: "[Q5259] translate 表驱动替换 vs 链式 replace：单遍扫描与级联顺序事故"
date: 2026-11-25
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5259 · translate 表驱动替换 vs 链式 replace：单遍扫描与级联顺序事故

难度：P6 ｜ 标签：str.translate、maketrans、replace、级联替换、单遍扫描、脱敏、多字符替换

**问**：一个日志脱敏函数写了 12 条 `text = text.replace(a, b)`，某天把手机号规则从 `1xxxxxxxxxx → ***` 改成"先遮区号再遮尾号"，结果中间几位被第二条规则二次替换，输出多出一串星号；另一次把 20 条规则改成 `translate` 后速度快了一个量级，但"把 `ab` 替换成 `X`"这条规则怎么都写不出来。`translate` 和链式 `replace` 的语义差异到底在哪？哪些替换它根本表达不了？

**答**：

- **结论**：`str.replace` 是"**逐条、全文、可级联**"：每条规则独立扫描一遍，前一条的输出是后一条的输入，所以规则之间会互相影响，结果依赖顺序；k 条规则就是 k 遍 O(n)，最坏 O(n·k)。`str.translate(table)` 是"**单遍、按字符查表**"：从左到右扫一遍，每个字符的码点去 table 里查目标（`str`、码点 `int` 或 `None`），命中就替换/删除，不命中原样输出；每个字符只被处理一次，**不会级联**——`{a: "b"}` 作用在 `"ab"` 上得到 `"bb"`，不会再把新产生的 `b` 变成别的。table 可以映射到**多字符串**（`ord("a") → "XY"`）或 `None`（删除），但**键必须是单个码点**：`{"ab": "X"}` 这种多字符源在 `maketrans` 阶段就会被拒绝；`None` 键/值、以及"按子串匹配"都不支持，后者只能用 `re.sub` 或自己写扫描。

- **取舍**：a) 规则之间**语义独立**（每个字符的替换不依赖其他规则的结果）时用 `translate`：单遍、O(n)、无顺序依赖，10+ 条规则时通常比链式 `replace` 快数倍；b) 规则有**优先级/级联**语义时（先转义 `&` 再转义 `<`，或先删前缀再匹配后缀）必须用链式 `replace`/`re.sub`，并且把顺序写进注释和测试；c) 需要"多字符源 → 单字符"或"正则模式"时用 `re.sub`，`str.replace` 只能做字面量、`translate` 只能做单字符；d) table 的构建成本要摊销：`str.maketrans` 每次调用都建 dict，热路径应在模块级建一次；`maketrans("abc", "xyz")` 的两参数形式要求两个串等长，三参数形式第三个串是"要删除的字符集"。

- **实战**：事故形态是"脱敏规则从 3 条加到 12 条后，输出长度翻倍"——规则 `("1", "*")` 把手机号首位变成 `*`，后面的规则 `("*", "")` 本意是删掉原文里的星号，结果把刚生成的 `*` 也删了；再往后 `("", "-")` 之类的空串规则更是灾难（`replace("", "-")` 会在每个字符间插入）。修复：把"字符级、互不影响"的规则合并成一张 `maketrans` 表（`1-9 → *`、删除控制字符用 `None`），把"子串/正则"规则单独用 `re.sub` 并显式排序；加一条性质测试"对同一输入，脱敏结果不随规则列表的排列顺序变化"（字符级规则才应满足），把级联依赖暴露出来。

```python
# translate 单遍不级联 vs 链式 replace 的级联/顺序依赖
import re
import time

cascade = "ab".replace("a", "b").replace("b", "c")
single = "ab".translate({ord("a"): "b"})
print("→ 链式 replace:", cascade, "| translate:", single)
assert cascade == "cc"          # 第一条产生的 b 被第二条继续替换
assert single == "bb"           # 每个原字符只处理一次

# 映射到多字符串 / 删除
table = {ord("a"): "XY", ord("b"): None, ord("c"): "中"}
out = "abc".translate(table)
print("→ 多字符目标与删除:", out)
assert out == "XY中"

# maketrans 三种形态
assert "abc".translate(str.maketrans("abc", "xyz")) == "xyz"
assert "abc".translate(str.maketrans({"a": "1"})) == "1bc"
assert "abc".translate(str.maketrans("abc", "xyz", "b")) == "xz"   # 第三参删除
print("→ maketrans 等长映射/字典/删除三形态均可用")

# 多字符源无法用 translate 表达
bad = ""
try:
    str.maketrans({"ab": "X"})
except ValueError as e:
    bad = str(e)
    print("→ 多字符键被拒绝:", e)
assert "length 1" in bad

sub = re.sub(r"ab", "X", "abab")
print("→ 多字符源只能用 re.sub:", sub)
assert sub == "XX"

# 单遍 vs 多遍: 规则越多, translate 的优势越大
text = "abcdefghij" * 20_000        # 20 万字符
rules = [(c, c.upper()) for c in "abcdefghij"]

t0 = time.perf_counter()
s1 = text
for a, b in rules:
    s1 = s1.replace(a, b)
d_replace = time.perf_counter() - t0

t0 = time.perf_counter()
s2 = text.translate({ord(a): b for a, b in rules})
d_translate = time.perf_counter() - t0

print("→ 20 万字符 x 10 条规则: replace", round(d_replace, 4), "s | translate", round(d_translate, 4), "s")
assert s1 == s2
assert d_translate < d_replace      # 10 遍扫描 vs 1 遍扫描

# 空串 replace 是经典陷阱: 每个字符间都插入
assert "ab".replace("", "-") == "-a-b-"
assert "ab".translate({ord("a"): ""}) == "b"   # translate 删字符用 None, 不是空串
```

**追问一**：为什么 `translate` 的键必须是单个码点，而不能是子串？—— 它的实现是"按字符查表"：内部对每个字符取 `Py_UCS4` 码点，直接索引一张按码点组织的映射（dict 或序列），一次查表决定输出；如果允许子串键，就必须在当前位置尝试所有长度的前缀（Trie/AC 自动机），那就退化成"多模式串匹配"，复杂度和 API 都完全不同。标准库把这件事留给 `re.sub`（正则引擎）或第三方 `pyahocorasick`。这也解释了为什么 `translate` 对"字符集替换/删除/音译"特别快：O(n) 次哈希查找，没有回溯、没有分配中间串；而"敏感词/多字符 token 替换"必须用自动机或正则。

**追问二**：`str.maketrans` 的三种形态分别适合什么？为什么"空串替换"在 replace 里是灾难、在 translate 里却不是？—— 三种形态：①两参数 `maketrans(from, to)`：等长字符串，逐字符映射，适合 Caesar/ROT13；②单参数 dict：`{ord: str|None}` 或 `{char: str|None}`（会自动转 ord），适合规则表来自配置/数据库；③三参数 `maketrans(from, to, delete)`：映射 + 删除一组字符，适合清洗控制字符。`replace("", x)` 的语义是"在每个字符边界（包括首尾）插入 x"，长度 n 的串会产生 2n+1 个片段，既慢又几乎不是业务想要的；`translate` 里删除字符用 `None`，空串目标没有特殊语义（映射到空串等于删除该字符），所以不会出现"边界插入"。

## 背诵要点

- `replace` 逐条全文、可级联、顺序敏感，k 条规则 O(n·k)；`translate` 单遍按码点查表、不级联、O(n)。
- `translate` 的键必须是单码点，值可为多字符串或 `None`（删除）；多字符源/正则模式用 `re.sub`。
- `maketrans` 三形态：等长映射、dict 表、第三参删除；空串 `replace` 会在每个边界插入，是事故源。

## 复盘追问

- 为什么 `"ab".replace("a","b").replace("b","c")` 得到 `"cc"` 而 `translate` 得到 `"bb"`？（replace 的输出是下一条的输入；translate 每个原字符只查一次表）
- 12 条脱敏规则该怎么拆分？（字符级、互不影响的合并成一张 maketrans；子串/正则规则单独 re.sub 并显式排序，加顺序无关性测试）

---
title: [Q5112] re.sub 反向引用注入事故
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5112 · re.sub 反向引用注入事故

> 难度:★★★★☆ | 标签:事故复盘, 正则, 安全

**问**:模板渲染函数里写 `re.sub(pattern, user_input, text)`，用户把"替换文本"填了 `\g<0>`，结果输出里出现了整段被匹配的内容甚至报 `invalid group reference`。这是怎么回事？怎么安全地让用户输入作为字面替换文本？

**答**:结论：`re.sub` 的第三个参数 **repl 不是纯字符串，而是"模板"**：其中 `\1`、`\g<name>`、`\g<0>` 会被解析为反向引用/组引用，`\n`、`\\` 等也会被转义处理。所以把用户输入直接当 repl 有两个风险：a) **注入**：`\g<0>` 展开为整个匹配，`\1` 展开为第 1 组，能拼出构造者预期的内容（如把黑名单词替换回原文绕过过滤）；b) **崩溃**：非法引用（`\9` 超出组数、孤立反斜杠）抛 `re.error`。解法不是自己转义反斜杠（容易漏 `\g<>` 等形式），而是用标准库给出的逃生门：`repl` 为**可调用对象**时，函数返回值按字面使用、不做模板展开——`lambda m: user_input` 即可。另一种官方方式是 `m.expand()` 只在确要模板语义时使用。取舍：函数式 repl 少一次模板解析，性能差异可忽略，语义却完全安全；唯一代价是放弃了模板能力——若产品本身需要"支持用户引用捕获组"，应白名单校验引用编号上限并 try/except 包住 expand。

```python
import re

text = "订单号: 2024-001，金额: 999 元"
pat = re.compile(r"\d{4}-\d{3}")

# 事故一：用户输入含 \g<0>，引用注入展开
evil = r"\g<0> **已作废**"
print(re.sub(pat, evil, text))       # 订单号: 2024-001 **已作废** ...原值复活了

# 事故二：非法引用直接崩
try:
    re.sub(pat, r"\g<9>", text)
except re.error as e:
    print("re.error:", e)

# 正确：repl 传函数，返回值按字面替换、零模板解析
user_input = r"\g<0> **已作废**"
print(re.sub(pat, lambda m: user_input, text))   # 字面输出 \g<0>，无展开

# 等价字面转义（若必须用字符串 repl）：只对反斜杠动手
escaped = user_input.replace("\\", r"\\")
print(re.sub(pat, escaped, text))                # 与函数式等价

# 确要支持组引用时的护栏：限制引用范围 + 兜底
def safe_expand(m, tpl):
    return re.sub(r"\\g<(\d+)>", lambda g: m.group(int(g.group(1)))
                  if int(g.group(1)) <= (m.re.groups or 0) else "", tpl)
print(safe_expand(pat.search(text), r"单号 \g<0>"))
```

**追问一层**:为什么 `re.sub(pat, user_input.replace("\\", "\\\\"), ...)` 这种手转义在多数字场景可靠、却仍不推荐？还有哪些 repl 模板语法要防？
**追二层**:`m.expand()`、`re.sub` 的模板解析共用什么实现？`\g<name>` 命名组的解析规则里，为什么 `\g<1>0` 与 `\g<10>` 有歧义而 `\g<01>` 没有？

**背诵要点**
- repl 是模板不是字符串：`\1`/`\g<name>`/`\g<0>` 展开引用，非法引用抛 re.error。
- 用户输入作替换文本一律用函数式 repl（`lambda m: s`），字面安全且免转义。
- 手工转义只处理反斜杠即可字面化，但函数式更不易漏。

**复盘追问**
- 这类注入在"敏感词过滤"场景会造成什么实际危害？提示：`\g<0>` 让被过滤词原样复活。
- 团队规范应落在哪个层？提示：linter 规则 + 替换函数封装 `literal_sub(pat, repl, text)`。

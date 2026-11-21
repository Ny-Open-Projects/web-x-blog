---
title: [Q5050] t-string 模板字符串与注入防护演进
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5050 · t-string（PEP 750，3.14）与注入防护的演进

> 难度:★★★☆ | 标签:t-string, PEP 750, 版本演进, 注入防护, 3.14

**问**：PEP 750 给 3.14 带来模板字符串（t-string）。它和 f-string 的本质区别是什么？为什么说它瞄准的是"f-string 时代的注入事故"？在 3.11/3.12 环境里如何写出兼容的降级实现？

**答**：f-string 在**调用点立即求值**为普通 str——字符串一旦生成，"哪里是模板、哪里是插值"的信息全部丢失，所以 SQL/HTML/shell 拼接场景无法在下游做安全检查，注入防护只能靠每个调用点自觉（参数化查询、转义）。t-string（`t"...{value}..."`）语法与 f-string 同构，但**不求值成 str**，而是产生 `string.templatelib.Template` 对象：静态片段（strings 元组）与插值（interpolations：表达式值 + 格式规格 + 转换）**结构化共存**。下游库拿到 Template 后可以：先检查每个插值的语义（SQL 驱动校验它是不是占位符位置、HTML 引擎自动转义插值、shell 包装拒绝插值），再决定渲染——**把"防护"从调用点自觉下沉到渲染方强制**，这是它对标"SQL 注入事故"的设计意图。版本演进脉络：% 格式化（C 时代遗产）→ str.format（运行时解析，format 注入面，Q5047）→ f-string（编译期，快但丢了结构）→ t-string（编译期语法 + 结构化运行时对象）。降级实现（3.9-3.13 无 `string.templatelib`）：自己定义一个最小 Template 类模拟 (strings, interpolations) 结构，用轻量 DSL（括号占位）保持下游接口一致，3.14 上线后无缝切换真 t-string。

```python
# file: code/01_语言核心与底层/q5050_tstring.py
import sys
print("python:", sys.version_info[:3])

try:
    from string.templatelib import Template, Interpolation   # 3.14+
    HAVE_TSTRING = sys.version_info >= (3, 14)
except ImportError:
    HAVE_TSTRING = False

# ---------- 3.9-3.13 的最小降级实现: 模拟 Template 结构 ----------
class Interp:
    def __init__(self, value, expr, conv=None, spec=""):
        self.value, self.expr, self.conversion, self.format_spec = value, expr, conv, spec

class FakeTemplate:
    """t-string 的结构化形态: 静态片段与插值共存, 不预渲染"""
    def __init__(self, strings, interpolations):
        self.strings = tuple(strings)
        self.interpolations = tuple(interpolations)

def t(template_str, **vals):
    """降级 DSL: '{name}' 占位 -> 结构化 Template"""
    strings, interps, buf, i = [], [], "", 0
    while i < len(template_str):
        j = template_str.find("{", i)
        if j < 0:
            buf += template_str[i:]; break
        buf += template_str[i:j]
        k = template_str.index("}", j)
        name = template_str[j + 1:k]
        strings.append(buf); buf = ""
        interps.append(Interp(vals[name], name))
        i = k + 1
    strings.append(buf)
    return FakeTemplate(strings, interps)

# ---------- 渲染方强制防护: 插值不允许携带引号/分号 (SQL 场景演示) ----------
def render_sql(tpl):
    parts = [tpl.strings[0]]
    for interp, tail in zip(tpl.interpolations, tpl.strings[1:]):
        v = str(interp.value)
        if any(c in v for c in "'\";"):
            raise ValueError(f"插值 {interp.expr!r} 非法, 必须走参数化")
        parts.append(v + tail)
    return "".join(parts)

user = "o'; DROP TABLE orders;--"
tpl = t("SELECT * FROM orders WHERE owner = '{owner}'", owner=user)
try:
    render_sql(tpl)
except ValueError as e:
    print("渲染方拦截注入:", str(e)[:45])

# 若是 f-string, 到下游已是成品字符串, 上述检查无从下手:
print("f-string 下游只能看到:", f"owner = '{user}'"[:35], "... 无结构可查")

if HAVE_TSTRING:                            # 仅 3.14+: 本机 3.12 走 else 分支
    # 真语法: real = t"SELECT * FROM orders WHERE owner = '{user}'"
    print("3.14 真模板: Template(strings, interpolations) 结构化对象")
else:
    print("3.14 前降级: 结构一致(静态片段/插值分离), 上线切换零改动")
```

**追问**：1) Template 对象为什么设计成不可迭代也不可拼接成 str？——防止用户"顺手"把它当字符串用（隐式渲染绕过防护），强制走显式渲染函数；这是"能力最小化"在类型设计上的体现。2) t-string 与 Jinja2 这类模板引擎的分工？——t-string 是**语言级内联**模板（片段就在调用代码里、表达式是真实 Python 表达式），Jinja2 是外部模板文件 + 沙箱语言；前者适合 SQL/HTML 片段级防护，后者适合页面级渲染，不互替。3) 为什么 PEP 750 迟迟才落地而 f-string 早就有了？——难点在插值结构（expression 字符串、conversion、format_spec）与延迟求值语义的标准化，以及生态（DB API、HTML 库）尚需约定渲染协议；3.14 先给原语，渲染方生态随后跟进。

## 背诵要点
- f-string 立即求值成 str，丢失模板结构 → 注入防护只能在调用点；t-string 产生结构化 Template（strings + interpolations）。
- 渲染方拿到结构可强制校验/转义/拒绝插值——防护从调用点自觉下沉为渲染方强制。
- 3.9-3.13 降级：自建最小 Template 结构（占位 DSL），3.14 切真语法接口不变。

## 复盘追问
- 你的 ORM 查询接口如何用"结构化模板"重构，让 SQL 注入在类型层面不可能？（提示：只接受 Template + 渲染器白名单，禁止裸 str 进入拼接层）
- 团队从 f-string 全面切 t-string 的迁移成本主要在哪里？（提示：下游渲染函数的生态覆盖、与 % 惰性日志的关系、3.14 基线之前的降级层维护）

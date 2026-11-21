---
title: [Q2027] 模板组合渲染:include 递归与循环包含检测
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2027 · 模板组合渲染:include 递归与循环包含检测

> 难度:★★★☆ | 标签:Agent, 模板, 图结构

**问**:系统提示越做越大,你们把公共段落抽成子模板互相 include,这会引入什么新故障?

**答**:模板组合本质是把图结构引入渲染,新故障有三类:循环包含让渲染递归爆栈;包含深度超限,模板里可能被埋了极深链条;引用缺失,占位的子模板不存在。渲染器维护包含栈,进入子模板前先查栈,命中即报循环并列出完整路径,同时设深度上限兜底;缺失模板显式报错而不是渲染出空段落。这三类错误都该在 CI 的模板单测里暴露,而不是线上渲染时才发现。演示里 a 引 b、b 引 a,报错直接给出 a 到 b 再到 a 的环路径。

```python
# file: code/06_Agent与LLM及系统设计/q2027_template_include.py
"""模板组合渲染:include 递归展开,栈检测循环包含与深度超限。"""
import re

INCLUDE_RE = re.compile(r"\{%\s*include\s+(\w+)\s*%\}")
MAX_DEPTH = 8


def render(templates, root, values, _stack=None, _depth=0):
    _stack = _stack or []
    if root in _stack:
        cycle = " -> ".join(_stack + [root])
        raise ValueError("循环包含:" + cycle)
    if _depth > MAX_DEPTH:
        raise ValueError("包含深度超过上限 %d" % MAX_DEPTH)
    if root not in templates:
        raise ValueError("模板 %s 不存在" % root)
    body = templates[root]

    def sub(m):
        return render(templates, m.group(1), values, _stack + [root], _depth + 1)

    out = INCLUDE_RE.sub(sub, body)
    for k in sorted(values):
        out = out.replace("{{" + k + "}}", str(values[k]))
    return out


if __name__ == "__main__":
    templates = {
        "base": "{% include header %}\n{{content}}\n{% include footer %}",
        "header": "【{{title}}】",
        "footer": "—— {{team}}",
    }
    out = render(templates, "base", {"title": "客服手册", "team": "平台组",
                                     "content": "正文第一段"})
    assert "【客服手册】" in out and "正文第一段" in out and "—— 平台组" in out
    assert "include" not in out, "渲染后不得残留 include 指令"

    # 循环包含:a 引 b b 引 a
    loop = {"a": "A {% include b %}", "b": "B {% include a %}"}
    try:
        render(loop, "a", {})
        raise AssertionError("循环包含必须报错")
    except ValueError as e:
        assert "循环包含" in str(e) and "a -> b -> a" in str(e)

    # 深度超限:一条长链
    chain = {"t0": "{% include t1 %}"}
    for i in range(1, 12):
        chain["t%d" % i] = "{%% include t%d %%}" % (i + 1)
    try:
        render(chain, "t0", {})
        raise AssertionError("深度超限必须报错")
    except ValueError as e:
        assert "深度" in str(e)

    try:
        render(templates, "ghost", {})
        raise AssertionError("缺失模板必须报错")
    except ValueError as e:
        assert "不存在" in str(e)
    print("组合渲染通过:递归展开正常,循环 链超长 缺失三类结构错误全拦截")
```

**追问**:
- 循环包含能不能自动剪? 答:可以按同一模板同层只展开一次去重,但语义更危险,默认拒绝、显式开启才放行
- 变量替换放在哪一层? 答:每层只替换自己的变量,父层不越权替换子层未声明的占位符,避免变量泄漏

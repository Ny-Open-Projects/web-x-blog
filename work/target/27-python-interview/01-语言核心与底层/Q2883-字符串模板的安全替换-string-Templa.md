---
title: [Q2883] 字符串模板的安全替换:string.Template 与 safe_substitute
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2883 · 字符串模板的安全替换:string.Template 与 safe_substitute

> 难度:★★☆☆☆ | 标签:string.Template, 模板, 安全

**问**:要让用户编辑一段带占位符的模板文本再渲染,用 str.format 安全吗?标准库有什么更合适的选择?

**答**:用户可编辑的模板不要用 `str.format`——format 的占位符支持属性路径与下标,`{0.__class__}` 这类写法能从格式串触达对象内部,历史上是真实的模板注入漏洞。标准库的正确答案是 `string.Template`:占位符只有 `$name` 与 `${name}` 两种形式,不解析任何属性访问,用户写不出逃逸路径。两种渲染模式分工明确:`substitute` 严格模式缺变量就抛 KeyError,适合程序内模板,错了立刻暴露;`safe_substitute` 缺啥留啥,适合草稿渲染;`$$` 是字面美元符的转义。缺变量的 KeyError 还可以在自己的 render 里拦下来翻译成业务可读的提示,如本例所示。一句话总结:模板来源越不可信,越要选表达能力更弱的模板引擎,「弱」在这里是安全属性。

```python
# file: code/01_语言核心与底层/q2883_string_template.py
"""string.Template 的安全替换:substitute 与 safe_substitute 的分工。"""
from string import Template

WELCOME = Template("你好 $name,你的订单 $order_id 已${action}。")


def render(template_text, mapping):
    """渲染用户可编辑的模板:缺变量时给出可读的错误。"""
    try:
        return Template(template_text).substitute(mapping)
    except KeyError as e:
        raise KeyError(f"模板缺少变量 {e},请检查上游数据") from None


if __name__ == "__main__":
    print("完整映射:", WELCOME.substitute(name="小明", order_id="A1024", action="发货"))

    try:
        WELCOME.substitute(name="小明")
    except KeyError as e:
        print("substitute 严格模式:", e)

    print("safe 模式缺啥留啥:", WELCOME.safe_substitute(name="小明"))

    user_typed = "你好 $name,余额 $$balance"
    print("用户输入模板:", render(user_typed, {"name": "小红", "balance": "100"}))
```

**追问**:1) safe_substitute 会不会把错误藏起来?——会,占位符原样出现在输出里就是「数据没配上」的信号,最好在渲染后用正则扫一遍残留的占位符并报警,而不是默默发出去。2) Template 与 format 的安全分界?——Template 只做 $identifier 纯替换、无属性链穿越;format 可被 {0.__init__.__globals__} 攻击(Q520);外部可控模板只用 Template/沙箱引擎。3) 替换缺失的三档语义?——substitute 抛 KeyError(严格)、safe_substitute 保留原样(宽容)、渲染后扫描(兜底检测)——严格与宽容按场景显式选择。4) 生产陷阱?——safe 输出直接发给用户(残留占位符);模板与数据键漂移无检测;i18n 模板混用 format。

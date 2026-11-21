---
title: [Q520] string.Template:安全的模板替换
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q520 · string.Template:安全的模板替换

> 难度:★★☆☆ | 标签:string, 模板

**问**:$name 形式的 Template 与 f-string/format 的定位差异?为什么不可信输入不用 % 格式化?

**答**:string.Template 的替换语法极简($name、${name}),规则是「标识符不存在则报错或留原样」,不做任何表达式求值——这使它适合:暴露给最终用户自定义的模板(邮件模板、通知文案)、避免 format 的格式串注入风险(攻击者控制 format 字符串可借 {0.__class__} 链读属性,即 format-string 漏洞)。substitute 缺键抛 KeyError,safe_substitute 缺键保留原样;substitute 的 map 参数支持 dict-like 默认值。f-string 是代码内嵌最快,但模板必须由开发者写死;「模板来自外部」的场景 Template 是 stdlib 里唯一正解。

```python
# file: code/01_语言核心与底层/q520_string_template.py
from string import Template

WELCOME = Template("Hello $name, your order ${order_id} is $status")

if __name__ == "__main__":
    print(WELCOME.substitute(name="Alice", order_id=7, status="shipped"))
    print(WELCOME.safe_substitute(name="Bob"))    # 缺键:保留 $order_id 原样

    try:
        WELCOME.substitute(name="Alice")
    except KeyError as e:
        print("missing key:", e)

    print(Template("${name}s book").substitute(name="Alice"))   # 边界定界
    user_input = "Robert'); DROP TABLE users;--"
    print("template does not execute:", Template("msg: $x").substitute(x=user_input))
```

**追问**:1) format 的格式串注入到底能偷什么?——攻击者控制模板串时可用 {0.__init__.__globals__} 穿越属性链泄露全局配置与密钥;不可信模板一律 Template 或专门沙箱引擎(Jinja2 sandbox)。2) 模板的三档安全等级?——f-string 是代码不是模板(没有注入面但不能外部化);str.format 可外部化但属性链可穿越(不安全);string.Template 只做 $identifier 纯文本替换,天然隔离。3) Template 的底层机制?——按 pattern 正则匹配 $$/$id/${id},safe_substitute 对缺失键保留原样不抛错,substitute 抛 KeyError——严格与宽容两档要按场景选。4) 生产陷阱?——用户可控模板喂给 .format() 是真实的信息泄露 CVE 模式;safe_substitute 静默留下错误占位符,不上线前校验不会被发现;i18n 模板选错档位把翻译文件变成攻击面。

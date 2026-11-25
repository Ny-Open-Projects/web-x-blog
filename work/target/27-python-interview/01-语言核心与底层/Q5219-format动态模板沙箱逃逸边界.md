---
title: "[Q5219] str.format 动态模板的逃逸面：属性链访问与白名单 Formatter"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5219 · str.format 动态模板的逃逸面：属性链访问与白名单 Formatter

难度：P6 ｜ 标签：str.format、format 模板注入、属性链、string.Formatter、沙箱逃逸、模板安全

**问**：`tpl.format(user)` 里的模板来自用户输入，为什么被认为是"半个模板注入"？`"{0.__class__}"` 能拿到什么？与 f-string、string.Template、SSTI 的安全边界分别差在哪？安全的动态模板渲染怎么写？

**答**：
结论：`str.format` 的字段语法支持**属性链与索引**（`{0.attr}`、`{0[k]}`），意味着模板作者可以访问传入对象上任意可达属性——用户可控的模板配上传入对象，等价于一次受限的表达式求值：`{0.__class__.__init__.__globals__}` 这类链可以一路摸到模块级全局（配置、密钥对象）。f-string 在编译期绑定变量名，模板即代码、无法动态下发，天然免疫这类注入；`string.Template` 只替换 `$identifier`，不支持属性访问，是标准库里**唯一为不可信模板设计**的替换器；SSTI（Jinja2 等模板引擎）则是完整表达式语言，逃逸面最大（Q6110）。所以安全边界从紧到松：Template > 白名单 format > 裸 format > 完整模板引擎给用户写。注意 Python 的 format **没有**某些语言那种"方法调用逃逸"（不能执行任意函数调用，只能取属性/索引），但属性链本身足以泄漏对象图内容。

取舍：a) 模板来源可信（代码内写死）：`str.format` 随便用；b) 模板半可信（管理员可配）：`string.Template` 或白名单 Formatter；c) 模板完全用户可控：只允许占位符替换（Template）或自研"纯占位符"语法（正则白名单提取键、逐键查表替换）；d) 需要 Formatter 定制时，拦截点选 `get_field`（键解析入口）而不是事后校验输出——逃逸发生在取值阶段；e) 根本原则：**渲染引擎的表达力与模板可信度必须匹配**，给不可信输入任何表达式能力都是漏洞预算超支。

实战：事故形态是"通知系统的文案模板开放给运营编辑，实现用了 `tpl.format(user=ctx)`，运营论坛流出 `{user.__class__.__init__.__globals__[settings].SECRET_KEY}` 的组合，把签名密钥打进了发送出去的短信链接；修复改 string.Template + 键白名单，模板保存时先干跑校验"。下面演示逃逸路径与拦截。

```python
from string import Formatter

WHITELIST = {"name", "level"}


class SafeFormatter(Formatter):
    """拦截 get_field: 键白名单 + 禁止属性链/索引"""

    def get_field(self, field_name, args, kwargs):
        key = field_name.split(".")[0].split("[")[0]
        if key not in WHITELIST or ("." in field_name or "[" in field_name):
            raise ValueError(f"模板键越界: {field_name!r}")
        return super().get_field(field_name, args, kwargs)


class User:
    secret = "s3cr3t-internal"

    def __init__(self, name, level):
        self.name = name
        self.level = level


u = User("alice", "gold")

print("[1] 裸 format 属性链可读:", "{0.secret}".format(u))
chain = "{0.__class__.__name__}"
print("[2] 类链可达:", chain.format(u))

sf = SafeFormatter()
for tpl in ("{0.name}({0.level})", "{0.secret}", "{0.__class__}"):
    try:
        print("[3] safe:", tpl, "->", sf.format(tpl, u))
    except ValueError as e:
        print("[3] safe:", tpl, "-> 拦截:", e)

print("[4] string.Template 不支持属性访问, 天然免疫:", "$name 与 ${level} 才是合法键")
```

**追问一**：format 的属性链能执行方法调用吗？为什么这限制了危害上限？—— 不能：format 字段语法只有属性访问（`.`）与索引（`[...]`），没有调用语法 `{0.foo()}` 是语法错误。所以最坏情形是**读**出对象图上的值（str 化后渲染），不能直接执行任意代码——危害等级低于 SSTI 的"表达式可调用任意函数"。但读取仍可链式深入：`__globals__`、`__builtins__`、环境对象都能被枚举，配合错误信息回显就是完整的信息泄漏通道。危害上限取决于"可渲染对象图有多深"，而不是 format 本身的表达力。

**追问二**：日志系统的 `logging` 为什么天然扛这类问题？—— logging 的消息格式化是**延迟的**（Q503）：调用方传 `msg` 与 `args`，真正拼接发生在 handler 里且模板是程序员写死的，用户输入只会进 `args` 的值位，永远到不了模板位。反面教材是 `logger.info(user_input)` 直接把用户输入当模板——里面若含 `{...}` 且后续被 `format` 处理，就复刻了同样的逃逸面（Q5175 的 extra 撞键是另一类日志坑）。"模板永远代码内、用户输入永远值位"是所有格式化系统的通用铁律。

## 背诵要点
- str.format 字段语法支持属性链/索引：用户可控模板 = 受限对象图读取，`__class__.__globals__` 可达。
- 安全边界从紧到松：string.Template（无属性访问）> 白名单 Formatter（拦截 get_field）> 裸 format > 全功能模板引擎（SSTI）。
- format 无方法调用语法，危害是"读"不是"执行"；模板永远代码内、用户输入永远值位。

## 复盘追问
- 运营可编辑模板为什么会漏密钥？（format 属性链深入对象图；改 Template+白名单并在保存时干跑校验）
- format 注入和 SSTI 的危害差在哪？（format 只读对象图无调用；SSTI 表达式可执行任意逻辑）

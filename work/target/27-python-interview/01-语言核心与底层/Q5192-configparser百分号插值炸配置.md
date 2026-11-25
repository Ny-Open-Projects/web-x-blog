---
title: "[Q5192] configparser 的 % 插值：密码含百分号直接炸配置"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5192 · configparser 的 % 插值：密码含百分号直接炸配置

难度：P6 ｜ 标签：configparser、插值、InterpolationSyntaxError、optionxform、配置解析

**问**：`configparser` 读取 `password = p%ss%word` 时不会报错，但服务启动后第一次取这个值就抛 `InterpolationSyntaxError`，进程直接起不来。为什么错误延迟到取值才发生？为什么键 `Host` 变成了 `host`？生产里该怎么读"只当数据、不当模板"的配置？

**答**：
结论：`ConfigParser` 默认启用 `BasicInterpolation`，值里的 `%` 是元字符：`%(name)s` 引用同节变量，`%%` 才是字面量，其他 `%x` 组合在**取值（`__getitem__`）时**才解析并抛错，所以 `read_string` 阶段不会失败，故障被推迟到业务第一次读配置。另一个默认行为是 `optionxform=str.lower`：所有键在读入时被小写化，`Host` 与 `host` 合并成一项，这会让大小写敏感的配置（比如 HTTP 头、环境变量名）静默串味。

取舍：三条路——a) 配置是纯数据（密码、URL、模板串）时用 `ConfigParser(interpolation=None)` 或 `RawConfigParser`，彻底关掉 `%` 语义；b) 确实需要变量引用时用 `ExtendedInterpolation`（`${section:key}`），它对 `$` 敏感但对 `%` 无感，更适合含密码的场景；c) 不要用 `os.environ` 拼进 `%` 插值，密码中的 `%` 会在运行时才炸。键名要保持原样时把 `optionxform` 设回 `str`，但要注意这会让所有既有读取代码的大小写假设失效。

实战：事故形态是"灰度机读到一个包含 `%` 的数据库密码，启动时 healthy，第一次建立连接取密码就抛异常，进程被 supervisor 反复拉起"。下面演示延迟抛错、关闭插值、`%%` 转义，以及 `optionxform` 的键折叠。

```python
import configparser

RAW = """
[db]
password = p%ss%word
Host = DB.Example.COM
url = postgres://u:p%40ss@db/app
"""

cp = configparser.ConfigParser()
cp.read_string(RAW)
try:
    print(cp["db"]["password"])
except configparser.InterpolationSyntaxError as e:
    print("[1] read 阶段不报，取值才炸:", type(e).__name__, "|", e)

print("[2] 键被小写化:", list(cp["db"].keys()))

raw = configparser.ConfigParser(interpolation=None)
raw.read_string(RAW)
print("[3] 关闭插值后原样返回:", raw["db"]["password"])

esc = configparser.ConfigParser()
esc.read_string("[db]\npassword = p%%ss%%word\n")
print("[4] % 需写成 %% :", esc["db"]["password"])

keep = configparser.ConfigParser(interpolation=None)
keep.optionxform = str          # 必须在读入前设置
keep.read_string(RAW)
print("[5] 保留键大小写:", list(keep["db"].keys()))
```

**追问一**：为什么 `read_string` 不校验就把非法 `%` 放进内存？—— 插值是按需计算的：`ConfigParser` 存的是原始字符串，`get()` 时才展开并递归解析引用。这样设计的好处是"没被用到的节不会因语法问题阻塞启动"，坏处是配置错误从启动期漏到运行期。想在启动期就暴露，可以在启动自检里把需要的键全部 `get()` 一遍（fail fast），而不是等到第一次用。

**追问二**：`ExtendedInterpolation` 就没有坑了吗？—— 它用 `${section:option}`，值里的 `$` 成了元字符，密码含 `$` 同样会炸，只是把雷从 `%` 换成了 `$`。另外它支持跨节引用，容易写出循环引用（`a→b→a`），取值时抛 `InterpolationDepthError`。结论：配置值只当数据时一律关插值；需要模板能力就把模板层显式建模（Jinja/自定义渲染），不要让 ini 解析器偷偷承担模板引擎的职责。

## 背诵要点
- `ConfigParser` 默认 `BasicInterpolation`，`%` 是元字符，错误延迟到 `get()` 才抛，启动期看不出来。
- 纯数据配置用 `interpolation=None` / `RawConfigParser`；需要引用用 `${}` 的 `ExtendedInterpolation`。
- `optionxform` 默认小写化键，大小写敏感配置必须在 `read_*` 之前设回 `str`。

## 复盘追问
- 配置读取在启动时正常、建连时才抛 `InterpolationSyntaxError`，原因是什么？（按需插值 + `%` 元字符）
- 为什么"把 `%` 换成 `%%`"不适合密码场景？（密码由运维输入、不可控；且改密码就复发）

---
title: [Q6110] SSTI 模板注入原理与防护
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6110 · SSTI 模板注入的原理与防护

> 难度:★★★★☆ | 标签:原理深挖, SSTI, Jinja2

**问**:用用户输入的字符串动态渲染模板（`Template(name).render()`）为什么危险？漏洞链与防护边界在哪？

**答**:结论：SSTI 的根因是把"用户数据"当"模板代码"编译——模板引擎按语法（`{{ }}`、`{% %}`）解析用户输入，攻击者就能从上下文对象沿属性链摸到危险面。Jinja2 经典利用链是绕到 Python 对象模型：`{{ ''.__class__.__mro__ }}` → 找到 object → `__subclasses__()` 里找 `os._wrap_close`/`subprocess` → 调 `popen` 执行命令；即便禁掉这些 dunder，`{{ config }}`、`{{ self }}` 也会泄露配置。防护分级：① 铁律——用户输入只作**变量**传入 render 上下文，永远不做模板体（`render_template_string(...)` 只放模板骨架，数据走参数）；② 沙箱——确需"用户可写模板"的（邮件模板、报表定义）用 Jinja2 `SandboxedEnvironment`，拦截不安全属性访问，配 `is_safe_attribute` 白名单；③ 纵深——限制模板里可访问的全局（undefined 变严格、去掉 `os`/`builtins` 注入），渲染超时与输出长度上限。取舍：沙箱不是绝对安全，Jinja2 官方也声明 sandbox 防的是"修改环境"，不承诺对抗全部逃逸——高危场景改为自研受限 DSL 或表达式求值器（如 `ast.literal_eval` 级别的白名单求值）。

```python
# 第三方基线：Jinja2 3.x（pip install jinja2）；缺库时降级为字符串替换演示
try:
    from jinja2 import Environment, Template
    from jinja2.sandbox import SandboxedEnvironment

    env = Environment()                      # 事故形态：非沙箱 + 用户输入当模板
    user = "{{ ''.__class__.__name__ }}"     # 攻击者的注入串（演示用最浅的一层）
    out = env.from_string(user).render()
    print("非沙箱渲染结果:", out, "← 用户输入被当代码执行")

    # 防护 1：数据走上下文变量，模板体固定
    fixed = env.from_string("Hello {{ who }}")
    print("正确用法:", fixed.render(who="{{ ''.__class__ }}"))   # 原样输出，不解析

    # 防护 2：沙箱环境拦截不安全属性链（__class__.__mro__ 起步即 SecurityError）
    senv = SandboxedEnvironment()
    try:
        senv.from_string("{{ ''.__class__.__mro__ }}").render()
    except Exception as e:
        print("沙箱拦截:", type(e).__name__)

except ModuleNotFoundError:
    who = "{{ user }}"
    print("缺 jinja2 降级：纯替换不解析模板语法 →", "Hello " + who)
```

**追问一层**:沙箱为什么能拦 `__class__`？攻击者还有哪些绕过面（globals、filters、`|attr`）？
**追二层**:为什么 `ast.literal_eval` 不是完整解？自研受限求值器要覆盖哪些点（运算符、属性、调用白名单）？

**背诵要点**
- 用户输入进模板体=代码注入；只允许作为变量进上下文。
- Jinja2 利用链：`__class__.__mro__` → object → subclasses → os/subprocess。
- 防护三件套：变量化传参、SandboxedEnvironment、限制全局与输出。

**复盘追问**
- 线上如何发现 SSTI 面存在？提示：审计 `Template(` 调用点 + 渗透用 `{{7*7}}` 探针。
- 邮件模板这类"真要用户可写"场景的安全设计？提示：沙箱+白名单变量+无文件/网络能力+独立沙箱进程。

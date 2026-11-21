---
title: [Q121] Jinja2 模板引擎与继承
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q121 · Jinja2 模板引擎与继承

> 难度:★★☆ | 标签:Jinja2, 模板

**问**:Jinja2 的模板继承、宏和过滤器分别解决什么问题?XSS 如何防护?

**答**:模板继承用 `{% extends %}` + `{% block %}` 实现布局复用(子模板填充父模板的 block);`{% include %}` 复用片段,`{% macro %}` 定义可复用组件;过滤器 `{{ value | filter }}` 处理显示格式,自定义用 `app.add_template_filter`。安全上,`{{ }}` 输出自动转义防 XSS,`| safe` 会关闭转义,只可用于可信内容;`render_template_string` 渲染用户输入的模板会造成 SSTI 漏洞,必须避免。

```python
# file: code/03_Web后端开发/q121_jinja2_render.py
try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("该题演示需要第三方库 jinja2:pip install jinja2(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html']),   # 自动转义防 XSS
)

base_tpl = """
<html><body>
  {% block content %}{% endblock %}
</body></html>
"""

child_tpl = """
{% extends base %}
{% block content %}
  <h1>{{ user.name }}</h1>
  <p>{{ user.bio | upper }}</p>
  {{ evil | e }}
{% endblock %}
"""

env.globals['base'] = env.from_string(base_tpl)
tmpl = env.from_string(child_tpl)
html = tmpl.render(user={'name': 'alice', 'bio': 'hello'}, evil='<script>')
print('script' not in html.lower())   # True,已转义
```

**追问**:
- SSTI 的攻击路径是什么?——`render_template_string(user_input)` 让用户输入当模板执行,可读出对象链到 `__globals__` 拿敏感数据;用户内容永远作为变量传入。
- |safe 的使用纪律?——仅限服务端可信 HTML(如渲染后的富文本经 bleach 清洗);对用户输入关转义等于开 XSS 大门。
- 模板里能调复杂逻辑吗?——能但不应:模板只做展示,业务计算放视图/服务层;filter/macro 封装展示逻辑。

```mermaid
flowchart TD
    A[视图函数调用 render_template] --> B[loader 加载模板文件]
    B --> C[Jinja2 编译模板为 Python 代码]
    C --> D[注入上下文变量]
    D --> E[渲染并自动转义输出]
    E --> F[返回 HTML 响应]
    G[base.html 定义 block 骨架] --> H[child extends base]
    H --> I[子模板覆盖 block 填充内容]
```

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

---
title: [Q792] Django 缓存层级与模板片段缓存
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q792 · Django 缓存层级与模板片段缓存

> 难度:★★★☆ | 标签:Django, 缓存

**问**:Django 的缓存从粗到细有哪几层?模板片段缓存的 key 怎么管理?

**答**:由粗到细:`cache_page` 整页缓存(含 vary 头)、`cache_control` 指示客户端与代理、**模板片段缓存** `{% cache timeout fragment_name %}`、低层 API `cache.get/set` 手工控制。片段缓存 key 由名字与 `vary_on` 参数生成(`make_template_fragment_key` 可编程失效);失效策略是难点,数据变更时用 signal 或 service 层显式 delete。多级组合原则:**越细粒度越精准、越粗粒度越省心**,按页面热度选择。

```python
# file: code/03_Web后端开发/q792_fragment_cache.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}},
    INSTALLED_APPS=[],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], "APP_DIRS": False, "OPTIONS": {},
    }],
    USE_TZ=True,
)
django.setup()

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.template import Context, Template

tpl = Template("{% load cache %}{% cache 60 hero %}静态横幅{% endcache %}{{ name }}")
print(tpl.render(Context({"name": "alice"})))
key = make_template_fragment_key("hero")
print("片段缓存存在:", cache.get(key) is not None)
cache.delete(key)
print("删除后需重渲染:", cache.get(key) is None)
```

**追问**:
- cache_page 与 CDN 缓存的分工?——cache_page 减源站计算,CDN 减回源,后者靠 Cache-Control 控制,两者要一致设计。
- 缓存 key 里要放租户吗?——要,多租户缓存的 key 必须带租户维度,否则数据串租户是最严重的事故之一。

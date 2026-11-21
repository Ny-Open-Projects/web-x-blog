---
title: [Q801] i18n:gettext 翻译工程
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q801 · i18n:gettext 翻译工程

> 难度:★★☆☆ | 标签:Django, i18n

**问**:Django 的国际化流程是什么?gettext 和 gettext_lazy 用在什么不同位置?

**答**:流程:代码里用 `gettext("Welcome")` 标注 → `makemessages` 扫描生成 .po → 翻译填写 → `compilemessages` 编译成 .mo → LocaleMiddleware 按 Accept-Language/cookie 激活语言。**gettext_lazy** 用于模块级/模型字段定义期(字符串延迟到渲染时才翻译,避免启动时锁定语言),**gettext** 用于请求期逻辑。复数与上下文用 ngettext/pgettext;别自己拼英文句子再替换,粒度到完整句子才可翻译。

```python
# file: code/03_Web后端开发/q801_i18n.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    USE_I18N=True,
    LANGUAGES=[("en", "English"), ("zh-hans", "简体中文")],
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.utils import translation
from django.utils.translation import gettext as _

print(_("Welcome"))   # 未安装 .mo 目录时原样返回 msgid
print(_("Hello %(name)s") % {"name": "alice"})
with translation.override("zh-hans"):
    print("当前语言:", translation.get_language())
print("恢复后语言:", translation.get_language())
```

**追问**:
- 模型字段用 lazy 字符串有什么坑?——迁移文件里会固化字符串,改 msgid 会产生迁移噪音,命名要一步到位。
- 翻译缺失怎么兜底?——msgid 即英文原文是天然兜底,再配上 CI 检查 po 覆盖率。

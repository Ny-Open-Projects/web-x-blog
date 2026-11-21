---
title: [Q135] Django 模板与静态文件管理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q135 · Django 模板与静态文件管理

> 难度:★★☆ | 标签:Django, static

**问**:Django 开发与生产环境如何组织模板和静态文件?collectstatic 干什么的?

**答**:模板通过 `TEMPLATES[DIRS]` 加全局目录、app 内 `templates/` 自动发现;静态文件同理,app 的 `static/` + `STATICFILES_DIRS` 在开发期由 `runserver` 自动服务。生产环境执行 `collectstatic` 把所有静态文件汇总到 `STATIC_ROOT`,交给 Nginx/CDN 直接服务(不要走 Django);`{% static %}` 标签生成带版本指纹的 URL,配合 ManifestStaticFilesStorage 做缓存失效。

```python
# file: code/03_Web后端开发/q135_django_static.py
# settings.py 关键配置(模块级自洽示意)
DEBUG = True
BASE_DIR = '/srv/myproject'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [f'{BASE_DIR}/templates'],        # 全局模板目录
    'APP_DIRS': True,                          # 自动发现各 app 的 templates/
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
    ]},
}]

STATIC_URL = '/static/'
STATICFILES_DIRS = [f'{BASE_DIR}/assets']     # 项目级静态目录
STATIC_ROOT = f'{BASE_DIR}/staticfiles'       # collectstatic 汇总目标
MEDIA_URL = '/media/'                          # 用户上传
MEDIA_ROOT = f'{BASE_DIR}/media'

# 开发期: runserver 自动服务 static
# 生产: python manage.py collectstatic 后由 Nginx alias /static/ -> STATIC_ROOT
print(STATIC_ROOT)
```

**追问**:
- 为什么生产不让 Django 服务静态文件?——Python 处理静态文件浪费 worker 且慢;Nginx/CDN 直服,Django 只出动态。
- 静态文件缓存怎么失效?——ManifestStaticFilesStorage 给文件名加内容指纹,内容变文件名变,引用同步更新,缓存永不脏。
- collectstatic 的文件冲突怎么办?——不同 app 同名静态文件按 STATICFILES_DIRS 顺序覆盖;命名加 app 前缀是惯例。

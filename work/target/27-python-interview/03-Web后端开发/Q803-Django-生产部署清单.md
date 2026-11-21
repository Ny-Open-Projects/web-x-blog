---
title: [Q803] Django 生产部署清单
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q803 · Django 生产部署清单

> 难度:★★★☆ | 标签:Django, 部署

**问**:Django 上生产的 settings 检查清单有哪些?漏一项分别会出什么事故?

**答**:核心项:`DEBUG=False`(否则报错页泄源码与配置)、`ALLOWED_HOSTS` 白名单(否则 Host 头攻击/请求直接被拒)、`SECRET_KEY` 从环境注入(否则签名伪造)、`collectstatic` + 静态服务交给 Nginx/CDN、`SECURE_SSL_REDIRECT`/HSTS、`CSRF_TRUSTED_ORIGINS`、数据库 `CONN_MAX_AGE`、日志配置落盘或 stdout。可用系统检查(`deploy` checks)+ 自写清单脚本固化进 CI。

```python
# file: code/03_Web后端开发/q803_deploy_checklist.py
import os

def check_settings(s: dict) -> list:
    problems = []
    if s.get("DEBUG", True):
        problems.append("DEBUG 必须为 False")
    if s.get("ALLOWED_HOSTS") in (None, [], ["*"]):
        problems.append("ALLOWED_HOSTS 必须白名单具体域名")
    if not s.get("SECRET_KEY"):
        problems.append("SECRET_KEY 必须来自环境变量或密钥服务")
    if s.get("SECURE_SSL_REDIRECT") is not True:
        problems.append("建议开启 HTTPS 强制跳转")
    return problems

prod = {
    "DEBUG": False,
    "ALLOWED_HOSTS": ["api.example.com"],
    "SECRET_KEY": os.environ.get("DJANGO_SECRET_KEY", ""),
    "SECURE_SSL_REDIRECT": True,
}
print("检查结果:", check_settings(prod))
```

**追问**:
- DEBUG=False 后 500 白屏怎么排查?——看日志的异常栈,ALLOWED_HOSTS 与静态路径是最常见的两个假白屏原因。
- python manage.py check --deploy 是什么?——官方部署安全检查器,覆盖 SECURE_* 与传输安全配置,应纳入发布流水线。

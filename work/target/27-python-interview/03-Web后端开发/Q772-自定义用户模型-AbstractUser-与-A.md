---
title: [Q772] 自定义用户模型:AbstractUser 与 AbstractBaseUser
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q772 · 自定义用户模型:AbstractUser 与 AbstractBaseUser

> 难度:★★★★ | 标签:Django, 用户模型

**问**:为什么自定义用户模型必须在第一个迁移之前定?两种基类怎么选?

**答**:`AbstractUser` 继承后**加字段**(保留 username、权限体系),`AbstractBaseUser` 从零定义(自己实现 USERNAME_FIELD 与 BaseUserManager),适合手机号/邮箱登录体系。必须趁早的原因:用户表被外键、迁移、admin 全局引用,中途更换等于重写历史迁移,官方文档明确"项目开始就定制"。所有指向用户的外键用 `settings.AUTH_USER_MODEL` 字符串,不要直接 import 用户类,否则循环导入与替换困难。

```python
# file: code/03_Web后端开发/q772_custom_user.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import connection, models

class UserManager(BaseUserManager):
    def create_user(self, username: str, password: str):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "username"
    objects = UserManager()
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(CustomUser)

u = CustomUser.objects.create_user(username="alice", password="s3cret!")
print("密码校验:", u.check_password("s3cret!"))
print("存储的是哈希:", u.password.startswith("pbkdf2"))
```

**追问**:
- USERNAME_FIELD 的要求?——必须是唯一字段,且自定义 Manager 要实现 create_user/create_superuser 约定。
- 第三方包引用 User 模型怎么办?——统一用 get_user_model() 或 settings.AUTH_USER_MODEL,生态都支持。

---
title: [Q742] pydantic-settings 多环境配置与优先级
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q742 · pydantic-settings 多环境配置与优先级

> 难度:★★★☆ | 标签:pydantic-settings, 配置

**问**:dev/staging/prod 三套环境,配置怎么组织?环境变量、.env、默认值谁覆盖谁?

**答**:用 `pydantic-settings` 的 BaseSettings 定义强类型配置,`env_prefix` 隔离命名空间(如 APP_DB_URL),`env_file=".env"` 支持本地开发。优先级从高到低:**构造参数 > 环境变量 > .env 文件 > 字段默认值**,这条链保证了"同一段代码,不同环境只换注入"。多环境差异通过环境注入解决,而不是维护三个配置类;类型错误在**启动时**就报,比运行时炸好得多。

```python
# file: code/03_Web后端开发/q742_settings.py
import os
try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("pip install pydantic-settings 后再运行")
    raise SystemExit(0)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")
    env: str = "dev"
    debug: bool = False
    db_url: str = "sqlite:///dev.db"
    redis_url: str = "redis://localhost:6379/0"

os.environ["APP_ENV"] = "prod"
os.environ["APP_DEBUG"] = "false"

s = Settings()
print(s.env, s.debug, s.db_url)
print("构造参数优先级最高:", Settings(env="staging").env)
```

**追问**:
- bool 类型的环境变量怎么解析?——接受 true/false/1/0/yes/no 等,pydantic-settings 负责转换,写错启动即报。
- .env 会上到生产吗?——不应该,生产只用真实环境变量或密钥服务,.env 只服务本地与 CI。

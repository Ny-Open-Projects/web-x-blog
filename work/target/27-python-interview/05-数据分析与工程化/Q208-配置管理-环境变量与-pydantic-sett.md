---
title: [Q208] 配置管理:环境变量与 pydantic-settings
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q208 · 配置管理:环境变量与 pydantic-settings

> 难度:★★★ | 标签:pydantic-settings, 12-factor

**问**:配置应该怎么管理?为什么配置文件里不能放密钥?

**答**:遵循 12-factor:**配置与代码分离**,同一镜像不同环境只改配置;配置来源优先级通常是环境变量 > .env 文件 > 默认值。**pydantic-settings** 把配置声明成类型安全的模型:字段类型即文档,启动时校验缺失/非法配置(快速失败好过半夜 500),自动读取环境变量(大小写不敏感、支持嵌套分隔符)、解析 .env,secret 只进环境变量不进代码仓库。坑点:`.env` 文件绝不能提交(进 .gitignore);布尔和列表的环境变量解析有语法讲究(如 JSON 列表);改配置类字段名后环境变量名也会变,部署要同步。

```python
# file: code/05_数据分析与工程化/q208_settings_demo.py
try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("该题演示需要第三方库 pydantic_settings:pip install pydantic-settings,原理见正文")
    raise SystemExit(0)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "demo"
    debug: bool = False
    db_url: str
    api_keys: list[str] = []


def load_settings(monkeypatch_env: dict) -> Settings:
    import os
    for k, v in monkeypatch_env.items():
        os.environ[k] = v
    return Settings(_env_file=None)


def test_settings_from_env():
    s = load_settings({
        "DB_URL": "postgres://localhost/t",
        "DEBUG": "true",
        "API_KEYS": '["k1","k2"]',
    })
    assert s.debug is True
    assert s.api_keys == ["k1", "k2"]
    assert s.db_url.startswith("postgres")
```

**追问**:
- 布尔和列表的环境变量怎么写?——布尔用 true/false 字符串,列表用 JSON(`['a','b']`);pydantic-settings 按 JSON 解析复合类型,手写逗号分隔要自定义。
- 配置校验失败该崩溃吗?——该,启动期 fail-fast 好过运行期半夜出错;missing 字段直接抛 ValidationError 阻止部署。
- 敏感配置怎么轮换?——secret 进环境变量/秘密管理器,轮换只改环境不改代码;配置类字段变更要走发布。

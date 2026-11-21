---
title: [Q204] pyproject.toml 与现代打包
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q204 · pyproject.toml 与现代打包

> 难度:★★★ | 标签:pyproject.toml, 打包, PEP 621

**问**:pyproject.toml 为什么能取代 setup.py 和 requirements.txt?

**答**:pyproject.toml 是 **PEP 517/518/621** 定义的统一项目元数据文件:`[build-system]` 声明构建后端(setuptools/hatchling/poetry-core/flit),`[project]` 声明名称、版本、依赖、entry point,工具配置(ruff/pytest/mypy)也集中在此。相比 setup.py 的优势:声明式、无任意代码执行(更安全)、格式标准化。dependencies 放**直接依赖且尽量宽松**(如 `>=1.0`),精确锁定交给 lock 文件(uv.lock/requirements.txt 冻结)。`[project.scripts]` 可以注册 CLI 命令,安装后直接可用。

```toml
# pyproject.toml 示例:非 python 文件
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproj"
version = "0.3.0"
requires-python = ">=3.11"
dependencies = ["httpx>=0.27", "pydantic-settings>=2.0"]

[project.optional-dependencies]
dev = ["pytest>=8", "mypy>=1.10", "ruff>=0.5"]

[project.scripts]
myproj = "myproj.cli:main"

[tool.pytest.ini_options]
addopts = "--cov=myproj --cov-branch"
markers = ["slow: 慢速测试"]
```

```python
# file: code/05_数据分析与工程化/q204_packaging_demo.py
import importlib.metadata

def get_version(fallback="0.0.0.dev0"):
    # 安装后可从包元数据读取版本,未安装时用 fallback
    try:
        return importlib.metadata.version("myproj")
    except importlib.metadata.PackageNotFoundError:
        return fallback

def test_version_fallback():
    assert isinstance(get_version(), str)
```

**追问**:
- 为什么 dependencies 放宽松、lock 放精确?——库作者声明兼容区间,应用靠 lock 锁死闭包;两者角色不同,混用会让升级无从判断。
- entry point 怎么声明?——`[project.scripts]` 定义命令,`[project.entry-points.pytest11]` 这类声明插件;安装即注册。
- setup.py 还需要吗?——纯声明式项目不需要;只有构建期动态逻辑(版本号生成)才需要钩子,且优先用构建后端的能力替代。

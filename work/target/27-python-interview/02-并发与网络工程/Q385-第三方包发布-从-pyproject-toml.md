---
title: [Q385] 第三方包发布:从 pyproject.toml 到 PyPI
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q385 · 第三方包发布:从 pyproject.toml 到 PyPI

> 难度:★★☆ | 标签:打包, pyproject, 发布

**问**:现在发布一个 Python 包,标准流程和文件结构是什么?

**答**:现代标准是 `pyproject.toml`(PEP 621 元数据)+ 构建后端(setuptools/hatchling/poetry-core)+ Twine 上传。流程:①写 `pyproject.toml` 声明名称、版本、依赖、Python 版本下限;②`pip install build; python -m build` 产出 sdist(.tar.gz)和 wheel(.whl);③`twine upload dist/*`(用 API token,别用密码);④版本号用语义化版本,发版打 git tag。注意:私包发私有 index(如公司 Nexus),上传前用 `twine check` 校验。

```python
# file: code/02_并发与网络工程/q385_package_files.py
"""以编程方式生成 pyproject.toml,演示现代包元数据。"""
from pathlib import Path

PYPROJECT = '''
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "myutils"
version = "1.2.0"
description = "个人工具集示例包"
requires-python = ">=3.9"
dependencies = ["requests>=2.31,<3"]

[project.optional-dependencies]
dev = ["pytest", "ruff"]

[project.scripts]
myutils-cli = "myutils.cli:main"
'''


def init_package(root="myutils-project"):
    root = Path(root)
    pkg = root / "myutils"
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "__init__.py").write_text('__version__ = "1.2.0"\n', encoding="utf-8")
    (pkg / "cli.py").write_text(
        'def main():\n    print("hello from myutils")\n', encoding="utf-8"
    )
    (root / "pyproject.toml").write_text(PYPROJECT, encoding="utf-8")
    return root


if __name__ == "__main__":
    p = init_package("/tmp/myutils-project")
    print("生成完成:", sorted(str(x.relative_to(p)) for x in p.rglob("*")))
    # 发布三步(在项目根目录执行):
    # python -m build          生成 sdist 和 wheel
    # twine check dist/*       校验元数据
    # twine upload dist/*      上传 PyPI 或私有 index
```

**追问**:
- wheel 和 sdist 的区别?wheel 是预构建产物,安装快、不需本地构建;sdist 是源码分发包,某些平台/场景需要;PyPI 要求两者都传。
- 版本号 `1.2.0` 里各位代表什么?语义化版本:主版本(不兼容变更).次版本(向后兼容的新功能).修订号(修复)。

---
title: [Q190] conftest.py 的作用与查找规则
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q190 · conftest.py 的作用与查找规则

> 难度:★★☆ | 标签:pytest, conftest

**问**:conftest.py 是什么?多层 conftest 怎么生效?

**答**:conftest.py 是 pytest 的**本地插件文件**,里面的 fixture 和 hook 对其所在目录及所有子目录自动生效,**不需要 import**。查找规则:pytest 收集测试时沿目录树向上查找,离测试最近的 conftest 优先——同名 fixture 会被内层覆盖外层,以此实现"默认实现在顶层、特殊实现在子目录覆盖"。它还适合放自定义 marker 注册、插件加载和 hook 实现(如 `pytest_addoption` 添加命令行参数)。注意:conftest 不能被跨包 import,需要共享给非测试代码的逻辑应放到普通模块。

```python
# file: code/05_数据分析与工程化/q190_conftest_demo.py
try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

@pytest.fixture
def base_config():
    return {"env": "test", "timeout": 5}

def test_uses_fixture(base_config):
    # 放在 tests/conftest.py 中即可被同目录所有测试直接使用
    assert base_config["env"] == "test"

def pytest_addoption(parser):
    # 实际项目写在 conftest.py 顶层,这里演示其内容
    parser.addoption("--env", default="test", help="指定测试环境")
```

**追问**:
- 想全局共享 fixture 又不在测试包内怎么办?——用 pytest 插件:在 pyproject.toml 里配置 `pytest11` entry point,或用 `-p` 参数加载。
- conftest 能被 import 吗?——不能,它不是包成员;要复用逻辑就提炼到普通模块或插件,conftest 只放 fixture 与 hook。
- 内层 conftest 覆盖外层的典型场景?——顶层 session 级假 DB,某个子目录用真实测试库覆盖同名 fixture;局部特殊化不动全局。
- pytest_addoption 怎么和 fixture 配合?——自定义命令行参数经 `request.config.getoption` 在 fixture 里读取;测试按选项切换行为。

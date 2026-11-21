---
title: [Q203] 项目结构:src 布局 vs 平铺布局
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q203 · 项目结构:src 布局 vs 平铺布局

> 难度:★★★ | 标签:src layout, 项目结构

**问**:为什么推荐 src 布局?它解决了什么实际问题?

**答**:src 布局把包放在 `src/<pkg>` 下,**只有安装后才能被 import**;平铺布局(<pkg>/ 直接在根目录)里,当前目录天然在 sys.path 上,测试 import 到的是**未安装的源码目录**。这带来两个 bug 温床:一,测试通过的项目发布后可能因为打包遗漏文件(如数据文件、生成代码)而 import 失败;二,根目录存在与依赖同名的目录时发生 shadowing。src 布局强制走与用户一致的安装路径,配合 `pip install -e .`,保证"测的就是装的"。测试目录放顶层 `tests/`,与包平行,不随包发布。

```text
# 项目结构示意:非 python 文件
myproj/
├── pyproject.toml
├── src/
│   └── myproj/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
├── tests/
│   ├── conftest.py
│   └── test_core.py
└── .pre-commit-config.yaml
```

```python
# file: code/05_数据分析与工程化/q203_layout_demo.py
# 实际项目应 from myproj.core import xxx,这里演示 src 布局的 import 纪律
def import_check():
    # 平铺布局下 pytest 根目录可直接 import myproj
    # src 布局下必须先 pip install -e . 否则 ImportError —— 这正是保护
    return "installed or editable install required"

def test_layout_discipline():
    assert "install" in import_check()
```

**追问**:
- `pip install -e .` 做了什么?——可编辑安装:把 src 包以链接方式注册进 site-packages(新版本用 PEP 660),改源码即时生效,同时保证 import 路径与真实安装一致。
- src 布局怎么调试本地代码?——`pip install -e .` 可编辑安装,改源码即时生效且 import 路径与用户一致。
- shadowing 事故长什么样?——根目录放了 `logging/` 目录,import logging 导入自己的目录;src 布局天然规避。
- tests 放包内还是包外?——src 布局下放顶层 tests/,不随包发布;包内 tests 会增加发布体积还可能被误 import。

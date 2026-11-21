---
title: [Q194] monkeypatch 与 fixture 化的测试替身
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q194 · monkeypatch 与 fixture 化的测试替身

> 难度:★★☆ | 标签:pytest, monkeypatch, 环境变量

**问**:pytest 的 monkeypatch 和 unittest.mock 的 patch 有什么区别?什么时候用哪个?

**答**:`monkeypatch` 是 pytest 内置 fixture,专做"临时改环境":`setenv/delenv` 改环境变量、`setattr` 改属性、`setitem` 改 dict、`chdir` 改目录,测试结束自动还原。定位差异:mock/patch 更适合"替换依赖并断言调用",monkeypatch 更适合"改全局状态"(环境变量、cwd、配置字典)。改环境变量务必用 `monkeypatch.setenv` 而不是手动 `os.environ`,后者一旦测试中途失败就会污染其他测试。

```python
# file: code/05_数据分析与工程化/q194_monkeypatch.py
import os

try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

def get_api_key():
    return os.environ.get("API_KEY", "")

def test_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key-123")
    assert get_api_key() == "test-key-123"

def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    assert get_api_key() == ""

def test_patch_module_attr(monkeypatch):
    import q194_monkeypatch as mod  # 引用自身模块演示 setattr
    monkeypatch.setattr(mod, "get_api_key", lambda: "stubbed")
    assert mod.get_api_key() == "stubbed"
```

**追问**:
- monkeypatch 和 patch 的边界?——改环境/cwd/字典用 monkeypatch(自动还原、按测试隔离);要断言调用与返回值才用 Mock/patch。
- monkeypatch 能改未导入的模块吗?——能,setattr 按名字延迟解析;但同样要 patch「使用处」的路径,与 patch 规则一致。
- 怎么验证 monkeypatch 生效了?——测试里直接读取改后的值断言;环境变量类别忘了用 setenv 而不是 os.environ 直改。

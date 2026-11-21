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

from unittest.mock import patch

def _now():
    return "real"

def greet():
    # 关键:这里引用的是本模块命名空间里的 _now
    return f"hello at {_now()}"

def test_patch_local_namespace():
    # 正确:patch 被测函数所在的模块名下的引用
    with patch("__main__._now", return_value="fake"):
        assert greet() == "hello at fake"

def test_real_function_untouched():
    with patch("__main__._now", return_value="fake"):
        pass
    # 作用域退出后恢复原实现
    assert greet() == "hello at real"

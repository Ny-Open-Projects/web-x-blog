import sys


def env_info():
    # 运行时判断当前解释器是否在 venv 内
    in_venv = sys.prefix != sys.base_prefix
    return {
        "in_venv": in_venv,
        "prefix": sys.prefix,
    }


def test_venv_detection():
    info = env_info()
    assert isinstance(info["in_venv"], bool)

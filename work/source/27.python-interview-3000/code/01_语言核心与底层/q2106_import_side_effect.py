"""模块导入副作用治理:main 守卫与延迟初始化。"""
import pathlib
import sys
import tempfile

BAD_SRC = '''print("connecting to production db ...")

def query():
    return "data"
'''

GOOD_SRC = '''_client = None

def get_client():
    global _client
    if _client is None:
        _client = "db-conn"        # 首次使用才初始化
    return _client

def query():
    return get_client() + ":data"

if __name__ == "__main__":
    print("only when run directly:", query())
'''


def run_import(src, label):
    with tempfile.TemporaryDirectory() as tmp:
        (pathlib.Path(tmp) / "dbmod.py").write_text(src, encoding="utf-8")
        sys.modules.pop("dbmod", None)
        sys.path.insert(0, tmp)
        try:
            print(f"[{label}] import 开始")
            __import__("dbmod")
            print(f"[{label}] import 结束")
        finally:
            sys.path.remove(tmp)
            sys.modules.pop("dbmod", None)


if __name__ == "__main__":
    run_import(BAD_SRC, "坏味道")
    run_import(GOOD_SRC, "治理后")

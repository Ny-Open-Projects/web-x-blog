"""循环依赖的延迟导入边界:类型走 TYPE_CHECKING,运行期走使用点导入。"""
import pathlib
import sys
import tempfile

B_SRC = '''from m_a import top_value

class B:
    pass
'''

A_BAD_SRC = '''import m_b

def top_value():
    return 1
'''

A_OK_SRC = '''import typing

if typing.TYPE_CHECKING:
    import m_b          # 只为类型检查器存在,运行时跳过

def top_value():
    return 1

def make_b():
    import m_b          # 运行期才需要:下沉到使用点
    return m_b.B()
'''


def attempt(src_a, label):
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        (root / "m_a.py").write_text(src_a, encoding="utf-8")
        (root / "m_b.py").write_text(B_SRC, encoding="utf-8")
        for name in ("m_a", "m_b"):
            sys.modules.pop(name, None)
        sys.path.insert(0, str(root))
        try:
            try:
                mod = __import__("m_a")
            except ImportError as e:
                return f"{label}: 导入失败 - {str(e)[:52]}..."
            if hasattr(mod, "make_b"):
                return f"{label}: 导入成功,make_b() -> {type(mod.make_b()).__name__}"
            return f"{label}: 导入成功"
        finally:
            sys.path.remove(str(root))
            for name in ("m_a", "m_b"):
                sys.modules.pop(name, None)


if __name__ == "__main__":
    print(attempt(A_BAD_SRC, "顶层互导"))
    print(attempt(A_OK_SRC, "延迟导入"))
    print("边界:类型引用进 TYPE_CHECKING,运行期引用下沉到使用点,根治靠拆公共模块")

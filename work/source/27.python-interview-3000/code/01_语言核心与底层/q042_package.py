import os
import sys
import tempfile

root = tempfile.mkdtemp()
pkg = os.path.join(root, "mypkg")
os.makedirs(pkg)
with open(os.path.join(pkg, "__init__.py"), "w") as f:
    f.write("__all__ = ['tool']\nfrom .tool import shout\n")
with open(os.path.join(pkg, "tool.py"), "w") as f:
    f.write("def shout(s):\n    return s.upper() + '!'\n")

sys.path.insert(0, root)

if __name__ == "__main__":
    import mypkg
    print(mypkg.shout("hello"))    # __init__ 里上提的 API
    print(mypkg.__all__)           # 星号导入的白名单
    from mypkg import tool
    print(tool is mypkg.tool)      # 同一模块对象
    print(sorted(os.listdir(pkg)))

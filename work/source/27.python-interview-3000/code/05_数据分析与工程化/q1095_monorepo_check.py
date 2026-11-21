import os
import tempfile
import textwrap

LAYOUT = textwrap.dedent("""
    repo/
      libs/          领域逻辑 零业务依赖
      apps/          api 与 worker 只依赖 libs
      packages/      对外发布的 wheel
      pyproject.toml + uv.lock
""")

def write_tree(root):
    files = {
        "libs/core/util.py": "def add(a, b):\n    return a + b\n",
        "apps/api/main.py": "import sys, pathlib\nsys.path.append(str(pathlib.Path(__file__).parents[2] / 'libs'))\nfrom core.util import add\nprint(add(1, 2))\n",
        "apps/api/bad.py": "import sys, pathlib\nsys.path.append(str(pathlib.Path(__file__).parents[2] / 'apps'))\n",
        "pyproject.toml": "[project]\nname = 'repo'\n",
    }
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

def check_no_cross_app_imports(root):
    """apps 之间禁止互相 import 的静态检查"""
    problems = []
    for dirpath, _, names in os.walk(root):
        for name in names:
            if not name.endswith(".py"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            with open(path) as f:
                text = f.read()
            if rel.startswith("apps/") and "parents[2] / 'apps'" in text:
                problems.append(rel)
    return problems

if __name__ == "__main__":
    print("推荐布局:", LAYOUT)
    with tempfile.TemporaryDirectory() as root:
        write_tree(root)
        bad = check_no_cross_app_imports(root)
        print("跨 app 依赖违规:", bad or "无")

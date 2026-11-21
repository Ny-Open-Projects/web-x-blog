"""相对导入边界:__package__ 与 beyond top-level 解剖。"""
import os
import subprocess
import sys
import tempfile

TREE = {
    "pkg/__init__.py": "",
    "pkg/base.py": "TAG = 'base'\n",
    "pkg/inner.py": "from . import base\nprint('inner ok:', base.TAG)\n",
    "pkg/too_deep.py": "from ... import nothing\nprint('never here')\n",
    "top.py": "import pkg.inner\n",
    "bad_top.py": "from .. import nothing\n",
    "top2.py": "import pkg.too_deep\n",
}


def build_tree(root):
    for rel, content in TREE.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def run(script, root):
    env = dict(os.environ, PYTHONPATH=root, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, os.path.join(root, script)],
                       capture_output=True, text=True, env=env, cwd=root)
    lines = (p.stdout + p.stderr).strip().splitlines()
    return p.returncode, lines[-1] if lines else ""


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        build_tree(root)
        rc, last = run("top.py", root)
        print("脚本 import 包内相对模块:", rc == 0, "|", last)
        rc, last = run("bad_top.py", root)
        print("顶层模块用 ..:", rc != 0, "|", last)
        rc, last = run("top2.py", root)
        print("包内模块向外多跳一层:", rc != 0, "|", last)
        code = ("import pkg, pkg.base;"
                "print('pkg.__package__:', repr(pkg.__package__),"
                "'| pkg.base.__package__:', repr(pkg.base.__package__))")
        env = dict(os.environ, PYTHONPATH=root, PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-c", code],
                           capture_output=True, text=True, env=env)
        print(p.stdout.strip() or p.stderr.strip().splitlines()[-1])

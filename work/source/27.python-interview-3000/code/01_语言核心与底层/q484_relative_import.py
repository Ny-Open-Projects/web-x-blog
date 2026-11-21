import os
import subprocess
import sys
import tempfile

RUNNER = """
from . import helper            # 包内相对导入
def run():
    return helper.help()
"""

HELPER = """
def help():
    return "helped"
"""

INIT = "from . import helper\n"

SCRIPT = """
import sys
sys.path.insert(0, {root!r})
from pkg import runner          # 入口:绝对导入
print("runner ->", runner.run())
"""

if __name__ == "__main__":
    root = tempfile.mkdtemp()
    pkg = os.path.join(root, "pkg")
    os.makedirs(pkg)
    for name, src in (("__init__.py", INIT), ("helper.py", HELPER), ("runner.py", RUNNER)):
        with open(os.path.join(pkg, name), "w", encoding="utf-8") as f:
            f.write(src)
    script = os.path.join(root, "entry.py")
    with open(script, "w", encoding="utf-8") as f:
        f.write(SCRIPT)

    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print("stdout:", result.stdout.strip())
    tail = result.stderr.strip().splitlines()[-1] if result.stderr else "(none)"
    print("stderr tail:", tail)

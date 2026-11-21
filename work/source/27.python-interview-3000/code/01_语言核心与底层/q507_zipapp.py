import os
import subprocess
import sys
import tempfile
import zipfile

MAIN_PY = 'def main():\n    print("zipapp is running")\n'
ENTRY_PY = "from main import main\nmain()\n"

def build_app(srcdir, target):
    with open(os.path.join(srcdir, "main.py"), "w", encoding="utf-8") as f:
        f.write(MAIN_PY)
    with open(os.path.join(srcdir, "__main__.py"), "w", encoding="utf-8") as f:
        f.write(ENTRY_PY)
    with zipfile.ZipFile(target, "w") as zf:      # 等价于 python -m zipapp
        for name in ("__main__.py", "main.py"):
            zf.write(os.path.join(srcdir, name), name)

if __name__ == "__main__":
    src = tempfile.mkdtemp()
    out = os.path.join(src, "tool.pyz")
    build_app(src, out)
    print("built:", out, os.path.getsize(out), "bytes")

    result = subprocess.run([sys.executable, out], capture_output=True, text=True)
    print("run:", result.stdout.strip())

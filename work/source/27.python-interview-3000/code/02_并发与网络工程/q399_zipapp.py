"""用 zipapp 打包一个可独立运行的应用。"""
import shutil
import tempfile
import zipfile
from pathlib import Path

APP_MAIN = '''\
import sys
def main():
    print("hello from pyz, args =", sys.argv[1:])
if __name__ == "__main__":
    main()
'''


def build_app(dest="/tmp/hello.pyz"):
    build_dir = Path(tempfile.mkdtemp()) / "helloapp"
    build_dir.mkdir(parents=True)
    (build_dir / "__main__.py").write_text(APP_MAIN, encoding="utf-8")
    (build_dir / "lib.py").write_text("VALUE = 42\n", encoding="utf-8")
    # shebang 让 pyz 在 Linux 可直接执行
    shutil.make_archive(str(build_dir) + "_zip", "zip", build_dir)
    import zipapp
    zipapp.create_archive(build_dir, target=dest, interpreter="/usr/bin/env python3")
    return dest


if __name__ == "__main__":
    app = build_app()
    print("生成:", app)
    with zipfile.ZipFile(app) as z:
        print("包内文件:", z.namelist())
    # 运行方式: python3 /tmp/hello.pyz --name test
    import subprocess
    import sys
    out = subprocess.run([sys.executable, app, "--name", "test"],
                         capture_output=True, text=True)
    print("运行输出:", out.stdout.strip())

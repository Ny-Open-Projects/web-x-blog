---
title: [Q399] zipapp:把脚本打包成单文件应用
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q399 · zipapp:把脚本打包成单文件应用

> 难度:★★☆ | 标签:zipapp, 打包, 分发

**问**:不想让用户装依赖环境,有没有比 Docker 更轻的分发方式?

**答**:`zipapp` 可把一个目录(含依赖)打成单个 `.pyz` 文件,目标机器只要有 Python 即可 `python app.pyz` 直接运行;若在文件头写入 shebang(`python -m zipapp -p "/usr/bin/env python3"`)还可在 Linux 上 chmod 后当可执行文件跑。适合内网工具分发;依赖要一起打进包里(先 `pip install -t` 到构建目录)。局限:纯 Python,含 C 扩展的包要保证目标平台兼容;大型服务仍推荐容器。

```python
# file: code/02_并发与网络工程/q399_zipapp.py
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
```

**追问**:
- `__main__.py` 在打包里起什么作用?zipapp 运行时把 zip 加入 sys.path 并执行其中 `__main__.py`,它是入口约定,类似目录的 `__main__` 机制。
- 怎么处理第三方依赖?构建时 `pip install -r requirements.txt -t build_dir/` 把依赖平铺进目录再打包;含 C 扩展需在目标平台构建。

---
title: "[Q5170] zipapp 冻结导入资源定位事故"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5170 · zipapp 冻结导入资源定位事故

难度：P7 ｜ 标签：zipapp、zipimport、__file__、importlib.resources、资源定位

**问**：把应用打成 `.pyz` 后，代码里 `os.path.join(os.path.dirname(__file__), "config.json")` 为什么在本地目录能跑、打包后却 `FileNotFoundError`/`NotADirectoryError`？`__file__` 在 zip 导入下到底是什么形态？`importlib.resources.files()` 为什么能读到而 `open()` 不能？冻结（freeze）/PyInstaller 这类方案又有什么不同的资源定位坑？

**答**：
结论：zipapp 里的模块不是从文件系统加载的，`zipimporter` 给出的 `__file__` 是**归档内虚拟路径**（如 `/path/app.pyz/pkg/mod.py`）——`app.pyz` 在文件树里是个**文件**而不是目录，所以 `os.path.dirname(__file__)` 指向的是"文件内部的假目录"，`os.path.exists()` 为假、`open()` 抛 `NotADirectoryError`。这是"把 `__file__` 当真实文件路径"这一类假设的集中崩溃点：`pathlib.Path(__file__).parent / "data"`、`pkg_resources.resource_filename`、相对路径配置全都失效。正确姿势是用 `importlib.resources.files(pkg).joinpath("data").read_text()`——它走加载器的 `get_resource_reader`，对 `zipimporter` 返回归档内的字节流，不依赖文件系统路径。

取舍：写"可打包"代码有一条硬规则——**永远不要用 `__file__` 推导资源路径**，从第一天就用 `importlib.resources`。`files()` 在 3.9+ 可用、3.12 对 zip 支持完善；若必须兼容老版本用 `importlib.resources.open_binary`。冻结方案（PyInstaller/Nuitka）则是另一套：资源被解包到临时目录（`sys._MEIPASS`），`__file__` 可能是临时路径，此时 `files()` 同样可用但要注意解包目录的生命周期与写入权限。三者的共同教训是"资源访问要过加载器 API，不碰具体路径"。

实战：事故形态是"开发机 `python -m app` 一切正常，打成 `.pyz` 上线后启动就找不到配置文件"——根因几乎都是 `__file__`-based 路径。排查用一行 `print(__file__, os.path.exists(os.path.dirname(__file__)))` 即可确认为虚拟路径。下面现场构造一个最小 zipapp，用子进程执行，对照 `open()` 失败与 `importlib.resources.files()` 成功。

```python
import tempfile, pathlib, zipfile, subprocess, sys

with tempfile.TemporaryDirectory() as td:
    root = pathlib.Path(td)
    pkg = root / "app"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("")
    (pkg / "data.txt").write_text("HELLO-FROM-ZIP")
    (pkg / "__main__.py").write_text(
        "import os\n"
        "from importlib.resources import files\n"
        "print('__file__:', __file__)\n"
        "naive = os.path.join(os.path.dirname(__file__), 'data.txt')\n"
        "print('naive exists:', os.path.exists(naive))\n"
        "try:\n"
        "    open(naive).read()\n"
        "except Exception as e:\n"
        "    print('naive open:', type(e).__name__)\n"
        "print('resource  :', files('app').joinpath('data.txt').read_text())\n"
    )

    pyz = root / "app.pyz"
    with zipfile.ZipFile(pyz, "w") as z:          # 等价于 zipapp.create_archive
        for f in sorted(pkg.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(root).as_posix())
        z.writestr("__main__.py", "import app.__main__\n")

    r = subprocess.run([sys.executable, str(pyz)],
                       capture_output=True, text=True)
    print("returncode:", r.returncode)
    print(r.stdout.strip())
    if r.stderr:
        print("stderr:", r.stderr.strip()[:200])
```

**追问一**：`importlib.resources.files()` 为什么能在 zip 里工作、而 `open(__file__-based-path)` 不能？——因为 `files()` 查询的是**包的加载器**（这里是 `zipimporter`），加载器实现 `get_resource_reader` 能从归档条目读出字节，整个过程不经过 OS 文件路径解析；`open()` 走的是文件系统，归档内的"路径"对 OS 不存在。换句话说资源定位的正确抽象是"包 + 相对名"，不是"绝对路径字符串"。

**追问二**：PEP 594 废弃 `pkg_resources` 后迁移到 `importlib.resources`，最大的行为差异是什么？——`pkg_resources.resource_filename` 会**把资源解压到临时文件**再返回真实路径（所以旧代码能 `open()`），而 `importlib.resources.files()` 返回的是可遍历/可读的 **Traversable 对象**，不保证对应真实文件路径；旧代码若把返回值直接喂给只接受 `str` 路径的第三方库，会失败——需要用 `as_file()` 上下文管理器在确实需要真实文件时显式物化（zip 场景下它自然会创建临时文件并保证生命周期）。

## 背诵要点
- zipapp 下 `__file__` 是归档内虚拟路径（`/x/app.pyz/pkg/mod.py`），`app.pyz` 是文件非目录 → `__file__`-based `open()` 必失败。
- 资源访问走加载器 API：`importlib.resources.files(pkg).joinpath(name).read_text()`，不依赖 OS 路径。
- 冻结方案资源在 `sys._MEIPASS` 等临时目录；需要真实文件路径时用 `as_file()` 物化并管理生命周期。

## 复盘追问
- 应用打成 `.pyz` 后启动找不到配置，如何用一行打印确认是虚拟路径问题并给出兼容源码/归档的修复？（打印 `__file__` 与 `os.path.exists`、改用 `files()`、讨论 `as_file()` 的物化时机）
- 为什么 `pkg_resources.resource_filename` 旧代码迁移后会出问题？（它解压到临时文件返回真路径，`files()` 返回 Traversable 不保证路径，讨论 as_file 的必要性）

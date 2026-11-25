---
title: "[Q7231] rootdir 推断错位：pyproject 与 pytest.ini 并存，conftest 没加载"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7231 · rootdir 推断错位：pyproject 与 pytest.ini 并存，conftest 没加载

难度：P6 ｜ 标签：pytest、rootdir、配置优先级、conftest 加载

基线：Python 3.12；pytest 8.x rootdir 推断与 ini 优先级；纯 Python 模拟向上查找与配置合并。

**问**：仓库根目录同时有 `pyproject.toml`（写了 `[tool.pytest.ini_options]`）和一份遗留的 `pytest.ini`。在根目录跑 `pytest` 正常，但在 `services/api/` 子目录里跑 `pytest`，根目录 conftest 的 fixture 找不到、`--cov` 配置也丢了。pytest 到底怎么决定 rootdir 和配置来源？

**答**：
- **结论**：rootdir 推断顺序：命令行参数 → `-c` 指定文件 → 从公共祖先目录**逐级向上**找第一个含 `pytest.ini` / `pyproject.toml`（且含 `[tool.pytest.ini_options]`）/ `tox.ini`（含 `[pytest]`）/ `setup.cfg`（含 `[tool:pytest]`）的目录，同时要求该目录能作为包根。**同一目录下配置文件有优先级且只会用一个**：`pytest.ini` > `pyproject.toml`，所以两者并存时 `pyproject.toml` 里那段被静默忽略。rootdir 决定 conftest 向上收集的边界、`--cov` 相对路径基准、以及 `rootdir` 相关的缓存路径。
- **取舍**：`pyproject.toml` 集中配置是现代做法，但必须删掉遗留 `pytest.ini`；monorepo 里每个子包各自 rootdir 能让子包独立跑测试，代价是共享 fixture 要下沉到各自 conftest 或用 `--rootdir` 显式钉住。
- **实战**：① 全仓只保留**一个** pytest 配置源；② CI 里 `pytest --rootdir=. -c pyproject.toml` 显式钉死，并用 `pytest --trace-config` 打印实际生效配置；③ 子目录运行用 `python -m pytest`（把 cwd 加入 `sys.path`，避免 import 错）；④ 用 `--collect-only -q` 断言收集数与预期一致。

```python
"""rootdir 推断：从测试路径向上找第一个配置文件；同目录按优先级取一个。"""
import os

PRIORITY = ["pytest.ini", "pyproject.toml", "tox.ini", "setup.cfg"]


def has_pytest_section(path: str) -> bool:
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return False
    if path.endswith("pyproject.toml"):
        return "[tool.pytest.ini_options]" in text
    if path.endswith("setup.cfg"):
        return "[tool:pytest]" in text
    if path.endswith("tox.ini"):
        return "[pytest]" in text
    return True                                  # pytest.ini 天然算配置


def find_config(start: str) -> tuple[str | None, str | None]:
    """逐级向上，返回 (rootdir, 选中的配置文件)。"""
    cur = os.path.abspath(start)
    while True:
        found = [n for n in PRIORITY
                 if os.path.isfile(os.path.join(cur, n))
                 and has_pytest_section(os.path.join(cur, n))]
        if found:
            return cur, os.path.join(cur, found[0])   # 优先级最高的那个
        parent = os.path.dirname(cur)
        if parent == cur:
            return None, None
        cur = parent


if __name__ == "__main__":
    root = "/tmp/demo_pytest_root"
    os.makedirs(f"{root}/services/api/tests", exist_ok=True)

    with open(f"{root}/pyproject.toml", "w") as f:
        f.write("[tool.pytest.ini_options]\naddopts = '-q --cov=app'\n")
    with open(f"{root}/pytest.ini", "w") as f:
        f.write("[pytest]\naddopts = -q\n")       # 遗留文件，优先级更高
    with open(f"{root}/services/api/conftest.py", "w") as f:
        f.write("# local fixtures\n")

    # 1) 从根目录跑
    rd, cfg = find_config(root)
    print("根目录跑 -> rootdir:", rd, "| 配置:", os.path.basename(cfg))

    # 2) 从子目录跑：向上找到根，但选中的是 pytest.ini
    rd2, cfg2 = find_config(f"{root}/services/api")
    print("子目录跑 -> rootdir:", rd2, "| 配置:", os.path.basename(cfg2))
    print("  pyproject 里的 --cov 被忽略:", "cov" not in open(cfg2).read())

    # 3) 删掉遗留 pytest.ini 后
    os.remove(f"{root}/pytest.ini")
    rd3, cfg3 = find_config(f"{root}/services/api")
    print("删除 pytest.ini -> 配置:", os.path.basename(cfg3),
          "| 含 cov:", "cov" in open(cfg3).read())

    # 4) 子目录自己也有配置时会截断向上查找
    with open(f"{root}/services/api/pytest.ini", "w") as f:
        f.write("[pytest]\n")
    rd4, cfg4 = find_config(f"{root}/services/api/tests")
    print("子包自带 pytest.ini -> rootdir:", rd4, "-> 根 conftest 不再被加载")
    print("结论：配置源必须唯一；rootdir 判错会连带丢 conftest 与插件参数")
```

**追问一**：`python -m pytest` 和 `pytest` 有什么区别？
→ 解析：`python -m pytest` 会把当前目录加入 `sys.path`，因此能 import 到本地包；`pytest` 可执行文件不会，于是出现 `ModuleNotFoundError: No module named 'app'`。容器/CI 里统一用 `python -m pytest` 能省掉一堆 `PYTHONPATH` 设置。

**追问二**：conftest.py 的加载范围怎么确定？
→ 解析：pytest 会加载 rootdir 到测试文件路径上**所有祖先目录**的 conftest.py，但不会加载兄弟目录的；子目录 conftest 里的 fixture 对其下所有测试可见。rootdir 判错（例如子包自带 `pytest.ini` 截断了向上查找）会导致父级 conftest 整个被跳过。

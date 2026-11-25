---
title: [Q7191] setup.py 到 pyproject.toml 迁移破坏点
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7191 · setup.py 到 pyproject.toml 迁移破坏点

难度：P6 ｜ 标签：版本演进、打包、pyproject、PEP 621

基线：Python 3.9+；setuptools 61+（原生 PEP 621）/ hatchling / uv；pip 23+。

**问**：老项目还是 `setup.py` + `setup.cfg`，团队要迁到 PEP 621 的 `pyproject.toml`。除了把元数据搬过去，还有哪些"搬家搬一半就坏"的坑？动态版本号、数据文件、自定义构建步骤怎么办？

**答**：
- **结论**：迁移破坏点集中在"元数据之外的构建逻辑"：
  1. **动态版本**：`setup.py` 里读 `__version__`/git tag 的逻辑要换成构建后端的原生能力（setuptools 的 `[tool.setuptools.dynamic]` + attr，或 hatch 的 `[tool.hatch.version]`），直接删 setup.py 会让 CI 里的 `python setup.py sdist` 类脚本失效；
  2. **打包范围变化**：`packages=find_packages()` → `[tool.setuptools.packages.find]`，命名空间包与 `package_data`（非 Python 文件）的迁移常被漏掉，装出来"缺配置文件"；
  3. **构建依赖**：`pyproject.toml` 的 `[build-system] requires` 决定隔离构建环境，老的本地 hack（编译前生成代码的脚本）要么写成 build backend 钩子，要么进 `requires`；
  4. **可编辑安装语义变化**：`pip install -e .` 在 setuptools 新版默认 PEP 660 模式，行为与老的 egg-link 有差异，个别 IDE/工具识别不了；
  5. **`python setup.py test/install` 已废弃**：CI 脚本全量换成 `python -m build` + `pip install`。
- **取舍**：可以渐进——先加 `[build-system]` 声明隔离构建，元数据逐步从 setup.cfg 搬；保留 setup.py 做过渡 shim（`from setuptools import setup; setup()`）直到确认没有外部工具直接调用它。
- **实战**：迁移验收清单——本地 `python -m build` 产出的 wheel/sdist 内容 diff（`unzip -l` 对比清单）；装到干净 venv 验证数据文件齐全；CI 构建/发布流程全路径跑通；uv/pip 安装与 editable 两模式都验证。

```python
# 打包迁移自检：对比 wheel 内容清单，找"搬家后丢文件"（标准库可运行）。
import zipfile

def diff_wheel(old: str, new: str, data_suffixes=(".json", ".yaml", ".toml")) -> list[str]:
    """old/new: 两个 wheel 路径，返回新版丢失/新增的文件。"""
    def names(path):
        with zipfile.ZipFile(path) as z:
            return set(z.namelist())
    old_n, new_n = names(old), names(new)
    lost = sorted(n for n in old_n - new_n if n.endswith(data_suffixes))
    extra = sorted(n for n in new_n - old_n)[:5]
    return [f"丢失数据文件: {n}" for n in lost] + \
           [f"新增文件: {n}" for n in extra]

def check_dynamic_version(pyproject: str) -> list[str]:
    """静态检查动态版本与 package_data 是否声明。"""
    issues = []
    if "version" not in pyproject and "dynamic" not in pyproject:
        issues.append("version 既未静态声明也未列入 dynamic -> 构建报错")
    if 'packages.find' in pyproject and 'package-data' not in pyproject \
            and "include-package-data" not in pyproject:
        issues.append("用了 packages.find 但没配 package-data -> 非 .py 文件不会进 wheel")
    return issues or ["打包配置自检通过"]

if __name__ == "__main__":
    print(check_dynamic_version("""
[project]
name = "svc"
dependencies = ["httpx"]
[tool.setuptools.packages.find]
where = ["src"]
"""))
    # ['version 既未静态声明也未列入 dynamic -> 构建报错',
    #  '用了 packages.find 但没配 package-data -> 非 .py 文件不会进 wheel']
```

**追问**：
- 一层：为什么 `[build-system] requires` 必须显式声明？→ 提示：PEP 517 隔离构建环境里没有你的老依赖，构建期 import 的东西（如代码生成器）要么进 requires 要么删掉。
- 二层：`pip install -e .` PEP 660 模式和老 egg-link 有什么实际差异？→ 提示：新模式装的是"editable wheel"，靠 import hook；个别静态分析器和老版本 setuptools-run 脚本不认，需要 `_editable_mode=compat` 兜底。

**背诵要点**：
1. 破坏点五件套：动态版本机制、packages.find/package_data 范围、build-system requires、PEP 660 editable 语义、setup.py CLI 全废弃。
2. 验收靠 wheel 内容 diff + 干净 venv 安装验证，不是"能 build"就行。
3. 渐进迁移：先 [build-system] 隔离构建，保留 setup.py shim 过渡，CI 全部换 python -m build。

**复盘追问**：
1. 迁移后线上服务为什么缺配置文件？提示：package_data/include-package-data 没配，wheel 里根本没有非 .py 文件。
2. 如何防止"有人还在跑 python setup.py sdist"？提示：仓库 grep + CI 门禁，构建脚本统一入口到 python -m build。

---
title: "[Q7198] package-data 缺失导致 wheel 丢失资源文件"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7198 · package-data 缺失导致 wheel 丢失资源文件

难度：P6 ｜ 标签：事故复盘、打包、pyproject、资源文件

基线：Python 3.12；setuptools 61+；zipfile 标准库演示 wheel 内容核对。

**问**：`pip install .` 后包能正常 import，但运行时报 `FileNotFoundError: templates/config.yaml`——这个文件明明在源码树里，本地源码模式跑也没问题。为什么装成 wheel 就没了？怎么防？

**答**：
- **结论**：wheel 构建默认只打包 Python 模块（`.py`），非代码资源（模板、配置、数据、证书）不会自动进包。要在 `pyproject.toml` 里显式声明：`[tool.setuptools] include-package-data = true` 配合 `MANIFEST.in` 的 `recursive-include mypkg/templates *.yaml`，或直接用 `[tool.setuptools.package-data]` 写 `mypkg = ["templates/*.yaml"]`。本地能跑是因为源码树里文件就在原地，wheel 没带过去才暴露。
- **取舍**：声明太宽会把测试、缓存、`__pycache__` 甚至敏感文件打进 wheel（体积膨胀 + 泄露风险）；太窄会漏文件。要精确列出 glob 并在 CI 里"拆开 wheel 检查清单"验证。读取侧用 `importlib.resources` 而不是 `os.path.join(__file__, ...)`（后者在 zip 包/命名空间包里会失效）。
- **实战**：把"构建 wheel → 解压列出资源文件 → 断言关键文件存在"做成 CI 步骤；用 `python -m build` 后检查 `.whl` 内容；对数据文件较大的场景评估是否该外置到包外并由配置指定路径。

```python
import io
import zipfile


def build_wheel(files: dict[str, bytes]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, data in files.items():
            z.writestr(name, data)
    return buf.getvalue()


def has_resource(wheel_bytes: bytes, rel: str) -> bool:
    with zipfile.ZipFile(io.BytesIO(wheel_bytes)) as z:
        return rel in z.namelist()


if __name__ == "__main__":
    target = "mypkg/templates/config.yaml"
    undeclared = build_wheel({"mypkg/__init__.py": b""})
    declared = build_wheel(
        {"mypkg/__init__.py": b"", target: b"key: value"}
    )
    print("未声明 -> 丢失:", has_resource(undeclared, target))
    print("已声明 -> 存在:", has_resource(declared, target))
```

**追问一**：为什么源码模式能跑、装成 wheel 就报缺文件？
→ 解析：源码运行时资源文件在文件系统原位置，代码用相对路径能读到；wheel 只装了被声明打包的文件，未声明的资源根本没进 site-packages，路径自然失效。

**追问二**：用 `importlib.resources` 读取资源相比 `open(__file__ + '/../x')` 好在哪？
→ 解析：`importlib.resources` 通过包系统定位资源，兼容 zip 包、命名空间包、可编辑安装等多种形态，不依赖文件系统具体路径，是官方推荐做法。

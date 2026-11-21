---
title: [Q7101] pytest 8 升级破坏点
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7101 · pytest 7 → 8 升级破坏点与测试套件演进

难度：P6 ｜ 标签：pytest / 版本演进 / 测试工程

**问**：测试套件几千条用例、十几个 pytest 插件，升级 pytest 8 后一批用例从"静默通过"变成报错。pytest 8 有哪些破坏点？怎么让大套件的升级可控？

**答**：
- **结论**：pytest 8 的主要破坏点：① `pytest.warns(None)` 彻底移除（7.x 已弃用）——想要"必须无告警"要用 `filterwarnings` mark 或 `recwarn` fixture；② `tmpdir`/py.path 局部化进一步弱化，官方主推 `tmp_path`（pathlib），自定义 fixture 返回 py.path 的插件会碎；③ fixture 作用域与缓存路径行为收紧：`--import-mode` 与 rootdir 解析更严格，conftest 里隐式 sys.path 注入的"魔法路径"用法会失效；④ collection 层面：同名测试文件（不同目录下 `test_a.py` 重名）在默认 import-mode 下更严格，需要 `__init__.py` 或 `--import-mode=importlib`；⑤ 参数化 ID 生成、`pytest.ini`/`pyproject.toml` 配置项改名（如 `python_classes` 检查更严格）。插件兼容矩阵是升级的最大变量：pytest-asyncio、pytest-cov、pytest-mock 都要配套升版本。
- **取舍**：升级策略：pin 住 pytest 主版本 + 每季度跟一次小版本；大版本升级在独立分支跑全量套件 + 插件矩阵表逐个核对。`--import-mode=importlib` 是长期正确的方向（免去空 `__init__.py`），但与一些依赖 sys.path 的插件冲突，要灰度切换。
- **实战**：步骤：① 升级前跑 `pytest --co -q` 只收集不执行，先看 collection 层炸掉多少；② 用 `-W error::pytest.PytestDeprecationWarning` 让 7.x 下的弃用告警变失败，先清零再升；③ 插件逐个按官方 release note 核对兼容版本表，pin 到测试过的组合；④ 复盘项：CI 加"pytest 版本升级演练"任务，每月在次要分支跑最新版，保持对破坏面的持续可见。

```python
# pytest 升级前弃用扫描与兼容矩阵校验（纯标准库模拟）
# 基线：Python 3.9+

import ast


DEPRECATED_7 = {
    "pytest.warns(None)": "移除于 8.0，改用 filterwarnings/recwarn",
    "tmpdir fixture": "弱化，改用 tmp_path (pathlib)",
    "setup()/teardown_method 混用 nose 风格": "8.x 收紧",
}

PLUGIN_MATRIX = {
    "pytest-asyncio": {"max_pytest": 8, "min_plugin": "0.23"},
    "pytest-cov": {"max_pytest": 8, "min_plugin": "4.1"},
    "pytest-mock": {"max_pytest": 8, "min_plugin": "3.12"},
}


def scan_sources(sources: dict[str, str]) -> dict[str, list[str]]:
    """静态扫描弃用模式（简化：字符串级匹配示意，AST 需按节点细化）"""
    out = {}
    for name, src in sources.items():
        hits = [f"{pat} -> {msg}" for pat, msg in DEPRECATED_7.items()
                if pat in src]
        if hits:
            out[name] = hits
    return out


def check_plugins(plugins: dict[str, str]) -> list[str]:
    """插件版本是否满足 pytest 8 兼容矩阵"""
    bad = []
    for name, ver in plugins.items():
        need = PLUGIN_MATRIX.get(name)
        if need is None:
            continue
        major = int(ver.split(".")[1])
        if major < int(need["min_plugin"].split(".")[1]):
            bad.append(f"{name} {ver} < {need['min_plugin']}，需升级")
    return bad


def main() -> None:
    srcs = {
        "test_a.py": "def test_x():\n    pytest.warns(None)\n",
        "conftest.py": "# tmpdir fixture 用法\n",
    }
    report = scan_sources(srcs)
    print(report)
    assert "test_a.py" in report and "conftest.py" in report
    bad = check_plugins({"pytest-asyncio": "0.21", "pytest-cov": "4.1"})
    print(bad)
    assert bad == ["pytest-asyncio 0.21 < 0.23，需升级"]
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 `pytest.warns(None)` 被移除而不是保留为"断言无告警"？
→ 一句话提示：它的语义歧义（既像"不检查"又像"断言无告警"）导致大量误用；官方把"无告警"职责交给 `filterwarnings = ["error"]` 配置，语义单一且全局可控。

**追问 2**：`--import-mode=importlib` 解决什么问题，代价是什么？
→ 一句话提示：默认 prepend 模式靠往 sys.path 插根目录来导入测试模块，造成重名文件冲突与 sys.path 污染；importlib 模式不再依赖 sys.path，代价是部分老插件对模块定位的假设失效，切换要验证插件兼容。

## 背诵要点
- pytest 8 破坏面：warns(None) 移除、tmp_path 化、collection/import-mode 收紧、插件矩阵全动。
- 升级流程：`--co` 先验收集 → `-W error::pytest.PytestDeprecationWarning` 清零弃用 → 插件版本表逐个 pin。
- 长期方向：`--import-mode=importlib`（免 sys.path 污染与空 __init__.py），灰度切换验证插件兼容。

## 复盘追问
- 为什么几千条用例的套件升级要先看 collection 而不是先跑用例？提示：收集失败会让整批用例没机会执行，错误形态也与断言失败不同；先收集能快速暴露结构性破坏（重名/导入错误），把修复分层。
- pin 死 pytest 主版本与"每月在分支跑最新版"怎么协作？提示：生产分支稳定、演练分支持续暴露新版破坏面，相当于把升级成本从"一次性大爆炸"摊平成"持续小额修复"，发现问题时还来得及反馈上游。

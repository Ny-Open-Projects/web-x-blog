---
title: [Q7050] pytest 7 到 8 迁移破坏点：yield 测试与 nose 风格的终清
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7050 · 版本演进：pytest 8 升级后几百个用例"跑通了但没测到"，怎么防？

> 难度:★★★ | 标签:版本演进, pytest, 测试工程

**问**：pytest 7 升到 8，CI 全绿，但后来发现一个模块的用例根本没被执行。pytest 8 有哪些静默行为变更？"全绿"为什么在测试框架升级中不可信？迁移审计怎么做成可执行的？

**答**：结论：pytest 8 的破坏点里有两类最危险——**静默不收集**（nose 风格 `setup`/`teardown` 方法不再被调用、模块内无 `test_` 前缀函数静默跳过，用例"存在但未执行"）与**异常断言语义变化**（`pytest.raises` 匹配范围、警告过滤升级为错误）让部分断言形同虚设。测试框架升级的金标准是**用例数与覆盖率双基线对拍**：升级前后收集的用例数、执行的断言数、覆盖率必须一致，"全绿"只是及格线之一。

机理与实战：
- **nose 风格终清**：pytest 8 不再执行类/模块上的 `setup()`（改名 fixture 或 `setup_method`）；如果团队历史用例用了 nose 风格的 setup 做数据准备，升级后用例会"缺前置直接跑"或因前置缺失而假通过——这类破坏不报错，最难发现。
- **yield 测试与 generator 收集**：旧版把生成器函数当 yield 型测试（已废弃多年），8 彻底移除；带 yield 的 test 函数会警告而非执行后半段——断言数量下降要用基线对拍才看得出。
- **警告变错误**：8 默认对部分弃用告警升级，若 CI 配置了 `-W error` 或 filterwarnings 严格模式，原本"告警后继续"的路径变成直接失败——反过来也可能因为过滤器写宽了而掩盖新弃用。
- **可执行迁移审计**：① `pytest --collect-only -q` 前后 diff 用例清单（数量+名字）；② 断言计数：开启 `--co` 对比 + 覆盖率文件 diff（行覆盖/分支覆盖）；③ static 扫描源码找 nose 风格 setup/yield test/`pytest.warns` 老用法；④ 固定 CI 用"覆盖率不低于基线"做门禁，防"跑通但没测到"。

```python
# 基线:Python 3.10+;纯标准库,pytest 8 迁移静态扫描:收集审计与破坏点检测
from __future__ import annotations
import ast
import re
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Finding:
    file: str
    line: int
    kind: str
    detail: str


def scan_test_file(path: Path) -> list[Finding]:
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    fs: list[Finding] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for sub in node.body:
                if isinstance(sub, ast.FunctionDef) and sub.name == "setup":
                    fs.append(Finding(path.name, sub.lineno, "nose-setup",
                                      "pytest 8 不再调用类内 setup(),改 setup_method 或 fixture"))
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
            if ast.get_docstring(node) is None and any(
                isinstance(n, ast.Yield) for n in ast.walk(node)
            ):
                fs.append(Finding(path.name, node.lineno, "yield-test",
                                  "生成器测试已移除,后半段断言不会执行"))
    # 2. 依赖缺前置的风险:setup 被改名前 test 用了其局部状态
    if re.search(r"def\s+setup\s*\(\s*self\s*\)", src):
        fs.append(Finding(path.name, 0, "silent-skip-risk",
                          "存在 nose 风格 setup,升级后相关用例可能静默缺前置"))
    return fs


def collect_baseline(test_dir: Path) -> dict[str, int]:
    """模拟 pytest --collect-only:统计收集到的用例数(按文件)。"""
    out: dict[str, int] = {}
    for p in test_dir.glob("test_*.py"):
        tree = ast.parse(p.read_text(encoding="utf-8"))
        n = sum(1 for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef)
                and node.name.startswith("test_"))
        out[p.name] = n
    return out


def guard_no_regression(old: dict[str, int], new: dict[str, int]) -> list[str]:
    """门禁:升级后收集数不得低于基线。"""
    issues = []
    for f, n in old.items():
        if new.get(f, 0) < n:
            issues.append(f"{f}: 收集数 {n} -> {new.get(f, 0)},存在静默丢失")
    return issues


def demo(tmp: Path) -> None:
    d = tmp / "tests"
    d.mkdir()
    (d / "test_legacy.py").write_text(
        "class TestCart:\n"
        "    def setup(self):\n"
        "        self.cart = []\n"
        "    def test_empty(self):\n"
        "        assert self.cart == []\n"
        "\n"
        "def test_gen():\n"
        "    yield 1\n",
        encoding="utf-8")
    fs = scan_test_file(d / "test_legacy.py")
    kinds = {f.kind for f in fs}
    print(f"破坏点: {sorted(kinds)}")
    assert "nose-setup" in kinds and "yield-test" in kinds and "silent-skip-risk" in kinds
    base = collect_baseline(d)
    assert base["test_legacy.py"] == 2
    # 升级后模拟:yield 测试不再收集
    new = {"test_legacy.py": 1}
    issues = guard_no_regression(base, new)
    assert issues
    print(f"收集对拍门禁: {issues}")
    print("迁移审计:收集清单 diff + 覆盖率基线 + nose/yield 静态扫描 ✅")


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        demo(Path(td))
```

**追问一**：为什么测试框架升级不能只跑测试套件当验证？
答：因为破坏点往往表现为"用例不执行"而非"用例失败"——全绿与没跑在结果页上长得一样。必须用"过程指标"（收集数、断言数、覆盖率）与升级前基线对拍，任何指标下降都是红旗。这是测试工程区别于普通代码升级的核心方法论：验证对象是"验证系统本身"。

**追问二**：fixture 作用域与参数化在 7→8 有什么值得注意的细节变更？
答：8 对 fixture 依赖解析报错更严格（循环依赖/未定义 fixture 从告警变错误）、参数化 id 生成规则微调、`pytest.raises` 的 match 正则应用范围收紧。这类变更的共同特征是"严格化"——老版本靠宽松语义跑过的用例，升级后要么报错（好事，暴露坏测试）要么语义变化（坏事，需对拍）。迁移 checklist 要按"报错类"和"语义类"分开处理。

## 背诵要点
- pytest 8 最危险的破坏是静默不收集：nose 风格 setup() 不再调用、yield 测试移除——用例"存在但未执行"，全绿不可信。
- 升级验证靠过程指标基线对拍：--collect-only 用例清单 diff + 断言/覆盖率不低于基线，作为 CI 门禁。
- 迁移审计四步：静态扫描（nose setup/yield test/老 warns 用法）→ 收集对拍 → 覆盖率对拍 → 严格化变更按"报错类/语义类"分治。

## 复盘追问
- 事故里"没测到"的模块是怎么在覆盖率门禁下漏网的？（提示：门禁只看了行覆盖没看分支覆盖，或该模块的覆盖率统计被 conftest 里的 exclude 配置覆盖；覆盖率口径本身也是需要版本演进的配置，升级时一并审计）
- 团队有 3000 个用例，逐个人工迁移不现实，怎么自动化？（提示：静态扫描输出分类清单→每类写一次机械替换（codemod/正则）→对拍门禁验证替换无损→分批合入；迁移的工程化核心是把"语义判断"收敛为可枚举的模式匹配）

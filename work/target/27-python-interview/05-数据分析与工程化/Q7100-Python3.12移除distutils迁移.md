---
title: [Q7100] Python 3.12 移除 distutils 的打包迁移
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7100 · Python 3.12 移除 distutils 的打包迁移

难度：P6 ｜ 标签：打包 / setuptools / 版本演进

**问**：项目升 Python 3.12 后 `import distutils` 直接报 ModuleNotFoundError，一些老包（setup.py 里用 distutils.command、或依赖 `distutils` 的库）全崩了。distutils 为什么被移除？迁移的标准路径是什么？

**答**：
- **结论**：distutils 是标准库里年久失修的构建工具（无依赖管理、无法声明构建需求），PEP 632 决定在 3.12 移除，生态统一到 setuptools + pyproject.toml（PEP 517/518）。迁移三条路径：① 自己代码用 `distutils.core.setup`/`distutils.command` → 改成 `setuptools`（setuptools 内置了兼容副本，装 setuptools 后 `import distutils` 可用，且 3.12 起 pip 安装 setuptools 时会注入 `SETUPTOOLS_USE_DISTUTILS` 兼容层）；② 用了 `distutils.util.strtobool` 等散装工具函数 → 自写 10 行等价函数（strtobool 这种小函数官方建议自己复制）；③ 第三方老包崩溃 → 升级该包，升级不了则把它 pin 住并自己在依赖里显式装 setuptools。CI 里 Python 3.11 → 3.12 升级的第一批失败基本全是这一类。
- **取舍**：继续靠 setuptools 的兼容层"不改也能跑" vs 彻底清理：兼容层是过渡品（setuptools 未来也可能再变），新代码绝不 import distutils；存量代码用 lint 规则（`flake8-no-pep420`/自定 banned-import）拦住新增。`setup.py` → `pyproject.toml` 的彻底迁移收益是构建可复现（`build-system.requires` 锁版本）与 editable install 行为统一（PEP 660），建议与 Python 升级同批做掉。
- **实战**：步骤：① CI 先建"Python 3.12 兼容矩阵"分支，让所有失败暴露；② 全库 grep `distutils`（含 `from distutils`），按三类分流处理；③ 检查依赖树（`pip install setuptools` 是否出现在所有运行环境——不只是构建环境，旧包运行时 import distutils 也需要它）；④ 复盘项：把"标准库移除清单"（distutils、asynchat、asyncore、smtpd、imghdr 等已在 3.12/3.13 移除的模块）做成升级检查项。

```python
# distutils 迁移检查器 + strtobool 等价实现（纯标准库）
# 基线：Python 3.9+（strtobool 等价函数自持，不依赖 distutils）

import ast
import sys


BANNED = ("distutils",)


def scan_imports(source: str) -> list[str]:
    """AST 扫描 banned import（比正则可靠：能识别 from distutils.util import x）"""
    hits = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in BANNED:
                    hits.append(f"line {node.lineno}: import {a.name}")
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in BANNED:
                hits.append(f"line {node.lineno}: from {node.module} import ...")
    return hits


def strtobool(v: str) -> int:
    """distutils.util.strtobool 的标准库等价实现"""
    v = v.strip().lower()
    if v in ("y", "yes", "t", "true", "on", "1"):
        return 1
    if v in ("n", "no", "f", "false", "off", "0"):
        return 0
    raise ValueError(f"invalid truth value {v!r}")


def main() -> None:
    src = (
        "from distutils.util import strtobool\n"
        "import distutils.core\n"
        "import os\n"
    )
    hits = scan_imports(src)
    print(hits)
    assert len(hits) == 2
    assert scan_imports("import setuptools") == []
    assert strtobool("TRUE") == 1 and strtobool("off") == 0
    try:
        strtobool("maybe")
        raise AssertionError("should raise")
    except ValueError:
        pass
    print("OK: 迁移检查 + strtobool 自持实现")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 distutils 移除后 pip 安装的老包还能跑？
→ 一句话提示：pip 安装 setuptools 时通过 import hook 注入兼容副本（`SETUPTOOLS_USE_DISTUTILS=stdlib/local` 机制），让 `import distutils` 在 3.12+ 仍可解析——但这是补丁不是承诺，新代码依赖它等于埋雷。

**追问 2**：`pyproject.toml` 的 `build-system.requires` 解决了什么老问题？
→ 一句话提示：老 `setup.py` 构建依赖（setuptools 版本等）没有声明位置，靠环境碰运气；PEP 517/518 把构建环境隔离出来并按 requires 精确安装，构建从"环境敏感"变成"可复现"。

## 背诵要点
- distutils 在 3.12 移除（PEP 632），生态统一到 setuptools + pyproject.toml（PEP 517/518/660）。
- 迁移三分流：setup 代码改 setuptools、散装工具函数（strtobool 等）自持实现、老第三方包升级或显式加 setuptools 依赖。
- 运行环境也要装 setuptools（不只构建环境）；AST 级 banned-import 扫描防新增。

## 复盘追问
- 为什么建议 banned-import 用 AST 而不是 grep？提示：正则匹配不到多行/别名/条件导入等形态，AST 能精确拿到 Import/ImportFrom 节点与行号，且不会把注释里的字符串误报。
- "标准库移除清单"里 3.13 还移除了什么值得列进检查表？提示：3.13 移除了 20+ 个"dead batteries"（pep594 相关：imghdr、sndhdr、cgi、telnetlib、crypt 等）；Python 大版本升级的检查项应该按官方 What's New 的 Removal 章节走查。

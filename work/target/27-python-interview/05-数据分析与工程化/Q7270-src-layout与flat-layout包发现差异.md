---
title: "[Q7270] import 撞名全靠 sys.path 运气：src layout 与 flat layout 的包发现差异"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7270 · import 撞名全靠 sys.path 运气：src layout 与 flat layout 的包发现差异

难度：P5 ｜ 标签：src layout、flat layout、包发现、import 解析、打包

基线：Python 3.12；用 sys.path 顺序查找模拟 flat layout 的顶层包冲突与 src layout 的命名空间隔离，全标准库实跑。

**问**：仓库里两个子项目都有顶层 `utils` 包，本地跑 A 项目没问题，B 项目一上线就 import 到错误的 utils——为什么 flat layout 会撞名？src layout 解决了什么问题？"测试时 import 的包"和"安装后 import 的包"为什么会不一样？

**答**：
- **结论**：flat layout 把包目录直接放在项目根（`proj-a/utils/`），**顶层包名进入全局命名空间**，import 解析沿 `sys.path` 顺序找第一个命中——两个项目的 `utils` 谁在前谁赢，顺序就是命运：pytest 把 rootdir 塞进 sys.path 的顺序、安装方式、启动目录的细微变化都会改变结果。src layout 把包放进 `src/<pkg>/` 并强制通过**安装**（`pip install -e .`）暴露：import 的永远是各自顶层包（`packa.utils`/`packb.utils`），命名空间互不重叠；更关键的一致性收益：**测试 import 的形态 = 用户安装后的形态**——flat layout 下测试能"蹭"到项目根的直接 import（未安装也能跑），发布后用户却必须装包再 import，两条路径的发现行为不同，"本地好好的、装上就报错"（模块漏打、data file 丢失）就是这么来的。src layout 从结构上杜绝"未安装可用"，逼着打包配置与真实一致。
- **取舍**：① src layout 的摩擦：开发期必须 editable install（Q7119 PEP 660 的实现），IDE 配置多一步；换来的是 import 真实性；② 单包小工具用 flat 没问题（无多项目、无顶层冲突风险）——不教条；③ 多项目 monorepo 里还可以用 workspace/uv workspace 类机制统一安装管理，src layout 是其中的基础设施；④ 顶层通用名（`utils`、`common`、`core`）在任何 layout 下都该避免——src layout 防的是"两包互相撞"，防不了"你的包名和第三方库撞"（PyPI 名与 import 名一致是另一个防线）。
- **实战**：① 新仓库默认 src layout + `hatchling`/`setuptools` 显式包发现配置（auto-discovery 在混合结构下有歧义，显式声明 `packages = [...]`）；② CI 里加"安装校验"：`pip install .` 后从仓库根**外**的目录跑测试 import，模拟真实用户路径；③ `pytest` 配置 `pythonpath` 补丁要慎用——它恢复的正是 flat layout 的"蹭路径"行为；④ 包内相对导入与绝对导入统一绝对（`from packa.utils import x`），可读且与安装形态一致。

```python
"""Q7270 src layout vs flat layout: 顶层包同名冲突 vs src 隔离。

模拟 import 机制: sys.path 顺序查找, 先命中者赢。
"""
# 各目录导出的顶层包/模块
TREES = {
    "/repo/proj-a": {"utils": "projA.utils", "app": "projA.app"},
    "/repo/proj-b": {"utils": "projB.utils", "core": "projB.core"},
    "/repo/wheelsrc/proj-a": {"src": {"packa": {"utils": "projA.src.packa.utils"}}},
}


def import_flat(python_path: list[str], top: str) -> str:
    """flat layout: 顶层包直接躺在项目根, 沿 sys.path 找第一个命中."""
    for root in python_path:
        if root in TREES and top in TREES[root]:
            return TREES[root][top]
    raise ModuleNotFoundError(top)


if __name__ == "__main__":
    path = ["/repo/proj-a", "/repo/proj-b"]
    # proj-a 的代码 import utils -> 命中谁?
    r1 = import_flat(path, "utils")
    print(f"flat: sys.path={path}, import utils -> {r1} (永远命中第一个)")
    # proj-b 想用自己的 utils? 没有机会, 除非调整 sys.path 顺序
    r2 = import_flat(["/repo/proj-b", "/repo/proj-a"], "utils")
    print(f"flat: 调整顺序后 import utils -> {r2} -> 全局只有一份 utils, 顺序即命运")

    # src layout: 包在 src/<pkg> 下, 安装后命名空间互不重叠
    pa = TREES["/repo/wheelsrc/proj-a"]["src"]["packa"]["utils"]
    print(f"src : packa.utils -> {pa}, projB 安装为 packb.utils, 互不可见互不冲突")

    ok = (r1 == "projA.utils" and r2 == "projB.utils" and pa == "projA.src.packa.utils")
    print(f"校验: flat 顶层冲突 + src 隔离 -> {'通过' if ok else '异常'}")
    print("结论：flat layout 的顶层包是全局单例, 两个项目同名必冲突;")
    print("      src layout 强制装进各自顶层包, 测试 import 的是已安装形态, 与运行时一致")
```

**追问一**：pytest 为什么会"帮倒忙"——rootdir insertion 是怎么让 flat layout 的包被 import 的？

→ 解析：pytest 的默认 rootdir 行为（rootdir/`conftest.py` 所在目录插入 `sys.path`，配合 legacy 的 `rootdir` 自动插入）会把测试所在目录塞进 `sys.path` 头部；flat layout 下项目根就是包的父目录，`import utils` 于是直接命中源码树——**未安装就能跑**，这个便利正是事故温床：① 打包配置漏了某个子包，测试照常全绿（蹭到了源码），用户装完 import 报 ModuleNotFoundError；② 测试 import 的 `utils` 可能是"项目根的源码版"，而用户拿到的是"site-packages 的安装版"，data 文件、编译扩展在两条路径上存在差异。src layout 下项目根下没有可直接 import 的包，pytest 只能走安装形态——摩擦变成了保险。工程校验：CI 用 `python -c "import packa"` 从非仓库目录验证，再跑测试；两者都过才算打包闭环。

**追问二**：namespace package（PEP 420 隐式命名空间）和 src layout 是什么关系？什么时候用得上？

→ 解析：PEP 420 命名空间包允许**同一个顶层包名由多个发行版分别提供**（如 `mycompany.tool.a` 和 `mycompany.tool.b` 分属两个安装包，运行时合并成一个 `mycompany.tool` 命名空间）：目录不带 `__init__.py`，import 系统把多处的同名目录拼接。它与 src layout 是正交的两件事：src layout 解决"项目内多包的发现与安装一致性"，namespace package 解决"跨发行版共享顶层命名空间"。用得上的场景：monorepo 拆包发布（每个子包独立版本独立发版，但逻辑上属于同一产品线）；用不上的场景：普通单应用——命名空间包放弃了部分工具兼容（打包器对无 `__init__.py` 目录的处理需显式配置），还引入"两处代码都定义了 `mycompany.tool.utils` 时静默合并"的隐患（与 flat 撞名同病）。决策顺序：先 src layout + 独立包名，确认真的需要跨发行版合并命名空间，再上 PEP 420——它是特殊场景的工具，不是默认架构。

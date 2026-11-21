---
title: [Q7011] ruff + pyright 的规则分层与 monorepo 增量检查
date: 2026-11-19
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7011 · ruff + pyright 规则分层

> 难度:★★☆ | 标签:静态检查, 工程化

**问**：ruff 和 pyright 分工是什么——哪些问题 ruff 该管、哪些必须 pyright/mypy？「规则全开 → CI 满屏红」的落地策略是什么（分层渐进），monorepo 全量检查 20 分钟怎么压到 2 分钟（增量与缓存）？

**答**：① 分工：**ruff 管「风格与确定性规则」**（lint/格式化/import 排序/死代码/复杂度，AST 快查，毫秒级）；**pyright/mypy 管「类型推断与跨文件语义」**（类型错误、Optional 穿透、泛型匹配——需要全程序分析，慢）；重叠区（如未定义名）以类型检查器为准。② 分层渐进三步：第一层全仓 `E/F/W` 基础正确性 + `ruff format` 统一（一次提交解决存量）；第二层新代码严格——CI 按增量目录开 `B/UP/SIM/ANN`（旧代码 `.ruff.toml` 逐目录豁免，改到哪开到哪）；第三层类型 strict 化同 Q7001 路线。③ 增量提速：ruff 本身快（Rust，全仓秒级）；瓶颈在 pyright——按变更目录 + 依赖闭包分析（`--outputjson` 过滤）、CI 缓存 venv 与类型 stubs、pre-commit 只查暂存文件、远程执行（monorepo 常用 Bazel/Pants 缓存）。

```python
# demo：规则分层配置与增量过滤器（纯标准库模拟）
import subprocess, pathlib, json

PYPROJECT = """
[tool.ruff]                          # 第一层：全仓基础（存量一次清完）
lint.select = ["E", "F", "W"]
[tool.ruff.lint.per-file-ignores]
"legacy/*" = ["ALL"]                 # 旧目录豁免，改到哪开到哪
[tool.ruff.lint.extend-select]       # 第二层：新代码严格（增量目录启用）
"""
STRICT_DIRS = {"services/api", "sdk/"}          # 严格化已完成目录

def lint_plan(changed_files: list[str]) -> dict:
    """CI 增量计划：严格目录走全规则，其余基础规则。"""
    plan = {"strict": [], "basic": []}
    for f in changed_files:
        (plan["strict"] if any(f.startswith(d) for d in STRICT_DIRS)
         else plan["basic"]).append(f)
    return plan

def typecheck_scope(changed: list[str], dep_map: dict[str, set[str]]) -> set[str]:
    """pyright 范围 = 变更文件 + 依赖闭包（只查受影响的）。"""
    scope = set()
    stack = list(changed)
    while stack:
        f = stack.pop()
        if f in scope: continue
        scope.add(f)
        stack.extend(dep_map.get(f, []))          # 依赖闭包传播
    return scope

if __name__ == "__main__":
    changed = ["services/api/user.py", "legacy/old.py", "sdk/client.py", "docs/x.py"]
    print("lint 计划:", lint_plan(changed))
    deps = {"services/api/user.py": {"services/api/schema.py", "sdk/base.py"},
            "sdk/client.py": {"sdk/base.py"}}
    scope = typecheck_scope(changed, deps)
    print("pyright 范围:", sorted(scope), f"（全仓 500 文件 → {len(scope)} 文件）")
    # 口径：ruff 全仓秒级必跑；pyright 只跑依赖闭包；CI 缓存 venv+stubs；
    # pre-commit 钩住暂存区，CI 钩全量正确性——两层闸门不重复。
    # 验证 pyproject 语法：ruff check --show-settings 前先 parse（此处省略外部调用）。
```

**追问**：1) 为什么不直接 mypy+flake8 全家桶？——flake8/isort/pylint 被 ruff 替代后工具链收敛（一个二进制、一套配置、快 10-100×），团队规则心智成本骤降；mypy vs pyright 看 IDE 生态（pyright 快、VSCode 原生，mypy 社区插件多）。2) `.ruff.toml` 逐目录豁免会失控吗？——豁免清单必须进台账（谁开的、为什么、何时删），豁免数是反向指标进 code review 检查项；「豁免不过夜」纪律。3) 类型检查缓存失效粒度？——pyright 按包级缓存（依赖变了才重查）；monorepo 里把稳定 SDK 包发 wheel 锁版本，检查器只看工作区变更。

## 背诵要点
1. 分工：ruff=风格+确定性规则（毫秒级全仓），pyright/mypy=类型推断+跨文件语义（增量跑）。
2. 分层渐进：基础规则全仓一次清 → 严格规则按增量目录启用 → 类型 strict 化（联动 Q7010）。
3. 提速三板斧：依赖闭包过滤、venv/stubs CI 缓存、pre-commit 只查暂存区。

## 复盘追问
1. 团队规范落了三个月又松弛了，机制上怎么防退化？（提示：豁免台账+豁免数指标、CI 强制门禁（不告警而是失败）、月度规则审计）
2. ruff format 和 black 有什么冲突处理？（提示：ruff format 兼容 black 风格——迁移期锁定同一版本避免 churn，过渡完成删 black）

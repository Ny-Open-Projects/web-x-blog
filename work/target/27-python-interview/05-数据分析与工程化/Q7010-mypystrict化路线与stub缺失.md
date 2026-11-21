---
title: [Q7010] mypy strict 化路线图与三方库 stub 缺失应对
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7010 · mypy strict 化路线图与三方库 stub 缺失应对

> 难度:★★★ | 标签:类型检查, mypy, 工程化

**问**：仓库 30 万行，mypy 一开报 8000 个错，团队直接放弃了。strict 化的正确路线是什么？遇到三方库没有类型标注（或 stub 是错的）怎么办？

**答**：结论：strict 化是"封存量、控增量"的工程，不是一次性修复：`disallow_untyped_defs` 等按模块渐进启用（mypy 的 per-module options），已达标模块锁 strict，新模块强制 strict，存量按改动频率分批清。stub 缺失的应对优先级：官方/社区 stub 包（`types-*`）> 库自带 py.typed > 自写最小 stub（`stubtest` 校验）> 降级 `ignore_missing_imports = True`（仅限该模块，并记录在案）。stub "错误"比"缺失"更危险——要覆盖（`types-` 包版本优先于库内声明）或上报修复，不能静默 ignore。

路线图与实战：
- 顺序：先 `check_untyped_defs = true`（不改代码语义，暴露最多价值）→ 对新代码 `disallow_untyped_defs` → 存量按目录渐进 → 最后开 `strict = true` 收口。每步用 CI 报告量化：typed 函数占比、strict 模块数，趋势可见团队才不会疲惫。
- 常见坑：`Any` 传染（一个 Any 参数让整条调用链失去检查）——strict 下用 `disallow_any_explicit` 控制；mypy cache 在 CI 不命中导致 10 分钟检查——缓存目录（`.mypy_cache`）按 lock 哈希缓存，与依赖缓存同层。
- 事故复盘：一次 stub 缺失让 mypy 对 `redis` 的调用全按 Any 放行，`decode_responses` 忘配导致 bytes 与 str 混用上线。修复：自写 `redis-stubs` 最小 stub（覆盖 get/set/decode_responses 签名），stubtest 对比真实库签名；同类第三方库建立"stub 登记表"（库→处理方式→负责人），缺失不可见才是最大风险。

```python
# 基线:Python 3.10+ / mypy 1.x;本文件自身可被 mypy 校验,演示渐进配置思想(可运行)
from typing import TypedDict

class ModulePolicy(TypedDict):
    path: str
    strict: bool          # per-module 渐进:存量 False,达标后翻 True

POLICIES: list[ModulePolicy] = [
    {"path": "src/new_service/*", "strict": True},
    {"path": "src/legacy/order/*", "strict": False},   # 待清理,按改动频率排期
]

def plan(policies: list[ModulePolicy], weekly_changes: dict[str, int]) -> list[str]:
    """按'改动频率 × 未 strict'排清理优先级(可运行)。"""
    todo = [p["path"] for p in policies if not p["strict"]]
    order = sorted(todo, key=lambda p: -weekly_changes.get(p, 0))
    return [f"清存量:{p}(周改动 {weekly_changes.get(p, 0)} 次)" for p in order]

def stub_action(lib: str) -> str:
    """stub 缺失的处置决策树。"""
    if lib.startswith("types-"):
        return f"安装 {lib} 并锁版本"
    return (f"{lib}: 1) 找 types-{lib} 2) 无则自写最小 stub+stubtest "
            f"3) 记入登记表,禁止全局 ignore_missing_imports")

if __name__ == "__main__":
    print(plan(POLICIES, {"src/legacy/order/*": 45}))
    print(stub_action("redis"))
```

**追问**：
- 一层追问：mypy 报错太多时为什么不该用大量 `# type: ignore` 压下去？——ignore 是全局豁免且会掩盖未来的真实错误；正确做法是 per-error-code 豁免（`# type: ignore[union-attr]`）+ 期限记录，或先修 `check_untyped_defs` 的结构性问题。
- 二层追问：py.typed 是什么、为什么有的库要装 types-xxx 有的不用？——`py.typed` 是 PEP 561 标记，表示库自带类型信息；没带的库 mypy 按 Any 处理（除非装社区 stub）。安装优先级是 stub 包覆盖库内声明（types-* 比 py.typed 新版更准时可临时覆盖）。
- 三层追问：mypy strict 下的性能问题怎么处理？——30 万行全量检查可超 10 分钟：CI 用增量 cache + 只对 PR 变更模块跑全深度（`--follow-imports=silent` 策略），夜间全量；另外 `mypy --fast` 实验特性与模块拆分（减少循环导入）都是常规手段。

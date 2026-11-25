---
title: [Q7176] mypy strict 渐进升级的版本演进与迁移
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7176 · 从"mypy 全绿"到 strict 全绿：类型检查的渐进演进路线

难度：P6 ｜ 标签：版本演进、mypy、类型标注
基线：mypy 1.x（`--strict` 全家桶）；Python 3.10+ 语法（`X | None`）；PEP 604/696。

**问**：团队仓库 30 万行，mypy 现在只开了几个宽松选项，CI 里类型检查"形同虚设"。想演进到 `--strict`，一次全开会必然报出几千个错误。渐进路线怎么设计？每一步动哪些配置？

**答**：**结论**：strict 是一组开关的合集（`disallow_untyped_defs`、`warn_return_any`、`no_implicit_optional` 等），**按模块渐进、按开关递增**：① 先开"全局低成本"开关（`no_implicit_optional`、`check_untyped_defs`），这类错误少、收益高；② 再按目录开 `disallow_untyped_defs`——用 per-module section 把新代码目录设 strict，旧目录维持现状；③ 用 `mypy --strict` 的输出做"欠账清单"，按目录错误数排序，逐目录清零后把该目录加入 strict 白名单；④ 用 pre-commit/CI 门禁锁住"欠账不增"——新增错误直接拒绝合并。另一个大坑是第三方库缺 stub：`ignore_missing_imports` 不要全局开，用 per-module 精确豁免。

**取舍**：mypy 版本本身也在演进：小版本升级常带来新错误（推断变严了），所以 **mypy 版本要与配置一起锁**——CI 里用 uv/pip 锁死版本，升级 mypy 与清零新错误作为一个独立变更，不要和业务变更混在一起。替代路线是 Pyright（默认更严、编辑器体验好），但两者规则差异不小，从 mypy 起家的仓库中途换工具的迁移成本要按"全量新错误数"评估，通常不值得，选一个长期养。

**实战**：渐进 strict 的配置生成与欠账清单工具（标准库演示）：

```python
# 渐进开启 strict 的配置生成器与欠账排序
STRICT_FLAGS = ["disallow_untyped_defs", "warn_return_any", "no_implicit_optional"]

GLOBAL_SAFE = ["no_implicit_optional", "check_untyped_defs"]  # 可全局开的低误报开关

modules = {  # 目录 -> (行数, 严格模式已开?, 当前错误数)
    "app/api":     (8_000,  True,  0),
    "app/models":  (15_000, True,  0),
    "app/legacy":  (40_000, False, 1_200),
    "app/parsers": (12_000, False, 340),
    "app/scripts": (6_000,  False, 2_100),
}

def gen_mypy_ini() -> str:
    lines = ["[mypy]"]
    for flag in GLOBAL_SAFE:
        lines.append(f"{flag} = True")
    lines.append("")
    for mod, (_, strict, errs) in modules.items():
        if strict:
            lines.append(f"[mypy-{mod.replace('/', '.')}]")
            for f in STRICT_FLAGS:
                lines.append(f"{f} = True")
            lines.append("")
    return "\n".join(lines)

print(gen_mypy_ini())

# 欠账清单：按"错误密度"排序，先清性价比高的
debt = sorted(
    ((m, e, rows) for m, (rows, strict, e) in modules.items()
     if not strict and e > 0),
    key=lambda t: t[1] / t[2], reverse=True)
print("\n欠账排序（错误密度降序）:")
for m, e, rows in debt:
    print(f"  {m}: {e} 错 / {rows:,} 行 = {e/rows:.4f} 密度")

# 门禁：欠账不增
def gate(current_total: int, baseline: int) -> str:
    if current_total > baseline:
        return f"BLOCK: 类型欠账 {current_total} > 基线 {baseline}"
    return f"PASS: 欠账 {current_total} <= 基线 {baseline}（可继续渐进清零）"

print(gate(sum(e for _, (_, _, e) in modules.items()), 3640))
```

**追问 1**：`check_untyped_defs` 与 `disallow_untyped_defs` 的区别是什么？为什么前者可以先全局开？
提示：前者检查无标注函数体内部逻辑（对现有代码侵入小），后者要求函数签名本身有标注（对增量开发有约束力）；先开前者等于"提前踩掉 most 错误"。

**追问 2**：mypy 升级后突然多出几百个错误怎么办？
提示：锁版本是常态；升级作为独立变更，先在分支跑出新错误清单，按"真实缺陷/标注噪音"分类，噪音用 per-module 配置收敛而不是全局放宽。

**追问 3**：`ignore_missing_imports` 全局开会有什么后患？
提示：缺 stub 的第三方 API 全部变成 Any，类型检查在这些边界上失明且永远不知道；正确做法 per-module 豁免并定期复查（上游可能已补 stub）。

## 背诵要点
1. strict 是开关合集：先全局开低成本开关（no_implicit_optional/check_untyped_defs），再按目录开 disallow_untyped_defs，错误密度排序清欠账。
2. 门禁核心是"欠账不增"：CI 基线数锁定，新增类型错误拒绝合并；mypy 版本与配置一起锁，升级独立变更。
3. 缺 stub 用 per-module 豁免，禁全局 ignore_missing_imports——全局豁免让类型检查在第三方边界永久失明。

## 复盘追问
1. 你们 CI 的类型检查现在报多少错、为什么一直没清？欠账基线有没有被"定期上调"过？
2. 如果明天要换 Pyright，你如何评估迁移成本？全量新错误数的盘点脚本会怎么写？

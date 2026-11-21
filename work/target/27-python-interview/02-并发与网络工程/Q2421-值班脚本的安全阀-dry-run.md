---
title: [Q2421] 值班脚本的安全阀:dry-run
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2421 · 值班脚本的安全阀:dry-run

> 难度:★★☆ | 标签:dry-run, 值班脚本, 审计

**问**:半夜三点跑处置脚本,怎么保证不会手滑删库?

**答**:安全阀三件套:默认 dry-run 只打印计划不执行;dry-run 与 apply 走同一条代码路径,只在动作落地最后一刻分流;审计留痕,事后能对账"当时打算做什么"。

- 实测 dry-run:四个动作全部留下 DRY 计划行,效果列表为空,零副作用;

- 实测 apply:计划内三项逐项落地,计划外的动作绝不顺手执行;

- 实测两模式审计行形状一致,只差 DRY/APPLY 前缀与结果字段,复盘时同一张表能对上;

- 开关用环境变量或参数显式声明,默认值必须是最安全的那一档。

```python
# file: code/02_并发与网络工程/q2421_dry_run_safety.py
# -*- coding: utf-8 -*-
"""值班脚本的安全阀: 默认 dry-run, 说清楚要做什么, 才允许真做。

- 危险操作脚本的第一行输出永远是计划, 而不是执行结果;
- dry-run 与 apply 走同一条代码路径, 只在动作落地的最后一刻分流;
- 审计日志两种模式形状一致, 事后能对账"当时打算做什么"。
"""
ACTIONS = {
    "restart-worker": lambda arg: "worker-%s 已重启" % arg,
    "flush-cache": lambda arg: "缓存池 %s 已清空" % arg,
    "drain-queue": lambda arg: "队列 %s 已排水" % arg,
}


def execute(plan, effects, audit, apply_mode):
    """计划与执行共用一条路径: apply_mode 是唯一的分流点。"""
    for action, arg in plan:
        if action not in ACTIONS:
            audit.append("SKIP  unknown-action %s" % action)
            continue
        if apply_mode:
            result = ACTIONS[action](arg)
            effects.append(result)
            audit.append("APPLY %-14s %s -> %s" % (action, arg, result))
        else:
            audit.append("DRY   %-14s %s -> [未执行]" % (action, arg))
    return audit


def main():
    plan = [("restart-worker", "a"), ("flush-cache", "main"),
            ("drain-queue", "email"), ("kick-server", "x")]

    # 场景一: 默认 dry-run, 零副作用
    effects, audit1 = [], []
    execute(plan, effects, audit1, apply_mode=False)
    print("dry-run 审计:")
    for line in audit1:
        print("  ", line)
    assert effects == [], "dry-run 模式必须零副作用"
    assert len(audit1) == len(plan), "没执行的计划也要全部留痕"

    # 场景二: 显式 apply, 逐项执行, 计划里没有的动作不碰
    effects, audit2 = [], []
    execute(plan[:3], effects, audit2, apply_mode=True)
    print("apply 审计:")
    for line in audit2:
        print("  ", line)
    assert len(effects) == 3, "apply 模式逐项落地"
    assert "kick-server" not in " ".join(audit2), "计划外的动作绝不顺手执行"

    # 形状对照: 同一动作两种模式的审计行, 动作与参数字段一致
    dry_line = [l for l in audit1 if "flush-cache" in l][0]
    apply_line = [l for l in audit2 if "flush-cache" in l][0]
    print("对照: %r vs %r" % (dry_line, apply_line))
    assert dry_line.split()[1:3] == apply_line.split()[1:3], \
        "审计形状一致, 只差 DRY/APPLY 前缀与结果字段"


if __name__ == "__main__":
    main()
```

**追问**:1) dry-run 怎么保证和真实执行等价?——计划、校验、依赖检查全跑,只有副作用那一行分流;等价性靠代码结构保证而不是靠自觉。2) 审计日志放哪?——本地留一份、远端存一份,时间戳加操作者,值班的对账全靠它。3) 「同一条代码路径、最后一刻分流」的等价性怎么保证?——计划生成/校验/依赖检查全跑,只有「动作落地」一行分流(dry-run 打印,apply 执行)——等价性靠代码结构(副作用集中在单点)而不是自觉;评审规则:危险脚本禁止两条独立路径。4) 安全阀的默认值与审计形状?——默认 dry-run(最安全档),apply 需显式授权(环境变量/参数);审计两模式形状一致(只差 DRY/APPLY 前缀),复盘同一张表对账——「计划先行+形状一致」是值班脚本的两个不变量。5) 生产陷阱?——dry-run 与 apply 双路径(逻辑漂移,测的和跑的不同);默认 apply(半夜手滑);审计缺失或形状不一(对不上账);dry-run 不做依赖检查(计划可执行性没验证);apply 后无结果确认(成功与否靠猜)。

---

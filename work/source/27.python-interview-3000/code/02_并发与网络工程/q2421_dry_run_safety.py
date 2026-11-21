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

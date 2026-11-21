"""写入模式选择器:按表形态与重放语义选 append overwrite 还是 upsert"""

RULES = [
    (lambda m: m["kind"] == "事件流水" and not m["replayable"],
     "append", "流水不可重放,只追加,重复靠去重键兜底"),
    (lambda m: m["kind"] == "事件流水" and m["replayable"],
     "overwrite_partition", "可重放流水按分区覆盖,重跑即重写当天"),
    (lambda m: m["kind"] == "聚合快照",
     "overwrite_partition", "聚合结果按分区覆盖,天然幂等"),
    (lambda m: m["kind"] == "维表",
     "upsert", "维表按业务键 upsert,保留最新属性"),
]


def decide(meta):
    for cond, mode, reason in RULES:
        if cond(meta):
            return mode, reason
    return "manual", "未匹配规则,禁止自动选择,转人工评审"


if __name__ == "__main__":
    cases = [
        {"kind": "事件流水", "replayable": False, "name": "埋点日志"},
        {"kind": "事件流水", "replayable": True, "name": "订单事实"},
        {"kind": "聚合快照", "replayable": True, "name": "渠道日聚合"},
        {"kind": "维表", "replayable": True, "name": "商品维表"},
        {"kind": "未知形态", "replayable": False, "name": "外部同步表"},
    ]
    for meta in cases:
        mode, reason = decide(meta)
        print(f"{meta['name']:<8} -> {mode:<20} {reason}")
    print("要点:写法选错,重跑不是翻倍就是丢历史;规则表进代码评审,新表形态先补规则再上线;append 表要配套去重键与迟到数据策略")

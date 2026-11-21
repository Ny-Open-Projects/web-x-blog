"""丢弃与死信的决策表: 条件到处置动作的显式映射"""

from collections import namedtuple

Event = namedtuple("Event", "id error retries critical")
# 决策表: 错误类型, 重试下限, 是否关键字段(None 不限) -> 动作, 理由
RULES = [
    ("格式错误", 0, True, "死信", "结构坏且关键字段缺失, 进死信等回放"),
    ("格式错误", 0, False, "丢弃", "非关键字段坏, 丢弃并计数, 别为垃圾占队列"),
    ("超时", 3, None, "死信", "重试预算耗尽, 转死信避免无限重试"),
    ("超时", 0, None, "重试", "预算未用完, 退避重试"),
    ("业务校验", 0, None, "隔离区", "格式对但业务不合理, 人工判定"),
]
FALLBACK = ("死信", "未匹配规则兜底, 宁可多存不可静默丢")


def route(event):
    for etype, min_retry, need_critical, action, why in RULES:
        if event.error != etype or event.retries < min_retry:
            continue
        if need_critical is not None and event.critical != need_critical:
            continue
        return action, why
    return FALLBACK


if __name__ == "__main__":
    stream = [
        Event("e1", "格式错误", 0, True),
        Event("e2", "格式错误", 0, False),
        Event("e3", "超时", 1, False),
        Event("e4", "超时", 5, False),
        Event("e5", "业务校验", 0, False),
        Event("e6", "未知异常", 0, False),
    ]
    for e in stream:
        action, why = route(e)
        print(f"{e.id} [{e.error} 重试{e.retries} 关键={e.critical}] -> {action}: {why}")
    print("要点: 决策表进配置走评审; 每个动作带计数; 兜底死信让未知形态暴露而不是被吞掉")

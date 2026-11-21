"""余额类指标必须用快照事实表:重放事件流会漏迟到数据,期末余额只认快照"""

# 已收到的钱包事件流水(day2 的 -30 迟到,暂未到)
TX = [
    ("u1", 1, 100),
    ("u1", 4, 50),
    ("u2", 1, 80),
    ("u2", 3, -20),
]
OPENING = {"u1": 0, "u2": 0}

SNAPSHOT = {  # 日末余额快照(权威)
    1: {"u1": 100, "u2": 80},
    2: {"u1": 70, "u2": 80},
    3: {"u1": 70, "u2": 60},
    4: {"u1": 120, "u2": 60},
}


def balance_from_events(tx, opening, day):
    """重放流水算余额:缺一条事件结果就错,且重放成本随历史增长"""
    bal = dict(opening)
    for u, d, amt in sorted(tx, key=lambda x: x[1]):
        if d <= day:
            bal[u] = bal.get(u, 0) + amt
    return bal


if __name__ == "__main__":
    replay = balance_from_events(TX, OPENING, 4)
    snap = SNAPSHOT[4]
    print(f"重放流水到 day4: {replay}  <- 少了迟到扣款,虚高 30")
    print(f"快照表 day4:     {snap}")
    print(f"day4 期末总余额(快照口径): {sum(snap.values())}")
    print("要点:余额/库存/在架数是'状态'不是'流量',建周期快照表按日全量落盘;流水只算变动量,状态指标永远以快照为准")

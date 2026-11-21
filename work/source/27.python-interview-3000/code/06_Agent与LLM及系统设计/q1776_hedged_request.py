"""对冲请求:主请求慢于对冲阈值时影子重发,先到先用其余取消,尾延迟被打掉。"""


class HedgedClient:
    """离散事件模拟:worker 为预设耗时列表,假时钟逐拍推进。"""

    def __init__(self, hedge_delay=1.0):
        self.hedge_delay = hedge_delay
        self.stats = {"hedged": 0, "cancelled": 0}

    def request(self, delays):
        launched = [{"delay": delays[0], "start": 0.0}]
        now = 0.0
        while True:
            now = round(now + 0.1, 2)
            if len(launched) < len(delays) and now >= self.hedge_delay:
                launched.append({"delay": delays[len(launched)], "start": now})
                self.stats["hedged"] += 1        # 对冲:影子请求上路
            done = [(now - l["start"], i) for i, l in enumerate(launched)
                    if now - l["start"] >= l["delay"]]
            if done:
                winner = min(done)               # 完成时刻最早者胜出
                self.stats["cancelled"] += len(launched) - 1
                return {"result": "resp", "at": now, "worker": winner[1]}


if __name__ == "__main__":
    c = HedgedClient(hedge_delay=1.0)
    r1 = c.request([0.3])
    assert r1 == {"result": "resp", "at": 0.3, "worker": 0}
    assert c.stats == {"hedged": 0, "cancelled": 0}, "主请求快,无需对冲"

    r2 = c.request([2.0, 0.5])
    assert r2["worker"] == 1 and r2["at"] == 1.5, "主慢:1.0 对冲,1.5 影子先回"
    assert c.stats["hedged"] == 1 and c.stats["cancelled"] == 1

    r3 = c.request([1.2, 1.5])
    assert r3["worker"] == 0 and r3["at"] == 1.2, "对冲已发但主请求先回"
    assert c.stats == {"hedged": 2, "cancelled": 2}, "在途对冲请求被取消"
    print("对冲请求通过:慢主请求被影子赛赢,快主请求取消在途对冲,尾延迟受控")

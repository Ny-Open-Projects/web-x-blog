"""指令优先级冲突仲裁:system 覆盖 developer 覆盖 user,同层不抢占,冲突留痕。"""

LEVELS = {"system": 0, "developer": 1, "user": 2}


class InstructionResolver:
    """同 tag 的指令按层级裁决:低 level 恒胜,被压制的指令记入 overridden。"""

    def __init__(self):
        self.won = {}
        self.overridden = []

    def submit(self, level, tag, text):
        assert level in LEVELS, "未知指令层级"
        cand = {"level": level, "rank": LEVELS[level], "text": text}
        cur = self.won.get(tag)
        if cur is None:
            self.won[tag] = cand
            return "accepted"
        if cand["rank"] < cur["rank"]:
            self.overridden.append({"tag": tag, "loser": cur, "winner": cand})
            self.won[tag] = cand
            return "overrides"
        self.overridden.append({"tag": tag, "loser": cand, "winner": cur})
        return "suppressed"                      # 同层或更低:不抢占

    def resolve(self):
        return {t: c["text"] for t, c in self.won.items()}


if __name__ == "__main__":
    r = InstructionResolver()
    assert r.submit("system", "language", "全程使用中文") == "accepted"
    assert r.submit("user", "language", "请用英文回答") == "suppressed"
    assert r.submit("developer", "language", "输出面向开发者") == "suppressed"
    assert r.submit("user", "length", "回答尽量简短") == "accepted"
    assert r.submit("developer", "length", "长度按开发者规范") == "overrides"
    assert r.resolve() == {"language": "全程使用中文", "length": "长度按开发者规范"}
    assert len(r.overridden) == 3, "每次压制与覆盖都要留痕"
    assert all(i["winner"]["rank"] <= i["loser"]["rank"] for i in r.overridden)
    print("指令仲裁通过:system 恒胜 user,同层不抢占,全部裁决可审计")

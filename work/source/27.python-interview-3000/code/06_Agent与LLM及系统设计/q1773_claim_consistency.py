"""答案一致性自检:声明级拆解逐条对来源,与他源矛盾的声明打冲突标记。"""

SOURCES = [
    {"id": "s1", "text": "A 产品 续航 为 十二 小时 支持 快充"},
    {"id": "s2", "text": "A 产品 续航 为 十八 小时"},
    {"id": "s3", "text": "A 产品 支持 快充 与 防水"},
]

CLAIM_SPLIT_STUB = ["A 产品 续航 为 十二 小时", "A 产品 支持 快充"]


class FakeLLM:
    """声明拆解桩:按预设把答案切成原子声明,离线确定。"""

    @staticmethod
    def split_claims(answer):
        return CLAIM_SPLIT_STUB


def source_tokens(text):
    return set(text.split())


class ConsistencyChecker:
    NUM_WORDS = ["十二", "十八", "二十"]

    def __init__(self, sources):
        self.sources = sources

    def check(self, answer):
        claims = FakeLLM.split_claims(answer)
        report = []
        for claim in claims:
            ctoks = set(claim.split())
            hits = [s for s in self.sources if ctoks <= source_tokens(s["text"])]
            report.append({"claim": claim,
                           "supported_by": [s["id"] for s in hits],
                           "conflict": self._contradict(claim)})
        return {"claims": report,
                "consistent": all(not c["conflict"] for c in report)}

    def _contradict(self, claim):
        """数值型声明:同一话题存在他源不同取值即冲突。"""
        if "续航" not in claim:
            return False
        claim_val = next((w for w in self.NUM_WORDS if w in claim), None)
        if claim_val is None:
            return False
        for s in self.sources:
            if "续航" in s["text"]:
                other = next((w for w in self.NUM_WORDS if w in s["text"]), None)
                if other and other != claim_val:
                    return True
        return False


if __name__ == "__main__":
    checker = ConsistencyChecker(SOURCES)
    report = checker.check("A 产品续航十二小时,支持快充")
    c1, c2 = report["claims"]
    assert c1["supported_by"] == ["s1"], "续航声明仅被 s1 支持"
    assert c1["conflict"] is True, "s2 记载十八小时,构成冲突"
    assert c2["supported_by"] == ["s1", "s3"] and c2["conflict"] is False
    assert report["consistent"] is False, "存在冲突声明则整份答案不通过"

    clean = ConsistencyChecker([SOURCES[0], SOURCES[2]]).check("A 产品续航十二小时,支持快充")
    assert clean["consistent"] is True, "移除矛盾来源后自检通过"
    print("一致性自检通过:声明拆解 逐条溯源,冲突声明可定位到来源与取值")

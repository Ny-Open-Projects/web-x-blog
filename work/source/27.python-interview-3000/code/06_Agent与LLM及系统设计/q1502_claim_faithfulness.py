"""忠实度校验:答案拆原子声明,逐条与检索证据做词面蕴含匹配,输出无据声明清单。"""
import re


def split_claims(answer):
    """把答案按句号分号拆成原子声明,长句再按逗号二分。"""
    parts = re.split(r"[。;]", answer)
    claims = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if len(p) > 10 and "," in p:
            claims.extend(s.strip() for s in p.split(",") if s.strip())
        else:
            claims.append(p)
    return claims


def tokens(text):
    """极简中文切词:2-gram 覆盖 + 单字,便于词面匹配。"""
    t = re.sub(r"\s", "", text)
    grams = {t[i:i + 2] for i in range(len(t) - 1)}
    return grams | set(t)


class FaithfulnessChecker:
    """声明级校验:每条声明与最相似证据算覆盖率,低于阈值判 unsupported。"""

    def __init__(self, threshold=0.35):
        self.threshold = threshold

    def check(self, answer, evidences):
        claims = split_claims(answer)
        report = []
        for c in claims:
            ct = tokens(c)
            best = 0.0
            best_ev = None
            for ev in evidences:
                et = tokens(ev)
                cover = len(ct & et) / max(1, len(ct))
                if cover > best:
                    best, best_ev = cover, ev
            report.append({"claim": c, "score": round(best, 2), "evidence": best_ev,
                           "supported": best >= self.threshold})
        return report

    def verdict(self, answer, evidences):
        report = self.check(answer, evidences)
        bad = [r for r in report if not r["supported"]]
        ratio = 1 - len(bad) / max(1, len(report))
        return {"faithfulness": round(ratio, 2), "unsupported": [r["claim"] for r in bad],
                "pass": ratio >= 0.8}


if __name__ == "__main__":
    evidences = ["退款在订单页申请后 48 小时内到账 原路退回",
                 "电子发票在个人中心申请 开票信息需与下单时一致"]

    grounded = FaithfulnessChecker().verdict("退款 48 小时内到账 原路退回。", evidences)
    assert grounded["pass"] is True and grounded["unsupported"] == []

    mixed = FaithfulnessChecker().verdict("退款 48 小时内到账。会员积分年底双倍返还。", evidences)
    assert mixed["pass"] is False, "含无据声明必须不通过"
    assert any("积分" in c for c in mixed["unsupported"]), "无据声明被点名"

    empty = FaithfulnessChecker().verdict("会员积分年底双倍返还。", evidences)
    assert empty["faithfulness"] == 0.0

    claims = split_claims("退款很快。积分规则复杂,年底清零;发票自助开具。")
    assert len(claims) == 4, "长句按逗号二分 声明数应为 4"
    print("忠实度校验通过:声明级打分 无据声明", mixed["unsupported"], "总分", mixed["faithfulness"])

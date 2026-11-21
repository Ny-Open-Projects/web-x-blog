"""引用覆盖率与悬空引用检查:每个陈述都要有引用编号,编号必须能解析到真实来源。"""
import re


def parse_citations(answer):
    """提取 [n] 形式引用:返回 (段落陈述, 引用编号列表) 与全文用过的编号。"""
    segs = []
    used = set()
    for para in [p.strip() for p in answer.split("\n") if p.strip()]:
        ids = [int(x) for x in re.findall(r"\[(\d+)\]", para)]
        used.update(ids)
        segs.append({"text": re.sub(r"\[\d+\]", "", para).strip(), "cites": ids})
    return segs, used


class CitationChecker:
    """引用检查:覆盖率 = 有引用陈述占比;悬空 = 指向不存在来源的编号。"""

    def __init__(self, sources):
        self.sources = sources             # 编号 -> 来源文本

    def check(self, answer):
        segs, used = parse_citations(answer)
        dangling = sorted(u for u in used if u not in self.sources)
        uncited = [s["text"] for s in segs if not s["cites"]]
        coverage = 1 - len(uncited) / max(1, len(segs))
        # 每个来源是否被至少引用一次 引用利用度
        utilized = {i for s in segs for i in s["cites"] if i in self.sources}
        unused_sources = sorted(set(self.sources) - utilized)
        return {"coverage": round(coverage, 2), "dangling": dangling,
                "uncited": uncited, "unused_sources": unused_sources}

    def require(self, answer, min_coverage=1.0):
        r = self.check(answer)
        problems = []
        if r["coverage"] < min_coverage:
            problems.append("覆盖率不足 " + str(r["coverage"]))
        if r["dangling"]:
            problems.append("悬空引用 " + str(r["dangling"]))
        return {"ok": not problems, "problems": problems, "detail": r}


if __name__ == "__main__":
    sources = {1: "退款规则文档", 2: "发票指南", 3: "会员协议"}
    ck = CitationChecker(sources)

    good = ck.require("退款 48 小时到账[1]。\n发票自助开具[2]。")
    assert good["ok"] is True and good["detail"]["coverage"] == 1.0
    assert good["detail"]["dangling"] == []
    assert good["detail"]["unused_sources"] == [3], "来源 3 未被引用应提示"

    partial = ck.check("退款 48 小时到账[1]。\n这句没有任何引用。")
    assert partial["coverage"] == 0.5 and partial["uncited"] == ["这句没有任何引用。"]

    dang = ck.require("积分不清零[9]。")
    assert dang["ok"] is False and dang["detail"]["dangling"] == [9]
    assert any("悬空" in p for p in dang["problems"])

    low = ck.require("没有引用的一句。", min_coverage=1.0)
    assert low["ok"] is False and any("覆盖率" in p for p in low["problems"])
    print("引用检查通过:覆盖率 1.0 与 0.5 悬空引用 9 被拦截 未用来源 3 被提示")

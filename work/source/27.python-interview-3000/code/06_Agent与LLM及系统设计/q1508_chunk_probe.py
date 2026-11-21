"""切块质量探针:过短 过长 近重复 无标题四类异常块检测,输出修复建议。"""
from collections import defaultdict


def shingles(text, k=4):
    t = "".join(text.split())
    return {t[i:i + k] for i in range(len(t) - k + 1)}


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


class ChunkProbe:
    """块质量探针:阈值化检测 + 近重复聚类,每类给一条修复建议。"""

    def __init__(self, min_len=20, max_len=100, dup_threshold=0.65):
        self.min_len, self.max_len, self.dup_t = min_len, max_len, dup_threshold

    def probe(self, chunks):
        """chunks: [{id, text, has_heading}] 返回异常清单与建议。"""
        issues = []
        for c in chunks:
            n = len(c["text"])
            if n < self.min_len:
                issues.append({"id": c["id"], "type": "too_short", "len": n,
                               "advice": "与相邻块合并后再入库"})
            elif n > self.max_len:
                issues.append({"id": c["id"], "type": "too_long", "len": n,
                               "advice": "按标题或段落二次切分"})
            if not c.get("has_heading", False):
                issues.append({"id": c["id"], "type": "no_heading", "len": n,
                               "advice": "补一级标题提升检索可定位性"})

        # 近重复:shingle Jaccard 超阈值即视为重复组
        sig = {c["id"]: shingles(c["text"]) for c in chunks}
        ids = [c["id"] for c in chunks]
        dup_groups = []
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                a, b = ids[i], ids[j]
                if a in sig and b in sig and jaccard(sig[a], sig[b]) >= self.dup_t:
                    for g in dup_groups:
                        if a in g or b in g:
                            g.update((a, b))
                            break
                    else:
                        dup_groups.append({a, b})
        for g in dup_groups:
            issues.append({"id": sorted(g)[0], "type": "near_duplicate",
                           "duplicates": sorted(g)[1:],
                           "advice": "保留信息最全的一块 其余标记删除"})
        return issues

    def health(self, chunks):
        issues = self.probe(chunks)
        types = defaultdict(int)
        for i in issues:
            types[i["type"]] += 1
        bad_chunks = {i["id"] for i in issues}
        return {"total": len(chunks), "issues": dict(types),
                "clean_ratio": round(1 - len(bad_chunks) / max(1, len(chunks)), 2)}


if __name__ == "__main__":
    base = "退款政策 说明 用户在订单页提交申请后 系统审核" + "细节" * 40
    chunks = [
        {"id": "c1", "text": base, "has_heading": True},                       # 过长
        {"id": "c2", "text": "太短", "has_heading": False},                    # 过短+无标题
        {"id": "c3", "text": "正常长度的块 讲发票开具流程与开具注意事项", "has_heading": True},
        {"id": "c4", "text": base.replace("系统审核", "系统复核"), "has_heading": True},  # 近重复
        {"id": "c5", "text": "无标题但长度正常的块 内容讲账户注销流程", "has_heading": False},
    ]
    probe = ChunkProbe()
    issues = probe.probe(chunks)
    kinds = sorted((i["id"], i["type"]) for i in issues)
    assert ("c1", "too_long") in kinds
    assert ("c2", "too_short") in kinds and ("c2", "no_heading") in kinds
    dup = [i for i in issues if i["type"] == "near_duplicate"][0]
    assert set(dup["duplicates"]) <= {"c1", "c4"} and dup["id"] in ("c1", "c4")
    assert ("c5", "no_heading") in kinds

    h = probe.health(chunks)
    assert h["total"] == 5 and h["issues"]["near_duplicate"] == 1
    assert h["clean_ratio"] == 0.2, "五块里只有 c3 完全干净"
    advice = {i["type"]: i["advice"] for i in issues}
    assert "合并" in advice["too_short"] and "切分" in advice["too_long"]
    print("切块探针通过:4 类异常全部检出 干净块占比 0.2 每类附修复建议")

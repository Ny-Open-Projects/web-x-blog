"""检索质量抽检自动化:按类目分层抽样 跑命中检查 输出可复现的周期报告。"""
import random


def stratified_sample(pool, per_class, rng):
    """每类抽 per_class 条,类内乱序取前 N,保证跨类覆盖。"""
    by_class = {}
    for item in pool:
        by_class.setdefault(item["class"], []).append(item)
    sample = []
    for cls in sorted(by_class):
        items = by_class[cls][:]
        rng.shuffle(items)
        sample.extend(items[:per_class])
    return sample


def run_audit(sample, retriever, k=2):
    checked = [{"q": s["q"], "class": s["class"],
                "hit": s["expect"] in retriever(s["q"], k)} for s in sample]
    passed = sum(1 for c in checked if c["hit"])
    by_class = {}
    for c in checked:
        stat = by_class.setdefault(c["class"], {"checked": 0, "passed": 0})
        stat["checked"] += 1
        stat["passed"] += int(c["hit"])
    return {"checked": len(checked), "passed": passed,
            "rate": passed / float(len(checked)) if checked else 1.0,
            "fails": [c["q"] for c in checked if not c["hit"]],
            "by_class": by_class}


if __name__ == "__main__":
    pool = []
    for i in range(10):
        pool.append({"q": "退货问题%d" % i, "class": "售后", "expect": "退货文档"})
    for i in range(10):
        pool.append({"q": "发票问题%d" % i, "class": "财务", "expect": "发票文档"})
    for i in range(10):
        pool.append({"q": "物流问题%d" % i, "class": "配送", "expect": "物流文档"})


    def retriever(q, k):
        """桩:售后类命中,发票偶发不中,物流总不中,制造可控的劣化分布。"""
        if "退货" in q:
            return ["退货文档", "其他"]
        if "发票" in q:
            return ["发票文档", "其他"] if q.endswith("0") or q.endswith("2") else ["旧版发票页"]
        return ["配送异常页"]


    rng = random.Random(42)
    sample = stratified_sample(pool, per_class=4, rng=rng)
    classes = sorted(set(s["class"] for s in sample))
    assert classes == ["售后", "财务", "配送"], "三类都必须被抽到"
    assert len(sample) == 12, "每类 4 条共 12 条"

    report = run_audit(sample, retriever)
    assert report["checked"] == 12
    assert report["by_class"]["售后"] == {"checked": 4, "passed": 4}
    assert report["by_class"]["配送"]["passed"] == 0
    assert report["rate"] < 0.7 and len(report["fails"]) > 0

    rng2 = random.Random(42)
    sample2 = stratified_sample(pool, per_class=4, rng=rng2)
    report2 = run_audit(sample2, retriever)
    assert report2 == report, "同种子抽样与评分必须可复现"
    print("抽检自动化通过:分层 12 条覆盖三类,售后满分 配送全挂,报告可复现")

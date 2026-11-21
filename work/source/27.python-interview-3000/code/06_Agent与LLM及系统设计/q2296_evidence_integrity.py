"""证据完整性校验:引用必须在库 内容哈希必须一致,检测证据被改 被删 链路断开。"""
import hashlib, re


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


class EvidenceStore:
    def __init__(self):
        self.blocks = {}

    def add(self, bid, text, source):
        self.blocks[bid] = {"text": text, "hash": digest(text), "source": source}

    def verify_citations(self, cited_ids):
        report = {"ok": [], "missing": [], "tampered": []}
        for cid in cited_ids:
            blk = self.blocks.get(cid)
            if blk is None:
                report["missing"].append(cid)
            elif digest(blk["text"]) != blk["hash"]:
                report["tampered"].append(cid)
            else:
                report["ok"].append(cid)
        report["pass"] = not report["missing"] and not report["tampered"]
        return report


def check_answer_refs(answer, id_map):
    used = set(int(m) for m in re.findall(r"\[(\d+)\]", answer))
    return sorted(n for n in used if n not in id_map)


if __name__ == "__main__":
    store = EvidenceStore()
    store.add("b1", "退货窗口 30 天", "policy.pdf#p1")
    store.add("b2", "退款 3 个工作日到账", "faq.html#q5")
    rep = store.verify_citations(["b1", "b2"])
    assert rep["pass"] and set(rep["ok"]) == {"b1", "b2"}
    store.blocks["b2"]["text"] = "退款 30 天到账"
    rep = store.verify_citations(["b1", "b2"])
    assert not rep["pass"] and rep["tampered"] == ["b2"], "内容被改哈希对不上"
    rep = store.verify_citations(["b1", "b9"])
    assert rep["missing"] == ["b9"], "引用了不存在的块"
    assert check_answer_refs("见[1]与[3]。", {1: "b1"}) == [3], "答案引用编号断链"
    print("证据完整性通过:存在性 内容哈希 篡改检测 断链编号")

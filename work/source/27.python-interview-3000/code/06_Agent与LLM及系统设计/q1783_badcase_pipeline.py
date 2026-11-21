"""坏例回流流水线:采集去重 规则预标 人工审核 入库评估集,触发回归门禁。"""
import hashlib


def fingerprint(q, a):
    return hashlib.md5((q + "||" + a).encode("utf-8")).hexdigest()[:10]


RULES = [("错误答案", ["不对"]), ("内容缺失", ["略"]), ("幻觉引用", ["据不存在的资料"])]


def auto_tag(q, a):
    for tag, kws in RULES:
        if any(k in a for k in kws):
            return tag
    return "待定"


class BadcasePipeline:
    def __init__(self):
        self.seen = set()
        self.review_queue = []
        self.eval_set = []
        self.stats = {"collected": 0, "dup_dropped": 0, "approved": 0, "rejected": 0}

    def collect(self, q, a):
        self.stats["collected"] += 1
        fp = fingerprint(q, a)
        if fp in self.seen:
            self.stats["dup_dropped"] += 1
            return None                          # 指纹去重
        self.seen.add(fp)
        item = {"q": q, "a": a, "fp": fp, "tag": auto_tag(q, a), "status": "pending"}
        self.review_queue.append(item)
        return item

    def review(self, fp, approve):
        item = next((i for i in self.review_queue
                     if i["fp"] == fp and i["status"] == "pending"), None)
        if item is None:
            raise KeyError("无可审核样本: " + fp)
        item["status"] = "approved" if approve else "rejected"
        if approve:
            self.stats["approved"] += 1
            self.eval_set.append(item)           # 入库即进回归集
        else:
            self.stats["rejected"] += 1
        return item


if __name__ == "__main__":
    pipe = BadcasePipeline()
    a = pipe.collect("Q 怎么退款", "这个答案不对")
    b = pipe.collect("Q 发票怎么开", "细节略")
    c = pipe.collect("Q 保修多久", "答案引用了据不存在的资料")
    assert a["tag"] == "错误答案" and b["tag"] == "内容缺失" and c["tag"] == "幻觉引用"

    pipe.collect("Q 怎么退款", "这个答案不对")     # 完全相同样本:指纹去重
    assert pipe.stats["dup_dropped"] == 1 and len(pipe.review_queue) == 3

    pipe.review(a["fp"], True)
    pipe.review(b["fp"], False)
    pipe.review(c["fp"], True)
    assert pipe.stats["approved"] == 2 and pipe.stats["rejected"] == 1
    assert [i["q"] for i in pipe.eval_set] == ["Q 怎么退款", "Q 保修多久"]

    re_review = False
    try:
        pipe.review(a["fp"], True)               # 已审样本不能再审
    except KeyError:
        re_review = True
    assert re_review and len(pipe.eval_set) == 2, "审核幂等,入库即触发回归扩充"
    print("坏例回流通过:指纹去重 规则预标 审核分流,通过者进入回归评估集")

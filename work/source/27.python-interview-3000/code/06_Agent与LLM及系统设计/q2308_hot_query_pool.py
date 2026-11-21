"""查询热词池:归一化聚类高频查询,超过阈值进热池,预热缓存与推荐词双输出。"""
import re
from collections import Counter


def norm_query(q):
    return re.sub(r"\s+", "", q.strip().lower())


def cluster_queries(logs, threshold=3):
    counts = Counter(norm_query(q) for q in logs)
    hot = {q: c for q, c in counts.items() if c >= threshold}
    return counts, hot


def build_pool(hot, top_n=5):
    ranked = sorted(hot.items(), key=lambda kv: (-kv[1], kv[0]))[:top_n]
    return {"prefetch": [q for q, _ in ranked],
            "suggest": sorted(q for q, _ in ranked)}


if __name__ == "__main__":
    logs = ["退货 政策", "退货政策", "退货政策", "退款进度", "退款 进度", "发票开具"]
    counts, hot = cluster_queries(logs, threshold=2)
    assert counts["退货政策"] == 3, "空白变体聚到同一键"
    assert set(hot) == {"退货政策", "退款进度"}
    assert "发票开具" not in hot, "低频查询不入热池"
    pool = build_pool(hot)
    assert pool["prefetch"][0] == "退货政策", "按频次排预计算池"
    assert pool["suggest"] == sorted(pool["prefetch"])
    print("热词池通过:归一聚类 阈值筛选 预热与建议双输出")

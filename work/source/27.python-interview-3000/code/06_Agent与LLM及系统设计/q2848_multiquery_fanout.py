"""Q2848 多查询并发扇出:有界并发 部分失败与 RRF 融合。

查询改写成多个变体后逐个串行检索太慢,全并发又怕打爆下游。用有界
并发扇出,单个变体失败只记账不连坐,成功的变体用倒数排名融合出
最终排序——三个查询挂一个,照样出结果。
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

FAKE_INDEX = {
    "退款流程是什么": ["d2", "d1", "d8"],
    "退款怎么申请": ["d1", "d2", "d3"],
    "坏了的查询": None,  # 检索时抛异常
}


def retriever(q):
    ranks = FAKE_INDEX.get(q)
    if ranks is None:
        raise RuntimeError("检索服务超时")
    return ranks


def fanout(queries, max_workers=2):
    ok, failed = [], []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(retriever, q): q for q in queries}
        for fut in as_completed(futs):
            q = futs[fut]
            try:
                ok.append((q, fut.result()))
            except Exception as exc:
                failed.append((q, type(exc).__name__))
    ok.sort(key=lambda x: x[0])  # 固定顺序保证融合确定性
    return [ranks for _, ranks in ok], failed


def rrf_fuse(rank_lists, k=60):
    scores = {}
    for ranks in rank_lists:
        for r, doc in enumerate(ranks):
            scores[doc] = scores.get(doc, 0.0) + 1.0 / (k + r + 1)
    return sorted(scores, key=lambda d: (-scores[d], d))


def main():
    queries = ["退款流程是什么", "退款怎么申请", "坏了的查询"]
    rank_lists, failed = fanout(queries)
    assert len(rank_lists) == 2, rank_lists      # 挂掉的不连坐
    assert failed == [("坏了的查询", "RuntimeError")], failed
    fused = rrf_fuse(rank_lists)
    assert fused[0] == "d1", fused  # d1 在两路都靠前,融合后第一
    assert "d2" in fused[:2], fused
    assert "d3" in fused, fused
    print("成功变体:", len(rank_lists), "失败:", failed)
    print("RRF 融合排序:", fused)
    print("两路共现的 d1 排第一,单路独有 d3 也有位置")


if __name__ == "__main__":
    main()

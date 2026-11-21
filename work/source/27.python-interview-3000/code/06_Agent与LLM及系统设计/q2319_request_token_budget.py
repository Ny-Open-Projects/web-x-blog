"""请求级 token 预算:先给输出留 max_tokens,再按 历史最旧 检索最低分 顺序裁剪,system 与问题不动。"""
def est(text):
    return max(1, len(text) // 2)


def fit_request(system, question, history, retrieval, max_output=256, window=1024):
    budget = window - max_output

    def total(hs, rs):
        return est(system) + est(question) + sum(est(h[1] if isinstance(h, tuple) else h) for h in hs) + sum(est(r["text"]) for r in rs)

    keep_hist, keep_ret = list(history), list(retrieval)
    dropped = {"history": 0, "retrieval": 0}
    while total(keep_hist, keep_ret) > budget:
        if keep_hist:
            keep_hist.pop(0)
            dropped["history"] += 1
        elif keep_ret:
            worst = min(range(len(keep_ret)), key=lambda i: keep_ret[i]["score"])
            keep_ret.pop(worst)
            dropped["retrieval"] += 1
        else:
            break
    return {"history": keep_hist, "retrieval": keep_ret, "dropped": dropped,
            "fits": total(keep_hist, keep_ret) <= budget,
            "used": total(keep_hist, keep_ret), "budget": budget}


if __name__ == "__main__":
    history = [("user", "第一问" + "字" * 200), ("assistant", "答" * 200),
               ("user", "第二问" + "字" * 200), ("assistant", "答" * 200)]
    retrieval = [{"text": "高分文档" + "案" * 196, "score": 0.9},
                 {"text": "低分文档" + "案" * 196, "score": 0.2}]
    r = fit_request("你是客服", "退货怎么办", history, retrieval, max_output=256, window=600)
    assert r["fits"], "裁剪后必须装进窗口"
    assert r["dropped"]["history"] > 0 and r["dropped"]["retrieval"] == 0, "先裁最旧历史"
    assert r["history"] == history[3:], "保留的是较新历史"
    r2 = fit_request("你是客服", "退货怎么办", [], retrieval, max_output=900, window=1024)
    assert r2["dropped"]["history"] == 0 and r2["dropped"]["retrieval"] >= 1, "没历史可裁就裁低分检索"
    assert r2["retrieval"][0]["score"] == 0.9, "高分文档幸存"
    r3 = fit_request("系统" + "超" * 2500, "问", [], [], max_output=0, window=1024)
    assert not r3["fits"], "system 加问题本身超窗 只能显式失败"
    print("请求级预算通过:输出预留 先裁旧史 再裁低分 不足则上抛")

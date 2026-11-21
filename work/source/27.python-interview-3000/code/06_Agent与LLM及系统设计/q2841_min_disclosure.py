"""Q2841 跨 Agent 委派的最小披露:字段投影与披露台账。

把任务委派给子 Agent 时,把整个上下文原样塞过去是最省事也最危险的:
成本 内部备注 客户隐私全跟着走。正确做法是按受派角色声明字段白名单,
投影出最小必要集合,给了什么 扣了什么全部进披露台账,审计可以复盘。
"""

DISCLOSURE_ALLOW = {
    "brief": ["query", "deadline"],
    "deep": ["query", "corpus_hint", "deadline"],
}


def delegate(to_agent, payload, ledger, run_id):
    """按白名单投影披露内容,并写台账。"""
    allow = DISCLOSURE_ALLOW[to_agent]
    out = {k: payload[k] for k in allow if k in payload}
    withheld = sorted(set(payload) - set(allow))
    ledger.append({
        "run": run_id,
        "to": to_agent,
        "given": sorted(out),
        "withheld": withheld,
    })
    return out


def main():
    payload = {
        "query": "对比两家供应商报价",
        "deadline": "2026-11-07",
        "corpus_hint": "procure_2026",
        "internal_cost": 87.5,          # 内部成本,不该出门
        "customer_phone": "13800001111",  # 隐私,不该出门
    }
    ledger = []
    brief = delegate("brief", payload, ledger, "run_1")
    deep = delegate("deep", payload, ledger, "run_1")
    assert sorted(brief) == ["deadline", "query"], brief
    assert sorted(deep) == ["corpus_hint", "deadline", "query"], deep
    assert "customer_phone" not in brief and "customer_phone" not in deep
    assert ledger[0]["withheld"] == ["corpus_hint", "customer_phone",
                                     "internal_cost"], ledger
    assert ledger[1]["withheld"] == ["customer_phone", "internal_cost"], ledger
    assert ledger[1]["given"] == ["corpus_hint", "deadline", "query"], ledger
    print("brief 子代理拿到:", sorted(brief))
    print("deep 子代理拿到:", sorted(deep))
    print("披露台账:", ledger[0])


if __name__ == "__main__":
    main()

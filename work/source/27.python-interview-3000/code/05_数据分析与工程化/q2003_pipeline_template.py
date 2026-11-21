"""管道参数化:一份模板渲染多渠道任务,必填校验与默认值合并"""

TEMPLATE = {
    "task": "agg_channel_{channel}",
    "sql": ("SELECT channel, SUM(amount) FROM dwd_orders "
            "WHERE dt = '{dt}' AND channel = '{channel}' GROUP BY channel"),
    "partition": "{dt}",
}
REQUIRED = ["channel", "dt", "owner"]
DEFAULTS = {"retries": 2, "priority": "normal"}


def render(template, params):
    missing = [k for k in REQUIRED if not params.get(k)]
    if missing:
        raise ValueError(f"缺少必填参数: {missing},拒绝渲染")
    merged = dict(DEFAULTS)
    merged.update(params)
    out = {}
    for k, v in template.items():
        s = str(v)
        for pk, pv in merged.items():
            s = s.replace("{" + pk + "}", str(pv))
        out[k] = s
    for k, v in merged.items():
        out.setdefault(k, v)
    return out


if __name__ == "__main__":
    for ch in ("search", "feed", "crm"):
        cfg = render(TEMPLATE, {"channel": ch, "dt": "2026-11-04",
                                "owner": "ops@" + ch})
        print(f"{cfg['task']} | {cfg['sql'][:58]}... | retries={cfg['retries']}")
    try:
        render(TEMPLATE, {"channel": "search", "dt": "2026-11-04"})
    except ValueError as e:
        print("故意缺参:", e)
    print("要点:N 个渠道共用一份模板,改动只发生在一处;必填缺失要一次性列全并显式报错,不许渲染出空字符串任务;渲染产物要能 dump 留档")

"""调度依赖拓扑排序:按就绪条件分层输出,成环立即报错并列出环上任务"""

DEPS = {
    "ods_sync": [],
    "dwd_clean": ["ods_sync"],
    "dwd_pay": ["ods_sync"],
    "dws_user": ["dwd_clean", "dwd_pay"],
    "ads_board": ["dws_user"],
    "report_mail": ["ads_board"],
}


def topo_levels(deps):
    """每一轮挑出'依赖已全部完成'的任务作为一批,批内可并行"""
    remaining = {t: set(ds) for t, ds in deps.items()}
    done = set()
    out = []
    while remaining:
        ready = sorted(t for t, ds in remaining.items() if ds <= done)
        if not ready:
            raise ValueError(f"依赖成环,无法调度: {sorted(remaining)}")
        out.append(ready)
        done.update(ready)
        for t in ready:
            remaining.pop(t)
    return out


if __name__ == "__main__":
    for i, level in enumerate(topo_levels(DEPS)):
        print(f"第 {i + 1} 批(可并行): {level}")
    try:
        topo_levels(dict(DEPS, ads_board=["ads_board"]))
    except ValueError as e:
        print("故意注入自环:", e)
    print("要点:分层=并行波次,批内无依赖可同时跑;成环要 fail fast 并打印环上任务,别让调度器空转")

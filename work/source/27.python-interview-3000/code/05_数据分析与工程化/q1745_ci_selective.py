"""CI 选择性重跑:按变更文件沿依赖图圈定受影响任务,只跑受影响的"""

GRAPH = {
    # 变更文件 -> 种子任务;任务 -> 下游任务,共用一张图
    "transform_dwd.py": ["dwd_clean", "dwd_pay"],
    "model_dws.py": ["dws_user"],
    "board_sql/": ["ads_board"],
    "dwd_clean": ["dws_user"],
    "dwd_pay": ["dws_user"],
    "dws_user": ["ads_board"],
}
ALL_TASKS = ["ods_sync", "dwd_clean", "dwd_pay", "dws_user", "ads_board", "report_mail"]


def affected(changed_files, graph, tasks):
    seeds = set()
    for f in changed_files:
        hit = graph.get(f)
        if hit is None:  # 目录前缀匹配
            for prefix, ds in graph.items():
                if prefix.endswith("/") and f.startswith(prefix):
                    seeds.update(x for x in ds if x in tasks)
                    break
        else:
            seeds.update(x for x in hit if x in tasks)
    selected, frontier = set(), set(seeds)
    while frontier:
        t = frontier.pop()
        if t in selected:
            continue
        selected.add(t)
        frontier.update(x for x in graph.get(t, []) if x in tasks)  # 沿任务->下游扩散
    return sorted(selected, key=tasks.index)


if __name__ == "__main__":
    for changed in (["transform_dwd.py"], ["model_dws.py"], ["board_sql/vip.sql"], ["docs/readme.md"]):
        runs = affected(changed, GRAPH, ALL_TASKS)
        print(f"变更 {changed} -> 重跑 {runs if runs else '无,跳过数据任务'}")
    print("要点:受影响圈定=变更文件映射种子任务,再沿血缘扩散;映射表与血缘同源生成防漂移,纯文档变更直接跳过省一半 CI 时间")

"""编排者-工人:结果驱动的动态派发,任务队列 + 预算上限。"""


class FakePlanner:
    def next_tasks(self, results):
        done = {r["task"]: r for r in results}
        if "collect" not in done:
            return [{"id": "collect", "type": "search"}]
        if "collect" in done and "review" not in done:
            return [{"id": "review", "type": "judge", "needs": "collect"}]
        if done.get("review", {}).get("verdict") == "data_missing" and "refetch" not in done:
            return [{"id": "refetch", "type": "search"}]
        return []


class Worker:
    def execute(self, task, results):
        if task["type"] == "search":
            if task["id"] == "refetch":
                return {"task": task["id"], "data": "补齐数据"}
            return {"task": task["id"], "data": "3 条结果(缺第 3 节)"}
        if task["type"] == "judge":
            src = next(r for r in results if r["task"] == "collect")
            if "缺" in src["data"]:
                return {"task": "review", "verdict": "data_missing"}
            return {"task": "review", "verdict": "pass"}
        raise ValueError(task["type"])


def orchestrate(max_tasks=10):
    planner, worker, queue, results = FakePlanner(), Worker(), [], []
    spawned = 0
    while spawned < max_tasks:
        tasks = planner.next_tasks(results)
        if not tasks:
            break
        for t in tasks:
            if t["id"] not in {r["task"] for r in results}:
                queue.append(t)
        if not queue:
            break
        t = queue.pop(0)
        results.append(worker.execute(t, results))
        spawned += 1
    return results, spawned


if __name__ == "__main__":
    results, n = orchestrate()
    for r in results:
        print(" ", r)
    assert n == 3, "collect -> review -> refetch 动态追加"
    ids = [r["task"] for r in results]
    assert ids.index("refetch") > ids.index("review"), "补数任务由审查结果动态触发"
    print("动态派发闭环:审查发现缺数据 -> 自动追加补数任务")

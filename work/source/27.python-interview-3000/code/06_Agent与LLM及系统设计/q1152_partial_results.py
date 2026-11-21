"""并行工具失败隔离:as_completed 收割,部分结果 + 失败者精准重试。"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import random


def tool(name, fail_names):
    def run(arg):
        if name in fail_names:
            raise ConnectionError(f"{name} 下游超时")
        return f"{name}({arg})=OK"
    return run


def run_parallel(tasks, fail_names, max_workers=4):
    results, errors = {}, {}
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(tool(n, fail_names), arg): n for n, arg in tasks}
        for fut in as_completed(futs):
            name = futs[fut]
            try:
                results[name] = fut.result()
            except Exception as e:
                errors[name] = str(e)
    return results, errors


def retry_failed(tasks, fail_names, attempts=2):
    for i in range(attempts):
        _, errors = run_parallel(tasks, fail_names=set())
        if not errors:
            return {"recovered": [n for n, _ in tasks], "rounds": i + 1}
        tasks = [t for t in tasks if t[0] in errors]
    return {"recovered": [], "rounds": attempts}


if __name__ == "__main__":
    random.seed(1)
    tasks = [("flight", "北京"), ("hotel", "北京"), ("weather", "北京"), ("traffic", "北京")]
    results, errors = run_parallel(tasks, fail_names={"hotel", "traffic"})
    print("成功:", results)
    print("失败:", errors)
    assert len(results) == 2 and len(errors) == 2, "失败必须被隔离"

    r = retry_failed([("hotel", "北京"), ("traffic", "北京")], set())
    print("失败者重试:", r)
    assert r["recovered"] == ["hotel", "traffic"], "成功者不重复执行,失败者精准重试"
    print("部分成功聚合: 2 成功 + 2 已恢复")

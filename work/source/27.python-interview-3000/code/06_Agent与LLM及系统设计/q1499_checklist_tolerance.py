"""任务清单容忍度:fail_fast 尽力而为 仲裁人三种策略,产出部分结果与失败清单。"""


class ChecklistRunner:
    """按策略执行清单:策略决定第一个失败后是否继续,以及何时整体判失败。"""

    POLICIES = ("fail_fast", "best_effort", "quorum")

    def __init__(self, policy, quorum_ratio=0.6):
        assert policy in self.POLICIES
        self.policy = policy
        self.quorum_ratio = quorum_ratio

    def run(self, tasks, executor):
        """tasks 有序子任务;executor(name) 成功返回值 失败抛异常。"""
        results, failures = {}, []
        for name in tasks:
            try:
                results[name] = executor(name)
            except Exception as exc:
                failures.append((name, str(exc)))
                if self.policy == "fail_fast":
                    break
        outcome = self._judge(results, failures, tasks)
        return {"results": results, "failures": failures, "outcome": outcome}

    def _judge(self, results, failures, tasks):
        if self.policy == "fail_fast":
            return "aborted" if failures else "completed"
        if self.policy == "best_effort":
            return "partial" if failures else "completed"
        ok = len(results) / len(tasks)
        return "quorum_met" if ok >= self.quorum_ratio else "quorum_failed"


if __name__ == "__main__":
    def make_exec(bad):
        def ex(name):
            if name in bad:
                raise ValueError(name + " 失败")
            return name + "-ok"
        return ex

    tasks = ["fetch", "parse", "render", "notify"]

    ff = ChecklistRunner("fail_fast").run(tasks, make_exec({"parse"}))
    assert ff["outcome"] == "aborted" and set(ff["results"]) == {"fetch"}
    assert len(ff["failures"]) == 1, "fail_fast 第一个失败立即停"

    be = ChecklistRunner("best_effort").run(tasks, make_exec({"parse"}))
    assert be["outcome"] == "partial" and set(be["results"]) == {"fetch", "render", "notify"}
    assert be["failures"] == [("parse", "parse 失败")]

    good_run = ChecklistRunner("best_effort").run(tasks, make_exec(set()))
    assert good_run["outcome"] == "completed"

    q_ok = ChecklistRunner("quorum", quorum_ratio=0.6).run(tasks, make_exec({"notify"}))
    assert q_ok["outcome"] == "quorum_met" and len(q_ok["results"]) == 3
    q_bad = ChecklistRunner("quorum", quorum_ratio=0.6).run(tasks, make_exec({"fetch", "parse", "render"}))
    assert q_bad["outcome"] == "quorum_failed" and len(q_bad["results"]) == 1
    print("容忍度通过:fail_fast 立停 best_effort 出部分结果 quorum 按比例仲裁")

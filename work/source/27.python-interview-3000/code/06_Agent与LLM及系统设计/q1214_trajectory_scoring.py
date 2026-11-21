"""Agent 轨迹评分:结果/效率/过程三维打分,分项保留,加权可调。"""


def score_trajectory(traj, task):
    result_ok = traj["final_answer"] == task["expected"]
    # 效率:步数与 token 相对预算
    step_ratio = traj["steps"] / task["optimal_steps"]
    eff_score = max(0.0, 1.0 - (step_ratio - 1) * 0.5)
    # 过程:工具失败与循环
    calls = traj["tool_calls"]
    fail_rate = calls.count("error") / len(calls) if calls else 0
    loop = any(calls[i:i + 2] == calls[i + 2:i + 4] == [calls[i], calls[i + 1]]
               for i in range(len(calls) - 3))
    proc_score = (1 - fail_rate) * (0.5 if loop else 1.0)
    total = 0.5 * result_ok + 0.25 * eff_score + 0.25 * proc_score
    return {"result": result_ok, "efficiency": round(eff_score, 2),
            "process": round(proc_score, 2), "total": round(total, 2), "loop": loop}


if __name__ == "__main__":
    task = {"expected": "已退款 100 元", "optimal_steps": 3}
    good = {"final_answer": "已退款 100 元", "steps": 3, "tool_calls": ["query", "refund", "notify"]}
    sloppy = {"final_answer": "已退款 100 元", "steps": 8,
              "tool_calls": ["query", "error", "query", "error", "query", "error", "refund", "notify"]}
    wrong = {"final_answer": "已退款 200 元", "steps": 3, "tool_calls": ["query", "refund", "notify"]}
    for name, traj in [("标准轨迹", good), ("绕路轨迹", sloppy), ("错误答案", wrong)]:
        s = score_trajectory(traj, task)
        print(f"{name}: {s}")
    s_good, s_sloppy, s_wrong = (score_trajectory(t, task) for t in (good, sloppy, wrong))
    assert s_good["total"] == 1.0
    assert s_sloppy["result"] and s_sloppy["efficiency"] < 1.0, "答对但低效要扣效率分"
    assert s_sloppy["process"] < 1.0 and s_sloppy["loop"], "连续失败触发循环检测"
    assert s_wrong["result"] is False and s_wrong["total"] < 0.6, "结果错是硬伤"
    print("三维分项保留:绕路与错误答案被清晰区分")

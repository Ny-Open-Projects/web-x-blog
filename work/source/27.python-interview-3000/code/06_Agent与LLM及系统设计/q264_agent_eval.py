"""Agent 评估:工具轨迹正确率 + LLM-as-Judge 打分(stub 评委),输出回归报告。"""

GOLD = {  # 任务 -> (期望工具序列, 参考答案要点)
    "查北京天气": (["get_weather"], "北京 晴"),
    "对比两地天气": (["get_weather", "get_weather", "compare"], "北京晴 上海雨"),
}


def judge(answer: str, reference: str) -> int:
    """stub 评委:按参考答案要点覆盖率打 1-5 分(真实实现用强模型 + rubric)。"""
    points = reference.split()
    hits = sum(1 for p in points if p in answer)
    return min(5, 1 + int(hits / len(points) * 4))


def evaluate(cases: dict, traces: dict) -> float:
    passed, total = 0, 0
    for task, (gold_tools, reference) in cases.items():
        tools, answer = traces[task]
        extra = max(0, len(tools) - len(gold_tools))           # 冗余调用
        aligned = sum(1 for t, g in zip(tools, gold_tools) if t == g)
        tool_acc = aligned / len(gold_tools)
        score = judge(answer, reference)
        ok = tool_acc == 1.0 and extra == 0 and score >= 4
        passed += ok
        total += 1
        print(f"  {task}: 工具正确率={tool_acc:.0%} 冗余={extra} "
              f"评委分={score} {'PASS' if ok else 'FAIL'}")
    rate = passed / total
    print(f"回归通过率 {passed}/{total}")
    return rate


if __name__ == "__main__":
    traces = {
        "查北京天气": (["get_weather"], "北京 晴 12 度"),
        # 轨迹有冗余(calc 不在计划中),结果要点齐全:结果层满分、轨迹层扣分
        "对比两地天气": (["get_weather", "calc", "compare"], "北京晴 上海雨"),
    }
    evaluate(GOLD, traces)

"""三种编排思想的最小实现对比:图编排 / 角色对话 / 自主循环。"""


class FakeLLM:
    def plan(self, goal):
        return ["收集资料", "整理要点", "输出报告"] if goal else []


def graph_orchestration(llm, goal):
    """图编排:节点与边写死在状态图里。"""
    graph = {"start": "research", "research": "outline", "outline": "write", "write": "end"}
    node, trace = "start", []
    while node != "end":
        if node == "research":
            trace.append("research: " + llm.plan(goal)[0])
        elif node == "outline":
            trace.append("outline: 固定大纲")
        elif node == "write":
            trace.append("write: 成稿")
        node = graph[node]
    return trace


def role_chat(llm, goal):
    """角色对话:按发言规则轮流,共享一份对话记录。"""
    roles = ["planner", "critic", "writer"]
    transcript, round_no = [], 0
    for role in roles:
        round_no += 1
        prev = transcript[-1] if transcript else goal
        transcript.append(f"{role} 回应: {prev}")
    return transcript


def autonomous_loop(llm, goal, max_steps=5):
    """自主循环:LLM 决定下一步,直到任务完成或步数用尽。"""
    done, steps = False, []
    plan = llm.plan(goal)
    for i, task in enumerate(plan):
        if i >= max_steps:
            break
        steps.append(f"step{i}: {task}")
        done = task == "输出报告"
        if done:
            break
    return steps, done


if __name__ == "__main__":
    llm = FakeLLM()
    t1 = graph_orchestration(llm, "写周报")
    print("图编排:", t1)
    assert len(t1) == 3 and t1[0].startswith("research")
    t2 = role_chat(llm, "写周报")
    print("角色对话:", t2)
    assert t2[0].startswith("planner")
    t3, ok = autonomous_loop(llm, "写周报")
    print("自主循环:", t3, "完成:", ok)
    assert ok, "规划的任务应能在循环内完成"
    print("三种编排均收敛,可控性: 图 > 对话 > 循环")

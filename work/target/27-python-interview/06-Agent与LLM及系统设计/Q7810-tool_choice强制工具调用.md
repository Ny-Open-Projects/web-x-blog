---
title: "[Q7810] tool_choice 强制工具调用：auto、required 与循环边界"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7810 · tool_choice 强制工具调用：auto、required 与循环边界

难度：P6 ｜ 标签：tool_choice、auto、required、强制工具、结构化抽取、循环边界、轮数预算

基线：库外知识卡，代码用标准库模拟 tool_choice 三种取值的行为与 Agent 循环收敛，不调用外部 API。

**问**：Agent 里模型有时该调工具却直接编了个答案，有时不需要工具又非要调一次搜索浪费两秒。加 `tool_choice="required"` 后空转问题没了，但另一个任务明明已完成，模型还在硬调工具直到烧满轮数。tool_choice 的 auto/required/指定函数各自什么行为？怎么组合才能"该调必调、完成即停"？

**答**：

- **结论**：`tool_choice` 控制模型与工具的"合同强度"。① **auto**（默认）：模型自主判断——没有工具意图就直接回答（省一次工具往返），有意图才调用；风险是意图判断不可靠，该调没调。② **required**：模型必须调一个工具（挑哪个它自己定）——保证"每轮都有行动"，适合任务必须走流程的场景（先查工单才能回复）；风险是任务其实已完成时被迫硬调，空转到轮数上限。③ **指定函数**（如 `tool_choice={"type":"function","name":"get_weather"}`）：锁死只能调这个函数——结构化抽取的标准姿势（把"从文本抽字段"建模成一次函数调用，输出 schema 就是函数参数 schema），别的工具再相关也进不去。三者的组合纪律：**required 用于"必须行动"的中间轮，auto 用于可收敛的对话轮，指定函数用于抽取/路由类单次调用；任何强制模式都必须配 max_rounds/预算兜底**，否则就是烧钱定时炸弹。
- **取舍**：required 与 auto 的选择不是"哪个更稳"，而是**任务有没有明确的完成信号**。有信号（工具返回结构化结果、模型能说 done）→ auto + 终止检测；没信号、流程驱动（工单必须流转到下一步）→ required + 步数预算。指定函数模式要警惕"参数编造"：模型被锁死在唯一工具上，没有工具可用时它会编造参数硬调（实测里把用户闲聊也塞进 city 参数），所以指定函数只适合输入明确可抽取的场景，并配参数校验+失败重试。另一个细节：auto 的意图判断模型每次可能不一致，同一输入忽调忽不调——对一致性敏感的场景（评测、回放测试）要么锁 tool_choice，要么在评测里把"是否调用"也当指标。
- **实战**：客服 Agent 用 auto 时 8% 的轮次该查工单没查（模型直接猜），改成 required 后正确率上来，但出现新问题：工单查完、模型该出最终答复时还在硬调工具，平均轮数从 3.2 涨到 5.6，成本涨 70%。修复：分阶段策略——首轮 required（保证必查工单），工具结果返回后切 auto 并在系统提示里注入"资料已齐备可作答"；终止条件改为"auto 轮给出 answer 即收"，同时保留 max_rounds=8 兜底。上线后正确率保持、轮数降回 3.5。教训：tool_choice 不是全局开关，是**每轮可调度的策略旋钮**，与终止条件一起设计。

下面模拟三种 tool_choice 的行为与 Agent 循环收敛。

```python
# Q7810 tool_choice 强制工具调用: auto/required/指定函数 的行为与循环边界
TOOLS = {
    "get_weather": lambda city: f"{city}: 晴 18°C",
    "search": lambda q: f"关于 {q} 的搜索结果",
}

def llm_decide(messages, tool_choice):
    """模拟模型决策: 返回 (action, args)
    auto: 看最后一条用户消息里有没有触发意图
    required: 必须调一个工具
    指定函数: 只能调那个函数"""
    last = messages[-1]["content"]
    if tool_choice == "auto" and "天气" not in last and "搜" not in last:
        return ("answer", last)               # 不需要工具 → 直接回答
    if tool_choice == "auto":
        return ("get_weather", {"city": "北京"}) if "天气" in last else ("search", {"q": last})
    if tool_choice == "get_weather":
        return ("get_weather", {"city": "北京"})   # 被锁死在这个工具
    if tool_choice == "required":
        return ("search", {"q": last})        # 必须调, 挑最相关的
    return ("answer", last)

# [1] auto: 无工具意图时不调用, 有意图时调用
msgs = [{"role": "user", "content": "你好"}]
act = llm_decide(msgs, "auto")
print(f"[1] auto 无意图: {act} (省一次工具往返)")
assert act[0] == "answer"
msgs = [{"role": "user", "content": "北京天气如何"}]
print(f"[1b] auto 有意图: {llm_decide(msgs, 'auto')}")
assert llm_decide(msgs, "auto")[0] == "get_weather"

# [2] required/指定函数: 无意图也强制调 — 用对了是保证, 用错了是浪费
act = llm_decide([{"role": "user", "content": "你好"}], "required")
print(f"[2] required: {act} (无意图也调了 search)")
assert act[0] == "search"
act = llm_decide(msgs, "get_weather")
print(f"[2b] 指定 get_weather: {act} (别的工具再相关也进不去)")
assert act[0] == "get_weather"

# [3] 循环边界: required 用于「每轮必须行动」的 Agent, 但终止条件要自己兜
def run_agent(task, tool_choice, max_rounds=3):
    msgs = [{"role": "user", "content": task}]
    for r in range(1, max_rounds + 1):
        act, args = llm_decide(msgs, tool_choice)
        if act == "answer":
            return f"final: {args}", r
        result = TOOLS[act](**args)
        msgs.append({"role": "assistant", "content": f"call {act}"})
        msgs.append({"role": "tool", "content": result})
    return "hit max_rounds", max_rounds

end, rounds = run_agent("查一下上海", "auto")
print(f"[3] auto 收敛: {end} (第 {rounds} 轮结束)")
assert end.startswith("final")
end, rounds = run_agent("你好", "required")
print(f"[3b] required 空转: {end} — 强制行动的任务若无法表达完成, 会烧满轮数预算")
assert end == "hit max_rounds"
print("    → 实测 auto 省往返但有漏调风险; required 保证行动但必须配 max_rounds/预算兜底; 指定函数适合结构化抽取")
```

**追问一**：指定函数模式做结构化抽取时，模型"编造参数"怎么防？—— 三层：① **schema 约束**（json schema 的 required/enum/最小长度）在 API 层拒绝非法参数；② **业务校验**（参数取值是否在数据库/知识库里真实存在，如 city 必须是城市字典里的值）在代码层验证，失败把校验错误回传给模型重试（自愈循环，一般 2 次预算）；③ **不可用即拒答**——重试仍失败就返回"无法抽取"，绝不把编造值当真值下游使用。经验值：给 2 次自愈重试预算，超过即人工/降级路径；自愈循环的错误信息要具体到字段（"city 必须在 [北京,上海,…] 中，收到 '北京市朝阳区'"），模糊报错会让模型继续编。

**追问二**：required 模式下模型"被迫空转"和 Agent 无进展检测有什么关系？—— required 空转是**合同强制**与**任务完成**的错配：模型被要求必须行动，但任务已无行动可做。Q7799 的无进展检测（动作签名重复/观测哈希不变）恰好是这类空转的探测器——required 连续多轮调用同一工具同参数，就是"强制行动但无事可做"的指纹。所以 required 模式必须配两道闸：无进展检测（软闸，触发后切回 auto 并注入"资料已齐备"提示给一次收尾机会）+ max_rounds（硬闸，直接终止返回部分结果）。只配硬闸会把"差一步就能答对"的任务也误杀，软闸在前是必要的。

## 背诵要点

- auto 智能但有漏调/不一致风险；required 保证行动但任务完成时会空转烧预算；指定函数 = 结构化抽取专用，别的工具进不去。
- required/指定函数必须配 max_rounds + 无进展检测双闸；阶段性策略（首轮 required、资料齐备后切 auto）兼顾正确率与轮数。
- 抽取类自愈重试预算 2 次，错误信息具体到字段；仍失败走"无法抽取"拒答，不用编造值。

## 复盘追问

- 模型 8% 的轮次该查工单没查，你为什么不用提示词加强而选 required？（提示词只提高概率不构成保证；正确率敏感的入口动作用合同级强制，成本差异用阶段切换消化）
- 评测里 auto 模式"同一输入忽调忽不调"，怎么处理？（把"是否调用"作为独立指标统计并设阈值；对回归测试锁死 tool_choice，先测合同行为再测 auto 自由度）

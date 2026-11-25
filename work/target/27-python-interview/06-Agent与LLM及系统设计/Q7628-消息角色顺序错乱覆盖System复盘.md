---
title: [Q7628] 消息列表角色顺序错乱覆盖 System Prompt 事故复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7628 · 消息列表角色顺序错乱导致 System Prompt 被覆盖的事故复盘

难度：P6 ｜ 标签：事故复盘 / 会话管理 / 上下文组装

**问**：多轮对话服务上线新功能"会话中途切换人设"，切换后用户发现助手忘了系统级规则（如必须带引用、禁止工具调用），部分请求还因 `system` 消息出现在中间被 API 拒绝。这类"角色顺序错乱"事故的机制是什么？会话存储层怎么设计才能结构性防住？

**答**：
- **结论**：机制是**消息列表被当成"可变流水"而不是"结构化序列"**：system 的锚定地位（必须在首位、部分 API 只允许一条且必须在前）依赖调用方自觉，任何一条写入路径（切人设、注入检索结果、HITL 追加）把消息 append/insert 到错误位置就破坏不变量。事故链条通常三层叠加：① 存储层只存 list 无角色约束；② 组装层把"system 更新"实现成 append 而不是替换首位；③ 校验缺失——发请求前没人检查不变量。结构性防法：**会话存储按区段建模**（system 区 / 工具区 / 对话区），API 只暴露"set_system / append_dialog"，禁止裸 list 操作；组装函数出口处跑不变量断言（system 在 0 位且仅一条、角色交替合法、工具消息有配对 tool_call_id），断言失败直接拒绝发送并告警——把"请求被 API 拒绝"前移成"组装时 fail-fast"。
- **取舍**：切人设时旧的 system 规则怎么处理？完全替换会丢历史约束（前面轮次按旧规则回答，新轮按新规则），部分模型对"中途改 system"的遵循度明显下降——更稳的方案是**新会话**或把变更点作为显式分割（旧轮标记 legacy），牺牲一点连续性换遵循度确定性。另一个取舍：不变量校验放组装层还是网关层？组装层校验能定位到代码路径，网关层校验能兜住所有出口（包括人工触发的历史重放），双保险成本不高，值得都做。
- **实战**：① 会话对象封装：`Session.set_system(text)` 内部替换首位并自增 system_version，其余路径无权限；② 发送前 invariant 校验函数 + 单测覆盖所有写路径；③ 区段标记持久化（system_version 进消息元数据），排障时能还原"哪个版本的人设在生效"；④ 监控 API 拒绝错误率，突变说明有写路径绕过了封装。

```python
# 会话区段模型: system 锚定首位, append_dialog 受控; 出口不变量断言
# 基线: Python 3.9+ 标准库
from dataclasses import dataclass, field


@dataclass
class Msg:
    role: str            # system | user | assistant | tool
    content: str
    tool_call_id: str | None = None


@dataclass
class Session:
    system: str
    system_version: int = 1
    dialog: list[Msg] = field(default_factory=list)

    def set_system(self, text: str) -> None:
        self.system = text          # 替换而非追加
        self.system_version += 1

    def append(self, m: Msg) -> None:
        if m.role == "system":
            raise ValueError("system 只能走 set_system, 禁止 append")
        self.dialog.append(m)

    def payload(self) -> list[Msg]:
        out = [Msg("system", self.system)] + self.dialog
        validate(out)
        return out


def validate(msgs: list[Msg]) -> None:
    if msgs[0].role != "system":
        raise ValueError("system 不在首位")
    if sum(m.role == "system" for m in msgs) != 1:
        raise ValueError("system 必须仅一条")


def main() -> None:
    s = Session("必须带引用; 禁止工具调用")
    s.append(Msg("user", "总结一下"))
    s.append(Msg("assistant", "好的[1]"))
    p = s.payload()
    assert p[0].role == "system" and len(p) == 3
    s.set_system("新版本规则 v2")
    assert s.system_version == 2
    p = s.payload()
    assert p[0].content == "新版本规则 v2"     # 替换首位而非追加
    try:
        s.append(Msg("system", "中途人设"))   # 事故路径被结构封死
    except ValueError as e:
        print("拦截:", e)
    print("OK: 区段建模+出口断言, 把 API 拒绝前移为组装期 fail-fast")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"中途切 system"的模型遵循度会下降？工程上怎么对冲？
→ 一句话提示：部分推理栈的注意力与 KV cache 组织对首位 system 有隐式偏置，中途变更让旧规则残留在历史里与新规则冲突；对冲 = 换新会话或显式 legacy 分割标记，让冲突可解释而不是隐形。

**追问 2**：工具消息（role=tool）与 assistant 的 tool_call_id 配对为什么也要进不变量？
→ 一句话提示：配对断裂（追加 tool 结果却丢了对应 assistant 调用）会直接被 API 拒绝或让模型产生幻觉续写——工具区段的不变量与 system 锚定同属一个校验函数，一次断言拦一类事故。

## 背诵要点
- 事故根因 = 消息列表当可变流水、system 锚定靠自觉；结构防法 = 区段建模（system/工具/对话）+ 封装写路径 + 出口不变量断言。
- 切人设：替换首位并自增 system_version（可追溯），避免中途 append；遵循度存疑时换新会话或 legacy 分割。
- 不变量集：system 在 0 位仅一条、工具消息与 tool_call_id 配对、角色序列合法；组装层与网关层双保险。

## 复盘追问
- 为什么"API 拒绝率监控"能反过来发现绕过封装的写路径？提示：所有合法写路径都过校验，被 API 拒绝说明存在未封装入口（如人工重放/脚本），拒绝率突变即绕行信号。
- 检索结果注入会话时应该进哪个区段、以什么角色？提示：进对话区以 user/tool 消息显式包裹（带来源标记），而不是伪装 system——伪装会破坏 system 唯一性不变量且让模型把检索当指令。

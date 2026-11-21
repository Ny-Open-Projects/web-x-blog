---
title: [Q1488] 输出降级模板:三级退路 full→template→minimal
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1488 · 输出降级模板:三级退路 full→template→minimal

> 难度:★★☆ | 标签:Agent, 降级, 输出

**问**:模型输出的 JSON 又解析失败了,用户端不能白屏,怎么设计退路?

**答**:把输出当成一条降级链而不是单点。第一级完整结构化输出,校验通过直接用;第二级模板填充,解析出来但字段缺失或为空时,把可信字段与产品侧默认值合并,补充缺失字段并打上 template_filled 标记;第三级最小安全回复,连解析都失败时返回固定的兜底话术,同时保留原始输出供离线排查。每一级都要带降级标记,下游据此决定是否展示、是否计费、是否进 badcase 队列。反模式是静默 try-except 后返回空字符串,用户看到空白,监控看不到异常。

```python
# file: code/06_Agent与LLM及系统设计/q1488_fallback_template.py
"""输出降级模板:结构化生成失败时逐级退到模板填充与最小安全回复,并带降级标记。"""
import json


class FallbackChain:
    """三级输出降级:完整 JSON → 字段模板 → 最小安全回复,每级都打上 degrade 标记。"""

    def __init__(self):
        self.level = None

    def produce(self, raw, slot_defaults):
        """raw 为模型原始输出字符串;按解析成败走降级链。"""
        parsed = self._try_json(raw)
        if parsed is not None and self._complete(parsed):
            self.level = "full"
            return {"degrade": "none", "answer": parsed}
        if parsed is not None:
            filled = dict(slot_defaults)
            filled.update({k: v for k, v in parsed.items() if v})
            self.level = "template"
            return {"degrade": "template_filled", "answer": filled,
                    "missing": sorted(self._required() - set(k for k, v in parsed.items() if v))}
        self.level = "minimal"
        return {"degrade": "minimal_safe",
                "answer": {"reply": slot_defaults["reply"], "action": "none"},
                "raw_kept": len(raw) > 0}

    @staticmethod
    def _try_json(raw):
        try:
            return json.loads(raw)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _required():
        return {"reply", "action"}

    @classmethod
    def _complete(cls, obj):
        return isinstance(obj, dict) and cls._required() <= set(obj) and all(obj.values())


if __name__ == "__main__":
    chain = FallbackChain()
    defaults = {"reply": "已在处理您的请求,请稍候。", "action": "none"}

    good = chain.produce('{"reply": "已为您预约明天上午十点。", "action": "book"}', defaults)
    assert good["degrade"] == "none" and good["answer"]["action"] == "book"

    partial = chain.produce('{"reply": "", "action": "query"}', defaults)
    assert partial["degrade"] == "template_filled"
    assert partial["answer"]["reply"] == defaults["reply"]      # 空字段用默认补齐
    assert partial["missing"] == ["reply"]

    broken = chain.produce('前半句 {"reply": "嗯", 后半句缺引号', defaults)
    assert broken["degrade"] == "minimal_safe"
    assert broken["answer"]["action"] == "none"
    assert broken["raw_kept"] is True                           # 原始输出已留档供排查

    empty = chain.produce("", defaults)
    assert empty["degrade"] == "minimal_safe" and empty["raw_kept"] is False
    assert [chain.level for chain in [chain]] == ["minimal"]
    print("输出降级通过:三级链路 full→template_filled→minimal_safe 全部按预期触发")
```

**追问**:
- 降级标记给谁看? 答:三份:前端按标记切换展示形态,计费侧按标记打折或免单,评估侧按标记归因;
- 模板里的默认话术谁维护? 答:和 prompt 一样进版本管理与回归测试,改默认值也要过评估集。

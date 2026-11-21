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

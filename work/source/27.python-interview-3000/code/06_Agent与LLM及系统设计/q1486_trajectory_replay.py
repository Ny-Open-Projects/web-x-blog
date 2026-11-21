"""失败轨迹录制与回放调试:录制 LLM 与工具事件,确定性回放并定位首个分歧点。"""
import json


class Recorder:
    """轨迹录制器:把每步 (类型, 输入, 输出) 按序写入事件流。"""

    def __init__(self):
        self.events = []

    def record(self, kind, payload):
        self.events.append({"seq": len(self.events), "kind": kind, "payload": payload})
        return self.events[-1]["seq"]


class ReplayPlayer:
    """回放器:不执行真实工具,按序号取录制结果,实现完全确定性复现。"""

    def __init__(self, events):
        self.events = events
        self.pos = 0

    def next_tool_result(self, tool, args):
        ev = self.events[self.pos]
        assert ev["kind"] == "tool", "回放轨迹错位 期望工具事件得到 " + ev["kind"]
        if ev["payload"]["tool"] != tool or ev["payload"]["args"] != args:
            raise Divergence(self.pos, ev["payload"], {"tool": tool, "args": args})
        self.pos += 1
        return ev["payload"]["result"]

    def next_llm_reply(self, prompt_hash):
        ev = self.events[self.pos]
        assert ev["kind"] == "llm"
        if ev["payload"]["prompt_hash"] != prompt_hash:
            raise Divergence(self.pos, ev["payload"], {"prompt_hash": prompt_hash})
        self.pos += 1
        return ev["payload"]["reply"]


class Divergence(Exception):
    """首个分歧点:回放输入与录制输入不一致的位置与两侧内容。"""

    def __init__(self, seq, recorded, got):
        self.seq, self.recorded, self.got = seq, recorded, got
        super().__init__(f"第 {seq} 步回放输入与录制不符")


def hash_of(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False)


class StubLLM:
    """桩模型:按脚本表回复,使两次运行输入一致时输出必然一致。"""

    def __init__(self, script):
        self.script = script

    def reply(self, messages):
        key = hash_of(messages)
        return self.script[key]


if __name__ == "__main__":
    llm_script = {"[\"system 你好\", \"user 查订单\"]": "调用 get_order",
                  "[\"system 你好\", \"user 查订单\", \"tool 订单已发货\"]": "告诉用户已发货"}
    tool_result = {"order": "订单已发货"}

    # 第一次运行:边跑边录
    rec = Recorder()
    llm = StubLLM(llm_script)
    msgs = ["system 你好", "user 查订单"]
    reply = llm.reply(msgs)
    rec.record("llm", {"prompt_hash": hash_of(msgs), "reply": reply})
    tool = reply.replace("调用 ", "")
    obs = tool_result["order"]
    rec.record("tool", {"tool": tool, "args": {"id": "A1"}, "result": obs})
    msgs = msgs + ["tool " + obs]
    final = llm.reply(msgs)
    rec.record("llm", {"prompt_hash": hash_of(msgs), "reply": final})
    assert final == "告诉用户已发货"

    # 回放一:同输入同结果,定位不到分歧
    player = ReplayPlayer(rec.events)
    assert player.next_llm_reply(hash_of(["system 你好", "user 查订单"])) == "调用 get_order"
    assert player.next_tool_result("get_order", {"id": "A1"}) == "订单已发货"
    assert player.next_llm_reply(hash_of(["system 你好", "user 查订单", "tool 订单已发货"])) == "告诉用户已发货"

    # 回放二:第二次运行里用户问题变了,回放应在首个工具事件处报出分歧
    player2 = ReplayPlayer(rec.events)
    diverged = None
    try:
        player2.next_llm_reply(hash_of(["system 你好", "user 查退款"]))   # 与录制不符
    except Divergence as d:
        diverged = d
    assert diverged is not None and diverged.seq == 0
    assert diverged.recorded["reply"] == "调用 get_order"
    print("轨迹回放通过:录制", len(rec.events), "个事件 确定性回放一致 分歧定位在第", diverged.seq, "步")

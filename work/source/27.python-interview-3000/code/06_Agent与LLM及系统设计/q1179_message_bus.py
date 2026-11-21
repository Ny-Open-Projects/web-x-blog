"""Agent 消息总线:发布订阅 + 信封协议 + correlation_id 关联 + 死信主题。"""
import itertools, json


class MessageBus:
    def __init__(self):
        self.subs = {}
        self.dead_letter = []
        self._ids = itertools.count(1)

    def subscribe(self, topic, agent):
        self.subs.setdefault(topic, []).append(agent)

    def publish(self, topic, sender, payload, correlation_id=None, msg_id=None):
        msg = {"id": msg_id if msg_id is not None else next(self._ids),
               "topic": topic, "sender": sender,
               "payload": payload, "correlation_id": correlation_id}
        handled = False
        for agent in self.subs.get(topic, []):
            try:
                agent.on_message(msg)
                handled = True
            except Exception as e:
                self.dead_letter.append({**msg, "error": str(e)})
        if self.subs.get(topic) and not handled:
            self.dead_letter.append({**msg, "error": "all_consumers_failed"})
        return msg["id"]


class Agent:
    def __init__(self, name, bus):
        self.name, self.bus, self.inbox = name, bus, []

    def on_message(self, msg):
        if msg["id"] in self.inbox:              # at-least-once 下的幂等消费
            return
        self.inbox.append(msg["id"])
        print(f"  [{self.name}] 收到 {msg['topic']} 来自 {msg['sender']}: {json.dumps(msg['payload'], ensure_ascii=False)}")
        if msg["topic"] == "task.created" and self.name == "worker":
            self.bus.publish("task.completed", self.name,
                             {"result": "done"}, correlation_id=msg["id"])


if __name__ == "__main__":
    bus = MessageBus()
    worker, auditor = Agent("worker", bus), Agent("auditor", bus)
    bus.subscribe("task.created", worker)
    bus.subscribe("task.created", auditor)
    bus.subscribe("task.completed", auditor)

    mid = bus.publish("task.created", "orchestrator", {"goal": "写摘要"})
    print("死信:", bus.dead_letter)

    # 网络重投同一封套(相同 msg id):订阅方幂等去重
    bus.publish("task.created", "orchestrator", {"goal": "写摘要"}, msg_id=mid)
    assert len(worker.inbox) == 1, "同 id 消息必须幂等"
    print(f"总线运转正常,worker 收到 {len(worker.inbox)} 条(重复投递被去重)")
    assert bus.subs and not bus.dead_letter

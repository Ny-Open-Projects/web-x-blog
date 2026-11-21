"""用标准库数据结构模拟 MQTT 的核心语义: 连接/订阅/发布/遗嘱/保留。"""
import queue
import threading
import time
from typing import Optional


class SimBroker:
    def __init__(self) -> None:
        self.subs: dict = {}        # client -> set of topic filters
        self.mailboxes: dict = {}   # client -> Queue
        self.retained: dict = {}    # topic -> last payload
        self.wills: dict = {}       # client -> will message
        self.online: set = set()

    def connect(self, client: str, will: Optional[str] = None) -> dict:
        # 注: str | None(PEP 604)运行时求值要 3.10+, 参数默认值注解
        # 在 3.9 直接 TypeError, 兼容写法用 Optional
        packet = {"type": "CONNECT", "client": client, "will": will}
        self.mailboxes[client] = queue.Queue()
        self.subs[client] = set()
        self.wills[client] = will
        self.online.add(client)
        return {"type": "CONNACK", "rc": 0}  # 连接成功

    def subscribe(self, client: str, topic_filter: str, delivery: bool = True) -> None:
        self.subs[client].add(topic_filter)
        if delivery:
            self.mailboxes[client].put(
                {"type": "SUBACK", "filter": topic_filter, "qos": 0})
        # 保留消息: 新订阅者立即收到最后一条
        for topic, payload in self.retained.items():
            if topic_matches(topic_filter, topic):
                self.mailboxes[client].put(
                    {"type": "PUBLISH", "topic": topic, "payload": payload,
                     "retained": True, "qos": 0})

    def publish(self, client: str, topic: str, payload: str,
                retain: bool = False) -> None:
        if retain:
            self.retained[topic] = payload
        for sub, filters in self.subs.items():
            if sub == client or sub not in self.online:
                continue
            for f in filters:
                if topic_matches(f, topic):
                    self.mailboxes[sub].put(
                        {"type": "PUBLISH", "topic": topic,
                         "payload": payload, "retained": False, "qos": 0})

    def disconnect(self, client: str, abnormal: bool = False) -> None:
        self.online.discard(client)
        will = self.wills.get(client)
        if abnormal and will:
            for sub, filters in self.subs.items():
                if sub in self.online and "status/+" in filters:
                    self.mailboxes[sub].put(
                        {"type": "PUBLISH", "topic": "status/lwt",
                         "payload": will, "retained": False, "qos": 0})


def topic_matches(flt: str, topic: str) -> bool:
    """MQTT 通配符: + 单层, # 多层 (必须位于末尾)。"""
    f_parts, t_parts = flt.split("/"), topic.split("/")
    for i, fp in enumerate(f_parts):
        if fp == "#":
            return i == len(f_parts) - 1
        if i >= len(t_parts):
            return False
        if fp != "+" and fp != t_parts[i]:
            return False
    return len(f_parts) == len(t_parts)


if __name__ == "__main__":
    def next_publish(broker, client):
        """跳过 SUBACK 等控制包, 取下一条 PUBLISH(模拟 SDK 只上抛数据包)。"""
        while True:
            msg = broker.mailboxes[client].get(timeout=1)
            if msg["type"] == "PUBLISH":
                return msg

    broker = SimBroker()
    print("sensor 连接 (带遗嘱):", broker.connect("sensor-1", will="sensor-1 offline"))
    print("app 连接:", broker.connect("app"))
    broker.subscribe("app", "status/+")
    broker.subscribe("app", "sensor/1/#")
    broker.subscribe("app", "data/#")

    broker.publish("sensor-1", "sensor/1/temp", "23.5", retain=True)
    time.sleep(0.05)
    print("app 收到:", next_publish(broker, "app"))

    print("app2 重连订阅后立即拿到保留消息:")
    broker.connect("app2")
    broker.subscribe("app2", "sensor/1/temp")
    print("  ", next_publish(broker, "app2"))

    print("sensor 异常掉线 → 遗嘱送达订阅者:")
    broker.disconnect("sensor-1", abnormal=True)
    print("  ", next_publish(broker, "app"))

---
title: [Q674] MQTT 概念:发布订阅、QoS 与遗嘱
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q674 · MQTT 概念:发布订阅、QoS 与遗嘱

> 难度:★★☆ | 标签:MQTT, 发布订阅, IoT

**问**:MQTT 的核心模型是什么?为什么 IoT 场景几乎都选它?

**答**:MQTT 是中心化 broker 的发布订阅协议:生产者按 topic 发布,消费者按通配符订阅,broker 负责路由——收发双方完全解耦,互不知道地址。三个杀手级特性贴合弱网设备:QoS 分级(最多一次/至少一次/恰好一次)让用户按重要度权衡成本;遗嘱消息(LWT)——连接异常断开时 broker 代发预设消息,天然实现"设备掉线告警";保留消息(retained)——新订阅者立即收到最后一条状态,免等下一轮上报。协议头最小 2 字节、长连接低功耗,这是它统治 IoT 的原因。

```python
# file: code/02_并发与网络工程/q674_mqtt_model.py
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
```

**追问**:1) 遗嘱和保留消息能叠加吗?——可以:遗嘱消息也可以设 retain,设备异常掉线后,后续所有订阅者都能立刻知道它已离线,这是"在线状态服务"的经典搭建方式。2) QoS 三级的代价与适用?——QoS0 最多一次(最快,丢得起的状态上报);QoS1 至少一次(一次 ACK 往返,可能重复,配业务幂等);QoS2 恰好一次(四步握手最贵,审计计费类才用);弱网高延迟下 QoS2 成本要实测再定。3) 遗嘱(LWT)怎么工作?——CONNECT 时注册遗嘱,会话异常断开(broker 未收到 DISCONNECT)时 broker 代发,正常下线不发;配合 retain 叠加(见原问)即可搭在线状态服务。4) 生产陷阱?——keepalive 过短,弱网频繁误判掉线触发遗嘱风暴;clean session 配置与订阅恢复预期不一致,重连后收不到消息;QoS1 没去重导致控制命令重复执行。

---

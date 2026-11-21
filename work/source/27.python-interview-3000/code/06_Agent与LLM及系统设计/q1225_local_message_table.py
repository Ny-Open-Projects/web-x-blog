"""本地消息表:业务与消息同事务 + relay 退避投递 + 消费端幂等。"""
import time


class Db:
    def __init__(self):
        self.orders, self.outbox = {}, []

    def create_order_with_message(self, order_id, msg):
        """同一'事务':订单与消息必须一起成功。"""
        self.orders[order_id] = {"status": "created"}
        self.outbox.append({"id": len(self.outbox) + 1, "payload": msg,
                            "state": "NEW", "retries": 0, "next_at": 0.0})
        return True


class Relay:
    def __init__(self, db, broker, backoff=0.05):
        self.db, self.broker, self.backoff = db, broker, backoff
        self.now = 0.0

    def tick(self):
        sent = 0
        for m in self.db.outbox:
            if m["state"] != "NEW" or self.now < m["next_at"]:
                continue
            if self.broker.publish(m["payload"]):
                m["state"] = "SENT"
                sent += 1
            else:
                m["retries"] += 1
                m["next_at"] = self.now + self.backoff * (2 ** m["retries"])
        return sent


class Broker:
    def __init__(self):
        self.queue, self.fail_next = [], 0
        self.delivered = []

    def publish(self, msg):
        if self.fail_next > 0:
            self.fail_next -= 1
            return False
        self.queue.append(msg)
        return True


class Consumer:
    def __init__(self):
        self.seen, self.processed = set(), []

    def consume(self, msg, msg_id):
        if msg_id in self.seen:                 # 消费幂等
            return
        self.seen.add(msg_id)
        self.processed.append(msg)


if __name__ == "__main__":
    db, broker = Db(), Broker()
    db.create_order_with_message("o-1", {"event": "order_created", "order": "o-1"})
    assert len(db.orders) == 1 and len(db.outbox) == 1, "业务与消息同事务落库"

    broker.fail_next = 1                        # 第一次投递失败
    relay = Relay(db, broker)
    relay.now = 1.0
    print("第一次 tick 发送:", relay.tick(), "条(失败退避)")
    assert db.outbox[0]["state"] == "NEW" and db.outbox[0]["retries"] == 1
    relay.now = 1.0 + 0.1                       # 退避到期
    print("第二次 tick 发送:", relay.tick(), "条")
    assert db.outbox[0]["state"] == "SENT"

    consumer = Consumer()
    consumer.consume(db.outbox[0]["payload"], "msg-1")
    consumer.consume(db.outbox[0]["payload"], "msg-1")   # MQ 重复投递
    assert len(consumer.processed) == 1, "消费端幂等去重"
    print("闭环: 同事务落库 -> 退避投递 -> 消费幂等 = 最终一致")

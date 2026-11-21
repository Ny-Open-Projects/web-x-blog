"""schema 版本协商: 生产者声明, 消费者适配或拒绝"""

REGISTRY = {
    "1.0": {"order_id": "str", "amount_cents": "int", "status": "str"},
    "1.1": {"order_id": "str", "amount_cents": "int", "status": "str", "channel": "str?"},
    "1.2": {"order_id": "str", "amount_cents": "int", "status": "str", "channel": "str?", "memo": "str?"},
    "2.0": {"order_id": "str", "amount_yuan": "float", "status": "str"},   # 语义破坏: 分改元
}
CONSUMER_SUPPORTS = {"1.0", "1.1"}   # 消费者已适配的版本


def negotiate(producer_version, consumer_supports):
    if producer_version in consumer_supports:
        return "直接读", producer_version
    major, minor = producer_version.split(".")
    same_major = sorted(
        (v for v in consumer_supports if v.split(".")[0] == major),
        key=lambda v: int(v.split(".")[1]),
        reverse=True,
    )
    if same_major and int(minor) >= int(same_major[0].split(".")[1]):
        return "适配读", same_major[0]   # 新增可选字段对老读者透明
    return "拒绝", None                   # 主版本变更, 必须升级消费端


if __name__ == "__main__":
    for pv in ["1.0", "1.1", "1.2", "2.0"]:
        mode, read_as = negotiate(pv, CONSUMER_SUPPORTS)
        if mode == "适配读":
            detail = f"按 {read_as} 解析, 新增字段走默认值"
        elif mode == "直接读":
            detail = ""
        else:
            detail = "主版本语义变更, 消费端升级前生产者保持双写"
        print(f"生产者 {pv} -> {mode} {detail}")
    print("要点: 次版本只加可选字段, 主版本必须双写迁移; 协商逻辑进公共库, 拒绝事件计数告警")

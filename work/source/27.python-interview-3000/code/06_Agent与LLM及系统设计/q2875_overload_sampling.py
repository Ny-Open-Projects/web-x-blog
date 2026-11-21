"""Q2875 过载采样降级:全量转抽样 确定性抽取与恢复回升。

观测日志和链路追踪自己就是最大的流量。过载时按积压水位分档:全量
保留,中度积压抽 1/2,重度抽 1/10;抽取按 trace_id 哈希取模,同一
trace 永远同命运,不会出现链路断一半;水位回落自动恢复全量。
"""

import hashlib

SAMPLE_N = {"L0": 1, "L1": 2, "L2": 10}


def shed_level(backlog):
    if backlog < 100:
        return "L0"
    if backlog < 500:
        return "L1"
    return "L2"


def keep(trace_id, level):
    n = SAMPLE_N[level]
    h = int(hashlib.md5(trace_id.encode("utf-8")).hexdigest(), 16)
    return h % n == 0


def handle_batch(trace_ids, backlog):
    level = shed_level(backlog)
    kept = [t for t in trace_ids if keep(t, level)]
    return level, kept


def main():
    ids = ["trace_%03d" % i for i in range(40)]
    # 空闲:全量
    lv1, kept1 = handle_batch(ids, backlog=30)
    assert lv1 == "L0" and len(kept1) == 40, (lv1, len(kept1))
    # 重度过载:抽样,量级约 1/10,且确定性可复现
    lv2, kept2 = handle_batch(ids, backlog=800)
    assert lv2 == "L2" and 0 < len(kept2) < len(ids), (lv2, len(kept2))
    lv2b, kept2b = handle_batch(ids, backlog=800)
    assert kept2b == kept2   # 同输入同水位:留痕结果完全一致
    # 每条 trace 的去留只由自身哈希决定,与批次无关
    for t in kept2:
        assert keep(t, "L2")
    # 恢复:水位回落,自动回全量
    lv3, kept3 = handle_batch(ids, backlog=50)
    assert lv3 == "L0" and len(kept3) == 40
    print("L0 全量:", len(kept1), "条")
    print("L2 抽样:", len(kept2), "条,留痕:", kept2[:4], "...")
    print("恢复后全量:", len(kept3), "条,降级无状态可逆")


if __name__ == "__main__":
    main()

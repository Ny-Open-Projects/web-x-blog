"""输入指纹跳过:对输入内容寻址,指纹没变就跳过,变了才重算"""

import hashlib
import json
import os
import tempfile

STATE = os.path.join(tempfile.mkdtemp(prefix="fp_demo_"), "fingerprints.json")


def fingerprint(inputs):
    """对输入键值对排序后哈希:内容决定指纹,顺序无关"""
    payload = json.dumps(sorted(inputs.items()), sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def load_fingerprints():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    return {}


def run_task(task, inputs, log):
    fp = fingerprint(inputs)
    old = load_fingerprints().get(task)
    if old == fp:
        log.append(f"{task}: SKIPPED(指纹 {fp} 未变)")
        return
    log.append(f"{task}: RAN(指纹 {old} -> {fp})")   # 这里替换为真正计算
    state = load_fingerprints()
    state[task] = fp
    with open(STATE, "w") as f:
        json.dump(state, f)


if __name__ == "__main__":
    log = []
    daily = {"dt": "2026-11-04", "rows": 1200, "rule_ver": "v3"}
    run_task("agg_daily", daily, log)
    run_task("agg_daily", daily, log)          # 输入没变 -> 跳过
    daily["rule_ver"] = "v4"                   # 规则升级 -> 重算
    run_task("agg_daily", daily, log)
    for line in log:
        print(" ", line)
    print("要点:指纹对内容哈希而不是对时间,同参数重跑天然幂等;规则版本必须纳入指纹,只盯数据不变会漏算逻辑变更;指纹状态要与结果数据同生命周期清理")

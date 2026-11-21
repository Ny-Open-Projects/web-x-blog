"""细粒度 checkpoint:批级状态原子落盘,崩溃恢复后结果与一次跑完一致"""

import json
import os
import tempfile

CKPT = os.path.join(tempfile.mkdtemp(prefix="ckpt_demo_"), "state.json")
RECORDS = [f"r{i}" for i in range(1, 13)]
BATCH = 3


def load_state():
    if os.path.exists(CKPT):
        with open(CKPT) as f:
            return json.load(f)
    return {"offset": 0, "results": []}


def save_state(state):
    tmp = CKPT + ".tmp"                 # 原子写: 先 tmp 后 replace
    with open(tmp, "w") as f:
        json.dump(state, f)
    os.replace(tmp, CKPT)


def process(rec):
    return rec.upper()


def run(records, crash_after=None):
    state = load_state()
    done = 0
    for i in range(state["offset"], len(records)):
        state["results"].append(process(records[i]))
        done += 1
        if crash_after is not None and state["offset"] + done >= crash_after:
            raise RuntimeError(f"模拟崩溃于第 {state['offset'] + done} 条")
        if done % BATCH == 0:
            state["offset"] += done
            done = 0
            save_state(state)
    state["offset"] = len(records)
    save_state(state)
    return state["results"]


if __name__ == "__main__":
    try:
        run(RECORDS, crash_after=7)
    except RuntimeError as e:
        print("第一次运行:", e)
    partial = load_state()
    print(f"崩溃后 checkpoint: offset={partial['offset']}, 已落盘 {partial['results']}")
    results = run(RECORDS)
    print("恢复续跑最终结果:", results)
    once = [process(r) for r in RECORDS]
    verdict = "完全一致,不重不漏" if results == once else "不一致,有 bug"
    print("与一次性跑完对比:", verdict)
    print("要点:粒度取批,批大小是恢复成本与落盘开销的折中;状态原子写;恢复正确性用'与一次跑完对账'自动验证,别靠肉眼")
